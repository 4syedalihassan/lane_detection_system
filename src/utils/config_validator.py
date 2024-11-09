# src/utils/config_validator.py
def validate_config(config):
    required_keys = ['camera', 'preprocessing', 'detection', 'tracking']
    for key in required_keys:
        if key not in config:
            raise ValueError(f"Missing configuration for: {key}")
