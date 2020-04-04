import pytest
from pyhtml import html


def test_root_element():
    assert html() == '<html></html>'
