import logging

from typing import Union
from xml.etree.ElementTree import Element

from jmeter_api.basics.post_processor.elements import BasicPostProcessor
from jmeter_api.basics.element.elements import Renderable
from jmeter_api.basics.utils import tree_to_str, Scope


class JSONExtractor(BasicPostProcessor, Renderable):

    root_element_name = 'JSONPostProcessor'

    def __init__(self, *,
                 scope: Union[str, Scope] = Scope.MAIN,
                 referenceNames: str = '',
                 jsonPathExprs: str = '',
                 match_numbers: int = 1,
                 defaultValues: str = None,
                 compute_concat: bool = False,
                 name: str = 'JSON Extractor',
                 comments: str = '',
                 is_enabled: bool = True
                 ):
        self.scope = scope
        self.referenceNames = referenceNames
        self.jsonPathExprs = jsonPathExprs
        self.match_numbers = match_numbers
        self.defaultValues = defaultValues
        self.compute_concat = compute_concat
        BasicPostProcessor.__init__(self, name=name, comments=comments, is_enabled=is_enabled)

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
    def referenceNames(self):
        return self._referenceNames

    @referenceNames.setter
    def referenceNames(self, value):
        if not isinstance(value, str):
            raise TypeError(
                f'arg: referenceNames should be str. {type(value).__name__} was given')
        self._referenceNames = value

    @property
    def jsonPathExprs(self):
        return self._jsonPathExprs

    @jsonPathExprs.setter
    def jsonPathExprs(self, value):
        if not isinstance(value, str):
            raise TypeError(
                f'arg: regexp should be str. {type(value).__name__} was given')
        self._jsonPathExprs = value

    @property
    def match_numbers(self):
        return self._match_numbers

    @match_numbers.setter
    def match_numbers(self, value):
        if not isinstance(value, int) or value < -1:
            raise TypeError(
                f'arg: match_no should be positive int or -1. {type(value).__name__} was given')
        self._match_numbers = str(value)

    @property
    def defaultValues(self):
        return self._defaultValues

    @defaultValues.setter
    def defaultValues(self, value):
        if not value is None and not isinstance(value, str):
            raise TypeError(
                f'arg: default_val should be str. {type(value).__name__} was given')
        self._defaultValues = value
        
    @property
    def compute_concat(self):
        return self._compute_concat

    @compute_concat.setter
    def compute_concat(self, value):
        if not isinstance(value, bool):
            raise TypeError(
                f'arg: referenceNames should be bool. {type(value).__name__} was given')
        self._compute_concat = str(value).lower()

    def to_xml(self) -> str:
        element_root, xml_tree = super()._add_basics()
        for element in list(element_root):
            try:
                if element.attrib['name'] == 'JSONPostProcessor.referenceNames':
                    element.text = self.referenceNames
                elif element.attrib['name'] == 'JSONPostProcessor.jsonPathExprs':
                    element.text = self.jsonPathExprs
                elif element.attrib['name'] == 'JSONPostProcessor.match_numbers':
                    element.text = self.match_numbers
            except KeyError:
                logging.error(f'Unable to render XML')
        if not self.defaultValues is None:
            el = Element("stringProp", attrib={"name":"JSONPostProcessor.defaultValues"})
            el.text = self.defaultValues
            element_root.append(el)
        if self.compute_concat:
            el = Element("boolProp", attrib={"name":"JSONPostProcessor.compute_concat"})
            el.text = self.compute_concat
            element_root.append(el)
        if not self.scope == Scope.MAIN.value:
            el = Element("stringProp", attrib={"name":"Sample.scope"})
            el.text = self.scope
            element_root.append(el)
            if self.scope == 'variable':
                el = Element("stringProp", attrib={"name":"Scope.variable"})
                el.text = self.variable
                element_root.append(el)
        return tree_to_str(xml_tree)
