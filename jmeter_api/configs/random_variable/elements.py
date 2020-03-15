import logging

from jmeter_api.basics.config.elements import BasicConfig
from jmeter_api.basics.utils import Renderable, FileEncoding, tree_to_str


class RandomVariable(BasicConfig, Renderable):

    root_element_name = 'RandomVariableConfig'

    def __init__(self, *,
                 minimum_value: int = 0,
                 maximum_value: int = None,
                 random_seed: int = 1,
                 variable_name: str,
                 output_format: str = '',
                 per_thread: bool = False,
                 name: str = 'Random Variable',
                 comments: str = '',
                 is_enabled: bool = True):
        self.minimum_value = minimum_value
        self.maximum_value = maximum_value
        self.random_seed = random_seed
        if not maximum_value is None and minimum_value >= maximum_value:
            raise ValueError('minimumValue must be less then end')
        self.per_thread = per_thread
        self.variable_name = variable_name
        self.output_format = output_format
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
    def per_thread(self) -> str:
        return self._per_thread

    @per_thread.setter
    def per_thread(self, value):
        if not isinstance(value, bool):
            raise TypeError(
                f'per_user must be bool. {type(value).__name__} was given')
        self._per_thread = str(value).lower()

    @property
    def output_format(self) -> str:
        return self._output_format

    @output_format.setter
    def output_format(self, value):
        if not isinstance(value, str):
            raise TypeError(
                f'format_ must be str. {type(value).__name__} was given')
        self._output_format = str(value).lower()

    @property
    def minimum_value(self) -> str:
        return self._minimum_value

    @minimum_value.setter
    def minimum_value(self, value):
        if not isinstance(value, int):
            raise TypeError(
                f'minimumValue must be int. {type(value).__name__} was given')
        self._minimum_value = str(value)

    @property
    def maximum_value(self) -> str:
        return self._maximum_value

    @maximum_value.setter
    def maximum_value(self, value):
        if value is None:
            self._end = ''
        elif not isinstance(value, int):
            raise TypeError(
                f'end must be int. {type(value).__name__} was given')
        self._maximum_value = str(value)

    @property
    def random_seed(self) -> str:
        return self._random_seed

    @random_seed.setter
    def random_seed(self, value):
        if not isinstance(value, int):
            raise TypeError(
                f'incr must be int. {type(value).__name__} was given')
        self._random_seed = str(value)

    def to_xml(self) -> str:
        element_root, xml_tree = super()._add_basics()

        for element in list(element_root):
            try:
                if element.attrib['name'] == 'variableName':
                    element.text = self.variable_name
                elif element.attrib['name'] == 'outputFormat':
                    element.text = self.output_format
                elif element.attrib['name'] == 'minimumValue':
                    element.text = self.minimum_value
                elif element.attrib['name'] == 'maximumValue':
                    element.text = self.maximum_value
                elif element.attrib['name'] == 'randomSeed':
                    element.text = self.random_seed
                elif element.attrib['name'] == 'perThread':
                    element.text = self.per_thread
            except KeyError:
                logging.error(
                    f'Unable to properly convert {self.__class__} to xml.')
        return tree_to_str(xml_tree)
