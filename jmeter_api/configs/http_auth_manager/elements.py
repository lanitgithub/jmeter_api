import logging

from typing import List, Optional
from enum import Enum
from xml.etree.ElementTree import Element

from jmeter_api.basics.config.elements import BasicConfig
from jmeter_api.basics.utils import Renderable, FileEncoding, tree_to_str


class AuthMechanism(Enum):
    BASIC = 'BASIC'
    DIGEST = 'DIGEST'
    KERBEROS = 'KERBEROS'
    BASIC_DIGEST = 'BASIC_DIGEST' 

class Auth(Renderable):
    
    TEMPLATE = 'auth.xml'
    root_element_name = 'elementProp'
    
    def __init__(self, *,
                 url: str = '',
                 username: str,
                 password: str,
                 domain: str = '',
                 realm: str = '',
                 mechanism: AuthMechanism = AuthMechanism.BASIC):
        self.url = url
        self.username = username
        self.password = password
        self.domain = domain
        self.realm = realm
        self.mechanism = mechanism

    @property
    def url(self) -> str:
        return self._url

    @url.setter
    def url(self, value):
        if not isinstance(value, str):
            raise TypeError(
                f'url must be str. {type(value).__name__} was given')
        self._url = value

    @property
    def username(self) -> str:
        return self._username

    @username.setter
    def username(self, value):
        if not isinstance(value, str):
            raise TypeError(
                f'username must be str. {type(value).__name__} was given')
        self._username = value

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
    def password(self) -> str:
        return self._password

    @password.setter
    def password(self, value):
        if not isinstance(value, str):
            raise TypeError(
                f'password must be str. {type(value).__name__} was given')
        self._password = value

    @property
    def realm(self) -> str:
        return self._realm

    @realm.setter
    def realm(self, value):
        if not isinstance(value, str):
            raise TypeError(
                f'realm must be str. {type(value).__name__} was given')
        self._realm = value

    @property
    def mechanism(self) -> str:
        return self._mechanism

    @mechanism.setter
    def mechanism(self, value):
        if not isinstance(value, AuthMechanism):
            raise TypeError(
                f'mechanism must be AuthMechanism. {type(value).__name__} was given')
        self._mechanism = value

    def to_xml(self) -> str:
        xml_tree: Optional[Element] = super().get_template()
        element_root = xml_tree.find(self.root_element_name)
        element_root.attrib['name'] = self.username
        
        for element in list(element_root):
            try:
                if element.attrib['name'] == 'Authorization.url':
                    element.text = self.url
                elif element.attrib['name'] == 'Authorization.username':
                    element.text = self.username
                elif element.attrib['name'] == 'Authorization.password':
                    element.text = self.password
                elif element.attrib['name'] == 'Authorization.domain':
                    element.text = self.domain
                elif element.attrib['name'] == 'Authorization.realm':
                    element.text = self.realm
            except KeyError:
                logging.error(
                    f'Unable to properly convert {self.__class__} to xml.')
        if not self.mechanism is AuthMechanism.BASIC:
            el = Element('stringProp', attrib={'name': 'Authorization.mechanism'})
            el.text = str(self.mechanism.value)
            element_root.append(el)
        return tree_to_str(xml_tree)


class HTTPAuthManager(BasicConfig, Renderable):

    root_element_name = 'AuthManager'

    def __init__(self, *,
                 auth_list: List[Auth] = [],
                 clear_each_iter: bool = False,
                 name: str = 'HTTP Authorization Manager',
                 comments: str = '',
                 is_enabled: bool = True):
        self.auth_list = auth_list
        self.clear_each_iter = clear_each_iter
        super().__init__(name=name, comments=comments, is_enabled=is_enabled)

    @property
    def clear_each_iter(self) -> bool:
        return self._clear_each_iter

    @clear_each_iter.setter
    def clear_each_iter(self, value):
        if not isinstance(value, bool):
            raise TypeError(
                f'clear_each_iter must be bool. {type(value).__name__} was given')
        self._clear_each_iter = value

    @property
    def auth_list(self) -> str:
        return self._auth_list

    @auth_list.setter
    def auth_list(self, value):
        if not isinstance(value, List):
            raise TypeError(
                f'auth_list must be List. {type(value).__name__} was given')
        for el in value:
            if not isinstance(el, Auth):
                raise TypeError(
                f'auth_list must contain only Auth. {type(value).__name__} was given')
        self._auth_list = value

    def to_xml(self) -> str:
        element_root, xml_tree = super()._add_basics()

        for element in list(element_root):
            try:
                if element.attrib['name'] == 'AuthManager.auth_list':
                    element.text = ''
                    for arg in self.auth_list:
                        element.text += arg.to_xml()
            except KeyError:
                logging.error(
                    f'Unable to properly convert {self.__class__} to xml.')
        if self.clear_each_iter:
            el = Element('boolProp', attrib={'name': 'AuthManager.clearEachIteration'})
            el.text = str(self.clear_each_iter).lower()
            element_root.append(el)
        return tree_to_str(xml_tree)
