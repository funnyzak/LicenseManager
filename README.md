# LicenseManager

LicenseManager 是一个 Python 库，用于管理软件许可证。提供硬件信息采集、许可证生成和验证功能。

## 功能

- 硬件信息采集和指纹生成
- 加密的许可证文件生成
- 基于时间戳的有效期验证
- 特性控制和用户数量限制

## 安装

使用 pip 安装 LicenseManager：

```bash
pip install -r requirements.txt
```

## 使用方法

### 简单用法

```python
from license_manager.hardware.fingerprint import HardwareFingerprint
from license_manager.generator.license_generator import LicenseGenerator
from license_manager.validator.license_validator import LicenseValidator

# 生成硬件指纹
hardware_id = 'hardware.id'
license_lic = 'license.lic'

fingerprint = HardwareFingerprint()
fingerprint.save_fingerprint(hardware_id)

# 生成许可证
generator = LicenseGenerator()
generator.generate_license(
    hardware_id_file=hardware_id,
    license_file=license_lic,
    license_options={
        'expiry_days': 365,
        'features': ['basic'],
        'max_users': 1
    }
)

# 验证许可证
# validator = LicenseValidator()
# is_valid = validator.validate_license('license.lic')
# print(f'许可证有效: {is_valid}')
```

### 高级用法

请参考 **examples/advanced_usage.py** 文件以了解更多高级用法。

## 项目结构

```plaintext
    ├── setup.py
    ├── examples/
    │   ├── __init__.py
    │   ├── simple_usage.py
    │   └── advanced_usage.py
    ├── tests/
    │   ├── __init__.py
    │   ├── test_hardware_info.py
    │   ├── test_license_generator.py
    │   └── test_license_validator.py
    └── license_manager/
        ├── __init__.py
        ├── hardware/
        │   ├── __init__.py
        │   ├── collector.py
        │   └── fingerprint.py
        ├── generator/
        │   ├── __init__.py
        │   └── license_generator.py
        ├── validator/
        │   ├── __init__.py
        │   └── license_validator.py
        ├── crypto/
        │   ├── __init__.py
        │   └── encryption.py
        └── utils/
            ├── __init__.py
            └── helpers.py
```
## 开发

```bash
# 安装依赖
pip install -r requirements.txt

# 运行示例
python examples/simple_usage.py

# 安装包
python setup.py install

# 验证安装
python -c "import license_manager"
```

## 测试

运行测试：

```bash
pytest tests/
```

## 许可证

MIT
