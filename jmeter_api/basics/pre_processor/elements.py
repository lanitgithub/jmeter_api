from jmeter_api.basics.element.elements import BasicElement
from abc import ABC


class BasicPreProcessor(BasicElement, ABC):

    def __init__(self,
                 name: str = 'BasicPreProcessor',
                 comments: str = '',
                 is_enabled: bool = True
                 ):
        super().__init__(name, comments, is_enabled)
