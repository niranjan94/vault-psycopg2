#!/usr/bin/env python
# -* encoding: utf-8 *-
import os
from setuptools import setup

HERE = os.path.dirname(__file__)

try:
    long_description = open(os.path.join(HERE, 'README.md')).read()
except IOError:
    long_description = None


setup(
    name="vault-psycopg2",
    version="0.1.0",
    packages=["vault_psycopg2"],
    classifiers=[],
    url="https://github.com/niranjan94/vault-psycopg2",
    author="Niranjan Rajendran (@niranjan94)",
    author_email="me@niranjan.io",
    maintainer="Niranjan Rajendran (@niranjan94)",
    maintainer_email="me@niranjan.io",
    description="Helper classes to integrate psycopg2 with Vault",
    long_description=long_description,
    install_requires=[
        "hvac>=0.3.0",
        "psycopg2>=2.0.0",
    ],
)
