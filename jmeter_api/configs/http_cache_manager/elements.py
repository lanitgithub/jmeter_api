import logging

from jmeter_api.basics.config.elements import BasicConfig
from jmeter_api.basics.utils import Renderable, tree_to_str


class HTTPCacheManager(BasicConfig, Renderable):
    root_element_name = 'CacheManager'

    def __init__(self, *,
                 clear_each_iteration: bool = False,
                 use_cache_control: bool = True,
                 max_elements_in_cache: int = 300,
                 name: str = 'HTTP_Cache_Manager',
                 comments: str = '',
                 is_enabled: bool = True):
        self.clear_each_iteration = clear_each_iteration
        self.use_cache_control = use_cache_control
        self.max_elements_in_cache = max_elements_in_cache
        super().__init__(name=name, comments=comments, is_enabled=is_enabled)

    @property
    def clear_each_iteration(self) -> bool:
        return self._clear_each_iteration

    @clear_each_iteration.setter
    def clear_each_iteration(self, value):
        if not isinstance(value, bool):
            raise TypeError(f'clear_each_iteration should be bool. '
                            f'{type(value).__name__} was given')
        self._clear_each_iteration = value

    @property
    def use_cache_control(self) -> bool:
        return self._use_cache_control

    @use_cache_control.setter
    def use_cache_control(self, value):
        if not isinstance(value, bool):
            raise TypeError(
                f'use_cache_control should be bool. {type(value).__name__} was given')
        self._use_cache_control = value

    @property
    def max_elements_in_cache(self) -> int:
        return self._max_elements_in_cache

    @max_elements_in_cache.setter
    def max_elements_in_cache(self, value):
        if not isinstance(value, int):
            raise TypeError(
                f'max_elements_in_cache should be int.'
                f' {type(value).__name__} was given')
        self._max_elements_in_cache = value

    def to_xml(self) -> str:
        element_root, xml_tree = super()._add_basics()

        for element in list(element_root):
            try:
                if element.attrib['name'] == 'clearEachIteration':
                    element.text = str(self.clear_each_iteration).lower()
                elif element.attrib['name'] == 'useExpires':
                    element.text = str(self.use_cache_control).lower()
                elif element.attrib['name'] == 'maxSize':
                    element.text = str(self.max_elements_in_cache)
            except KeyError:
                logging.error(
                    f'Unable to properly convert {self.__class__} to xml.')
        return tree_to_str(xml_tree)
