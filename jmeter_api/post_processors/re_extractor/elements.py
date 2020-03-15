import logging
import re

from xml.etree.ElementTree import SubElement, Element
from enum import Enum
from typing import Union

from jmeter_api.basics.post_processor.elements import BasicPostProcessor
from jmeter_api.basics.utils import Renderable
from jmeter_api.basics.utils import tree_to_str, Scope


class Field(Enum):
    BODY = 'false'
    BODY_UNESCAPED = 'unescaped'
    BODY_AS_DOC = 'as_document'
    RESP_HEADERS = 'true'
    REQ_HEADERS = 'request_headers'
    URL = 'URL'
    RES_CODE = 'code'
    RES_MESSAGE = 'message'


class RegExpPost(BasicPostProcessor, Renderable):

    root_element_name = 'RegexExtractor'

    def __init__(self,
                 name: str = 'Regular Expression Extractor',
                 scope: Union[str, Scope] = Scope.MAIN,
                 field_to_check: Field = Field.BODY,
                 var_name: str = '',
                 regexp: str = '',
                 template: int = None,
                 match_no: int = None,
                 default_val: str = '',
                 comments: str = '',
                 is_enabled: bool = True
                 ):
        super().__init__(name=name, comments=comments, is_enabled=is_enabled)
        self.scope = scope
        self.field_to_check = field_to_check
        self.var_name = var_name
        self.regexp = regexp
        self.template = template
        self.match_no = match_no
        self.default_val = default_val

    @property
    def variable(self):
        return self._variable

    @variable.setter
    def variable(self, value):
        self._variable = value
        
    @property
    def scope(self):
        return self._scope

    @scope.setter
    def scope(self, value):
        if not isinstance(value, (str, Scope)):
            raise TypeError(
                f'arg: scope should be str or Scope. {type(value).__name__} was given')
        if isinstance(value, str):
            self._scope = "variable"
            self.variable = value
        elif isinstance(value, Scope):
            self._scope = value.value

    @property
    def field_to_check(self):
        return self._field_to_check

    @field_to_check.setter
    def field_to_check(self, value):
        if not isinstance(value, Field):
            raise TypeError(
                f'arg: field_to_check should be Field. {type(value).__name__} was given')
        self._field_to_check = value.value

    @property
    def var_name(self):
        return self._var_name

    @var_name.setter
    def var_name(self, value):
        if not isinstance(value, str):
            raise TypeError(
                f'arg: var_name should be str. {type(value).__name__} was given')
        self._var_name = value

    @property
    def regexp(self):
        return self._regexp

    @regexp.setter
    def regexp(self, value):
        if not isinstance(value, str):
            raise TypeError(
                f'arg: regexp should be str. {type(value).__name__} was given')
        try:
            re.compile(value)
        except re.error as error:
            print(error)
            raise ValueError('Invalid regular expression.')
        self._regexp = value

    @property
    def template(self):
        return self._template

    @template.setter
    def template(self, value):
        if value is not None and not isinstance(value, int):
            raise TypeError(
                f'arg: common_thread_group_template.xml should be int or None. {type(value).__name__} was given')
        if value is not None and value < 1:
            raise ValueError(
                f'arg: common_thread_group_template.xml should be greater or equal than 1.')
        self._template = value

    @property
    def match_no(self):
        return self._match_no

    @match_no.setter
    def match_no(self, value):
        if value is not None and not isinstance(value, int):
            raise TypeError(
                f'arg: match_no should be int. {type(value).__name__} was given')
        if value is not None and value < 0:
            raise ValueError(f'arg: match_no should be greater than 0.')
        self._match_no = value

    @property
    def default_val(self):
        return self._default_val

    @default_val.setter
    def default_val(self, value):
        if not isinstance(value, str):
            raise TypeError(
                f'arg: default_val should be str. {type(value).__name__} was given')
        self._default_val = value

    def to_xml(self) -> str:
        element_root, xml_tree = super()._add_basics()
        flag = True
        for element in list(element_root):
            try:
                if element.attrib['name'] == 'TestPlan.comments':
                    element.text = self.comments
                elif element.attrib['name'] == 'RegexExtractor.useHeaders':
                    element.text = self.field_to_check
                elif element.attrib['name'] == 'RegexExtractor.refname':
                    element.text = self.var_name
                elif element.attrib['name'] == 'RegexExtractor.regex':
                    element.text = self.regexp
                elif element.attrib['name'] == 'RegexExtractor.template':
                    if self.template is None:
                        element.text = ''
                    else:
                        element.text = str(self.template)
                elif element.attrib['name'] == 'RegexExtractor.default':
                    element.text = self.default_val
                elif element.attrib['name'] == 'RegexExtractor.match_number':
                    if self.match_no is None:
                        element.text = ''
                    else:
                        element.text = str(self.match_no)

                if flag:
                    if not self.scope == Scope.MAIN.value:
                        el = Element("stringProp", attrib={"name":"Sample.scope"})
                        el.text = self.scope
                        element_root.append(el)
                        if self.scope == 'variable':
                            el = Element("stringProp", attrib={"name":"Scope.variable"})
                            el.text = self.variable
                            element_root.append(el)

                    if self.default_val == 'empty':
                        element = SubElement(element_root, 'boolProp')
                        element.set('name', 'RegexExtractor.default_empty_value')
                        element.text = 'true'
                    flag = False
            except KeyError:
                logging.error(f'Unable to render XML')
        return tree_to_str(xml_tree)
