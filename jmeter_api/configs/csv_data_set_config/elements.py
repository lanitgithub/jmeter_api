import os
import logging

from typing import List
from enum import Enum

from jmeter_api.basics.config.elements import BasicConfig
from jmeter_api.basics.utils import Renderable, FileEncoding, tree_to_str


class ShareMode(Enum):
    ALL = 'shareMode.all'
    GROUP = 'shareMode.group'
    THREAD = 'shareMode.thread'


class CsvDataSetConfig(BasicConfig, Renderable):

    root_element_name = 'CSVDataSet'

    def __init__(self, *,
                 file_path: str,
                 variable_names: List[str],
                 file_encoding: FileEncoding = FileEncoding.UTF8,
                 ignore_first_line: bool = False,
                 delimiter: str = ",",
                 quoted_data: bool = False,
                 recycle: bool = True,
                 stop_thread: bool = False,
                 share_mode: ShareMode = ShareMode.ALL,
                 name: str = 'CsvDataSetConfig',
                 comments: str = '',
                 is_enabled: bool = True):
        self.file_path = file_path
        self.delimiter = delimiter
        self.variable_names = variable_names
        self.file_encoding = file_encoding
        self.ignore_first_line = ignore_first_line
        self.quoted_data = quoted_data
        self.recycle = recycle
        self.stop_thread = stop_thread
        self.share_mode = share_mode
        super().__init__(name=name, comments=comments, is_enabled=is_enabled)

    @property
    def file_path(self) -> str:
        return self._file_path

    @file_path.setter
    def file_path(self, value):
        if not os.path.isfile(value):
            raise FileNotFoundError(f'{value} is not file')
        self._file_path = value

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
    def ignore_first_line(self) -> bool:
        return self._ignore_first_line

    @ignore_first_line.setter
    def ignore_first_line(self, value):
        if not isinstance(value, bool):
            raise TypeError(
                f'ignore_first_line must be bool. {type(value).__name__} was given')
        self._ignore_first_line = value

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
    def quoted_data(self) -> bool:
        return self._quoted_data

    @quoted_data.setter
    def quoted_data(self, value):
        if not isinstance(value, bool):
            raise TypeError(
                f'quoted_data must be bool. {type(value).__name__} was given')
        self._quoted_data = value

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
    def stop_thread(self) -> bool:
        return self._stop_thread

    @stop_thread.setter
    def stop_thread(self, value):
        if not isinstance(value, bool):
            raise TypeError(
                f'stop_thread must be bool. {type(value).__name__} was given')
        self._stop_thread = value

    @property
    def share_mode(self) -> ShareMode:
        return self._share_mode

    @share_mode.setter
    def share_mode(self, value):
        if not isinstance(value, ShareMode):
            raise TypeError(
                f'share_mode must be ShareMode. {type(value).__name__} was given')
        else:
            self._share_mode = value

    def to_xml(self) -> str:
        element_root, xml_tree = super()._add_basics()

        for element in list(element_root):
            try:
                if element.attrib['name'] == 'delimiter':
                    element.text = self.delimiter
                elif element.attrib['name'] == 'fileEncoding':
                    element.text = self.file_encoding.value
                elif element.attrib['name'] == 'filename':
                    element.text = self.file_path
                elif element.attrib['name'] == 'ignoreFirstLine':
                    element.text = str(self.ignore_first_line).lower()
                elif element.attrib['name'] == 'quotedData':
                    element.text = str(self.quoted_data).lower()
                elif element.attrib['name'] == 'recycle':
                    element.text = str(self.recycle).lower()
                elif element.attrib['name'] == 'shareMode':
                    element.text = self.share_mode.value
                elif element.attrib['name'] == 'stopThread':
                    element.text = str(self.stop_thread).lower()
                elif element.attrib['name'] == 'variableNames':
                    element.text = self.variable_names
            except KeyError:
                logging.error(
                    f'Unable to properly convert {self.__class__} to xml.')
        return tree_to_str(xml_tree)
