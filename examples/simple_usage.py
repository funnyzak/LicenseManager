from license_manager.hardware.collector import HardwareCollector
from license_manager.hardware.fingerprint import HardwareFingerprint
from license_manager.generator.license_generator import LicenseGenerator
from license_manager.validator.license_validator import LicenseValidator
from license_manager.crypto.encryption import generate_key
import logging

def main():
    logger = logging.getLogger(__name__)

    # 生成硬件指纹
    hardware_file = 'hardware.json'
    hardware_id_file = 'hardware.id'
    fingerprint_file = 'fingerprint.json'
    license_lic = 'license.lic'
    license_key = generate_key()

    collector = HardwareCollector()
    # 保存硬件信息
    collector.save_hardware_info(hardware_id_file, base64_encode=True)
    collector.save_hardware_info(hardware_file, base64_encode=False)

    fingerprint = HardwareFingerprint()
    # 保存指纹信息
    fingerprint.save_fingerprint(hardware_id_file, fingerprint_file)

    # 生成许可证
    generator = LicenseGenerator()

    generator.generate_license(
        hardware_id_file=hardware_file,
        license_file=license_lic,
        license_key=license_key,
        license_options={
            'expiry_days': 365,
            'features': ['basic', 'premium'],
            'max_users': 5
        }
    )

    # 验证许可证
    Validator = LicenseValidator()
    valid_rlt = Validator.validate_license(license_lic, validate_footprint=True, license_key=license_key)
    if valid_rlt['valid']:
        logger.info("License is valid!")
        logger.info(f"Expires on: {valid_rlt['expiry']}")
        logger.info(f"Features: {valid_rlt['features']}")
        logger.info(f"Max users: {valid_rlt['max_users']}")

if __name__ == '__main__':
    main()