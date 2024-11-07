# setup.py
from setuptools import setup, find_packages

setup(
    name="calpi",
    version="0.1",
    packages=find_packages(),
    author="DevMaster42",  # Your alias here
    author_email="your.email@example.com",  # Or leave it blank if you prefer
    description="Calculate Pi easily with the Calpi library",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/mylibrary",  
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
