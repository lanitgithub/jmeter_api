from abc import ABC

from jmeter_api.basics.utils import Renderable
import logging


class BasicElement(ABC):

    root_element_name = 'Arguments'

    def __init__(self, name: str = 'BasicElement', comments: str = '', is_enabled: bool = True):
        logging.info(f'{type(self).__name__} | Init started')
        self.name = name
        self.comments = comments
        self.is_enabled = is_enabled

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value) -> None:
        if not isinstance(value, str):
            raise TypeError(
                f'arg: name must be str. {type(value).__name__} was given.')
        self._name = value

    @property
    def comments(self) -> str:
        return self._comments

    @comments.setter
    def comments(self, value) -> None:
        if not isinstance(value, str):
            raise TypeError(
                f'arg: comments must be str. {type(value).__name__} was given.')
        self._comments = value

    @property
    def is_enabled(self) -> bool:
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, value) -> None:
        if not isinstance(value, bool):
            raise TypeError(
                f'arg: is_enabled must be bool. {type(value).__name__} was given.')
        self._is_enabled = value
