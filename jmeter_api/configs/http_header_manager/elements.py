import logging

from typing import List, Optional, Union
from xml.etree.ElementTree import Element

from jmeter_api.basics.config.elements import BasicConfig
from jmeter_api.basics.utils import Renderable, FileEncoding, tree_to_str


class Header(Renderable):
    
    TEMPLATE = 'header.xml'
    root_element_name = 'elementProp'
    
    def __init__(self, *,
                 name: str,
                 value: str):
        self.name = name
        self.value = value

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

    def to_xml(self) -> str:
        xml_tree: Optional[Element] = super().get_template()
        element_root = xml_tree.find(self.root_element_name)
        element_root.attrib['name'] = self.name
        
        for element in list(element_root):
            try:
                if element.attrib['name'] == 'Header.name':
                    element.text = self.name
                elif element.attrib['name'] == 'Header.value':
                    element.text = self.value
            except KeyError:
                logging.error(
                    f'Unable to properly convert {self.__class__} to xml.')
        return tree_to_str(xml_tree)


class HTTPHeaderManager(BasicConfig, Renderable):

    root_element_name = 'HeaderManager'

    def __init__(self, *,
                 headers: Union[List[Header],dict] = [],
                 name: str = 'HTTP Header Manager',
                 comments: str = '',
                 is_enabled: bool = True):
        self.headers = headers
        super().__init__(name=name, comments=comments, is_enabled=is_enabled)

    @property
    def headers(self) -> str:
        return self._headers

    @headers.setter
    def headers(self, value):
        if not isinstance(value, List):
            raise TypeError(
                f'headers must be List. {type(value).__name__} was given')
        for i in range(len(value)):
            if not isinstance(value[i], (Header, dict)):
                raise TypeError(
                f'headers must contain Header or dict. {type(value).__name__} was given')
            if isinstance(value[i], dict):
                if not len(value[i]) == 1:
                    raise ValueError('dict must be like "header":"value"')
                h = list(value[i])[0]
                v = value[i][h]
                value[i] = Header(name=h, value=v)
        self._headers = value

    def to_xml(self) -> str:
        element_root, xml_tree = super()._add_basics()

        for element in list(element_root):
            try:
                if element.attrib['name'] == 'HeaderManager.headers':
                    element.text = ''
                    for arg in self.headers:
                        element.text += arg.to_xml()
            except KeyError:
                logging.error(
                    f'Unable to properly convert {self.__class__} to xml.')
        return tree_to_str(xml_tree)
