from setuptools import setup, find_packages

setup(
    name="screenium",
    version="0.1.0",
    author="Cass Chin",
    author_email="casschin@gmail.com",
    description="Python wrapper for Appium",
    license="MIT",
    keywords="python appium selenium",
    url="https://github.com/casschin/screenium",
    packages=find_packages(),
    install_requires=["selenium", "Appium-Python-Client"]
)
