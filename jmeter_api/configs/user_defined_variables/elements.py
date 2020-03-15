import logging

from typing import List, Optional
from xml.etree.ElementTree import Element

from jmeter_api.basics.config.elements import BasicConfig
from jmeter_api.basics.utils import Renderable, FileEncoding, tree_to_str


class Argument(Renderable):
    
    TEMPLATE = 'argument.xml'
    root_element_name = 'elementProp'
    
    def __init__(self, *,
                 name: str,
                 value: str,
                 desc: str = '',
                 metadata: str = '='):
        self.name = name
        self.value = value
        self.desc = desc
        self.metadata = metadata

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError(
                f'name must be str. {type(value).__name__} was given')
        self._name = value

    @property
    def value(self) -> str:
        return self._value

    @value.setter
    def value(self, value):
        if not isinstance(value, str):
            raise TypeError(
                f'value must be str. {type(value).__name__} was given')
        self._value = value

    @property
    def desc(self) -> str:
        return self._desc

    @desc.setter
    def desc(self, value):
        if not isinstance(value, str):
            raise TypeError(
                f'variable_name must be str. {type(value).__name__} was given')
        self._desc = value

    @property
    def metadata(self) -> str:
        return self._metadata

    @metadata.setter
    def metadata(self, value):
        if not isinstance(value, str):
            raise TypeError(
                f'variable_name must be str. {type(value).__name__} was given')
        self._metadata = value

    def to_xml(self) -> str:
        xml_tree: Optional[Element] = super().get_template()
        element_root = xml_tree.find(self.root_element_name)
        element_root.attrib['name'] = self.name
        
        for element in list(element_root):
            try:
                if element.attrib['name'] == 'Argument.name':
                    element.text = self.name
                elif element.attrib['name'] == 'Argument.value':
                    element.text = self.value
                elif element.attrib['name'] == 'Argument.desc':
                    element.text = self.desc
                elif element.attrib['name'] == 'Argument.metadata':
                    element.text = self.metadata
            except KeyError:
                logging.error(
                    f'Unable to properly convert {self.__class__} to xml.')
        return tree_to_str(xml_tree)


class UserDefineVariables(BasicConfig, Renderable):

    root_element_name = 'Arguments'

    def __init__(self, *,
                 arguments: List[Argument] = [],
                 name: str = 'User Defined Variables',
                 comments: str = '',
                 is_enabled: bool = True):
        self.arguments = arguments
        super().__init__(name=name, comments=comments, is_enabled=is_enabled)

    @property
    def arguments(self) -> str:
        return self._arguments

    @arguments.setter
    def arguments(self, value):
        if not isinstance(value, List):
            raise TypeError(
                f'arguments must be List. {type(value).__name__} was given')
        for el in value:
            if not isinstance(el, Argument):
                raise TypeError(
                f'arguments must contain only Argument. {type(value).__name__} was given')
        self._arguments = value

    def to_xml(self) -> str:
        element_root, xml_tree = super()._add_basics()

        for element in list(element_root):
            try:
                if element.attrib['name'] == 'Arguments.arguments':
                    element.text = ''
                    for arg in self.arguments:
                        element.text += arg.to_xml()
            except KeyError:
                logging.error(
                    f'Unable to properly convert {self.__class__} to xml.')
        return tree_to_str(xml_tree)
