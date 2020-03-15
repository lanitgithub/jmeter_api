from jmeter_api.basics.thread_group.bzm_elements import BasicBzmThreadGroup, ThreadGroupAction, Unit
from jmeter_api.basics.utils import Renderable, IncludesElements, tree_to_str


class ConcurrencyThreadGroup(BasicBzmThreadGroup, Renderable):

    root_element_name = 'com.blazemeter.jmeter.threads.concurrency.ConcurrencyThreadGroup'

    def __init__(self, *,
                 target_concurrency: int = 0,
                 ramp_up: int = 0,
                 steps: int = 1,
                 hold: int = 0,
                 iterations: int = None,
                 log_filename: str = None,
                 unit:  Unit = Unit.MINUTE,
                 on_sample_error: ThreadGroupAction = ThreadGroupAction.CONTINUE,
                 name: str = 'bzm - Concurrency Thread Group',
                 comments: str = '',
                 is_enabled: bool = True):
        self.target_concurrency = target_concurrency
        self.ramp_up = ramp_up
        self.steps = steps
        self.hold = hold
        self.iterations = iterations
        BasicBzmThreadGroup.__init__(self,
                                     log_filename=log_filename,
                                     unit=unit,
                                     on_sample_error=on_sample_error,
                                     name=name,
                                     comments=comments,
                                     is_enabled=is_enabled)

    @property
    def target_concurrency(self) -> str:
        return self._target_concurrency

    @target_concurrency.setter
    def target_concurrency(self, value: int):
        if not isinstance(value, int) or value < 0:
            raise TypeError(
                f'target_concurrency must be positive int. target_concurrency {type(value)} = {value}')
        else:
            self._target_concurrency = str(value)
            
    @property
    def ramp_up(self) -> str:
        return self._ramp_up

    @ramp_up.setter
    def ramp_up(self, value: int):
        if not isinstance(value, int) or value < 0:
            raise TypeError(
                f'ramp_up must be positive int. ramp_up {type(value)} = {value}')
        else:
            self._ramp_up = str(value)
            
    @property
    def steps(self) -> str:
        return self._steps

    @steps.setter
    def steps(self, value: int):
        if not isinstance(value, int) or value < 0:
            raise TypeError(
                f'steps must be positive int. steps {type(value)} = {value}')
        else:
            self._steps = str(value)
            
    @property
    def hold(self) -> str:
        return self._hold

    @hold.setter
    def hold(self, value: int):
        if not isinstance(value, int) or value < 0:
            raise TypeError(
                f'hold must be positive int. hold {type(value)} = {value}')
        else:
            self._hold = str(value)

    @property
    def iterations(self) -> str:
        return self._iterations

    @iterations.setter
    def iterations(self, value: int):
        if value is None:
            self._iterations = ""
        elif not isinstance(value, int) or value < 0:
            raise TypeError(
                f'iterations must be positive int. iterations {type(value)} = {value}')
        else:
            self._iterations = str(value)
            
    def to_xml(self) -> str:
        element_root, xml_tree = super()._add_basics()

        for element in list(element_root):
            try:
                if element.attrib['name'] == 'ThreadGroup.on_sample_error':
                    element.text = self.on_sample_error.value
                elif element.attrib['name'] == 'TargetLevel':
                    element.text = self.target_concurrency
                elif element.attrib['name'] == 'RampUp':
                    element.text = self.ramp_up
                elif element.attrib['name'] == 'Steps':
                    element.text = self.steps
                elif element.attrib['name'] == 'Hold':
                    element.text = self.hold
                elif element.attrib['name'] == 'LogFilename':
                    element.text = self.log_filename
                elif element.attrib['name'] == 'Unit':
                    element.text = self.unit.value
                elif element.attrib['name'] == 'Iterations':
                    element.text = self.iterations
            except KeyError:
                continue
        content_root = xml_tree.find('hashTree')
        content_root.text = self._render_inner_elements()
        return tree_to_str(xml_tree)
