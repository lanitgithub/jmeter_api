import logging

from typing import Union
from xml.etree.ElementTree import Element

from jmeter_api.basics.assertion.elements import BasicAssertion
from jmeter_api.basics.utils import Renderable, tree_to_str, Scope


class DurationAssertion(BasicAssertion, Renderable):

    root_element_name = 'DurationAssertion'

    def __init__(self, *,
                 duration: int,
                 scope: Scope = Scope.MAIN,
                 name: str = 'Duration Assertion',
                 comments: str = '',
                 is_enabled: bool = True
                 ):
        self.duration = duration
        self.scope = scope
        BasicAssertion.__init__(
            self, name=name, comments=comments, is_enabled=is_enabled)
        
    @property
    def duration(self) -> str:
        return self._duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, int):
            raise TypeError(
                f'duration must be int. {type(value).__name__} was given')
        self._duration = str(value)

    @property
    def scope(self) -> str:
        return self._scope

    @scope.setter
    def scope(self, value):
        if not isinstance(value, Scope):
            raise TypeError(
                f'scope must be Scope. {type(value).__name__} was given')
        self._scope = value.value
        
    def to_xml(self) -> str:
        element_root, xml_tree = super()._add_basics()
        for element in list(element_root):
            try:
                if element.attrib['name'] == 'DurationAssertion.duration':
                    element.text = self.duration
            except KeyError:
                logging.error('Unable to set xml parameters')
        if not self.scope == Scope.MAIN.value:
            el = Element("stringProp", attrib={"name":"Sample.scope"})
            el.text = self.scope
            element_root.append(el)
        return tree_to_str(xml_tree)
