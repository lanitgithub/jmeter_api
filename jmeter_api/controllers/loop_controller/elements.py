from jmeter_api.basics.controller.elements import BasicController
from jmeter_api.basics.utils import Renderable, IncludesElements, tree_to_str


class LoopController(BasicController, Renderable):

    root_element_name = 'LoopController'
    TEMPLATE = 'loop_controller_template.xml'

    def __init__(self, *,
                 continue_forever: bool = False,
                 loops: int = None,
                 name: str = 'Loop Controller',
                 comments: str = '',
                 is_enabled: bool = True,):
        self.continue_forever = continue_forever
        if not continue_forever:
            if loops is None:
                loops = 1
            if loops == -1:
                raise ValueError("continue_forever can't be false, while loops equal -1")
            self.loops = loops
        else:
            if loops is None:
                loops = -1
            if loops > -1:
                raise ValueError("continue_forever can't be true, while loops not equal -1")            
            self.loops = loops
        BasicController.__init__(self, name=name, comments=comments, is_enabled=is_enabled)         
    
    @property
    def continue_forever(self):
        return self._continue_forever

    @continue_forever.setter
    def continue_forever(self, value: bool):
        if not isinstance(value, bool):
            raise TypeError(f'continue_forever must be bool. continue_forever {type(value)} = {value}')
        else:
            self._continue_forever = str(value).lower()

    @property
    def loops(self):
        return self._loops

    @loops.setter
    def loops(self, value: int):
        if not isinstance(value, int) or value < -1:
            raise TypeError(f'arg: loops should be positive int or -1. {type(value).__name__} was given')
        self._loops = value

    def to_xml(self) -> str:
        element_root, xml_tree = super()._add_basics()

        for element in list(element_root):
            try:
                if element.attrib['name'] == 'LoopController.continue_forever':
                    element.text = str(self.continue_forever)
                elif element.attrib['name'] == 'LoopController.loops':
                    element.text = str(self.loops)
            except KeyError:
                continue

        content_root = xml_tree.find('hashTree')
        content_root.text = self._render_inner_elements()
        return tree_to_str(xml_tree)
