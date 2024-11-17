import hashlib
import datetime
import json
import base64
from ..utils.helpers import setup_logging, save_to_file, load_from_file, is_base64_encoded
from .collector import HardwareCollector


class HardwareFingerprint:
    def __init__(self):
        self.logger = setup_logging()

    def generate_fingerprint(self, hardware_dict=None):
        """Generate a unique hardware fingerprint
        Args:
            hardware_info (dict): Hardware information dictionary
        Returns:
            str: Hardware fingerprint
        """
        try:
            hardware_info_str = str(hardware_dict or HardwareCollector().collect_hardware_info())
            fingerprint = hashlib.sha256(hardware_info_str.encode()).hexdigest()
            return fingerprint
        except Exception as e:
            self.logger.error(f"Error generating fingerprint: {e}")
            return None

    def save_fingerprint(self, hardware_id_file="hardware.id", filename="fingerprint.json"):
        """Save hardware fingerprint to file
        Args:
            hardware_id_file (str): Path to hardware ID file
            filename (str): Output filename
        Returns:
            bool: True if successful, False otherwise
        """
        hardware_info = HardwareCollector().hareware_info_from_id_file(hardware_id_file)
    
        fingerprint = self.generate_fingerprint(hardware_dict=hardware_info)
        if fingerprint:
            data = {
                "fingerprint": fingerprint,
                "hardware_info": hardware_info,
                "timestamp": datetime.datetime.now().isoformat(),
            }
            return save_to_file(data, filename)
        return False
    

    def verify_fingerprint(self, hardware_id_file, stored_fingerprint):
        """Verify hardware fingerprint
        Args:
            hardware_id_file (str): Path to hardware ID file
            stored_fingerprint (str): Stored fingerprint
        Returns:
            bool: True if fingerprints match, False otherwise
        """
        hardware_info = HardwareCollector().hareware_info_from_id_file(hardware_id_file)
        hardware_fingerprint = self.generate_fingerprint(hardware_dict=hardware_info)
        return hardware_fingerprint == stored_fingerprint
