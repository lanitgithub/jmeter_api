import logging

from jmeter_api.basics.assertion.elements import BasicAssertion
from jmeter_api.basics.utils import Renderable, tree_to_str


class JSONAssertion(BasicAssertion, Renderable):

    root_element_name = 'JSONPathAssertion'

    def __init__(self, *,
                 validation: bool = False,
                 expect_null: bool = False,
                 invert: bool = False,
                 is_regex: bool = True,
                 expected_value: str = '',
                 json_path: str = '$.',
                 name: str = 'JSON Assertion',
                 comments: str = '',
                 is_enabled: bool = True
                 ):
        self.validation = validation
        self.expect_null = expect_null
        self.invert = invert
        self.is_regex = is_regex
        self.expected_value = expected_value
        self.json_path = json_path
        BasicAssertion.__init__(
            self, name=name, comments=comments, is_enabled=is_enabled)

    @property
    def json_path(self) -> str:
        return self._json_path

    @json_path.setter
    def json_path(self, value):
        if not isinstance(value, str):
            raise TypeError(
                f'json_path must be str. {type(value).__name__} was given')
        self._json_path = value

    @property
    def expected_value(self) -> str:
        return self._expected_value

    @expected_value.setter
    def expected_value(self, value):
        if not isinstance(value, str):
            raise TypeError(
                f'expected_value must be str. {type(value).__name__} was given')
        self._expected_value = value

    @property
    def validation(self) -> bool:
        return self._validation

    @validation.setter
    def validation(self, value):
        if not isinstance(value, bool):
            raise TypeError(
                f'validation must be bool. {type(value).__name__} was given')
        self._validation = value

    @property
    def expect_null(self) -> bool:
        return self._expect_null

    @expect_null.setter
    def expect_null(self, value):
        if not isinstance(value, bool):
            raise TypeError(
                f'expect_null must be bool. {type(value).__name__} was given')
        self._expect_null = value

    @property
    def invert(self) -> bool:
        return self._invert

    @invert.setter
    def invert(self, value):
        if not isinstance(value, bool):
            raise TypeError(
                f'invert must be bool. {type(value).__name__} was given')
        self._invert = value

    @property
    def is_regex(self) -> bool:
        return self._is_regex

    @is_regex.setter
    def is_regex(self, value):
        if not isinstance(value, bool):
            raise TypeError(
                f'is_regex must be bool. {type(value).__name__} was given')
        self._is_regex = value
        
    def to_xml(self) -> str:
        element_root, xml_tree = super()._add_basics()
        for element in list(element_root):
            try:
                if element.attrib['name'] == 'JSON_PATH':
                    element.text = self.json_path
                elif element.attrib['name'] == 'EXPECTED_VALUE':
                    element.text = str(self.expected_value).lower()
                elif element.attrib['name'] == 'JSONVALIDATION':
                    element.text = str(self.validation).lower()
                elif element.attrib['name'] == 'EXPECT_NULL':
                    element.text = str(self.expect_null).lower()
                elif element.attrib['name'] == 'INVERT':
                    element.text = str(self.invert).lower()
                elif element.attrib['name'] == 'ISREGEX':
                    element.text = str(self.is_regex).lower()
            except KeyError:
                logging.error('Unable to set xml parameters')

        return tree_to_str(xml_tree)
