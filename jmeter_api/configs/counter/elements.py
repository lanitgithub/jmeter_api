import logging

from xml.etree.ElementTree import Element

from jmeter_api.basics.config.elements import BasicConfig
from jmeter_api.basics.utils import Renderable, FileEncoding, tree_to_str


class Counter(BasicConfig, Renderable):

    root_element_name = 'CounterConfig'

    def __init__(self, *,
                 start: int = 0,
                 end: int = None,
                 incr: int = 1,
                 variable_name: str,
                 format_: str = '',
                 reset_on_tg_iteration: bool = False,
                 per_user: bool = False,
                 name: str = 'Counter',
                 comments: str = '',
                 is_enabled: bool = True):
        self.start = start
        self.end = end
        self.incr = incr
        if not end is None and start >= end:
            raise ValueError('start must be less then end')
        self.per_user = per_user
        self.reset_on_tg_iteration = reset_on_tg_iteration
        self.variable_name = variable_name
        self.format_ = format_
        super().__init__(name=name, comments=comments, is_enabled=is_enabled)

    @property
    def variable_name(self) -> str:
        return self._variable_name

    @variable_name.setter
    def variable_name(self, value):
        if not isinstance(value, str):
            raise TypeError(
                f'variable_name must be str. {type(value).__name__} was given')
        self._variable_name = value

    @property
    def per_user(self) -> bool:
        return self._per_user

    @per_user.setter
    def per_user(self, value):
        if not isinstance(value, bool):
            raise TypeError(
                f'per_user must be bool. {type(value).__name__} was given')
        self._per_user = value

    @property
    def reset_on_tg_iteration(self) -> bool:
        return self._reset_on_tg_iteration

    @reset_on_tg_iteration.setter
    def reset_on_tg_iteration(self, value):
        if not isinstance(value, bool):
            raise TypeError(
                f'per_user must be bool. {type(value).__name__} was given')
        
        if value and not self.per_user:
            raise ValueError('reset_on_tg_iteration cant be True while per_user is False')
        self._reset_on_tg_iteration = value

    @property
    def format_(self) -> str:
        return self._format_

    @format_.setter
    def format_(self, value):
        if not isinstance(value, str):
            raise TypeError(
                f'format_ must be str. {type(value).__name__} was given')
        self._format_ = value

    @property
    def start(self) -> str:
        return self._start

    @start.setter
    def start(self, value):
        if not isinstance(value, int) or value < 0:
            raise TypeError(
                f'start must be positive int. {type(value).__name__} was given')
        self._start = str(value)

    @property
    def end(self) -> str:
        return self._end

    @end.setter
    def end(self, value):
        if value is None:
            self._end = ''
        elif not isinstance(value, int) or value < 0:
            raise TypeError(
                f'end must be positive int. {type(value).__name__} was given')
        self._end = str(value)

    @property
    def incr(self) -> str:
        return self._incr

    @incr.setter
    def incr(self, value):
        if not isinstance(value, int) or value <= 0:
            raise TypeError(
                f'incr must be positive int. {type(value).__name__} was given')
        self._incr = str(value)

    def to_xml(self) -> str:
        element_root, xml_tree = super()._add_basics()

        for element in list(element_root):
            try:
                if element.attrib['name'] == 'CounterConfig.name':
                    element.text = self.variable_name
                elif element.attrib['name'] == 'CounterConfig.format':
                    element.text = self.format_
                elif element.attrib['name'] == 'CounterConfig.start':
                    element.text = self.start
                elif element.attrib['name'] == 'CounterConfig.end':
                    element.text = self.end
                elif element.attrib['name'] == 'CounterConfig.incr':
                    element.text = self.incr
                elif element.attrib['name'] == 'CounterConfig.per_user':
                    element.text = str(self.per_user).lower()
            except KeyError:
                logging.error(
                    f'Unable to properly convert {self.__class__} to xml.')
        if self.per_user and self.reset_on_tg_iteration:
            el = Element("boolProp", attrib={"name": 'CounterConfig.reset_on_tg_iteration'})
            el.text = str(self.reset_on_tg_iteration).lower()
            element_root.append(el)
        return tree_to_str(xml_tree)
