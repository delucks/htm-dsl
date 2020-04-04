from typing import Union, List

from pyhtml.exceptions import InvalidMarkupArity


class HTMLElement:
    def __init__(self, name: str, self_closed: bool = False, arity: int = -1):
        self.name = name
        self.self_closed = self_closed
        self.arity = 0 if self_closed else arity

    def __call__(self, *args) -> str:
        self.check_arity(*args)
        return self.render(*args)

    def check_arity(self, *args) -> None:
        if self.arity < 0:
            return
        nested_markup = [a for a in args if isinstance(a, str)]
        if len(nested_markup) > self.arity:
            raise InvalidMarkupArity(f'Markup {" ".join(nested_markup)} is greater than arity {self.arity}')

    def render(self, *args) -> str:
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
