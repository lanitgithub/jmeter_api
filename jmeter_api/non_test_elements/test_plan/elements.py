from typing import Union
from xml.etree.ElementTree import tostring, Element
from xml.sax.saxutils import unescape

from jmeter_api.basics.non_test_elements.elements import NonTestElements
from jmeter_api.basics.pre_processor.elements import BasicPreProcessor
from jmeter_api.basics.post_processor.elements import BasicPostProcessor
from jmeter_api.basics.config.elements import BasicConfig
from jmeter_api.basics.assertion.elements import BasicAssertion
from jmeter_api.basics.listener.elements import BasicListener
from jmeter_api.basics.timer.elements import BasicTimer
from jmeter_api.basics.thread_group.elements import BasicThreadGroup
from jmeter_api.basics.test_fragment.elements import BasicTestFragment
from jmeter_api.basics.utils import Renderable, IncludesElements, test_plan_wrapper


class TestPlan(NonTestElements, IncludesElements, Renderable):
    root_element_name = 'TestPlan'

    def __init__(self,
                 variables: dict = {},
                 functional_mode: bool = False,
                 teardown_on_shutdown: bool = True,
                 serialize_threadgroups: bool = False,
                 name='BasicElement',
                 comments='',
                 is_enabled=True):
        self.variables = variables
        self.functional_mode = functional_mode
        self.teardown_on_shutdown = teardown_on_shutdown
        self.serialize_threadgroups = serialize_threadgroups
        IncludesElements.__init__(self)
        NonTestElements.__init__(self, name=name, comments=comments, is_enabled=is_enabled)
        
    #Can include NonTestElemnts, with the exception of TestPlan
    def append(self, new_element: Union[BasicTimer, BasicConfig, BasicPreProcessor, BasicPostProcessor, BasicThreadGroup,\
                                        BasicAssertion, BasicListener, BasicTestFragment, "NonTestElemnts"]):
        if not isinstance(new_element, (BasicTimer, BasicConfig, BasicPreProcessor, BasicPostProcessor, BasicThreadGroup,\
                                        BasicAssertion, BasicListener, BasicTestFragment)):
            raise TypeError(
                f'new_element must be BasicTimer, BasicConfig, BasicPreProcessor, BasicPostProcessor, BasicAssertion,\
                BasicListener, BasicThreadGroup, BasicTestFragment or NonTestElemnts (with the exception of TestPlan).\
                {type(new_element)} was given')
        self._elements.append(new_element)
        return self

    @property
    def variables(self):
        return self._variables

    @variables.setter
    def variables(self, value: dict):
        if not isinstance(value, dict):
            raise TypeError(
                f'variables must be bool. variables {type(value)} = {value}')
        else:
            self._variables = value
            
    @property
    def functional_mode(self):
        return self._functional_mode

    @functional_mode.setter
    def functional_mode(self, value: bool):
        if not isinstance(value, bool):
            raise TypeError(
                f'functional_mode must be bool. functional_mode {type(value)} = {value}')
        else:
            self._functional_mode = value

    @property
    def teardown_on_shutdown(self):
        return self._teardown_on_shutdown

    @teardown_on_shutdown.setter
    def teardown_on_shutdown(self, value: bool):
        if not isinstance(value, bool):
            raise TypeError(
                f'teardown_on_shutdown must be bool. teardown_on_shutdown {type(value)} = {value}')
        else:
            self._teardown_on_shutdown = value

    @property
    def serialize_threadgroups(self):
        return self._serialize_threadgroups

    @serialize_threadgroups.setter
    def serialize_threadgroups(self, value: bool):
        if not isinstance(value, bool):
            raise TypeError(
                f'serialize_threadgroups must be bool. serialize_threadgroups {type(value)} = {value}')
        else:
            self._serialize_threadgroups = value

    def to_xml(self):
        element_root, xml_tree = super()._add_basics()

        element_root.set('enabled', str(self.is_enabled).lower())
        element_root.set('testname', self.name)

        for element in list(element_root):
            try:
                if element.attrib['name'] == 'TestPlan.comments':
                    element.text = self.comments
                elif element.attrib['name'] == 'TestPlan.functional_mode':
                    element.text = str(self.functional_mode).lower()
                elif element.attrib['name'] == 'TestPlan.tearDown_on_shutdown':
                    element.text = str(self.teardown_on_shutdown).lower()
                elif element.attrib['name'] == 'TestPlan.serialize_threadgroups':
                    element.text = str(self.serialize_threadgroups).lower()
                elif element.attrib['name'] == 'TestPlan.user_defined_variables':
                    for arg_name in self.variables:
                        el_prop = Element("elementProp", attrib={"name": arg_name, "elementType": "Argument"})
                        sub_el = Element("stringProp", attrib={"name": "Argument.name"})
                        sub_el.text = arg_name
                        el_prop.append(sub_el)
                        sub_el = Element("stringProp", attrib={"name": "Argument.value"})
                        sub_el.text = self.variables[arg_name]
                        el_prop.append(sub_el)
                        sub_el = Element("stringProp", attrib={"name": "Argument.metadata"})
                        sub_el.text = "="
                        el_prop.append(sub_el)
                        element[0].append(el_prop)
            except KeyError:
                continue

        content_root = xml_tree.find('hashTree')
        content_root.text = self._render_inner_elements()
        xml_data = ''
        for element in list(xml_tree):
            xml_data += tostring(element).decode('utf8')
        return test_plan_wrapper(unescape(xml_data))
