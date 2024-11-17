from setuptools import setup, find_packages

setup(
    name='LicenseManager',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'cryptography>=3.4.7,<4.0',
        'WMI>=1.4.9,<2.0',
        'psutil>=5.8.0,<=6.0.0',
    ],
    author='funnyzak',
    author_email='silenceace@gmail.com',
    description='A package for managing software licenses.',
    url='https://github.com/funnyzak/LicenseManager',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)