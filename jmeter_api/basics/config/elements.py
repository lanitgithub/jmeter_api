from jmeter_api.basics.element.elements import BasicElement


class BasicConfig(BasicElement):
    def __init__(self,
                 name: str = 'BasicConfig',
                 comments: str = '',
                 is_enabled: bool = True):
        super().__init__(name=name, comments=comments, is_enabled=is_enabled)
