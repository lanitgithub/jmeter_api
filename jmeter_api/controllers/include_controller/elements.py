import os

from jmeter_api.basics.controller.elements import BasicController
from jmeter_api.basics.utils import Renderable, IncludesElements, tree_to_str


class IncludeController(BasicController, Renderable):

    root_element_name = 'IncludeController'
    TEMPLATE = 'include_controller_template.xml'

    def __init__(self, *,
                 includePath: str,
                 name: str = 'Include Controller',
                 comments: str = '',
                 is_enabled: bool = True,):
        self.includePath = includePath
        BasicController.__init__(self, name=name, comments=comments, is_enabled=is_enabled)         

    def append(self, new_element):
        raise RuntimeError("IncludeController cannot append elements")
                       
    @property
    def includePath(self):
        return self._includePath

    @includePath.setter
    def includePath(self, value: str):
        if not isinstance(value, str):
            raise TypeError(f'switchValue must be str. switchValue {type(value)} = {value}')
        if not os.path.isfile(value):
            raise OSError('File ' + value + ' not found')
        filename, file_extension = os.path.splitext(value)
        if not file_extension == '.jmx':
            raise ValueError('File must be a jmx file')
        else:
            self._includePath = value

    def to_xml(self) -> str:
        element_root, xml_tree = super()._add_basics()

        for element in list(element_root):
            try:
                if element.attrib['name'] == 'IncludeController.includepath':
                    element.text = str(self.includePath)
            except KeyError:
                continue
        return tree_to_str(xml_tree)
