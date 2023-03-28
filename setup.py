from setuptools import setup


setup(
    name="comp0034-cw2-i-Shizuka-moto",
    version="1.0",
    packages=["flaskapp"],
    include_package_data=True,
    install_requires=["flask", "pandas", "flask-sqlalchemy", "openpyxl", "flask-wtf", "flask-login"],
)