[![Build Status](https://travis-ci.com/niranjan94/vault-psycopg2.svg?branch=master)](https://travis-ci.com/niranjan94/vault-psycopg2) [![PyPI version](https://badge.fury.io/py/vault-psycopg2.svg)](https://badge.fury.io/py/vault-psycopg2)

### vault-psycopg2

> Helper classes to integrate psycopg2 with Vault


#### Usage:


```bash
pip install vault-psycopg2
```

```python
from vault_psycopg2 import VaultPsycopg

vp = VaultPsycopg(
    database_config={
        'host': 'localhost',
        'dbname': 'name_of_database'
    },
    vault_config={
        'server': 'http://127.0.0.1:8200',
        'connection_mode': 'ec2',
        'nonce': '5daa3d21-4e21-4bd5-8978-fcb81e658d8b',
        'role': 'some-instance'
    }
)

# An instance of psycopg2.Connection that is properly authenticated
vp.connection
```

##### Other examples of vault config:

```python
vault_config={
    'server': 'http://127.0.0.1:8200',
    'connection_mode': 'token',
    'token': '5daa3d21-4e21-4bd5-8978-fcb81e658d8b'
}
```

```python
vault_config={
    'server': 'http://127.0.0.1:8200',
    'connection_mode': 'userpass',
    'username': 'john.doe',
    'password': 'xyzzyabc'
}
```

