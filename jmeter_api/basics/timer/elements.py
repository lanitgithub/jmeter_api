from abc import ABC

from jmeter_api.basics.element.elements import BasicElement


class BasicTimer(BasicElement, ABC):
    def __init__(self,
                 name: str = 'BasicTimer',
                 comments: str = '',
                 is_enabled: bool = True
                 ):
        super().__init__(name=name, comments=comments, is_enabled=is_enabled)
