import time
import json
from ..crypto.encryption import decrypt
from ..utils.helpers import setup_logging, load_from_file
from ..hardware.fingerprint import HardwareFingerprint
from ..hardware.collector import HardwareCollector

class LicenseValidator:
    def __init__(self):
        self.logger = setup_logging()
        self.fingerprint = HardwareFingerprint()

    def validate_license(self, license_file, license_key, validate_footprint=True):
        """
        Validate license file
        Args:
            license_file (str): Path to license file
            license_key (str): License key
            validate_footprint (bool): Validate current hardware fingerprint
        
        Returns:
            dict: Validation result with status and details
        """
        try:
            # Load and decrypt license
            encrypted_license = load_from_file(license_file)
            if not encrypted_license:
                return self._validation_failed("Could not load license file")
            self.logger.info("License loaded successfully %s", encrypted_license)

            license_data = json.loads(decrypt(encrypted_license, key=license_key))   
                     
            current_hareware_fingerprint = self.fingerprint.generate_fingerprint(hardware_dict=HardwareCollector().collect_hardware_info())

            if validate_footprint and license_data['hardware_fingerprint'] != current_hareware_fingerprint:
                return self._validation_failed("Hardware fingerprint mismatch")

            # Check expiration
            current_time = int(time.time())
            if current_time > license_data['expires_at'] or current_time < license_data['issued_at']:
                return self._validation_failed("License has expired")

            rlt = {
                'valid': True,
                'expiry': license_data['expires_at'],
                'features': license_data['features'],
                'max_users': license_data['max_users']
            }
            self.logger.info("License validation successful, details: %s", rlt)

            return rlt

        except Exception as e:
            self.logger.error(f"License validation error: {e}")
            return self._validation_failed(str(e))

    def _validation_failed(self, message):
        return {
            'valid': False,
            'message': message
        }