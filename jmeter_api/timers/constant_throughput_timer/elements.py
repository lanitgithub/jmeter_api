from typing import Union
from enum import Enum

from jmeter_api.basics.timer.elements import BasicTimer
from jmeter_api.basics.utils import Renderable, tree_to_str


class BasedOn(Enum):
    THIS_THREAD_ONLY = '0'
    ALL_ACTIVE_THREADS = '1'
    ALL_ACTIVE_THREADS_IN_CURRENT_THREAD = '2'
    ALL_ACTIVE_SHARED_THREADS = '3'
    ALL_ACTIVE_SHARED_THREADS_IN_CURRENT_THREAD = '4'


class ConstantThroughputTimer(BasicTimer, Renderable):
    """
    Constant throughput timer class.
    """
    root_element_name = 'ConstantThroughputTimer'

    def __init__(self, *,
                 name: str = 'Constant Throughput Timer',
                 targ_throughput: float = 0,
                 based_on: BasedOn = BasedOn.THIS_THREAD_ONLY,
                 comments='',
                 is_enabled: bool = True):
        super().__init__(name=name, comments=comments, is_enabled=is_enabled)
        self.targ_throughput = targ_throughput
        self.based_on = based_on

    @property
    def targ_throughput(self):
        return self._targ_throughput

    @targ_throughput.setter
    def targ_throughput(self, value: Union[float, int]):
        if not isinstance(value, float) and not isinstance(value, int) or value < 0:
            raise TypeError(f'arg: targ_throughput should be positive int or float. {type(value).__name__} was given')
        self._targ_throughput = value

    @property
    def based_on(self):
        return self._based_on

    @based_on.setter
    def based_on(self, value: BasedOn):
        if not isinstance(value, BasedOn):
            raise TypeError(
                f'arg: based_on should be BasedOn. {type(value).__name__} was given')
        else:
            self._based_on = value

    def __repr__(self):
        return f'Constant throughput timer: {self._name}, throughput: {self.targ_throughput}'

    def to_xml(self) -> str:
        """
        Set all parameters in xml and convert it to the string.
        :return: xml in string format
        """
        # default name and stuff setup
        element_root, xml_tree = super()._add_basics()

        int_prop = element_root.find('intProp')
        int_prop.text = self.based_on.value

        double_prop = element_root.find('doubleProp')
        double_prop_value = double_prop.find('value')
        double_prop_value.text = str(self.targ_throughput)

        return tree_to_str(xml_tree)
