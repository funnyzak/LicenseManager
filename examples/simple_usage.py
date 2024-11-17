from license_manager.generator.license_generator import LicenseGenerator
from license_manager.validator.license_validator import LicenseValidator

hardware_id_file = 'hardware.id'
license_file = 'license.lic'

# Generate license
generator = LicenseGenerator()
generator.generate_license(hardware_id_file, license_file)

# Validate license
validator = LicenseValidator()
is_valid = validator.validate_license(license_file, hardware_id_file)
print(f'License valid: {is_valid}')