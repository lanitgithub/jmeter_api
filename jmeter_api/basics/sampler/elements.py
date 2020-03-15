from abc import ABC
from typing import Union
from xml.etree.ElementTree import SubElement

from jmeter_api.basics.element.elements import BasicElement
from jmeter_api.basics.pre_processor.elements import BasicPreProcessor
from jmeter_api.basics.post_processor.elements import BasicPostProcessor
from jmeter_api.basics.config.elements import BasicConfig
from jmeter_api.basics.timer.elements import BasicTimer
from jmeter_api.basics.assertion.elements import BasicAssertion
from jmeter_api.basics.listener.elements import BasicListener
from jmeter_api.basics.utils import IncludesElements
from jmeter_api.basics.utils import Renderable, tree_to_str


class BasicSampler(BasicElement, IncludesElements, ABC):
    def __init__(self,
                 name: str = 'BasicSampler',
                 comments: str = '',
                 is_enabled: bool = True
                 ):
        IncludesElements.__init__(self)
        super().__init__(name=name, comments=comments, is_enabled=is_enabled)

    def append(self, new_element: Union[BasicTimer, BasicConfig, BasicPreProcessor, BasicPostProcessor, BasicAssertion, BasicListener]):
        if not isinstance(new_element, (BasicTimer, BasicConfig, BasicPreProcessor, BasicPostProcessor, BasicAssertion, BasicListener)):
            raise TypeError(
                f'new_element must be BasicTimer, BasicConfig, BasicPreProcessor, BasicPostProcessor, BasicAssertion or BasicListener. {type(new_element)} was given')
        self._elements.append(new_element)
        return self


class FileUpload(Renderable):

    TEMPLATE = 'file_upload_template.xml'

    def __init__(self,
                 file_path: str = '',
                 param_name: str = '',
                 mime_type: str = ''
                 ):
        self.file_path = file_path
        self.param_name = param_name
        self.mime_type = mime_type

    @property
    def file_path(self):
        return self._file_path

    @file_path.setter
    def file_path(self, value):
        if not isinstance(value, str):
            raise TypeError(f'arg: file_path should be str. {type(value).__name__} was given')
        self._file_path = value

    @property
    def param_name(self):
        return self._param_name

    @param_name.setter
    def param_name(self, value):
        if not isinstance(value, str):
            raise TypeError(f'arg: param_name should be str. {type(value).__name__} was given')
        self._param_name = value

    @property
    def mime_type(self):
        return self._mime_type

    @mime_type.setter
    def mime_type(self, value):
        if not isinstance(value, str):
            raise TypeError(f'arg: mime_type should be str. {type(value).__name__} was given')
        self._mime_type = value

    def to_xml(self):

        xml_tree = self.get_template()

        for element in list(xml_tree):
            element.set('name', self.file_path)
            for el in list(element):
                if el.attrib['name'] == 'File.path':
                    el.text = self.file_path
                elif el.attrib['name'] == 'File.paramname':
                    el.text = self.param_name
                elif el.attrib['name'] == 'File.mimetype':
                    el.text = self.mime_type

        return tree_to_str(xml_tree)


class UserDefinedVariables(Renderable):

    TEMPLATE = 'user_defined_variables.xml'

    def __init__(self,
                 name: str = '',
                 value: Union[str, int] = '',
                 url_encode: bool = False,
                 content_type: str = '',
                 use_equals: bool = True
                 ):
        self.name = name
        self._value = value
        self.url_encode = url_encode
        self.content_type = content_type
        self.use_equals = use_equals

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError(f'arg: name should be str. {type(value).__name__} was given')
        self._name = value

    @property
    def _value(self):
        return self.__value

    @_value.setter
    def _value(self, value):
        if not isinstance(value, (int, str)):
            raise TypeError(f'arg: value should be str or int. {type(value).__name__} was given')
        self.__value = value

    @property
    def url_encode(self):
        return self._url_encode

    @url_encode.setter
    def url_encode(self, value):
        if not isinstance(value, bool):
            raise TypeError(f'arg: url_encode should be bool. {type(value).__name__} was given')
        self._url_encode = value

    @property
    def content_type(self):
        return self._content_type

    @content_type.setter
    def content_type(self, value):
        if not isinstance(value, str):
            raise TypeError(f'arg: content_type should be str. {type(value).__name__} was given')
        self._content_type = value

    @property
    def use_equals(self):
        return self._use_equals

    @use_equals.setter
    def use_equals(self, value):
        if not isinstance(value, bool):
            raise TypeError(f'arg: use_equals should be bool. {type(value).__name__} was given')
        self._use_equals = value

    def to_xml(self):
        xml_tree = self.get_template()
        flag = True
        for element in list(xml_tree):
            element.set('name', self.name)
            for el in list(element):
                if el.attrib['name'] == 'HTTPArgument.always_encode':
                    el.text = str(self.url_encode).lower()
                elif el.attrib['name'] == 'Argument.value':
                    el.text = str(self._value)
                elif el.attrib['name'] == 'HTTPArgument.use_equals':
                    el.text = str(self.use_equals).lower()
                elif el.attrib['name'] == 'Argument.name':
                    el.text = self.name

                if self.content_type and flag:
                    e = SubElement(element, 'stringProp')
                    e.set('name', 'HTTPArgument.content_type')
                    e.text = self.content_type
                    flag = False
        return tree_to_str(xml_tree)
