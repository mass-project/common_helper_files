import os
import subprocess
from setuptools import setup, find_packages

setup(
    name="common_helper_files",
    version=subprocess.check_output(['git', 'describe', '--always'], cwd=os.path.dirname(os.path.abspath(__file__))).strip().decode('utf-8'),
    packages=find_packages(),
    install_requires=[
        'hurry.filesize >= 0.9'
    ],
    description="file operation helper functions"
)
