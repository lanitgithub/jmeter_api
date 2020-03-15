from abc import ABC
from typing import Union

from jmeter_api.basics.element.elements import BasicElement
from jmeter_api.basics.pre_processor.elements import BasicPreProcessor
from jmeter_api.basics.post_processor.elements import BasicPostProcessor
from jmeter_api.basics.controller.elements import BasicController
from jmeter_api.basics.config.elements import BasicConfig
from jmeter_api.basics.sampler.elements import BasicSampler
from jmeter_api.basics.assertion.elements import BasicAssertion
from jmeter_api.basics.listener.elements import BasicListener
from jmeter_api.basics.sampler.elements import BasicSampler
from jmeter_api.basics.timer.elements import BasicTimer
from jmeter_api.basics.utils import IncludesElements


class BasicTestFragment(BasicElement, IncludesElements, ABC):
    def __init__(self,
                 name: str = 'BasicTestFragment',
                 comments: str = '',
                 is_enabled: bool = True):
        IncludesElements.__init__(self)
        super().__init__(name=name,
                         comments=comments,
                         is_enabled=is_enabled)

    def append(self, new_element: Union[BasicSampler, BasicTimer, BasicConfig, BasicController,\
                                        BasicPreProcessor, BasicPostProcessor, BasicAssertion, BasicListener]):
        if not isinstance(new_element, (BasicSampler, BasicTimer, BasicConfig, BasicController,\
                                        BasicPreProcessor, BasicPostProcessor, BasicAssertion, BasicListener)):
            raise TypeError(
                f'new_element must be BasicSampler, BasicTimer, BasicConfig, BasicPreProcessor,\
                BasicPostProcessor, BasicAssertion, BasicListener or BasicController. {type(new_element)} was given')
        self._elements.append(new_element)
        return self


print.__call__()
