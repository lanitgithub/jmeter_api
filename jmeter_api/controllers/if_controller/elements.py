from jmeter_api.basics.controller.elements import BasicController
from jmeter_api.basics.utils import Renderable, IncludesElements, tree_to_str


class IfController(BasicController, Renderable):

    root_element_name = 'IfController'
    TEMPLATE = 'if_controller_template.xml'

    def __init__(self, *,
                 condition: str,
                 evaluateAll: bool = False,
                 useExpression: bool = True,
                 name: str = 'If Controller',
                 comments: str = '',
                 is_enabled: bool = True,):
        self.condition = condition
        self.evaluateAll = evaluateAll
        self.useExpression = useExpression
        BasicController.__init__(self, name=name, comments=comments, is_enabled=is_enabled)         
    
    @property
    def evaluateAll(self):
        return self._evaluateAll

    @evaluateAll.setter
    def evaluateAll(self, value: bool):
        if not isinstance(value, bool):
            raise TypeError(f'evaluateAll must be bool. evaluateAll {type(value)} = {value}')
        else:
            self._evaluateAll = str(value).lower()
           
    @property
    def useExpression(self):
        return self._useExpression

    @useExpression.setter
    def useExpression(self, value: bool):
        if not isinstance(value, bool):
            raise TypeError(f'useExpression must be bool. useExpression {type(value)} = {value}')
        else:
            self._useExpression = str(value).lower()
                       
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
                if element.attrib['name'] == 'IfController.condition':
                    element.text = str(self.condition)
                elif element.attrib['name'] == 'IfController.evaluateAll':
                    element.text = str(self.evaluateAll)
                elif element.attrib['name'] == 'IfController.useExpression':
                    element.text = str(self.useExpression)
            except KeyError:
                continue

        content_root = xml_tree.find('hashTree')
        content_root.text = self._render_inner_elements()
        return tree_to_str(xml_tree)
