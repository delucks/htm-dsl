import pytest
from pyhtml.elements import *
from pyhtml.exceptions import InvalidMarkupArity


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
    assert html(body(h4('title'), br(), 'body text')) == '<html><body><h4>title</h4><br></br>body text</body></html>'


def test_sequential_element():
    assert body(h1('some'), h2('text'), h3('here')) == '<body><h1>some</h1><h2>text</h2><h3>here</h3></body>'


def test_element_arity():
    with pytest.raises(InvalidMarkupArity):
        h1('some', 'shit')


def test_complex_construction():
    assert (
        html(
            head(title('A more complex page')),
            body(h1('My title'), h2('With a subtitle...'), p("and here's my ", b("body text"), "."), hr(), "but we aren't done yet"),
        )
        == "<html><head><title>A more complex page</title></head><body><h1>My title</h1><h2>With a subtitle...</h2><p>and here's my <b>body text</b>.</p><hr></hr>but we aren't done yet</body></html>"
    )

def test_attributes():
    assert html('foo', lang='en') == '<html lang="en">foo</html>'
    assert a("Destination", href="https://foo.bar") == '<a href="https://foo.bar">Destination</a>'
