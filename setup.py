from setuptools import setup

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name = 'num2word',
    version = '1.0.0',
    description = 'Convert any number to word',
    py_modules = ['num2word'],
    package_dir = {'': 'src'},
    classifiers = [
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU general Public License v2",
        "Operating System :: OS Independent",
    ],
    long_description = long_description,
    long_description_content_type = "text/markdown",
)