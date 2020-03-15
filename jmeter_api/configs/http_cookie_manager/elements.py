import logging

from typing import List, Optional
from enum import Enum
from xml.etree.ElementTree import Element

from jmeter_api.basics.config.elements import BasicConfig
from jmeter_api.basics.utils import Renderable, FileEncoding, tree_to_str


class CookiePolicy(Enum):
    STANDARD = 'standard'
    STANDARD_STRICT = 'standard-strict'
    IGNORE = 'ignoreCookies'
    NETSCAPE = 'netscape'
    DEFAULT = 'default'
    RFC2109 = 'rfc2109'
    RFC2965 = 'RFC2965'
    BEST_MATCH = 'best-match'
    

class Cookie(Renderable):
    
    TEMPLATE = 'cookie.xml'
    root_element_name = 'elementProp'
    
    def __init__(self, *,
                 name: str,
                 value: str,
                 domain: str = '',
                 path: str = '',
                 secure: bool = False,
                 expires: int = 0,
                 path_specified: bool = True,
                 domain_specified: bool = True):
        self.name = name
        self.value = value
        self.domain = domain
        self.path = path
        self.secure = secure
        self.expires = expires
        self.path_specified = path_specified
        self.domain_specified = domain_specified

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
    def domain(self) -> str:
        return self._domain

    @domain.setter
    def domain(self, value):
        if not isinstance(value, str):
            raise TypeError(
                f'domain must be str. {type(value).__name__} was given')
        self._domain = value

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
    def expires(self) -> str:
        return self._expires

    @expires.setter
    def expires(self, value):
        if not isinstance(value, int):
            raise TypeError(
                f'expires must be int. {type(value).__name__} was given')
        self._expires = str(value)

    @property
    def secure(self) -> str:
        return self._secure

    @secure.setter
    def secure(self, value):
        if not isinstance(value, bool):
            raise TypeError(
                f'secure must be bool. {type(value).__name__} was given')
        self._secure = str(value).lower()

    @property
    def path_specified(self) -> str:
        return self._path_specified

    @path_specified.setter
    def path_specified(self, value):
        if not isinstance(value, bool):
            raise TypeError(
                f'path_specified must be bool. {type(value).__name__} was given')
        self._path_specified = str(value).lower()

    @property
    def domain_specified(self) -> str:
        return self._domain_specified

    @domain_specified.setter
    def domain_specified(self, value):
        if not isinstance(value, bool):
            raise TypeError(
                f'domain_specified must be bool. {type(value).__name__} was given')
        self._domain_specified = str(value).lower()

    def to_xml(self) -> str:
        xml_tree: Optional[Element] = super().get_template()
        element_root = xml_tree.find(self.root_element_name)
        element_root.attrib['name'] = self.name
        element_root.attrib['testname'] = self.name
        
        for element in list(element_root):
            try:
                if element.attrib['name'] == 'Cookie.value':
                    element.text = self.value
                elif element.attrib['name'] == 'Cookie.domain':
                    element.text = self.domain
                elif element.attrib['name'] == 'Cookie.path':
                    element.text = self.path
                elif element.attrib['name'] == 'Cookie.secure':
                    element.text = self.secure
                elif element.attrib['name'] == 'Cookie.expires':
                    element.text = self.expires
                elif element.attrib['name'] == 'Cookie.path_specified':
                    element.text = self.path_specified
                elif element.attrib['name'] == 'Cookie.domain_specified':
                    element.text = self.domain_specified
            except KeyError:
                logging.error(
                    f'Unable to properly convert {self.__class__} to xml.')
        return tree_to_str(xml_tree)


class HTTPCookieManager(BasicConfig, Renderable):

    root_element_name = 'CookieManager'

    def __init__(self, *,
                 cookies: List[Cookie] = [],
                 clear_each_iter: bool = False,
                 policy: CookiePolicy = CookiePolicy.STANDARD,
                 name: str = 'HTTP Cookie Manager',
                 comments: str = '',
                 is_enabled: bool = True):
        self.cookies = cookies
        self.policy = policy
        self.clear_each_iter = clear_each_iter
        super().__init__(name=name, comments=comments, is_enabled=is_enabled)

    @property
    def policy(self):
        return self._policy

    @policy.setter
    def policy(self, value):
        if not isinstance(value, CookiePolicy):
            raise TypeError(
                f'policy must be CookiePolicy. {type(value).__name__} was given')
        self._policy = value

    @property
    def clear_each_iter(self) -> str:
        return self._clear_each_iter

    @clear_each_iter.setter
    def clear_each_iter(self, value):
        if not isinstance(value, bool):
            raise TypeError(
                f'clear_each_iter must be bool. {type(value).__name__} was given')
        self._clear_each_iter = str(value).lower()

    @property
    def cookies(self) -> str:
        return self._cookies

    @cookies.setter
    def cookies(self, value):
        if not isinstance(value, List):
            raise TypeError(
                f'arguments must be List. {type(value).__name__} was given')
        for el in value:
            if not isinstance(el, Cookie):
                raise TypeError(
                f'arguments must contain only Cookie. {type(value).__name__} was given')
        self._cookies = value

    def to_xml(self) -> str:
        element_root, xml_tree = super()._add_basics()

        for element in list(element_root):
            try:
                if element.attrib['name'] == 'CookieManager.cookies':
                    element.text = ''
                    for arg in self.cookies:
                        element.text += arg.to_xml()
                elif element.attrib['name'] == 'CookieManager.clearEachIteration':
                    element.text = self.clear_each_iter
            except KeyError:
                logging.error(
                    f'Unable to properly convert {self.__class__} to xml.')
        if not self.policy is CookiePolicy.STANDARD:
            el = Element('stringProp', attrib={'name': 'CookieManager.policy'})
            el.text = str(self.policy.value)
            element_root.append(el)
        return tree_to_str(xml_tree)
