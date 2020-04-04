class HTMLElement:
    def __init__(self, name, self_closed=False):
        self.name = name
        self.self_closed = self_closed

    def __call__(self, children=[]):
        return f'<{self.name}>' + ''.join([c() for c in children]) + f'</{self.name}>'


html = HTMLElement('html')
