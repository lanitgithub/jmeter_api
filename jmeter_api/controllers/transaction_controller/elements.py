from jmeter_api.basics.controller.elements import BasicController
from jmeter_api.basics.utils import Renderable, IncludesElements, tree_to_str


class TransactionController(BasicController, Renderable):

    root_element_name = 'TransactionController'
    TEMPLATE = 'transaction_controller_template.xml'

    def __init__(self, *,
                 includeTimers: bool = False,
                 parent: bool = False,
                 name: str = 'Transaction Controller',
                 comments: str = '',
                 is_enabled: bool = True,):
        self.includeTimers = includeTimers
        self.parent = parent
        BasicController.__init__(self, name=name, comments=comments, is_enabled=is_enabled)         
    
    @property
    def includeTimers(self):
        return self._includeTimers

    @includeTimers.setter
    def includeTimers(self, value: bool):
        if not isinstance(value, bool):
            raise TypeError(f'includeTimers must be bool. includeTimers {type(value)} = {value}')
        else:
            self._includeTimers = str(value).lower()
           
    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, value: bool):
        if not isinstance(value, bool):
            raise TypeError(f'parent must be bool. parent {type(value)} = {value}')
        else:
            self._parent = str(value).lower()
  
    def to_xml(self) -> str:
        element_root, xml_tree = super()._add_basics()

        for element in list(element_root):
            try:
                if element.attrib['name'] == 'TransactionController.includeTimers':
                    element.text = str(self.includeTimers)
                elif element.attrib['name'] == 'TransactionController.parent':
                    element.text = str(self.parent)
            except KeyError:
                continue

        content_root = xml_tree.find('hashTree')
        content_root.text = self._render_inner_elements()
        return tree_to_str(xml_tree)
