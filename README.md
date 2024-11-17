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
    ├── setup.py                           # 项目配置文件
    ├── examples/                          # 示例代码目录
    │   └── simple_usage.py                # 简单用法示例
    ├── tests/                             # 测试代码目录
    │   └── test_hardware_info.py          # 许可证验证测试
    └── license_manager/                   # LicenseManager 库目录
        ├── hardware/                      # 硬件信息采集模块
        │   ├── collector.py               # 硬件信息采集器
        │   └── fingerprint.py             # 硬件指纹生成器
        ├── generator/                     # 许可证生成模块
        │   └── license_generator.py       # 许可证生成器
        ├── validator/                     # 许可证验证模块
        │   └── license_validator.py       # 许可证验证器
        ├── crypto/                        # 加密模块
        │   └── encryption.py              # 加密工具
        └── utils/                         # 工具模块
            └── helpers.py                 # 辅助工具
```
```
## 开发

```bash
# 安装依赖
pip install -r requirements.txt

# 安装包
pip install -e .

# 运行示例
python -m examples.simple_usage

# 验证安装
python -c "import license_manager"
```

## 测试

运行测试：

```bash
# 运行所有测试
python3 -m unittest discover -s tests

# 运行单个测试
python -m unittest tests.test_filename
```

## 许可证

MIT
