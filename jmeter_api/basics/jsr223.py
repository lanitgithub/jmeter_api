import os
import logging

from abc import ABC
from enum import Enum


class ScriptLanguage(Enum):
    GROOVY = 'groovy'
    BEANSHELL = 'beanshell'
    BSH = 'bsh'
    ECMASCRIPT = 'ecmasript'
    JAVA = 'java'
    JS = 'javascript'
    JEXL = 'jexl'
    JEXL2 = 'jexl2'


class JSR223(ABC):
    def __init__(self, *,
                 cache_key: bool = True,
                 filename: str = '',
                 parameters: str = '',
                 script: str = '',
                 script_language: ScriptLanguage = ScriptLanguage.GROOVY,
                 name: str = 'JSR223 Element',
                 comments: str = '',
                 is_enabled: bool = True
                 ):
        """

        :type source_type: object
        """
        self.cache_key = cache_key
        self.filename = filename
        self.parameters = parameters
        self.script = script
        self.script_language = script_language

    @property
    def filename(self):
        return self._filename

    @filename.setter
    def filename(self, value):
        if not isinstance(value, str):
            raise TypeError(
                f'arg: filename should be str. {type(value).__name__} was given')
        if not value == '':
            if not os.path.isfile(value):
                raise OSError('File ' + value + ' not found')
        self._filename = value

    @property
    def parameters(self):
        return self._parameters

    @parameters.setter
    def parameters(self, value):
        if not isinstance(value, str):
            raise TypeError(
                f'arg: parameters should be str. {type(value).__name__} was given')
        self._parameters = value

    @property
    def script(self):
        return self._script

    @script.setter
    def script(self, value):
        if not isinstance(value, str):
            raise TypeError(
                f'arg: script should be str. {type(value).__name__} was given')
        self._script = value

    @property
    def script_language(self):
        return self._script_language

    @script_language.setter
    def script_language(self, value):
        if not isinstance(value, ScriptLanguage):
            raise TypeError(
                f'arg: script_language should be ScriptLanguage. {type(value).__name__} was given')
        self._script_language = value

    @property
    def cache_key(self):
        return self._cache_key

    @cache_key.setter
    def cache_key(self, value):
        if not isinstance(value, bool):
            raise TypeError(
                f'arg: cache_key should be bool. {type(value).__name__} was given')
        self._cache_key = str(value).lower()
