"""Test the module."""

import os

import pytest

from lsre.module import MyModule


@pytest.fixture
def my_module() -> MyModule:
    """Init the module."""
    return MyModule('Rohit')


@pytest.fixture
def set_secret(monkeypatch: pytest.MonkeyPatch) -> None:
    """Set the secret."""
    monkeypatch.setenv('MY_SECRET', 'my_secret')


@pytest.fixture
def delete_secret(monkeypatch: pytest.MonkeyPatch) -> None:
    """Delete the secret if it exists."""
    monkeypatch.delenv('MY_SECRET', raising=False)


def test_run(my_module: MyModule) -> None:
    """Test the run method."""
    greeting = my_module.run()
    if greeting != 'Hello Rohit':
        pytest.fail(
            f'Expected greeting to be "Hello Rohit", but got "{greeting}"',
        )


@pytest.mark.usefixtures('set_secret')
def test_get_secret(my_module: MyModule) -> None:
    """Test the get_secret method."""
    secret = my_module.get_secret()
    if secret != os.getenv('MY_SECRET'):
        pytest.fail(f'Expected secret to be "my_secret", but got "{secret}"')


@pytest.mark.usefixtures('delete_secret')
def test_get_secret_no_secret(my_module: MyModule) -> None:
    """Test the get_secret method when the secret is not set."""
    with pytest.raises(ValueError, match='Secret not found'):
        my_module.get_secret()
