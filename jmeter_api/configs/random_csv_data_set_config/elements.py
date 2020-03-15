import os
import logging

from typing import List

from jmeter_api.basics.config.elements import BasicConfig
from jmeter_api.basics.utils import Renderable, FileEncoding, tree_to_str


class RandomCsvDataSetConfig(BasicConfig, Renderable):

    root_element_name = 'com.blazemeter.jmeter.RandomCSVDataSetConfig'

    def __init__(self, *,
                 filename: str,
                 variable_names: List[str],
                 file_encoding: FileEncoding = FileEncoding.UTF8,
                 delimiter: str = ",",
                 random_order: bool = True,
                 ignore_first_line: bool = False,
                 recycle: bool = True,
                 independent_per_thread: bool = False,
                 name: str = 'bzm - Random CSV Data Set Config',
                 comments: str = '',
                 is_enabled: bool = True):
        self.filename = filename
        self.delimiter = delimiter
        self.variable_names = variable_names
        self.file_encoding = file_encoding
        self.ignore_first_line = ignore_first_line
        self.random_order = random_order
        self.recycle = recycle
        self.independent_per_thread = independent_per_thread
        super().__init__(name=name, comments=comments, is_enabled=is_enabled)

    @property
    def filename(self) -> str:
        return self._filename

    @filename.setter
    def filename(self, value):
        if not isinstance(value, str):
            raise TypeError(
                f'filename must be str. {type(value).__name__} was given')
        if not os.path.isfile(value):
            raise FileNotFoundError(f'{value} is not file')
        self._filename = value

    @property
    def variable_names(self) -> str:
        vnames = self.delimiter.join(self._variable_names)
        return vnames

    @variable_names.setter
    def variable_names(self, value: List[str]):
        if not isinstance(value, list):
            raise TypeError(
                f'variable_names must be List[str]. {type(value).__name__} was given')
        for element in value:
            if not isinstance(element, str):
                raise TypeError(
                    f'All elements must be str. {type(element).__name__} was given')
            if element.isdigit():
                raise TypeError(
                    f'All elements must contain chars. {type(element).__name__} was given')
        self._variable_names = value

    @property
    def file_encoding(self) -> FileEncoding:
        return self._fileEncoding

    @file_encoding.setter
    def file_encoding(self, value):
        if not isinstance(value, FileEncoding):
            raise TypeError(
                f'file_encoding must be FileEncoding. {type(value).__name__} was given')
        else:
            self._fileEncoding = value

    @property
    def delimiter(self) -> str:
        return self._delimiter

    @delimiter.setter
    def delimiter(self, value):
        if not isinstance(value, str):
            raise TypeError(
                f'delimiter must be str. {type(value).__name__} was given')
        self._delimiter = value

    @property
    def ignore_first_line(self) -> bool:
        return self._ignore_first_line

    @ignore_first_line.setter
    def ignore_first_line(self, value):
        if not isinstance(value, bool):
            raise TypeError(
                f'ignore_first_line must be bool. {type(value).__name__} was given')
        self._ignore_first_line = value

    @property
    def random_order(self) -> bool:
        return self._random_order

    @random_order.setter
    def random_order(self, value):
        if not isinstance(value, bool):
            raise TypeError(
                f'quoted_data must be bool. {type(value).__name__} was given')
        self._random_order = value

    @property
    def recycle(self) -> bool:
        return self._recycle

    @recycle.setter
    def recycle(self, value):
        if not isinstance(value, bool):
            raise TypeError(
                f'recycle must be bool. {type(value).__name__} was given')
        self._recycle = value

    @property
    def independent_per_thread(self) -> bool:
        return self._independent_per_thread

    @independent_per_thread.setter
    def independent_per_thread(self, value):
        if not isinstance(value, bool):
            raise TypeError(
                f'stop_thread must be bool. {type(value).__name__} was given')
        self._independent_per_thread = value


    def to_xml(self) -> str:
        element_root, xml_tree = super()._add_basics()

        for element in list(element_root):
            try:
                if element.attrib['name'] == 'delimiter':
                    element.text = self.delimiter
                elif element.attrib['name'] == 'fileEncoding':
                    element.text = self.file_encoding.value
                elif element.attrib['name'] == 'filename':
                    element.text = self.filename
                elif element.attrib['name'] == 'ignoreFirstLine':
                    element.text = str(self.ignore_first_line).lower()
                elif element.attrib['name'] == 'randomOrder':
                    element.text = str(self.random_order).lower()
                elif element.attrib['name'] == 'rewindOnTheEndOfList':
                    element.text = str(self.recycle).lower()
                elif element.attrib['name'] == 'independentListPerThread':
                    element.text = str(self.independent_per_thread).lower()
                elif element.attrib['name'] == 'variableNames':
                    element.text = self.variable_names
            except KeyError:
                logging.error(
                    f'Unable to properly convert {self.__class__} to xml.')
        return tree_to_str(xml_tree)
