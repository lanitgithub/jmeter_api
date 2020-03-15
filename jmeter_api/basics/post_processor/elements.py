from abc import ABC

from jmeter_api.basics.element.elements import BasicElement


class BasicPostProcessor(BasicElement, ABC):

    def __init__(self,
                 name: str = 'BasicPostProcessor',
                 comments: str = '',
                 is_enabled: bool = True
                 ):
        super().__init__(name, comments, is_enabled)
