from setuptools import setup
from setuptools import find_packages

setup(
    name='sales-taxes',
    version='1.0.0',
    description='This package calculates total price and sales taxes of items given by user.',
    author='Ehsan Attar',
    author_email='ehsanattar@gmail.com',
    packages=find_packages(exclude='test'),
    entry_points={
        'console_scripts': [
            'sales-taxes-cli = sales_taxes.main:main',
        ],
    },
)
