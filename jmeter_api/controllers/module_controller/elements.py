from random import random
from xml.etree.ElementTree import Element

from jmeter_api.basics.controller.elements import BasicController
from jmeter_api.basics.utils import Renderable, IncludesElements, tree_to_str


class ModuleController(BasicController, Renderable):

    root_element_name = 'ModuleController'
    TEMPLATE = 'module_controller_template.xml'

    def __init__(self, *,
                 node_path: str,
                 name: str = 'Module Controller',
                 comments: str = '',
                 is_enabled: bool = True,):
        self.node_path = node_path
        BasicController.__init__(self, name=name, comments=comments, is_enabled=is_enabled)

    def append(self, new_element):
        raise RuntimeError("ModuleController cannot append elements")
                       
    @property
    def node_path(self):
        return self._node_path

    @node_path.setter
    def node_path(self, value: str):
        if not isinstance(value, str):
            raise TypeError(f'switchValue must be str. switchValue {type(value)} = {value}')
        if len(value.split('/')) < 3:
            raise ValueError('node_path must be like TEST_PLAN_NAME/THREAD_\
                            GRUOP_OR_TEST_FRAGMENT_NAME(/CONTROLLER_NAME)+')
        else:
            self._node_path = value

    def to_xml(self) -> str:
        element_root, xml_tree = super()._add_basics()

        for element in list(element_root):
            try:
                if element.attrib['name'] == 'ModuleController.node_path':
                    names = self.node_path.split('/')
                    for name in names:
                        el = Element("stringProp", attrib={"name": str(int(random()*10000000000))})
                        el.text = str(name)
                        element.append(el)
            except KeyError:
                continue
        return tree_to_str(xml_tree)
