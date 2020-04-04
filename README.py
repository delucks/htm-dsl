from pyhtml.elements import *
from pyhtml import HTMLElement

contents = body(
    h1('htm-dsl'),
    p(
        'This is a simple DSL that generates HTML from python. Constructing a HTML document is a matter of nesting functions.\n',
        pre(
            """
from pyhtml.elements import *

html(
    head(title("Some webpage")),
    body(
        h1("Title"),
        p(
            "Freely mixing strings with ",
            code("htm-dsl"),
            " functions allows you to interpolate tags in text"
        )
    )
)\n"""
        ),
        br(),
        'For an example, look at ',
        code(__file__),
        ', which generates this README!',
    ),
)

with open('README.md', 'w') as f:
    f.write(contents + '\n')
