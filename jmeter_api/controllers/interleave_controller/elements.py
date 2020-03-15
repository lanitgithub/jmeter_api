from jmeter_api.basics.controller.elements import BasicController
from jmeter_api.basics.utils import Renderable, IncludesElements, tree_to_str


class InterleaveController(BasicController, Renderable):

    root_element_name = 'InterleaveControl'
    TEMPLATE = 'interleave_controller_template.xml'

    def __init__(self, *,
                 ignoreSubControllers: bool = False,
                 accrossThreads: bool = False,
                 name: str = 'Interleave Controller',
                 comments: str = '',
                 is_enabled: bool = True,):
        self.ignoreSubControllers = ignoreSubControllers
        self.accrossThreads = accrossThreads
        BasicController.__init__(self, name=name, comments=comments, is_enabled=is_enabled)         
    
    @property
    def ignoreSubControllers(self):
        return self._ignoreSubControllers

    @ignoreSubControllers.setter
    def ignoreSubControllers(self, value: bool):
        if not isinstance(value, bool):
            raise TypeError(f'ignoreSubControllers must be bool. ignoreSubControllers {type(value)} = {value}')
        else:
            if value:
                self._ignoreSubControllers = 0
            else:
                self._ignoreSubControllers = 1

    @property
    def accrossThreads(self):
        return self._accrossThreads

    @accrossThreads.setter
    def accrossThreads(self, value: bool):
        if not isinstance(value, bool):
            raise TypeError(f'ignoreSubControllers must be bool. ignoreSubControllers {type(value)} = {value}')
        else:
            self._accrossThreads = str(value).lower()

    def to_xml(self) -> str:
        element_root, xml_tree = super()._add_basics()

        for element in list(element_root):
            try:
                if element.attrib['name'] == 'InterleaveControl.style':
                    element.text = str(self.ignoreSubControllers)
                elif element.attrib['name'] == 'InterleaveControl.accrossThreads':
                    element.text = str(self.accrossThreads)
            except KeyError:
                continue

        content_root = xml_tree.find('hashTree')
        content_root.text = self._render_inner_elements()
        return tree_to_str(xml_tree)
