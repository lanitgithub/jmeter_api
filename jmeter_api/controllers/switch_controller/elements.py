from jmeter_api.basics.controller.elements import BasicController
from jmeter_api.basics.utils import Renderable, IncludesElements, tree_to_str


class SwitchController(BasicController, Renderable):

    root_element_name = 'SwitchController'
    TEMPLATE = 'switch_controller_template.xml'

    def __init__(self, *,
                 switchValue: str,
                 name: str = 'Switch Controller',
                 comments: str = '',
                 is_enabled: bool = True,):
        self.switchValue = switchValue
        BasicController.__init__(self, name=name, comments=comments, is_enabled=is_enabled)         
                       
    @property
    def switchValue(self):
        return self._switchValue

    @switchValue.setter
    def switchValue(self, value: str):
        if not isinstance(value, str):
            raise TypeError(f'switchValue must be str. switchValue {type(value)} = {value}')
        else:
            self._switchValue = value

    def to_xml(self) -> str:
        element_root, xml_tree = super()._add_basics()

        for element in list(element_root):
            try:
                if element.attrib['name'] == 'SwitchController.value':
                    element.text = str(self.switchValue)
            except KeyError:
                continue

        content_root = xml_tree.find('hashTree')
        content_root.text = self._render_inner_elements()
        return tree_to_str(xml_tree)
