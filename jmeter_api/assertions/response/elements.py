import logging

from random import random
from enum import Enum
from typing import Union, List
from xml.etree.ElementTree import Element

from jmeter_api.basics.assertion.elements import BasicAssertion
from jmeter_api.basics.utils import Renderable, tree_to_str, Scope


class TestField(Enum):
    REQUEST_DATA = "Assertion.request_data"
    REQUEST_HEADERS = "Assertion.request_headers"
    URL = "Assertion.sample_label"
    DOCUMENT = "Assertion.response_data_as_document"
    RESPONSE_HEADERS = "Assertion.response_headers"
    RESPONSE_BODY = "Assertion.response_data"
    RESPONSE_CODE = "Assertion.response_code"
    RESPONSE_MESSAGE = "Assertion.response_message"


class TestType(Enum):
    CONTAINS = 2
    MATCHES = 1
    EQUALS = 8
    SUBSTRING = 16

    
class ResponseAssertion(BasicAssertion, Renderable):

    root_element_name = 'ResponseAssertion'

    def __init__(self, *,
                 ignore_status: bool = False,
                 test_field: TestField = TestField.RESPONSE_BODY,
                 test_type: TestType = TestType.SUBSTRING,
                 test_type_not: bool = False,
                 test_type_or: bool = False,
                 patterns: List[str] = [],
                 custom_message: str = '',
                 scope: Union[str, Scope] = Scope.MAIN,
                 name: str = 'Response Assertion',
                 comments: str = '',
                 is_enabled: bool = True):
        self.ignore_status = ignore_status
        self.test_field = test_field
        self.setTestType(test_type, test_type_not, test_type_or)
        self.custom_message = custom_message
        self.patterns = patterns
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
    def test_type(self) -> str:
        return self._test_type

    def setTestType(self, test_type, test_type_not, test_type_or):
        if not isinstance(test_type, TestType):
            raise TypeError(
                f'test_type must be TestType. {type(test_type).__name__} was given')
        if not isinstance(test_type_not, bool):
            raise TypeError(
                f'test_type_not must be bool. {type(test_type_not).__name__} was given')
        if not isinstance(test_type_or, bool):
            raise TypeError(
                f'test_type_or must be bool. {type(test_type_or).__name__} was given')
        s = test_type.value
        if test_type_not:
            s = s + 4
        if test_type_or:
            s = s + 32
        self._test_type = str(s)

    @property
    def ignore_status(self) -> str:
        return self._ignore_status

    @ignore_status.setter
    def ignore_status(self, value: bool):
        if not isinstance(value, bool):
            raise TypeError(
                f'ignore_status must be bool. {type(value).__name__} was given')
        self._ignore_status = str(value).lower()

    @property
    def custom_message(self) -> str:
        return self._custom_message

    @custom_message.setter
    def custom_message(self, value: str):
        if not isinstance(value, str):
            raise TypeError(
                f'custom_message must be str. {type(value).__name__} was given')
        self._custom_message = value

    @property
    def patterns(self):
        return self._patterns

    @patterns.setter
    def patterns(self, value):
        if not isinstance(value, List):
            raise TypeError(
                f'patterns must be List[str]. {type(value).__name__} was given')
        for v in value:
            if not isinstance(v, str):
                raise TypeError(
                    f'patterns must be List[str]. {type(value).__name__} was given')
        self._patterns = value
        
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
                if element.attrib['name'] == 'Assertion.custom_message':
                    element.text = self.custom_message
                if element.attrib['name'] == 'Assertion.test_field':
                    element.text = self.test_field
                if element.attrib['name'] == 'Assertion.assume_success':
                    element.text = self.ignore_status
                if element.attrib['name'] == 'Assertion.test_type':
                    element.text = self.test_type
                if element.attrib['name'] == 'Asserion.test_strings':
                    for s in self.patterns:
                        el = Element("stringProp", attrib={"name": str(int(random()*100))})
                        el.text = s
                        element.append(el)
            except KeyError:
                logging.error('Unable to set xml parameters')
        if not self.scope == Scope.MAIN.value:
            el = Element("stringProp", attrib={"name": "Sample.scope"})
            el.text = self.scope
            element_root.append(el)
            if self.scope == 'variable':
                el = Element("stringProp", attrib={"name": "Assertion.variable"})
                el.text = self.variable
                element_root.append(el)
        return tree_to_str(xml_tree)
