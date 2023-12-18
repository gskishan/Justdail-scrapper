from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in just_dial/__init__.py
from just_dial import __version__ as version

setup(
	name="just_dial",
	version=version,
	description="General Use",
	author="Harish",
	author_email="harish@01",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
