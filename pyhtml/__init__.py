class HTMLElement:
    def __init__(self, name, self_closed=False):
        self.name = name
        self.self_closed = self_closed

    def __call__(self, *args):
        nested = ''
        for arg in args:
            if isinstance(arg, HTMLElement):
                nested += arg()
            else:
                nested += arg
        if self.self_closed:
            return f'<{self.name}/>'
        else:
            return f'<{self.name}>' + nested + f'</{self.name}>'
