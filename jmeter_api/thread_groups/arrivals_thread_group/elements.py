from jmeter_api.basics.thread_group.bzm_elements import BasicBzmThreadGroup, ThreadGroupAction, Unit
from jmeter_api.basics.utils import Renderable, IncludesElements, tree_to_str


class ArrivalsThreadGroup(BasicBzmThreadGroup, Renderable):

    root_element_name = 'com.blazemeter.jmeter.threads.arrivals.ArrivalsThreadGroup'

    def __init__(self, *,
                 target_rate: int = 0,
                 ramp_up: int = 0,
                 steps: int = 1,
                 hold: int = 0,
                 iterations: int = None,
                 concurrency_limit: int = None,
                 log_filename: str = None,
                 unit:  Unit = Unit.MINUTE,
                 on_sample_error: ThreadGroupAction = ThreadGroupAction.CONTINUE,
                 name: str = 'bzm - Arrivals Thread Group',
                 comments: str = '',
                 is_enabled: bool = True):
        self.target_rate = target_rate
        self.ramp_up = ramp_up
        self.steps = steps
        self.hold = hold
        self.iterations = iterations
        self.concurrency_limit = concurrency_limit
        BasicBzmThreadGroup.__init__(self,
                                     log_filename=log_filename,
                                     unit=unit,
                                     on_sample_error=on_sample_error,
                                     name=name,
                                     comments=comments,
                                     is_enabled=is_enabled)

    @property
    def target_rate(self) -> str:
        return self._target_rate

    @target_rate.setter
    def target_rate(self, value: int):
        if not isinstance(value, int) or value < 0:
            raise TypeError(
                f'target_rate must be positive int. target_rate {type(value)} = {value}')
        else:
            self._target_rate = str(value)
            
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

    @property
    def concurrency_limit(self) -> str:
        return self._concurrency_limit

    @concurrency_limit.setter
    def concurrency_limit(self, value: int):
        if value is None:
            self._concurrency_limit = ""
        elif not isinstance(value, int) or value < 0:
            raise TypeError(
                f'concurrency_limit must be positive int. concurrency_limit {type(value)} = {value}')
        else:
            self._concurrency_limit = str(value)
            
    def to_xml(self) -> str:
        element_root, xml_tree = super()._add_basics()

        for element in list(element_root):
            try:
                if element.attrib['name'] == 'ThreadGroup.on_sample_error':
                    element.text = self.on_sample_error.value
                elif element.attrib['name'] == 'TargetLevel':
                    element.text = self.target_rate
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
                elif element.attrib['name'] == 'ConcurrencyLimit':
                    element.text = self.concurrency_limit
            except KeyError:
                continue
        content_root = xml_tree.find('hashTree')
        content_root.text = self._render_inner_elements()
        return tree_to_str(xml_tree)
