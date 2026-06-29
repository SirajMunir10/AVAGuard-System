#!/usr/bin/env python3
"""
Enhanced LoRA Fine-Tuning Script for Security Domain Knowledge

This script fine-tunes a base language model using LoRA (Low-Rank Adaptation)
on your domain-specific dataset (CIS security knowledge, cybersecurity courses, etc.)

Features:
- Configurable base model (TinyLlama, Llama-3, Mistral, etc.)
- Validation set support
- Gradient accumulation for larger effective batch sizes
- Mixed precision training (FP16/BF16)
- Detailed logging
- Resumable training from checkpoints
"""

import argparse
import logging
import os
import sys
from pathlib import Path

import torch
from datasets import load_dataset
from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    TrainingArguments,
    Trainer,
    DataCollatorForLanguageModeling,
    EarlyStoppingCallback,
)
from peft import LoraConfig, get_peft_model, TaskType

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('training.log')
    ]
)
logger = logging.getLogger(__name__)

# ==============================================================================
# Default Configuration
# ==============================================================================
DEFAULT_CONFIG = {
    "model_name": "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    "train_file": "../data/train.jsonl",
    "val_file": "../data/validation.jsonl",
    "output_dir": "lora-output",
    "adapter_dir": "lora-adapters",
    "max_length": 512,
    "batch_size": 2,
    "gradient_accumulation_steps": 4,
    "learning_rate": 2e-4,
    "num_epochs": 3,
    "lora_r": 16,
    "lora_alpha": 32,
    "lora_dropout": 0.05,
    "warmup_ratio": 0.03,
    "weight_decay": 0.01,
}

# Supported models with their specific LoRA target modules
MODEL_TARGETS = {
    "tinyllama": ["q_proj", "v_proj", "k_proj", "o_proj"],
    "llama": ["q_proj", "v_proj", "k_proj", "o_proj", "gate_proj", "up_proj", "down_proj"],
    "mistral": ["q_proj", "v_proj", "k_proj", "o_proj", "gate_proj", "up_proj", "down_proj"],
    "phi": ["q_proj", "v_proj", "k_proj", "dense"],
    "default": ["q_proj", "v_proj"],
}


def get_target_modules(model_name: str) -> list:
    """Determine the correct LoRA target modules based on model architecture."""
    model_lower = model_name.lower()
    for key, modules in MODEL_TARGETS.items():
        if key in model_lower:
            return modules
    logger.warning(f"Unknown model architecture, using default target modules.")
    return MODEL_TARGETS["default"]


def load_and_prepare_data(train_file: Path, val_file: Path, tokenizer, max_length: int):
    """Load and tokenize the dataset."""
    logger.info(f"Loading training data from {train_file}")
    
    data_files = {"train": str(train_file)}
    
    if val_file and val_file.exists():
        data_files["validation"] = str(val_file)
        logger.info(f"Loading validation data from {val_file}")
    
    dataset = load_dataset("json", data_files=data_files)
    
    def tokenize_function(examples):
        return tokenizer(
            examples["text"],
            truncation=True,
            padding="max_length",
            max_length=max_length,
            return_tensors=None,
        )
    
    tokenized_dataset = dataset.map(
        tokenize_function,
        batched=True,
        remove_columns=["text"],
        desc="Tokenizing dataset",
    )
    
    logger.info(f"Training samples: {len(tokenized_dataset['train'])}")
    if "validation" in tokenized_dataset:
        logger.info(f"Validation samples: {len(tokenized_dataset['validation'])}")
    
    return tokenized_dataset


def setup_model_and_tokenizer(model_name: str, use_flash_attention: bool = False):
    """Load the base model and tokenizer."""
    logger.info(f"Loading model: {model_name}")
    
    tokenizer = AutoTokenizer.from_pretrained(
        model_name,
        trust_remote_code=True,
    )
    
    # Set pad token if not present
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
        
    # Determine compute dtype and device
    if torch.cuda.is_available():
        compute_dtype = torch.bfloat16 if torch.cuda.is_bf16_supported() else torch.float16
        device_map = "auto"
    else:
        compute_dtype = torch.float32
        device_map = "cpu"
        logger.warning("CUDA not available, training on CPU (this will be slow)")
    
    model_kwargs = {
        "torch_dtype": compute_dtype,
        "device_map": device_map,
        "trust_remote_code": True,
    }
    
    if use_flash_attention and torch.cuda.is_available():
        model_kwargs["attn_implementation"] = "flash_attention_2"
        logger.info("Using Flash Attention 2")
    
    model = AutoModelForCausalLM.from_pretrained(model_name, **model_kwargs)
    model.config.use_cache = False  # Required for gradient checkpointing
    
    return model, tokenizer


def setup_lora(model, config: dict):
    """Configure and apply LoRA to the model."""
    target_modules = get_target_modules(config["model_name"])
    logger.info(f"LoRA target modules: {target_modules}")
    
    lora_config = LoraConfig(
        r=config["lora_r"],
        lora_alpha=config["lora_alpha"],
        target_modules=target_modules,
        lora_dropout=config["lora_dropout"],
        bias="none",
        task_type=TaskType.CAUSAL_LM,
    )
    
    model = get_peft_model(model, lora_config)
    model.print_trainable_parameters()
    
    return model


def train(config: dict, resume_from_checkpoint: str = None):
    """Main training function."""
    logger.info("=" * 60)
    logger.info("Starting LoRA Fine-Tuning for Security Domain Knowledge")
    logger.info("=" * 60)
    logger.info(f"Configuration: {config}")
    
    # Setup
    model, tokenizer = setup_model_and_tokenizer(config["model_name"])
    model = setup_lora(model, config)
    
    # Load data
    train_file = Path(config["train_file"])
    val_file = Path(config["val_file"]) if config.get("val_file") else None
    
    if not train_file.exists():
        logger.error(f"Training file not found: {train_file}")
        logger.error("Please run the ingestion scripts first to create training data.")
        sys.exit(1)
    
    dataset = load_and_prepare_data(train_file, val_file, tokenizer, config["max_length"])
    
    # Data collator
    data_collator = DataCollatorForLanguageModeling(
        tokenizer=tokenizer,
        mlm=False,
    )
    
    # Training arguments
    training_args = TrainingArguments(
        output_dir=config["output_dir"],
        per_device_train_batch_size=config["batch_size"],
        gradient_accumulation_steps=config["gradient_accumulation_steps"],
        num_train_epochs=config["num_epochs"],
        learning_rate=config["learning_rate"],
        warmup_ratio=config["warmup_ratio"],
        weight_decay=config["weight_decay"],
        logging_steps=10,
        save_strategy="epoch",
        evaluation_strategy="epoch" if "validation" in dataset else "no",
        load_best_model_at_end=True if "validation" in dataset else False,
        save_total_limit=3,
        report_to="none",
        fp16=torch.cuda.is_available() and not torch.cuda.is_bf16_supported(),
        bf16=torch.cuda.is_available() and torch.cuda.is_bf16_supported(),
        gradient_checkpointing=True,
        optim="adamw_torch",
        dataloader_num_workers=0,
        dataloader_pin_memory=False,
    )
    
    # Callbacks
    callbacks = []
    if "validation" in dataset:
        callbacks.append(EarlyStoppingCallback(early_stopping_patience=2))
    
    # Trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=dataset["train"],
        eval_dataset=dataset.get("validation"),
        data_collator=data_collator,
        callbacks=callbacks,
    )
    
    # Train
    logger.info("Starting training...")
    trainer.train(resume_from_checkpoint=resume_from_checkpoint)
    
    # Save final adapter
    logger.info(f"Saving adapter to {config['adapter_dir']}")
    model.save_pretrained(config["adapter_dir"])
    tokenizer.save_pretrained(config["adapter_dir"])
    
    logger.info("=" * 60)
    logger.info("Training Complete!")
    logger.info(f"Adapter saved to: {config['adapter_dir']}")
    logger.info("=" * 60)


def main():
    parser = argparse.ArgumentParser(
        description="Fine-tune an LLM with LoRA for Security Domain Knowledge",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    
    parser.add_argument(
        "--model", "-m",
        default=DEFAULT_CONFIG["model_name"],
        help="Base model name or path (e.g., 'meta-llama/Meta-Llama-3-8B', 'mistralai/Mistral-7B-v0.1')",
    )
    parser.add_argument(
        "--train-file",
        default=DEFAULT_CONFIG["train_file"],
        type=Path,
        help="Path to training JSONL file",
    )
    parser.add_argument(
        "--val-file",
        default=DEFAULT_CONFIG["val_file"],
        type=Path,
        help="Path to validation JSONL file",
    )
    parser.add_argument(
        "--output-dir",
        default=DEFAULT_CONFIG["output_dir"],
        help="Directory for training checkpoints",
    )
    parser.add_argument(
        "--adapter-dir",
        default=DEFAULT_CONFIG["adapter_dir"],
        help="Directory to save final LoRA adapter",
    )
    parser.add_argument(
        "--epochs", "-e",
        default=DEFAULT_CONFIG["num_epochs"],
        type=int,
        help="Number of training epochs",
    )
    parser.add_argument(
        "--batch-size", "-b",
        default=DEFAULT_CONFIG["batch_size"],
        type=int,
        help="Per-device batch size",
    )
    parser.add_argument(
        "--learning-rate", "-lr",
        default=DEFAULT_CONFIG["learning_rate"],
        type=float,
        help="Learning rate",
    )
    parser.add_argument(
        "--max-length",
        default=DEFAULT_CONFIG["max_length"],
        type=int,
        help="Maximum sequence length",
    )
    parser.add_argument(
        "--lora-r",
        default=DEFAULT_CONFIG["lora_r"],
        type=int,
        help="LoRA rank (higher = more capacity but slower)",
    )
    parser.add_argument(
        "--lora-alpha",
        default=DEFAULT_CONFIG["lora_alpha"],
        type=int,
        help="LoRA alpha (scaling factor)",
    )
    parser.add_argument(
        "--resume",
        default=None,
        help="Resume training from checkpoint directory",
    )
    
    args = parser.parse_args()
    
    config = {
        "model_name": args.model,
        "train_file": args.train_file,
        "val_file": args.val_file,
        "output_dir": args.output_dir,
        "adapter_dir": args.adapter_dir,
        "num_epochs": args.epochs,
        "batch_size": args.batch_size,
        "learning_rate": args.learning_rate,
        "max_length": args.max_length,
        "lora_r": args.lora_r,
        "lora_alpha": args.lora_alpha,
        "lora_dropout": DEFAULT_CONFIG["lora_dropout"],
        "gradient_accumulation_steps": DEFAULT_CONFIG["gradient_accumulation_steps"],
        "warmup_ratio": DEFAULT_CONFIG["warmup_ratio"],
        "weight_decay": DEFAULT_CONFIG["weight_decay"],
    }
    
    train(config, resume_from_checkpoint=args.resume)


if __name__ == "__main__":
    main()
