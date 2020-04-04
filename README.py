from pyhtml.elements import *
from pyhtml import HTMLElement

code = HTMLElement('code')

contents = body(
    h1('htm-dsl'),
    hr(),
    h2('A small DSL that generates HTML from Python'),
    p('For an example, look at ', code('README.py'), ', which generates this README!')
)

with open('README.md', 'w') as f:
    f.write(contents + '\n')
