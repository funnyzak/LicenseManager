import base64
import os
import json
import logging
from datetime import datetime

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    return logging.getLogger(__name__)

def save_to_file(data, filename):
    """Helper function to save data to file"""
    try:
        with open(filename, 'w') as f:
            if isinstance(data, (dict, list)):
                json.dump(data, f)
            else:
                f.write(str(data))
        return True
    except Exception as e:
        logging.error(f"Error saving to file: {e}")
        return False

def load_from_file(filename):
    """Helper function to load data from file"""
    try:
        with open(filename, 'r') as f:
            if filename.endswith('.json'):
                return json.load(f)
            return f.read()
    except Exception as e:
        logging.error(f"Error loading from file {filename}: {e}")
        return None

def get_expiry_date(timestamp):
    """Convert timestamp to readable date"""
    return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

def is_base64_encoded(data):
    """Check if data is base64 encoded"""
    try:
        return base64.b64encode(base64.b64decode(data)) == data
    except Exception:
        return False