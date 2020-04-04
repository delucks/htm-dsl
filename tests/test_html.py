import pytest
from pyhtml.elements import *


def test_root_element():
    assert html() == '<html></html>'


def test_head_elements():
    assert html(head()) == '<html><head></head></html>'
    assert html(head(title('My webpage!'))) == '<html><head><title>My webpage!</title></head></html>'


def test_body_elements():
    assert html(body()) == '<html><body></body></html>'
    assert html(body('some text')) == '<html><body>some text</body></html>'
    assert html(body(h4('some text'))) == '<html><body><h4>some text</h4></body></html>'
    assert html(body(h4('title'), 'body text')) == '<html><body><h4>title</h4>body text</body></html>'
    assert html(
        body(
            h4('title'),
            br(),
            'body text'
        )
    ) == '<html><body><h4>title</h4><br/>body text</body></html>'
