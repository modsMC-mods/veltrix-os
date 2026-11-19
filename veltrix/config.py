import json
from pathlib import Path

CONFIG_DIR = Path.home() / ".config" / "veltrix-os"
CONFIG_FILE = CONFIG_DIR / "config.json"
DEFAULT_CONFIG = {"theme": "midnight", "safe_terminal": True, "fullscreen": False}

def load_config():
    try:
        data = json.loads(CONFIG_FILE.read_text(encoding="utf-8")) if CONFIG_FILE.exists() else {}
    except (OSError, json.JSONDecodeError):
        data = {}
    return {**DEFAULT_CONFIG, **data}

def save_config(data):
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    CONFIG_FILE.write_text(json.dumps({**DEFAULT_CONFIG, **data}, indent=2), encoding="utf-8")
