from distutils.core import setup
from setuptools import find_packages

setup(
    name='snowflake',
    version='0.1',
    author='Jindong Li',
    author_email='jindong.li@fau.de',
    packages=find_packages(),
    install_requires=['numpy', 'turtle', 'random']
)