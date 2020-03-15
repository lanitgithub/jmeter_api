import logging

from typing import List, Optional, Union
from xml.etree.ElementTree import Element
from enum import Enum

from jmeter_api.basics.config.elements import BasicConfig
from jmeter_api.basics.utils import Renderable, FileEncoding, tree_to_str


class Implementation(Enum):
    JAVA = 'Java'
    HTTP = 'HttpClient4'


class IpSourceType(Enum):
    IP = '0'
    DEVICE = '1'
    DEVICE_IPV4 = '2'
    DEVICE_IPV6 = '3'


class PostBodyRaw(Renderable):

    TEMPLATE = 'postbody.xml'
    root_element_name = 'elementProp'
    
    def __init__(self, *,
                 value: str,
                 metadata: str = '=',
                 encode: bool = False):
        self.metadata = metadata
        self.value = value
        self.encode = encode
        
    @property
    def encode(self) -> str:
        return self._encode

    @encode.setter
    def encode(self, value):
        if not isinstance(value, bool):
            raise TypeError(
                f'encode must be bool. {type(value).__name__} was given')
        self._encode = str(value).lower()

    @property
    def metadata(self) -> str:
        return self._metadata

    @metadata.setter
    def metadata(self, value):
        if not isinstance(value, str):
            raise TypeError(
                f'metadata must be str. {type(value).__name__} was given')
        self._metadata = value
        
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
        
        for element in list(element_root):
            try:
                if element.attrib['name'] == 'HTTPArgument.always_encode':
                    element.text = self.encode
                elif element.attrib['name'] == 'Argument.value':
                    element.text = self.value
                elif element.attrib['name'] == 'Argument.metadata':
                    element.text = self.metadata
            except KeyError:
                logging.error(
                    f'Unable to properly convert {self.__class__} to xml.')
        return tree_to_str(xml_tree)
    
        
class Argument(Renderable):
    
    TEMPLATE = 'argument.xml'
    root_element_name = 'elementProp'
    
    def __init__(self, *,
                 name: str,
                 value: str,
                 encode: bool = False,
                 use_equals: bool = True,
                 content_type: str = 'text/plain'):
        self.name = name
        self.value = value
        self.encode = encode
        self.use_equals = use_equals
        self.content_type = content_type
        if use_equals:
            self.metadata = '='
        else:
            self.metadata = ''
            
    @property
    def encode(self) -> str:
        return self._encode

    @encode.setter
    def encode(self, value):
        if not isinstance(value, bool):
            raise TypeError(
                f'encode must be bool. {type(value).__name__} was given')
        self._encode = str(value).lower()
        
    @property
    def use_equals(self) -> str:
        return self._use_equals

    @use_equals.setter
    def use_equals(self, value):
        if not isinstance(value, bool):
            raise TypeError(
                f'use_equals must be bool. {type(value).__name__} was given')
        self._use_equals =str(value).lower()
        
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
    def metadata(self) -> str:
        return self._metadata

    @metadata.setter
    def metadata(self, value):
        if not isinstance(value, str):
            raise TypeError(
                f'metadata must be str. {type(value).__name__} was given')
        self._metadata = value
        
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
    def content_type(self) -> str:
        return self._content_type

    @content_type.setter
    def content_type(self, value):
        if not isinstance(value, str):
            raise TypeError(
                f'content_type must be str. {type(value).__name__} was given')
        self._content_type = value

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
                elif element.attrib['name'] == 'Argument.metadata':
                    element.text = self.metadata
                elif element.attrib['name'] == 'HTTPArgument.always_encode':
                    element.text = self.encode
                elif element.attrib['name'] == 'HTTPArgument.use_equals':
                    element.text = self.use_equals
            except KeyError:
                logging.error(
                    f'Unable to properly convert {self.__class__} to xml.')
        if not self.content_type == 'text/plain':
            el = Element('stringProp', attrib={'name': 'HTTPArgument.content_type'})
            el.text = self.content_type
            element_root.append(el)
        return tree_to_str(xml_tree)


class HTTPRequestDefaults(BasicConfig, Renderable):

    root_element_name = 'ConfigTestElement'

    def __init__(self, *,
                 arguments: Union[List[Argument], str] = [],
                 domain: str = '',
                 port: int = None,
                 protocol: str = '',
                 encoding: FileEncoding = None,
                 path: str = '',
                 concurrent_pool: int = 6,
                 connect_timeout: int = None,
                 response_timeout: int = None,
                 image_parser: bool = False,
                 concurrent_dwn: bool = False,
                 md5: bool = False,
                 embedded_url_re: str = None,
                 ip_source: str = None,
                 ip_source_type: IpSourceType = None,
                 proxy_scheme: str = None,
                 proxy_host: str = None,
                 proxy_port: int = None,
                 proxy_user: str = None,
                 proxy_pass: str = None,
                 implementation: Implementation = None,
                 name: str = 'HTTP Request Defaults',
                 comments: str = '',
                 is_enabled: bool = True):
        # basic fields
        self.arguments = arguments
        self.domain = domain
        self.port = port
        self.protocol = protocol
        self.encoding = encoding
        self.path = path
        self.concurrent_pool = concurrent_pool
        self.connect_timeout = connect_timeout
        self.response_timeout = response_timeout
        # advanced fields
        self.image_parser = image_parser
        self.concurrent_dwn = concurrent_dwn
        self.md5 = md5
        self.embedded_url_re = embedded_url_re
        self.ip_source = ip_source
        self.ip_source_type = ip_source_type
        self.proxy_scheme = proxy_scheme
        self.proxy_host = proxy_host
        self.proxy_port = proxy_port
        self.proxy_user = proxy_user
        self.proxy_pass = proxy_pass
        self.implementation = implementation
        super().__init__(name=name, comments=comments, is_enabled=is_enabled)

    # basic fields
    @property
    def arguments(self):
        return self._arguments

    @arguments.setter
    def arguments(self, value):
        if not isinstance(value, (List, str)):
            raise TypeError(
                f'arguments must be List or str. {type(value).__name__} was given')
        if isinstance(value, List):
            for i in range(len(value)):
                if not isinstance(value[i], Argument):
                    raise TypeError(
                    f'arguments list must contain Argument. {type(value).__name__} was given')
        self._arguments = value

    @property
    def domain(self) -> str:
        return self._domain

    @domain.setter
    def domain(self, value):
        if not isinstance(value, str):
            raise TypeError(
                f'domain must be str. {type(value).__name__} was given')
        self._domain = value

    @property
    def port(self) -> str:
        return self._port

    @port.setter
    def port(self, value):
        if value is None:
            self._port = ""
        elif not isinstance(value, int) or value < 0:
            raise TypeError(
                f'port must be positive int. {type(value).__name__} was given')
        else:
            self._port = str(value)

    @property
    def protocol(self) -> str:
        return self._protocol

    @protocol.setter
    def protocol(self, value):
        if not isinstance(value, str):
            raise TypeError(
                f'protocol must be str. {type(value).__name__} was given')
        self._protocol = value
        
    @property
    def encoding(self) -> str:
        return self._encoding

    @encoding.setter
    def encoding(self, value):
        if value is None:
            self._encoding = ""
        elif not isinstance(value, FileEncoding):
            raise TypeError(
                f'encoding must be FileEncoding. {type(value).__name__} was given')
        else:
            self._encoding = value.value

    @property
    def path(self) -> str:
        return self._path

    @path.setter
    def path(self, value):
        if not isinstance(value, str):
            raise TypeError(
                f'path must be str. {type(value).__name__} was given')
        self._path = value

    @property
    def concurrent_pool(self) -> str:
        return self._concurrent_pool

    @concurrent_pool.setter
    def concurrent_pool(self, value):
        if not isinstance(value, int) or value < 0:
            raise TypeError(
                f'concurrent_pool must be positive int. {type(value).__name__} was given')
        self._concurrent_pool = str(value)

    @property
    def connect_timeout(self) -> str:
        return self._connect_timeout

    @connect_timeout.setter
    def connect_timeout(self, value):
        if value is None:
            self._connect_timeout = ""
        elif not isinstance(value, int) or value < 0:
            raise TypeError(
                f'connect_timeout must be positive int. {type(value).__name__} was given')
        else:
            self._connect_timeout = str(value)

    @property
    def response_timeout(self) -> str:
        return self._response_timeout

    @response_timeout.setter
    def response_timeout(self, value):
        if value is None:
            self._response_timeout = ""
        elif not isinstance(value, int) or value < 0:
            raise TypeError(
                f'response_timeout must be positive int. {type(value).__name__} was given')
        else:
            self._response_timeout = str(value)

    # advanced fields
    @property
    def image_parser(self) -> bool:
        return self._image_parser

    @image_parser.setter
    def image_parser(self, value):
        if not isinstance(value, bool):
            raise TypeError(
                f'image_parser must be bool. {type(value).__name__} was given')
        self._image_parser = value
    
    @property
    def concurrent_dwn(self) -> bool:
        return self._concurrent_dwn

    @concurrent_dwn.setter
    def concurrent_dwn(self, value):
        if not isinstance(value, bool):
            raise TypeError(
                f'concurrent_dwn must be bool. {type(value).__name__} was given')
        self._concurrent_dwn = value

    @property
    def md5(self) -> bool:
        return self._md5

    @md5.setter
    def md5(self, value):
        if not isinstance(value, bool):
            raise TypeError(
                f'md5 must be bool. {type(value).__name__} was given')
        self._md5 = value

    @property
    def embedded_url_re(self) -> str:
        return self._embedded_url_re

    @embedded_url_re.setter
    def embedded_url_re(self, value):
        if value is None:
            self._embedded_url_re = ""
        elif not isinstance(value, str):
            raise TypeError(
                f'embedded_url_re must be str. {type(value).__name__} was given')
        else:
            self._embedded_url_re = value

    @property
    def ip_source(self) -> str:
        return self._ip_source

    @ip_source.setter
    def ip_source(self, value):
        if value is None:
            self._ip_source = ""
        elif not isinstance(value, str):
            raise TypeError(
                f'ip_source must be str. {type(value).__name__} was given')
        else:
            self._ip_source = value

    @property
    def ip_source_type(self) -> str:
        return self._ip_source_type

    @ip_source_type.setter
    def ip_source_type(self, value):
        if value is None:
            self._ip_source_type = ""
        elif not isinstance(value, IpSourceType):
            raise TypeError(
                f'ip_source_type must be IpSourceType. {type(value).__name__} was given')
        else:
            self._ip_source_type = value.value

    @property
    def proxy_scheme(self) -> str:
        return self._proxy_scheme

    @proxy_scheme.setter
    def proxy_scheme(self, value):
        if value is None:
            self._proxy_scheme = ""
        elif not isinstance(value, str):
            raise TypeError(
                f'proxy_scheme must be str. {type(value).__name__} was given')
        else:
            self._proxy_scheme = value

    @property
    def proxy_host(self) -> str:
        return self._proxy_host

    @proxy_host.setter
    def proxy_host(self, value):
        if value is None:
            self._proxy_host = ""
        elif not isinstance(value, str):
            raise TypeError(
                f'proxy_host must be str. {type(value).__name__} was given')
        else:
            self._proxy_host = value

    @property
    def proxy_port(self) -> str:
        return self._proxy_port

    @proxy_port.setter
    def proxy_port(self, value):
        if value is None:
            self._proxy_port = ""
        elif not isinstance(value, int) or value < 0:
            raise TypeError(
                f'proxy_port must be positive int. {type(value).__name__} was given')
        else:
            self._proxy_port = str(value)

    @property
    def proxy_user(self) -> str:
        return self._proxy_user

    @proxy_user.setter
    def proxy_user(self, value):
        if value is None:
            self._proxy_user = ""
        elif not isinstance(value, str):
            raise TypeError(
                f'proxy_user must be str. {type(value).__name__} was given')
        else:
            self._proxy_user = value

    @property
    def proxy_pass(self) -> str:
        return self._proxy_pass

    @proxy_pass.setter
    def proxy_pass(self, value):
        if value is None:
            self._proxy_pass = ""
        elif not isinstance(value, str):
            raise TypeError(
                f'proxy_pass must be str. {type(value).__name__} was given')
        else:
            self._proxy_pass = value

    @property
    def implementation(self) -> str:
        return self._implementation

    @implementation.setter
    def implementation(self, value):
        if value is None:
            self._implementation = ""
        elif not isinstance(value, Implementation):
            raise TypeError(
                f'implementation must be Implementation. {type(value).__name__} was given')
        else:
            self._implementation = value.value
            
    def to_xml(self) -> str:
        element_root, xml_tree = super()._add_basics()

        for element in list(element_root):
            try:
                # basic fields
                if element.attrib['name'] == 'HTTPSampler.domain':
                    element.text = self.domain
                elif element.attrib['name'] == 'HTTPSampler.port':
                    element.text = self.port
                elif element.attrib['name'] == 'HTTPSampler.protocol':
                    element.text = self.protocol
                elif element.attrib['name'] == 'HTTPSampler.contentEncoding':
                    element.text = self.encoding
                elif element.attrib['name'] == 'HTTPSampler.path':
                    element.text = self.path
                elif element.attrib['name'] == 'HTTPSampler.connect_timeout':
                    element.text = self.connect_timeout
                elif element.attrib['name'] == 'HTTPSampler.response_timeout':
                    element.text = self.response_timeout
                elif element.attrib['name'] == 'HTTPSampler.concurrentPool':
                    element.text = self.concurrent_pool
                elif element.attrib['name'] == 'HTTPsampler.Arguments':
                    arg_elem = element[0]
                    if isinstance(self.arguments, str):
                        # Post Body
                        el = Element("boolProp", attrib={"name": "HTTPSampler.postBodyRaw"})
                        el.text = 'true'
                        element_root.append(el)
                        arg_elem.text = PostBodyRaw(value=self.arguments).to_xml()
                    else:
                        # Arguments
                        arg_elem.text = ''
                        for arg in self.arguments:
                            arg_elem.text += arg.to_xml()
            except KeyError:
                logging.error(
                    f'Unable to properly convert {self.__class__} to xml.')
            # advanced fields
            if self.image_parser:
                el = Element("boolProp", attrib={"name": "HTTPSampler.image_parser"})
                el.text = str(self.image_parser).lower()
                element_root.append(el)
            if self.concurrent_dwn:
                el = Element("boolProp", attrib={"name": "HTTPSampler.concurrentDwn"})
                el.text = str(self.concurrent_dwn).lower()
                element_root.append(el)
            if self.md5:
                el = Element("boolProp", attrib={"name": "HTTPSampler.md5"})
                el.text = str(self.md5).lower()
                element_root.append(el)
            if len(self.ip_source_type) > 0:
                el = Element("intProp", attrib={"name": "HTTPSampler.ipSourceType"})
                el.text = self.ip_source_type
                element_root.append(el)
            if len(self.embedded_url_re) > 0:
                el = Element("stringProp", attrib={"name": "HTTPSampler.embedded_url_re"})
                el.text = self.embedded_url_re
                element_root.append(el)
            if len(self.proxy_scheme) > 0:
                el = Element("stringProp", attrib={"name": "HTTPSampler.proxyScheme"})
                el.text = self.proxy_scheme
                element_root.append(el)
            if len(self.proxy_host) > 0:
                el = Element("stringProp", attrib={"name": "HTTPSampler.proxyHost"})
                el.text = self.proxy_host
                element_root.append(el)
            if len(self.proxy_port) > 0:
                el = Element("stringProp", attrib={"name": "HTTPSampler.proxyPort"})
                el.text = self.proxy_port
                element_root.append(el)
            if len(self.proxy_user) > 0:
                el = Element("stringProp", attrib={"name": "HTTPSampler.proxyUser"})
                el.text = self.proxy_user
                element_root.append(el)
            if len(self.proxy_pass) > 0:
                el = Element("stringProp", attrib={"name": "HTTPSampler.proxyPass"})
                el.text = self.proxy_pass
                element_root.append(el)
            if len(self.implementation) > 0:
                el = Element("stringProp", attrib={"name": "HTTPSampler.implementation"})
                el.text = self.implementation
                element_root.append(el)
            if len(self.ip_source) > 0:
                el = Element("stringProp", attrib={"name": "HTTPSampler.ipSource"})
                el.text = self.ip_source
                element_root.append(el)
        return tree_to_str(xml_tree)
