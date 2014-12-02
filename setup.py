from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='efpl-cf1',
    version=version,
    description='EFPL Custom Field Changes',
    author='Systematric',
    author_email='kolate.sambhaji@gmail.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
