from setuptools import setup, find_packages

setup(
    name="nt-telegram-bot",
    version="0.1.0",
    author="SN02",
    description="A simple pyton telegram libary",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ziyocamp/py-gram-bot",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
)
