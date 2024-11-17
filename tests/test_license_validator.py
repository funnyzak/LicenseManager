import unittest
from license_manager.validator.license_validator import LicenseValidator

class TestLicenseValidator(unittest.TestCase):
    def test_validate_license(self):
        validator = LicenseValidator()
        is_valid = validator.validate_license('license.lic', 'hardware.id')
        self.assertTrue(is_valid)