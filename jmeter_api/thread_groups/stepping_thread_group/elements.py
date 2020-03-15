from jmeter_api.basics.thread_group.elements import BasicThreadGroup, ThreadGroupAction
from jmeter_api.basics.utils import Renderable, IncludesElements, tree_to_str


class SteppingThreadGroup(BasicThreadGroup, Renderable):

    root_element_name = 'kg.apc.jmeter.threads.SteppingThreadGroup'

    def __init__(self, *,
                 num_threads: int = 100,
                 initial_delay: int = 0,
                 start_users_count: int = 10,
                 start_users_count_burst: int = 0,
                 start_users_period: int = 30,
                 stop_users_count: int = 5,
                 stop_users_period: int = 1,
                 hold: int = 60,
                 ramp_up: int = 5,
                 on_sample_error: ThreadGroupAction = ThreadGroupAction.CONTINUE,
                 name: str = 'jp@gc - Stepping Thread Group (deprecated)',
                 comments: str = '',
                 is_enabled: bool = True):
        self.num_threads = num_threads
        self.initial_delay = initial_delay
        self.start_users_count = start_users_count
        self.start_users_count_burst = start_users_count_burst
        self.start_users_period = start_users_period
        self.stop_users_count = stop_users_count
        self.stop_users_period = stop_users_period
        self.hold = hold
        self.ramp_up = ramp_up
        BasicThreadGroup.__init__(self,
                                  on_sample_error=on_sample_error,
                                  name=name,
                                  comments=comments,
                                  is_enabled=is_enabled)

    @property
    def num_threads(self):
        return self._num_threads

    @num_threads.setter
    def num_threads(self, value: int):
        if not isinstance(value, int) or value < 0:
            raise TypeError(
                f'num_threads must be positive int. num_threads {type(value)} = {value}')
        self._num_threads = value

    @property
    def initial_delay(self):
        return self._initial_delay

    @initial_delay.setter
    def initial_delay(self, value: int):
        if not isinstance(value, int) or value < 0:
            raise TypeError(
                f'initial_delay must be positive int. initial_delay {type(value)} = {value}')
        self._initial_delay = value

    @property
    def start_users_count(self):
        return self._start_users_count

    @start_users_count.setter
    def start_users_count(self, value: int):
        if not isinstance(value, int) or value < 0:
            raise TypeError(
                f'start_users_count must be positive int. start_users_count {type(value)} = {value}')
        self._start_users_count = value

    @property
    def start_users_count_burst(self):
        return self._start_users_count_burst

    @start_users_count_burst.setter
    def start_users_count_burst(self, value: int):
        if not isinstance(value, int) or value < 0:
            raise TypeError(
                f'start_users_count_burst must be positive int. start_users_count_burst {type(value)} = {value}')
        self._start_users_count_burst = value
        
    @property
    def start_users_period(self):
        return self._start_users_period

    @start_users_period.setter
    def start_users_period(self, value: int):
        if not isinstance(value, int) or value < 0:
            raise TypeError(
                f'start_users_period must be positive int. start_users_period {type(value)} = {value}')
        self._start_users_period = value

    @property
    def stop_users_count(self):
        return self._stop_users_count

    @stop_users_count.setter
    def stop_users_count(self, value: int):
        if not isinstance(value, int) or value < 0:
            raise TypeError(
                f'stop_users_count must be positive int. stop_users_count {type(value)} = {value}')
        self._stop_users_count = value

    @property
    def stop_users_period(self):
        return self._stop_users_period

    @stop_users_period.setter
    def stop_users_period(self, value: int):
        if not isinstance(value, int) or value < 0:
            raise TypeError(
                f'stop_users_period must be positive int. stop_users_period {type(value)} = {value}')
        self._stop_users_period = value

    @property
    def hold(self):
        return self._hold

    @hold.setter
    def hold(self, value: int):
        if not isinstance(value, int) or value < 0:
            raise TypeError(
                f'hold must be positive int. hold {type(value)} = {value}')
        self._hold = value
        
    @property
    def ramp_up(self):
        return self._ramp_up

    @ramp_up.setter
    def ramp_up(self, value: int):
        if not isinstance(value, int) or value < 0:
            raise TypeError(
                f'ramp_up must be positive int. ramp_up {type(value)} = {value}')
        self._ramp_up = value
            
    def to_xml(self) -> str:
        element_root, xml_tree = super()._add_basics()

        for element in list(element_root):
            try:
                if element.attrib['name'] == 'ThreadGroup.on_sample_error':
                    element.text = self.on_sample_error.value
                elif element.attrib['name'] == 'ThreadGroup.num_threads':
                    element.text = str(self.num_threads)
                elif element.attrib['name'] == 'Threads initial delay':
                    element.text = str(self.initial_delay)
                elif element.attrib['name'] == 'Start users count':
                    element.text = str(self.start_users_count)
                elif element.attrib['name'] == 'Start users count burst':
                    element.text = str(self.start_users_count_burst)
                elif element.attrib['name'] == 'Start users period':
                    element.text = str(self.start_users_period)
                elif element.attrib['name'] == 'Stop users count':
                    element.text = str(self.stop_users_count)
                elif element.attrib['name'] == 'Stop users period':
                    element.text = str(self.stop_users_period)
                elif element.attrib['name'] == 'flighttime':
                    element.text = str(self.hold)
                elif element.attrib['name'] == 'rampUp':
                    element.text = str(self.ramp_up)
            except KeyError:
                continue
        content_root = xml_tree.find('hashTree')
        content_root.text = self._render_inner_elements()
        return tree_to_str(xml_tree)
