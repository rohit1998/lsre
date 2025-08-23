"""Test the regex functions."""

from typing import Any, NamedTuple

import pytest

import lsre


class Case(NamedTuple):
    """Case class."""

    text: Any
    expected: bool | None


@pytest.mark.parametrize(
    ('text', 'expected'),
    [
        Case(text='abc123', expected=True),
        Case(text='_123', expected=False),
        Case(text='12345', expected=True),
        Case(text='ABC', expected=True),
        Case(text='#67', expected=False),
    ],
)
def test_is_alphanumeric(text: str, expected: bool) -> None:
    """Test for alphanumeric.

    Args:
        text (str): input string
        expected (bool): expected output for input
    """
    assert lsre.is_alphanumeric(text=text) == expected


@pytest.mark.parametrize(
    ('text', 'expected'),
    [
        Case(text='user@example.com', expected=True),
        Case(text='user.name+tag@sub.domain.co', expected=True),
        Case(text='user_name@example.co.uk', expected=True),
        Case(text='.user@example.com', expected=False),
        Case(text='user..name@example.com', expected=False),
        Case(text='user@', expected=False),
        Case(text='@example.com', expected=False),
        Case(text='user.@example.com', expected=False),
        Case(text='user@-example.com', expected=False),
        Case(text='user@example-.com', expected=False),
        Case(text='user@sub-example.com', expected=True),
    ],
)
def test_is_email(text: str, expected: bool) -> None:
    """Test for email.

    Args:
        text (str): input string
        expected (bool): expected output for input
    """
    assert lsre.is_email(text=text) == expected


@pytest.mark.parametrize(
    ('text', 'expected'),
    [
        Case(text='http://example.com', expected=True),
        Case(text='https://example.com/path?query=1', expected=True),
        Case(text='ftp://ftp.example.org', expected=True),
        Case(text='http://127.0.0.1:8000/path', expected=True),
        Case(text='ftp://user:pass@ftp.example.org', expected=True),
        Case(text='example.com', expected=False),
        Case(text='://bad', expected=False),
        Case(text='http://localhost', expected=True),
        Case(text='http://sub-domain.example.com', expected=True),
        Case(text='ftp://user.name:pass@ftp.example.org', expected=True),
        Case(text='http://example.com:12345/path?query=1#frag', expected=True),
        Case(text='http://example.com/path-with-hyphen', expected=True),
        Case(text='http://127.0.0.1', expected=True),
        Case(text='http://[::1]', expected=False),
        Case(text='http://例子.测试', expected=False),
    ],
)
def test_is_url(text: str, expected: bool) -> None:
    """Test for URL.

    Args:
        text (str): input string
        expected (bool): expected output for input
    """
    assert lsre.is_url(text=text) == expected


@pytest.mark.parametrize(
    ('text', 'expected'),
    [
        Case(text='192.168.0.1', expected=True),
        Case(text='0.0.0.0', expected=True),  # noqa: S104
        Case(text='255.255.255.255', expected=True),
        Case(text='256.0.0.1', expected=False),
        Case(text='192.168.1', expected=False),
    ],
)
def test_is_ipv4(text: str, expected: bool) -> None:
    """Test for IPv4.

    Args:
        text (str): input string
        expected (bool): expected output for input
    """
    assert lsre.is_ipv4(text=text) == expected


@pytest.mark.parametrize(
    ('text', 'expected'),
    [
        Case(text='::1', expected=True),
        Case(text='fe80::1', expected=True),
        Case(text='2001:0db8:85a3:0000:0000:8a2e:0370:7334', expected=True),
        Case(text='2001::85a3::8a2e', expected=False),
    ],
)
def test_is_ipv6(text: str, expected: bool) -> None:
    """Test for IPv6.

    Args:
        text (str): input string
        expected (bool): expected output for input
    """
    assert lsre.is_ipv6(text=text) == expected


@pytest.mark.parametrize(
    ('text', 'expected'),
    [
        Case(text='+1-800-555-1212', expected=True),
        Case(text='8005551212', expected=True),
        Case(text='(800) 555-1212', expected=True),
        Case(text='+44 20 7946 0958', expected=True),
        Case(text='123', expected=False),
        Case(text='+123456789012345', expected=True),
        Case(text='+1234567890123456', expected=False),
        Case(text='phone', expected=False),
    ],
)
def test_is_phone_number(text: str, expected: bool) -> None:
    """Test for phone number.

    Args:
        text (str): input string
        expected (bool): expected output for input
    """
    assert lsre.is_phone_number(text=text) == expected


@pytest.mark.parametrize(
    ('text', 'expected'),
    [
        Case(text='4111 1111 1111 1111', expected=True),
        Case(text='4012888888881881', expected=True),
        Case(text='378282246310005', expected=True),
        Case(text='123456789012', expected=False),
    ],
)
def test_is_credit_card(text: str, expected: bool) -> None:
    """Test for credit card number.

    Args:
        text (str): input string
        expected (bool): expected output for input
    """
    assert lsre.is_credit_card(text=text) == expected


@pytest.mark.parametrize(
    ('text', 'expected'),
    [
        Case(text='2025-08-22', expected=True),
        Case(text='1999-12-31', expected=True),
        Case(text='2020-02-29', expected=True),
        Case(text='2000-13-01', expected=False),
        Case(text='31-12-1999', expected=False),
    ],
)
def test_is_iso_date(text: str, expected: bool) -> None:
    """Test for ISO date.

    Args:
        text (str): input string
        expected (bool): expected output for input
    """
    assert lsre.is_iso_date(text=text) == expected


@pytest.mark.parametrize(
    ('text', 'expected'),
    [
        Case(text='23:59', expected=True),
        Case(text='00:00:00', expected=True),
        Case(text='23:59:59', expected=True),
        Case(text='24:00', expected=False),
        Case(text='00:60', expected=False),
    ],
)
def test_is_time(text: str, expected: bool) -> None:
    """Test for time.

    Args:
        text (str): input string
        expected (bool): expected output for input
    """
    assert lsre.is_time(text=text) == expected


@pytest.mark.parametrize(
    ('text', 'expected'),
    [
        Case(text='#fff', expected=True),
        Case(text='#ABC', expected=True),
        Case(text='#123456', expected=True),
        Case(text='123456', expected=False),
        Case(text='#ggg', expected=False),
        Case(text='#ab', expected=False),
    ],
)
def test_is_hex_color(text: str, expected: bool) -> None:
    """Test for hex color.

    Args:
        text (str): input string
        expected (bool): expected output for input
    """
    assert lsre.is_hex_color(text=text) == expected


@pytest.mark.parametrize(
    ('text', 'expected'),
    [
        Case(text='123e4567-e89b-12d3-a456-426614174000', expected=True),
        Case(text='00000000-0000-0000-0000-000000000000', expected=True),
        Case(text='550e8400-e29b-41d4-a716-446655440000', expected=True),
        Case(text='550e8400e29b41d4a716446655440000', expected=False),
        Case(text='not-a-uuid', expected=False),
    ],
)
def test_is_uuid(text: str, expected: bool) -> None:
    """Test for UUID.

    Args:
        text (str): input string
        expected (bool): expected output for input
    """
    assert lsre.is_uuid(text=text) == expected


@pytest.mark.parametrize(
    ('text', 'expected'),
    [
        Case(text='my-slug', expected=True),
        Case(text='another-slug-123', expected=True),
        Case(text='a', expected=True),
        Case(text='a--b', expected=False),
        Case(text='-start', expected=False),
        Case(text='end-', expected=False),
        Case(text='Not A Slug', expected=False),
    ],
)
def test_is_slug(text: str, expected: bool) -> None:
    """Test for slug.

    Args:
        text (str): input string
        expected (bool): expected output for input
    """
    assert lsre.is_slug(text=text) == expected


@pytest.mark.parametrize(
    ('text', 'expected'),
    [
        Case(text='Aa1!aaaa', expected=True),
        Case(text='Str0ng#Pass', expected=True),
        Case(text='P@ssw0rd', expected=True),
        Case(text='Password1', expected=False),
        Case(text='weak', expected=False),
        Case(text='Password', expected=False),
    ],
)
def test_is_strong_password(text: str, expected: bool) -> None:
    """Test for strong password.

    Args:
        text (str): input string
        expected (bool): expected output for input
    """
    assert lsre.is_strong_password(text=text) == expected
