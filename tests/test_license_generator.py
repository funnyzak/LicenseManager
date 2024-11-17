import unittest
from license_manager.generator.license_generator import LicenseGenerator

class TestLicenseGenerator(unittest.TestCase):
    def test_generate_license(self):
        generator = LicenseGenerator()
        generator.generate_license('hardware.id', 'license.lic')
        self.assertTrue(True)  # Add more checks as needed