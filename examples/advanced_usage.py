from license_manager.hardware.fingerprint import HardwareFingerprint
from license_manager.generator.license_generator import LicenseGenerator
from license_manager.validator.license_validator import LicenseValidator
from license_manager.utils.helpers import get_expiry_date
import logging

def main():
    logger = logging.getLogger(__name__)

    # Generate hardware fingerprint
    fingerprint = HardwareFingerprint()
    if not fingerprint.save_fingerprint('hardware.id'):
        logger.error("Failed to generate hardware fingerprint")
        return

    # Generate license with expiry and features
    generator = LicenseGenerator()
    license_data = {
        'expiry_days': 365,
        'features': ['basic', 'premium'],
        'max_users': 5
    }
    
    if not generator.generate_license('hardware.id', 'license.lic', license_data):
        logger.error("Failed to generate license")
        return

    # Validate license
    validator = LicenseValidator()
    result = validator.validate_license('license.lic')
    
    if result['valid']:
        logger.info("License is valid!")
        logger.info(f"Expires on: {get_expiry_date(result['expiry'])}")
        logger.info(f"Features: {result['features']}")
        logger.info(f"Max users: {result['max_users']}")
    else:
        logger.error(f"License validation failed: {result['message']}")

if __name__ == '__main__':
    main()
