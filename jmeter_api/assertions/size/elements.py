import logging
from enum import Enum

from typing import Union
from xml.etree.ElementTree import Element

from jmeter_api.basics.assertion.elements import BasicAssertion
from jmeter_api.basics.utils import Renderable, tree_to_str, Scope


class TestField(Enum):
    FULL = "SizeAssertion.response_network_size"
    HEADER = "SizeAssertion.response_headers"
    RESPONSE_BODY = "SizeAssertion.response_data"
    RESPONSE_CODE = "SizeAssertion.response_code"
    RESPONSE_MESSAGE = "SizeAssertion.response_message"


class Operator(Enum):
    EQUAL = "1"
    NOT_EQUAL = "2"
    MORE = "3"
    LESS = "4"
    MORE_OR_EQUAL = "5"
    LESS_OR_EQUAL = "6"

    
class SizeAssertion(BasicAssertion, Renderable):

    root_element_name = 'SizeAssertion'

    def __init__(self, *,
                 size: int,
                 test_field: TestField = TestField.FULL,
                 operator: Operator = Operator.EQUAL,
                 scope: Union[str, Scope] = Scope.MAIN,
                 name: str = 'Size Assertion',
                 comments: str = '',
                 is_enabled: bool = True):
        self.size = size
        self.test_field = test_field
        self.operator = operator
        self.scope = scope
        BasicAssertion.__init__(
            self, name=name, comments=comments, is_enabled=is_enabled)

    @property
    def variable(self):
        return self._variable

    @variable.setter
    def variable(self, value):
        self._variable = value
        
    @property
    def size(self) -> str:
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int) or value < 0:
            raise TypeError(
                f'size must be positive int. {type(value).__name__} was given')
        self._size = str(value)

    @property
    def operator(self) -> str:
        return self._operator

    @operator.setter
    def operator(self, value):
        if not isinstance(value, Operator):
            raise TypeError(
                f'operator must be Operator. {type(value).__name__} was given')
        self._operator = value.value
        
    @property
    def test_field(self) -> str:
        return self._test_field

    @test_field.setter
    def test_field(self, value):
        if not isinstance(value, TestField):
            raise TypeError(
                f'test_field must be TestField. {type(value).__name__} was given')
        self._test_field = value.value
        
    @property
    def scope(self) -> str:
        return self._scope

    @scope.setter
    def scope(self, value):
        if not isinstance(value, (str, Scope)):
            raise TypeError(
                f'scope must be Scope or str. {type(value).__name__} was given')
        if isinstance(value, str):
            self._scope = "variable"
            self.variable = value
        elif isinstance(value, Scope):
            self._scope = value.value
        
    def to_xml(self) -> str:
        element_root, xml_tree = super()._add_basics()
        for element in list(element_root):
            try:
                if element.attrib['name'] == 'SizeAssertion.size':
                    element.text = self.size
                if element.attrib['name'] == 'Assertion.test_field':
                    element.text = self.test_field
                if element.attrib['name'] == 'SizeAssertion.operator':
                    element.text = self.operator
            except KeyError:
                logging.error('Unable to set xml parameters')
        if not self.scope == Scope.MAIN.value:
            el = Element("stringProp", attrib={"name":"Sample.scope"})
            el.text = self.scope
            element_root.append(el)
            if self.scope == 'variable':
                el = Element("stringProp", attrib={"name":"Assertion.variable"})
                el.text = self.variable
                element_root.append(el)
        return tree_to_str(xml_tree)
