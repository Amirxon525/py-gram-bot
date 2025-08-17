from setuptools import setup, find_packages

setup(
    name="tigram_nt_bot",
    version="0.1.0",
    author="SN2",
    description="A simple pyton telegram libary",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Amirxon525/py-gram-bot",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
)
