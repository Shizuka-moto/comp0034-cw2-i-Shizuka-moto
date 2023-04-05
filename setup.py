# Import the required module
from setuptools import setup

# Configure the setup function
setup(
    # Provide the package name
    name="comp0034-cw2-i-Shizuka-moto",

    # Provide the package version
    version="1.0",

    # List the packages included in the distribution
    packages=["flaskapp"],

    # Include package data files
    include_package_data=True,

    # List the dependencies required for the package
    install_requires=[
        "flask",
        "pandas",
        "flask-sqlalchemy",
        "openpyxl",
        "flask-wtf",
        "flask-login",
    ],
)