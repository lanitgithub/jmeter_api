from jmeter_api.basics.element.elements import BasicElement
from abc import ABC


class BasicAssertion(BasicElement, ABC):

    def __init__(self,
                 name: str = 'BasicAssertion',
                 comments: str = '',
                 is_enabled: bool = True
                 ):
        super().__init__(name, comments, is_enabled)
