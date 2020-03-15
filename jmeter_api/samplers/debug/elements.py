import logging

from jmeter_api.basics.sampler.elements import BasicSampler
from jmeter_api.basics.utils import IncludesElements, Renderable, tree_to_str


class DebugSampler(BasicSampler, Renderable):

    root_element_name = 'DebugSampler'

    def __init__(self, *,
                 display_props: bool = False,
                 display_vars: bool = True,
                 display_sys_props: bool = False,
                 name: str = 'Debug Sampler',
                 comments: str = '',
                 is_enabled: bool = True
                 ):
        """

        :type source_type: object
        """
        self.display_props = display_props
        self.display_vars = display_vars
        self.display_sys_props = display_sys_props
        BasicSampler.__init__(
            self, name=name, comments=comments, is_enabled=is_enabled)

    @property
    def display_props(self):
        return self._display_props

    @display_props.setter
    def display_props(self, value):
        if not isinstance(value, bool):
            raise TypeError(
                f'arg: display_props must be bool. {type(value).__name__} was given')
        self._display_props = str(value).lower()

    @property
    def display_vars(self):
        return self._display_vars

    @display_vars.setter
    def display_vars(self, value):
        if not isinstance(value, bool):
            raise TypeError(
                f'arg: display_vars must be bool. {type(value).__name__} was given')
        self._display_vars = str(value).lower()

    @property
    def display_sys_props(self):
        return self._display_sys_props

    @display_sys_props.setter
    def display_sys_props(self, value):
        if not isinstance(value, bool):
            raise TypeError(
                f'arg: display_sys_props must be bool. {type(value).__name__} was given')
        self._display_sys_props = str(value).lower()

    def to_xml(self) -> str:
        """
        Set all parameters in xml and convert it to the string.
        :return: xml in string format
        """
        # default name and stuff setup
        element_root, xml_tree = super()._add_basics()
        
        for element in list(element_root):
            try:
                if element.attrib['name'] == 'displayJMeterProperties':
                    element.text = self.display_props
                elif element.attrib['name'] == 'displayJMeterVariables':
                    element.text = self.display_vars
                elif element.attrib['name'] == 'displaySystemProperties':
                    element.text = self.display_sys_props
            except KeyError:
                logging.error('Unable to set xml parameters')
                
        # render inner renderable elements
        if len(self) == 1:
            content_root = xml_tree.find('hashTree')
            content_root.text = self._render_inner_elements().replace('<hashTree />', '')
        elif len(self) > 1:
            content_root = xml_tree.find('hashTree')
            content_root.text = self._render_inner_elements()
        return tree_to_str(xml_tree)
