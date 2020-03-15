import logging

from enum import Enum

from jmeter_api.basics.sampler.elements import BasicSampler
from jmeter_api.basics.utils import IncludesElements, Renderable, tree_to_str


class ActionOnThread(Enum):
    STOP = '0'
    PAUSE = '1'
    STOP_NOW = '2'
    START_NEXT_THREAD_GROUP = '3'
    BREAK_CURRENT_LOOP = '5'
    GO_TO_NEXT_ITER = '4'


class Target(Enum):
    CURRENT_THREAD = '0'
    ALL_THREAD = '2'


class FlowControlAction(BasicSampler, Renderable):

    root_element_name = 'TestAction'

    def __init__(self, *,
                 name: str = 'Flow Control Action',
                 logical_action_on_thread: ActionOnThread = ActionOnThread.PAUSE,
                 pause: int = 0,
                 target: Target = Target.CURRENT_THREAD,
                 comments: str = '',
                 is_enabled: bool = True
                 ):
        BasicSampler.__init__(self, name=name, comments=comments, is_enabled=is_enabled)
        self.logical_action_on_thread = logical_action_on_thread
        self.pause = pause
        self.target = target

    @property
    def logical_action_on_thread(self):
        return self._logical_action_on_thread

    @logical_action_on_thread.setter
    def logical_action_on_thread(self, value):
        if not isinstance(value, ActionOnThread):
            raise TypeError(
                f'arg: logical_action_on_thread should be ActionOnThread. {type(value).__name__} was given')
        self._logical_action_on_thread = value

    @property
    def pause(self):
        return self._pause

    @pause.setter
    def pause(self, value):
        if not isinstance(value, int):
            raise TypeError(
                f'arg: pause should be int. {type(value).__name__} was given')
        if value < 0:
            raise ValueError('arg: pause should be positive')
        self._pause = value

    @property
    def target(self):
        return self._target

    @target.setter
    def target(self, value):
        if not isinstance(value, Target):
            raise TypeError(
                f'arg: target should be Target. {type(value).__name__} was given')
        self._target = value

    def to_xml(self) -> str:
        """
        Set all parameters in xml and convert it to the string.
        :return: xml in string format
        """
        # default name and stuff setup
        element_root, xml_tree = super()._add_basics()
        for element in list(element_root):
            try:
                if element.attrib['name'] == 'ActionProcessor.action':
                    element.text = self.logical_action_on_thread.value
                elif element.attrib['name'] == 'ActionProcessor.target' and\
                        (self.logical_action_on_thread is ActionOnThread.STOP or
                         self.logical_action_on_thread is ActionOnThread.STOP_NOW):
                    element.text = self.target.value
                elif element.attrib['name'] == 'ActionProcessor.duration' and\
                        self.logical_action_on_thread is ActionOnThread.PAUSE:
                    element.text = str(self.pause)
            except Exception:
                logging.error(
                    f'Unable to render xml from {type(self).__class__}')
        return tree_to_str(xml_tree, hashtree=True)
