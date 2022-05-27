import pytest
from corty import __version__  # type: ignore


def test_version():
    assert __version__ == "0.1.0"
