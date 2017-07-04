from setuptools import setup, find_packages
from common_helper_files import __version__

setup(
    name="common_helper_files",
    version=__version__,
    packages=find_packages(),
    install_requires=[
        'hurry.filesize >= 0.9'
    ],
    description="file operation helper functions",
    license="MIT License"
)
