from setuptools import find_packages, setup
reqs = open("requirements.txt").read().splitlines()

setup(
    name="gentaxo",
    version="0.1.0",
    description="",
    packages=find_packages(),
    install_requires=reqs,
)
