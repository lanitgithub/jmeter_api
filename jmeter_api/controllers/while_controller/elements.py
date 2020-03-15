from jmeter_api.basics.controller.elements import BasicController
from jmeter_api.basics.utils import Renderable, IncludesElements, tree_to_str


class WhileController(BasicController, Renderable):

    root_element_name = 'WhileController'
    TEMPLATE = 'while_controller_template.xml'

    def __init__(self, *,
                 condition: str,
                 name: str = 'While Controller',
                 comments: str = '',
                 is_enabled: bool = True,):
        self.condition = condition
        BasicController.__init__(self, name=name, comments=comments, is_enabled=is_enabled)         
                        
    @property
    def condition(self):
        return self._condition

    @condition.setter
    def condition(self, value: str):
        if not isinstance(value, str):
            raise TypeError(f'condition must be str. condition {type(value)} = {value}')
        else:
            self._condition = value

    def to_xml(self) -> str:
        element_root, xml_tree = super()._add_basics()

        for element in list(element_root):
            try:
                if element.attrib['name'] == 'WhileController.condition':
                    element.text = str(self.condition)
            except KeyError:
                continue

        content_root = xml_tree.find('hashTree')
        content_root.text = self._render_inner_elements()
        return tree_to_str(xml_tree)
