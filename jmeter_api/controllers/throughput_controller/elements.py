from enum import Enum

from jmeter_api.basics.controller.elements import BasicController
from jmeter_api.basics.utils import Renderable, IncludesElements, tree_to_str


class ThroughputMode(Enum):
    TOTAL = 'TotalExecution'
    PERCENT = 'PercentExecution'
    

class ThroughputController(BasicController, Renderable):

    root_element_name = 'ThroughputController'
    TEMPLATE = 'throughput_controller_template.xml'

    def __init__(self, *,
                 perThread: bool = False,
                 throughput: float = 1,
                 throughputMode: ThroughputMode = ThroughputMode.TOTAL,
                 name: str = 'Throughput Controller',
                 comments: str = '',
                 is_enabled: bool = True,):
        self.throughputMode = throughputMode
        self.perThread = perThread
        self.throughput = throughput
        BasicController.__init__(self, name=name, comments=comments, is_enabled=is_enabled)         
    
    @property
    def perThread(self):
        return self._perThread

    @perThread.setter
    def perThread(self, value: bool):
        if not isinstance(value, bool):
            raise TypeError(f'perThread must be bool. perThread {type(value)} = {value}')
        else:
            self._perThread = str(value).lower()
            
    @property
    def throughputMode(self):
        return self._throughputMode

    @throughputMode.setter
    def throughputMode(self, value: ThroughputMode):
        if not isinstance(value, ThroughputMode):
            raise TypeError(f'throughputMode should be ThroughputMode. {type(value).__name__} was given')
        self._throughputMode = value
        
    @property
    def throughput(self):
        if self.throughputMode == ThroughputMode.TOTAL:
            return self._throughputTotal
        else:
            return self._throughputPercent

    @throughput.setter
    def throughput(self, value):
        if self.throughputMode == ThroughputMode.TOTAL:
            if not isinstance(value, int):
                raise TypeError(f'throughput for ThroughputMode.TOTAL should be int. {type(value).__name__} was given')
            if value < 0:
                raise ValueError(f'throughput for ThroughputMode.TOTAL should be positive.')
            self._throughputTotal = int(value)
        else:
            if not isinstance(value, (float, int)):
                raise TypeError(f'throughput for ThroughputMode.\
                PERCENT should be float. {type(value).__name__} was given')
            if value < 0 or value > 100:
                raise ValueError(f'throughput for ThroughputMode.PERCENT should be positive and less then 100.')
            self._throughputPercent = float(value)

    def to_xml(self) -> str:
        element_root, xml_tree = super()._add_basics()

        for element in list(element_root):
            try:
                if element.tag == 'FloatProperty':
                    for el in element:
                        if el.tag == 'value':
                            if self.throughputMode == ThroughputMode.PERCENT:
                                el.text = str(self.throughput)
                            else:
                                el.text = str(float(1))
                elif element.attrib['name'] == 'ThroughputController.style':
                    if self.throughputMode == ThroughputMode.TOTAL:
                        element.text = "0"
                    else:
                        element.text = "1"
                elif element.attrib['name'] == 'ThroughputController.perThread':
                    element.text = str(self.perThread)
                elif element.attrib['name'] == 'ThroughputController.maxThroughput':
                    if self.throughputMode == ThroughputMode.TOTAL:
                        element.text = str(self.throughput)
                    else:
                        element.text = "1"
            except KeyError:
                continue

        content_root = xml_tree.find('hashTree')
        content_root.text = self._render_inner_elements()
        return tree_to_str(xml_tree)
