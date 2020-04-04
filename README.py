from pyhtml.elements import *
from pyhtml import HTMLElement

code = HTMLElement('code')

contents = body(
    h1('htm-dsl'),
    p(
        'This is a simple DSL that generates HTML from python. Constructing a HTML document is a matter of nesting functions.',
        br(),
        'For an example, look at ',
        code('README.py'),
        ', which generates this README!'
    )
)

with open('README.md', 'w') as f:
    f.write(contents + '\n')
