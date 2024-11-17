import unittest
from license_manager.hardware.collector import HardwareCollector

class TestHardwareInfo(unittest.TestCase):
    def test_collect_hardware_info(self):
        info = HardwareCollector().collect_hardware_info()
        self.assertIsNotNone(info)