from pyhtml import HTMLElement


html = HTMLElement('html')
head = HTMLElement('head')
title = HTMLElement('title')
body = HTMLElement('body')
h1 = HTMLElement('h1', arity=1)
h2 = HTMLElement('h2', arity=1)
h3 = HTMLElement('h3', arity=1)
h4 = HTMLElement('h4', arity=1)

br = HTMLElement('br', self_closed=True)
hr = HTMLElement('hr', self_closed=True)
