"""Configuration management for AVAGuard CLI."""

import configparser
import os
import logging
from pathlib import Path
from typing import Dict, List, Optional

logger = logging.getLogger(__name__)

def resolve_config_path(config_path_param: Optional[str] = None) -> Path:
    # 1. Environment Variable
    env_path = os.environ.get('AVAGUARD_CONFIG')
    if env_path:
        return Path(env_path)
        
    # 2. Parameter (if not default config.ini or if it already exists)
    if config_path_param:
        param_path = Path(config_path_param)
        if param_path.exists() or config_path_param != 'config.ini':
            return param_path

    # 3. Home folder paths
    home = Path.home()
    if os.name == 'nt':
        home_path = home / '.avaguard' / 'config.ini'
    else:
        home_path = home / '.config' / 'avaguard' / 'config.json'
        
    if home_path.exists():
        return home_path
        
    # 4. Fallback: if home path doesn't exist, we default to it to keep clean configs
    return home_path

class Config:
    """Manages application configuration from config.ini or config.json files."""
    
    def __init__(self, config_path: Optional[str] = None):
        """
        Initialize configuration.
        
        Args:
            config_path: Path to configuration file
        """
        resolved_path = resolve_config_path(config_path)
        self.config_path = str(resolved_path)
        self.config = configparser.ConfigParser()
        
        # Set default values
        self._set_defaults()
        
        if not resolved_path.exists():
            print(f"⚠  Configuration file not found: {self.config_path}")
            print("   Creating default configuration...")
            self._create_default_config()
        else:
            self._load_config()
            
        self._enforce_file_permissions(resolved_path)
        self._ensure_output_dirs()
    
    def _set_defaults(self):
        """Set default configuration values."""
        # Set default values for all sections
        self.config['azure'] = {
            'tenant_id': 'YOUR_TENANT_ID',
            'client_id': 'YOUR_CLIENT_ID', 
            'client_secret': 'YOUR_CLIENT_SECRET'
        }
        
        self.config['scan'] = {
            'tier': 'free',
            'use_mock_data': 'true',
            # 'mock_data_file': 'AVAMockData.json',
            'mock_data_file': 'mock_data/enterprise_dataset.json',
            'default_checks': ''
        }
        
        self.config['output'] = {
            'reports_dir': 'output/reports',
            'logs_dir': 'output/logs',
            'format': 'both'
        }
        
        self.config['advanced'] = {
            'timeout': '30',
            'max_retries': '3',
            'retry_delay': '5'
        }
        
        self.config['portal'] = {
            'url': 'http://localhost:8000'
        }
    
    def _create_default_config(self):
        """Create a default configuration file."""
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(self.config_path) if os.path.dirname(self.config_path) else '.', exist_ok=True)
        
        if self.config_path.endswith('.json'):
            import json
            data = {}
            for section in self.config.sections():
                data[section] = dict(self.config[section])
            with open(self.config_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4)
        else:
            with open(self.config_path, 'w') as f:
                self.config.write(f)
        
        print(f"✓ Default configuration created at: {self.config_path}")
        print("  Please edit this file to configure Azure credentials for live mode.")
        
    def _load_config(self):
        """Load configuration from file."""
        if self.config_path.endswith('.json'):
            import json
            try:
                with open(self.config_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                for section, options in data.items():
                    if not self.config.has_section(section):
                        self.config.add_section(section)
                    for key, val in options.items():
                        self.config.set(section, key, str(val))
            except Exception as e:
                logger.error(f"Error loading JSON config: {e}")
        else:
            self.config.read(self.config_path)
            
    def _enforce_file_permissions(self, path: Path):
        """
        Enforce strict permissions on the configuration file.
        On Unix/macOS: chmod 600 (owner read/write only).
        On Windows: restrict ACL to owner only using icacls.
        """
        try:
            if os.name != 'nt':
                path.chmod(0o600)
                logger.info(f"Enforced 600 permissions on Unix: {path}")
            else:
                import subprocess
                username = os.environ.get('USERNAME')
                if username:
                    subprocess.run(
                        ['icacls', str(path), '/inheritance:r', '/grant', f'{username}:F'],
                        capture_output=True, check=True
                    )
                    logger.info(f"Enforced restricted ACL for {username} on Windows: {path}")
        except Exception as e:
            logger.warning(f"Could not enforce strict file permissions on {path}: {e}")
    
    def _ensure_output_dirs(self):
        """Create output directories if they don't exist."""
        Path(self.reports_dir).mkdir(parents=True, exist_ok=True)
        Path(self.logs_dir).mkdir(parents=True, exist_ok=True)
        
        # Also create mock data directory if needed
        mock_data_dir = os.path.dirname(self.mock_data_file)
        if mock_data_dir:
            Path(mock_data_dir).mkdir(parents=True, exist_ok=True)
    
    @property
    def tenant_id(self) -> str:
        """Azure AD Tenant ID."""
        return self.config['azure'].get('tenant_id', 'YOUR_TENANT_ID')
    
    @property
    def client_id(self) -> str:
        """Azure App Registration Client ID."""
        return self.config['azure'].get('client_id', 'YOUR_CLIENT_ID')
    
    @property
    def client_secret(self) -> str:
        """Azure App Registration Client Secret."""
        return self.config['azure'].get('client_secret', 'YOUR_CLIENT_SECRET')
    
    @property
    def tier(self) -> str:
        """Azure subscription tier (free or premium)."""
        return self.config['scan'].get('tier', 'free').lower()
    
    @property
    def is_premium(self) -> bool:
        """Check if premium tier is configured."""
        return self.tier == 'premium'
    
    @property
    def default_checks(self) -> List[str]:
        """Get list of default checks to run."""
        checks_str = self.config['scan'].get('default_checks', '')
        if not checks_str:
            return []
        return [c.strip() for c in checks_str.split(',') if c.strip()]
    
    @property
    def reports_dir(self) -> str:
        """Directory for generated reports."""
        return self.config['output'].get('reports_dir', 'output/reports')
    
    @property
    def logs_dir(self) -> str:
        """Directory for log files."""
        return self.config['output'].get('logs_dir', 'output/logs')
    
    @property
    def output_format(self) -> str:
        """Report output format."""
        return self.config['output'].get('format', 'both')
    
    @property
    def timeout(self) -> int:
        """API request timeout in seconds."""
        return int(self.config['advanced'].get('timeout', '30'))
    
    @property
    def max_retries(self) -> int:
        """Maximum number of API retry attempts."""
        return int(self.config['advanced'].get('max_retries', '3'))
    
    @property
    def retry_delay(self) -> int:
        """Delay between retry attempts in seconds."""
        return int(self.config['advanced'].get('retry_delay', '5'))
    
    @property
    def use_mock_data(self) -> bool:
        """Check if mock data mode is enabled."""
        return self.config['scan'].getboolean('use_mock_data', True)
    
    @property
    def mock_data_file(self) -> str:
        """Path to mock data JSON file.""" 
        return self.config['scan'].get('mock_data_file', 'mock_data/enterprise_dataset.json')
    
    @property
    def portal_url(self) -> str:
        """Returns the configured portal URL with fallback to localhost default."""
        url = self.config['portal'].get('url', 'http://localhost:8000')
        if not url or not url.strip():
            return 'http://localhost:8000'
        return url.strip().rstrip('/')
    
    def get_credentials(self) -> Dict[str, str]:
        """
        Get Azure credentials as dictionary.
        
        Returns:
            Dictionary with tenant_id, client_id, client_secret
        """
        return {
            'tenant_id': self.tenant_id,
            'client_id': self.client_id,
            'client_secret': self.client_secret
        }
    
    def is_azure_configured(self) -> bool:
        """
        Check if Azure credentials are properly configured.
        
        Returns:
            bool: True if Azure credentials are set (not default values)
        """
        return (self.tenant_id not in ['', 'YOUR_TENANT_ID'] and 
                self.client_id not in ['', 'YOUR_CLIENT_ID'] and 
                self.client_secret not in ['', 'YOUR_CLIENT_SECRET'])