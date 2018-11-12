import threading

import psycopg2


class VaultPsycopg:
    _instance = None
    _lock = threading.Lock()
    _vault_wrapper = None

    _database_connection = None

    database_config = {}
    vault_config = {}

    def __new__(cls, **kwargs):
        if VaultPsycopg._instance is None:
            with VaultPsycopg._lock:
                if VaultPsycopg._instance is None:
                    VaultPsycopg._instance = super(VaultPsycopg, cls).__new__(cls, **kwargs)
        return VaultPsycopg._instance

    def __init__(self, database_config=None, vault_config=None):
        self.vault_config = vault_config
        self.database_config = database_config
        if vault_config:
            from vault_psycopg2.vault import Vault
            self._vault_wrapper = Vault(**vault_config)

    @property
    def connection(self):

        if self._database_connection:
            try:
                cursor = self._database_connection.cursor()
                cursor.execute('SELECT 1')
                return self._database_connection
            except psycopg2.OperationalError:
                pass

        if self._vault_wrapper and self.database_config.get('role') is not None:
            credentials = self._vault_wrapper.client.read('database/creds/' + self.database_config.get('role'))
            user = credentials['data']['username']
            password = credentials['data']['password']
        else:
            user = self.database_config.get('user')
            password = self.database_config.get('password')

        self._database_connection = psycopg2.connect(
            host=self.database_config.get('host'),
            port=self.database_config.get('port'),
            dbname=self.database_config.get('dbname'),
            user=user,
            password=password,
        )

        return self._database_connection
