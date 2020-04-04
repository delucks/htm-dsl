from typing import Union, List

from pyhtml.exceptions import InvalidMarkupArity

def format_attrs(**kwargs):
    output = ''
    for key, value in kwargs.items():
        output += f' {key}="{value}"'
    return output

class HTMLElement:
    def __init__(self, name: str, arity: int = -1):
        self.name = name
        self.arity = arity

    def __call__(self, *args, **kwargs) -> str:
        self.check_arity(*args)
        return self.render(*args, **kwargs)

    def check_arity(self, *args) -> None:
        if self.arity < 0:
            return
        nested_markup = [a for a in args if isinstance(a, str)]
        if len(nested_markup) > self.arity:
            raise InvalidMarkupArity(f'Markup {" ".join(nested_markup)} is greater than arity {self.arity}')

    def render(self, *args, **kwargs) -> str:
        nested = ''
        for arg in args:
            if isinstance(arg, HTMLElement):
                nested += arg()
            else:
                nested += arg
        return f'<{self.name}{format_attrs(**kwargs)}>' + nested + f'</{self.name}>'
