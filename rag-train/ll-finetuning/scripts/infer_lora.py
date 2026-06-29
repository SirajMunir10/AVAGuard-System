#!/usr/bin/env python3
"""
Inference Script for Fine-Tuned Security Domain Model

Use this script to chat with your LoRA-adapted model after training.

Features:
- Interactive chat mode
- Single prompt mode
- Configurable generation parameters
- System prompt support for specialized responses
"""

import argparse
import sys
from pathlib import Path

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, GenerationConfig
from peft import PeftModel

# Default system prompts for security context
SYSTEM_PROMPTS = {
    "security": (
        "You are a cybersecurity expert specialized in CIS benchmarks and system hardening. "
        "Provide accurate, detailed responses about security configurations, compliance checks, "
        "and remediation steps. Always explain the rationale behind security recommendations."
    ),
    "check_generator": (
        "You are an expert at writing compliance check scripts. When asked about a security control, "
        "provide a Python script that can verify the system's compliance with that control. "
        "Include registry checks, command parsing, and clear pass/fail logic."
    ),
    "general": "",
}


def load_model(base_model: str, adapter_path: str, use_gpu: bool = True):
    """Load the base model with LoRA adapter."""
    print(f"Loading base model: {base_model}")
    
    tokenizer = AutoTokenizer.from_pretrained(base_model, trust_remote_code=True)
    
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    
    # Determine device and dtype
    if use_gpu and torch.cuda.is_available():
        device_map = "auto"
        torch_dtype = torch.bfloat16 if torch.cuda.is_bf16_supported() else torch.float16
        print("Using GPU with mixed precision")
    else:
        device_map = "cpu"
        torch_dtype = torch.float32
        print("Using CPU (this will be slower)")
    
    model = AutoModelForCausalLM.from_pretrained(
        base_model,
        torch_dtype=torch_dtype,
        device_map=device_map,
        trust_remote_code=True,
    )
    
    # Load LoRA adapter
    adapter_path = Path(adapter_path)
    if adapter_path.exists():
        print(f"Loading LoRA adapter from: {adapter_path}")
        model = PeftModel.from_pretrained(model, str(adapter_path))
        print("Adapter loaded successfully!")
    else:
        print(f"Warning: Adapter path {adapter_path} not found. Using base model only.")
    
    model.eval()
    return model, tokenizer


def generate_response(
    model,
    tokenizer,
    prompt: str,
    system_prompt: str = "",
    max_new_tokens: int = 512,
    temperature: float = 0.7,
    top_p: float = 0.9,
    top_k: int = 50,
    repetition_penalty: float = 1.1,
):
    """Generate a response from the model."""
    
    # Format prompt with system context if provided
    if system_prompt:
        full_prompt = f"### System:\n{system_prompt}\n\n### User:\n{prompt}\n\n### Assistant:\n"
    else:
        full_prompt = f"### User:\n{prompt}\n\n### Assistant:\n"
    
    inputs = tokenizer(full_prompt, return_tensors="pt").to(model.device)
    
    generation_config = GenerationConfig(
        max_new_tokens=max_new_tokens,
        temperature=temperature,
        top_p=top_p,
        top_k=top_k,
        repetition_penalty=repetition_penalty,
        do_sample=True,
        pad_token_id=tokenizer.pad_token_id,
        eos_token_id=tokenizer.eos_token_id,
    )
    
    with torch.no_grad():
        outputs = model.generate(**inputs, generation_config=generation_config)
    
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    # Extract only the assistant's response
    if "### Assistant:" in response:
        response = response.split("### Assistant:")[-1].strip()
    
    return response


def interactive_mode(model, tokenizer, system_prompt: str):
    """Run interactive chat session."""
    print("\n" + "=" * 60)
    print("Security Domain Expert - Interactive Mode")
    print("=" * 60)
    print("Type 'quit' or 'exit' to end the session.")
    print("Type 'clear' to reset conversation context.")
    print("=" * 60 + "\n")
    
    while True:
        try:
            user_input = input("\n[You]: ").strip()
            
            if not user_input:
                continue
            
            if user_input.lower() in ["quit", "exit"]:
                print("\nGoodbye!")
                break
            
            if user_input.lower() == "clear":
                print("\n[Context cleared]")
                continue
            
            print("\n[Assistant]: ", end="", flush=True)
            response = generate_response(model, tokenizer, user_input, system_prompt)
            print(response)
            
        except KeyboardInterrupt:
            print("\n\nInterrupted. Goodbye!")
            break


def main():
    parser = argparse.ArgumentParser(
        description="Chat with your fine-tuned Security Domain Model",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    
    parser.add_argument(
        "--model", "-m",
        default="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
        help="Base model name or path",
    )
    parser.add_argument(
        "--adapter", "-a",
        default="lora-adapters",
        help="Path to LoRA adapter directory",
    )
    parser.add_argument(
        "--prompt", "-p",
        default=None,
        help="Single prompt to process (omit for interactive mode)",
    )
    parser.add_argument(
        "--system",
        default="security",
        choices=list(SYSTEM_PROMPTS.keys()),
        help="System prompt preset",
    )
    parser.add_argument(
        "--max-tokens",
        default=512,
        type=int,
        help="Maximum tokens to generate",
    )
    parser.add_argument(
        "--temperature",
        default=0.7,
        type=float,
        help="Sampling temperature (higher = more creative)",
    )
    parser.add_argument(
        "--cpu",
        action="store_true",
        help="Force CPU inference",
    )
    
    args = parser.parse_args()
    
    # Load model
    model, tokenizer = load_model(args.model, args.adapter, use_gpu=not args.cpu)
    system_prompt = SYSTEM_PROMPTS.get(args.system, "")
    
    if args.prompt:
        # Single prompt mode
        response = generate_response(
            model, tokenizer, args.prompt, system_prompt,
            max_new_tokens=args.max_tokens,
            temperature=args.temperature,
        )
        print(response)
    else:
        # Interactive mode
        interactive_mode(model, tokenizer, system_prompt)


if __name__ == "__main__":
    main()