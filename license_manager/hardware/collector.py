import psutil
import uuid
import platform
import subprocess
import json
import base64
from ..utils.helpers import setup_logging, save_to_file, load_from_file

class HardwareCollector:
    def __init__(self):
        self.logger = setup_logging()

    def get_mac_addresses(self):
        macs = []
        for interface, addrs in psutil.net_if_addrs().items():
            for addr in addrs:
                if addr.family == psutil.AF_LINK:
                    macs.append(addr.address)
        return macs

    def get_cpu_id(self):
        if platform.system() == "Windows":
            return platform.processor()
        elif platform.system() == "Darwin":
            command = "/usr/sbin/sysctl -n machdep.cpu.brand_string"
            return subprocess.check_output(command, shell=True).strip().decode()
        elif platform.system() == "Linux":
            command = "cat /proc/cpuinfo | grep 'model name' | uniq"
            return subprocess.check_output(command, shell=True).strip().decode().split(":")[1]
        return "Unknown"

    def get_board_serial(self):
        try:
            return str(uuid.UUID(int=uuid.getnode()))
        except:
            return "Unknown"

    def collect_hardware_info(self):
        return {
            'macs': self.get_mac_addresses(),
            'cpu': self.get_cpu_id(),
            'board': self.get_board_serial()
        }

    def save_hardware_info(self, filename="hardware.json", base64_encode=False):
        data = self.collect_hardware_info()

        if base64_encode:
            data = base64.b64encode(json.dumps(data).encode()).decode() 
        save_to_file(data, filename)

    def hareware_info_from_id_file(self, hardware_id_file = "hardware.id"):
        hardware_info = load_from_file(hardware_id_file)
        if not hardware_info:
            self.logger.error("Error loading hardware info")

        if isinstance(hardware_info, str):
            hardware_info = json.loads(base64.b64decode(hardware_info).decode())

        return hardware_info
# 使用示例
if __name__ == "__main__":
    collector = HardwareCollector()
    collector.save_hardware_info()