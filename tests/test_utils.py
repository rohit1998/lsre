"""Test the regex functions."""

import pytest

from lsre.utils import enforce_str_arg


def test_enforce_str_arg_string_input() -> None:
    """Test wrapper function for valid input string datatype."""

    @enforce_str_arg
    def echo(text: str) -> str:
        """Return the same string supplied."""
        return text

    assert echo('hello') == 'hello'


@pytest.mark.parametrize(
    'bad_value',
    [
        123,
        None,
        [],
        {},
    ],
)
def test_enforce_str_arg_non_string_input(bad_value: str) -> None:
    """Test wrapper function for invalid input string datatype."""

    @enforce_str_arg
    def noop(text: str) -> bool:
        return True

    with pytest.raises(TypeError):
        noop(bad_value)
