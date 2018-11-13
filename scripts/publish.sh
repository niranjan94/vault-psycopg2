#!/usr/bin/env bash

rm -rf build dist vault_psycopg2.egg-info
python3 setup.py sdist bdist_wheel
twine check dist/*
twine upload dist/*
rm -rf build dist vault_psycopg2.egg-info
