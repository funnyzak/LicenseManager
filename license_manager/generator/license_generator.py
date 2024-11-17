import time
import json
from ..crypto.encryption import encrypt
from ..utils.helpers import setup_logging, save_to_file
from ..hardware.fingerprint import HardwareFingerprint
from ..hardware.collector import HardwareCollector

class LicenseGenerator:
    def __init__(self):
        self.logger = setup_logging()
        self.fingerprint = HardwareFingerprint()

    def generate_license(self, hardware_id_file, license_file, license_options=None, license_key=None):
        """
        Generate encrypted license file
        
        Args:
            hardware_id_file: Path to hardware ID file
            license_file: Path to output license file
            license_options: Dictionary containing license options
        """
        try:
            # Load hardware info
            hardware_info = HardwareCollector().hareware_info_from_id_file(hardware_id_file)
            hardware_fingerprint = self.fingerprint.generate_fingerprint(hardware_dict=hardware_info)

            if not hardware_fingerprint:
                return False
            
            # Prepare license data
            current_time = int(time.time())
            license_data = {
                'hardware_fingerprint': hardware_fingerprint,
                'hardware_info': hardware_info,
                'issued_at': current_time,
                'expires_at': current_time + (license_options.get('expiry_days', 365) * 86400),
                'features': license_options.get('features', ['basic']),
                'max_users': license_options.get('max_users', 1)
            }

            self.logger.info(f"License data: {json.dumps(license_data, indent=4)}")

            # Encrypt and save license
            encrypted_license = encrypt(json.dumps(license_data), key=license_key)
            encrypted_license_str = encrypted_license.decode()

            if save_to_file(encrypted_license_str, license_file):
                self.logger.info(f"License generated successfully: {license_file}")
                return True
                
            return False

        except Exception as e:
            self.logger.error(f"Error generating license: {e}")
            return False