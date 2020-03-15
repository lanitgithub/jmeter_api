from abc import ABC
from enum import Enum

from jmeter_api.basics.thread_group.elements import BasicThreadGroup, ThreadGroupAction


class Unit(Enum):
    MINUTE = 'M'
    SECOND = 'S'


class BasicBzmThreadGroup(BasicThreadGroup, ABC):
    def __init__(self,
                 log_filename: str = None,
                 unit:  Unit = Unit.MINUTE,
                 on_sample_error: ThreadGroupAction = ThreadGroupAction.CONTINUE,
                 name: str = 'BasicBzmThreadGroup',
                 comments: str = '',
                 is_enabled: bool = True):
        self.log_filename = log_filename
        self.unit = unit
        BasicThreadGroup.__init__(self,
                        name=name,
                        comments=comments,
                        is_enabled=is_enabled,
                        on_sample_error=on_sample_error)

    @property
    def log_filename(self) -> str:
        return self._log_filename

    @log_filename.setter
    def log_filename(self, value):
        if value is None:
            self._log_filename = ""
        elif not isinstance(value, str):
            raise TypeError(
                f'log_filename must be str. {type(value)} was given')
        else:
            self._log_filename = value

    @property
    def unit(self):
        return self._unit

    @unit.setter
    def unit(self, value):
        if not isinstance(value, Unit):
            raise TypeError(
                f'unit must be Unit. {type(value)} was given')
        self._unit = value
