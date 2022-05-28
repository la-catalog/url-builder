from pathlib import Path

from setuptools import find_packages, setup

long_description = Path("README.md").read_text()

setup(
    name="url-builder",
    version="0.0.1",
    description="Create url for marketplace",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/thiagola92/url-builder",
    author="thiagola92",
    author_email="thiagola92@gmail.com",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    keywords="url, builder",
    license="MIT",
    packages=find_packages(exclude=["tests"]),
    install_requires=[],
    python_requires=">=3.10",
)
