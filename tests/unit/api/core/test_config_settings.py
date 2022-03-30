import os
from unittest import mock

import pytest

from api.core.config import settings


@pytest.fixture
def mock_env_vars(monkeypatch):
    monkeypatch.setenv("DB_TYPE", "fakeDbType")
    monkeypatch.setenv("DB_USER", "fakeDbUser")
    monkeypatch.setenv("DB_PASSWORD", "fakeDbPass")
    monkeypatch.setenv("DB_CLUSTER", "fakeDbCluter")
    monkeypatch.setenv("DB_NAME", "fakeDbName")

@pytest.fixture(name='config')
def create_config():
    return settings

@pytest.mark.parametrize("env_var", ["DB_TYPE", "DB_USER", "DB_PASSWORD", "DB_CLUSTER", "DB_NAME"])
def test_database_credentials_load_when_env_vars_is_empty(mock_env_vars, config, env_var):

    with mock.patch.dict(os.environ, {env_var: ''}):
        with pytest.raises(ValueError) as exception:
            config.get_database_credentials()
        assert f'{env_var} environment variable is missing!' == str(exception.value)

@pytest.mark.parametrize("env_var", ["DB_TYPE", "DB_USER", "DB_PASSWORD", "DB_CLUSTER", "DB_NAME"])
def test_database_credentials_load_when_env_vars_is_(mock_env_vars, monkeypatch, config, env_var):
    monkeypatch.delenv(env_var, raising=True)

    with pytest.raises(ValueError) as exception:
        config.get_database_credentials()
    assert f'{env_var} environment variable is missing!' == str(exception.value)

def test_credentials_load(mock_env_vars, config):
    credentials = config.get_database_credentials()
    
    assert credentials["DB_TYPE"] == "fakeDbType"
    assert credentials["DB_USER"] == "fakeDbUser"
    assert credentials["DB_PASSWORD"] == "fakeDbPass"
    assert credentials["DB_CLUSTER"] == "fakeDbCluter"
    assert credentials["DB_NAME"] == "fakeDbName"