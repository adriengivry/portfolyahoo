from setuptools import setup, find_packages

setup(
    name="portfolyahoo",
    version="1.0",
    author="Adrien GIVRY",
    author_email="contact@adrien-givry.com",
    description="Unofficial API to manage your portfolios on Yahoo Finance",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="MIT",
    packages=find_packages(),
    url="https://github.com/adriengivry/portfolyahoo",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords="yahoo finance, finance, stocks, etfs, mutual funds, portfolio",
    python_requires=">=3.8",
)
