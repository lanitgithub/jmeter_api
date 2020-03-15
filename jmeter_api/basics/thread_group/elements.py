from abc import ABC
from typing import Union
from enum import Enum

from jmeter_api.basics.element.elements import BasicElement
from jmeter_api.basics.config.elements import BasicConfig
from jmeter_api.basics.sampler.elements import BasicSampler
from jmeter_api.basics.timer.elements import BasicTimer
from jmeter_api.basics.pre_processor.elements import BasicPreProcessor
from jmeter_api.basics.post_processor.elements import BasicPostProcessor
from jmeter_api.basics.controller.elements import BasicController
from jmeter_api.basics.assertion.elements import BasicAssertion
from jmeter_api.basics.listener.elements import BasicListener
from jmeter_api.basics.test_fragment.elements import BasicTestFragment
from jmeter_api.basics.utils import IncludesElements


class ThreadGroupAction(Enum):
    CONTINUE = 'continue'
    START_NEXT_LOOP = 'startnextloop'
    STOP_THREAD = 'stopthread'
    STOP_TEST = 'stoptest'
    STOP_TEST_NOW = 'stoptestnow'


class BasicThreadGroup(BasicElement, IncludesElements, ABC):
    def __init__(self,
                 name: str = 'BasicThreadGroup',
                 comments: str = '',
                 is_enabled: bool = True,
                 on_sample_error: ThreadGroupAction = ThreadGroupAction.CONTINUE):
        self.on_sample_error = on_sample_error
        IncludesElements.__init__(self)
        super().__init__(name=name,
                         comments=comments,
                         is_enabled=is_enabled)

    def append(self, new_element: Union[BasicSampler, BasicTimer, BasicConfig, BasicController, BasicListener,\
                                        BasicPreProcessor, BasicPostProcessor, BasicAssertion, BasicTestFragment]):
        if not isinstance(new_element, (BasicSampler, BasicTimer, BasicConfig, BasicController, BasicListener,\
                                        BasicPreProcessor, BasicPostProcessor, BasicAssertion, BasicTestFragment)):
            raise TypeError(
                f'new_element must be BasicSampler, BasicTimer, BasicConfig, BasicListener, BasicPreProcessor,\
                BasicPostProcessor, BasicAssertion, BasicTestFragment or BasicController. {type(new_element)} was given')
        self._elements.append(new_element)
        return self

    @property
    def on_sample_error(self) -> ThreadGroupAction:
        return self._on_sample_error

    @on_sample_error.setter
    def on_sample_error(self, value):
        if not isinstance(value, ThreadGroupAction):
            raise TypeError(
                f'on_sample_error must be ThreadGroupAction. on_sample_error {type(value)} = {value}')
        else:
            self._on_sample_error = value


class BasicStandartThreadGroup(BasicThreadGroup, ABC):
    def __init__(self,
                 num_threads: int = 1,
                 ramp_time: int = 0,
                 continue_forever: bool = False,
                 loops: int = None,
                 is_sheduler_enable: bool = False,
                 sheduler_duration: int = None,
                 sheduler_delay:  int = None,
                 on_sample_error: ThreadGroupAction = ThreadGroupAction.CONTINUE,
                 name: str = 'BasicStandartThreadGroup',
                 comments: str = '',
                 is_enabled: bool = True):
        self.num_threads = num_threads
        self.ramp_time = ramp_time
        self.continue_forever = continue_forever
        if not continue_forever:
            if loops is None:
                loops = 1
            if loops == -1:
                raise ValueError("continue_forever can't be false, while loops equal -1")
            self.loops = loops
        else:
            if loops is None:
                loops = -1
            if loops > -1:
                raise ValueError("continue_forever can't be true, while loops not equal -1")            
            self.loops = loops
        self.is_sheduler_enable = is_sheduler_enable
        if not is_sheduler_enable and not sheduler_duration is None:
            raise ValueError("duration can't be setted, while scheduler is equal false")
        if not is_sheduler_enable and not sheduler_delay is None:
            raise ValueError("delay can't be setted, while scheduler is equal false")
        self.sheduler_duration = sheduler_duration
        self.sheduler_delay = sheduler_delay
        BasicThreadGroup.__init__(self,
                        name=name,
                        comments=comments,
                        is_enabled=is_enabled,
                        on_sample_error=on_sample_error)

    @property
    def num_threads(self) -> int:
        return self._num_threads

    @num_threads.setter
    def num_threads(self, value):
        if not isinstance(value, int) or value < 1:
            raise TypeError(
                f'num_threads must be positive int. {type(value)} was given')
        else:
            self._num_threads = value

    @property
    def ramp_time(self) -> int:
        return self._ramp_time

    @ramp_time.setter
    def ramp_time(self, value):
        if not isinstance(value, int) or value < 0:
            raise TypeError(
                f'ramp_time must be positive int or zero. {type(value)} was given')
        self._ramp_time = value
    
    @property
    def continue_forever(self) -> bool:
        return self._continue_forever

    @continue_forever.setter
    def continue_forever(self, value: bool):
        if not isinstance(value, bool):
            raise TypeError(f'continue_forever must be bool. continue_forever {type(value)} = {value}')
        else:
            self._continue_forever = value

    @property
    def loops(self) -> int:
        return self._loops

    @loops.setter
    def loops(self, value: int):
        if not isinstance(value, int) or value < -1:
            raise TypeError(f'arg: loops should be positive int or -1. {type(value).__name__} was given')
        self._loops = value

    @property
    def is_sheduler_enable(self) -> bool:
        return self._is_sheduler_enable

    @is_sheduler_enable.setter
    def is_sheduler_enable(self, value: bool):
        if not isinstance(value, bool):
            raise TypeError(f'is_sheduler_enable must be bool. continue_forever {type(value)} = {value}')
        else:
            self._is_sheduler_enable = value
            
    @property
    def sheduler_duration(self) -> str:
        return self._sheduler_duration

    @sheduler_duration.setter
    def sheduler_duration(self, value):
        if value is None:
            self._sheduler_duration = ""
        else:
            if not isinstance(value, int) or value < 0:
                raise TypeError(
                    f'sheduler_duration must be positive int or zero. {type(value)} was given')
            self._sheduler_duration = str(value)
        
    @property
    def sheduler_delay(self) -> str:
        return self._sheduler_delay

    @sheduler_delay.setter
    def sheduler_delay(self, value):
        if value is None:
            self._sheduler_delay = ""
        else:
            if not isinstance(value, int) or value < 0:
                raise TypeError(
                    f'sheduler_delay must be positive int or zero. {type(value)} was given')
            self._sheduler_delay = str(value)
        
