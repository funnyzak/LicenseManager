import unittest
from license_manager.hardware.collector import collect_hardware_info

class TestHardwareInfo(unittest.TestCase):
    def test_collect_hardware_info(self):
        info = collect_hardware_info()
        self.assertIsNotNone(info)