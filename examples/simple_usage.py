from license_manager.hardware.collector import HardwareCollector
from license_manager.hardware.fingerprint import HardwareFingerprint
from license_manager.generator.license_generator import LicenseGenerator
from license_manager.validator.license_validator import LicenseValidator
from license_manager.crypto.encryption import generate_key

# 生成硬件指纹
hardware_file = 'hardware.json'
hardware_id_file = 'hardware.id'
fingerprint_file = 'fingerprint.json'
license_lic = 'license.lic'
license_key = generate_key()

collector = HardwareCollector()
collector.save_hardware_info(hardware_id_file, base64_encode=True)
collector.save_hardware_info(hardware_file, base64_encode=False)

fingerprint = HardwareFingerprint()
fingerprint.save_fingerprint(hardware_id_file, fingerprint_file)

# 生成许可证
generator = LicenseGenerator()
generator.generate_license(
    hardware_id_file=hardware_file,
    license_file=license_lic,
    license_key=license_key,
    license_options={}
)

# 验证许可证
Validator = LicenseValidator()
Validator.validate_license(license_lic, validate_footprint=True, license_key=license_key)