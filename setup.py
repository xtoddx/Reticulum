import setuptools

exec(open("RNS/_version.py", "r").read())

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rns",
    version=__version__,
    author="Mark Qvist",
    author_email="mark@unsigned.io",
    description="Self-configuring, encrypted and resilient mesh networking stack for LoRa, packet radio, WiFi and everything in between",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/markqvist/reticulum",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['cryptography>=3.4.7', 'pyserial', 'netifaces>=0.10.4', 'six'],
    python_requires='>=3.6',
)
