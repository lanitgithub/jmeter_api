import logging
import os

from jmeter_api.basics.sampler.elements import BasicSampler
from jmeter_api.basics.utils import IncludesElements, Renderable, tree_to_str


class BeanShell(BasicSampler, Renderable):

    root_element_name = 'BeanShellSampler'

    def __init__(self, *,
                 resetInterpreter: bool = False,
                 filename: str = '',
                 parameters: str = '',
                 query: str = '',
                 name: str = 'BeanShell Sampler',
                 comments: str = '',
                 is_enabled: bool = True
                 ):
        """

        :type source_type: object
        """
        self.resetInterpreter = resetInterpreter
        self.filename = filename
        self.parameters = parameters
        self.query = query
        BasicSampler.__init__(
            self, name=name, comments=comments, is_enabled=is_enabled)

    @property
    def filename(self):
        return self._filename

    @filename.setter
    def filename(self, value):
        if not isinstance(value, str):
            raise TypeError(
                f'arg: filename should be str. {type(value).__name__} was given')
        if not value == '':
            if not os.path.isfile(value):
                raise OSError('File ' + value + ' not found')
            filename, file_extension = os.path.splitext(value)
            if not file_extension == '.bsh':
                raise ValueError('File must have bsh extension')
        self._filename = value

    @property
    def parameters(self):
        return self._parameters

    @parameters.setter
    def parameters(self, value):
        if not isinstance(value, str):
            raise TypeError(
                f'arg: parameters should be str. {type(value).__name__} was given')
        self._parameters = value

    @property
    def query(self):
        return self._query

    @query.setter
    def query(self, value):
        if not isinstance(value, str):
            raise TypeError(
                f'arg: query should be str. {type(value).__name__} was given')
        self._query = value

    @property
    def resetInterpreter(self):
        return self._resetInterpreter

    @resetInterpreter.setter
    def resetInterpreter(self, value):
        if not isinstance(value, bool):
            raise TypeError(
                f'arg: resetInterpreter should be bool. {type(value).__name__} was given')
        self._resetInterpreter = str(value).lower()

    def to_xml(self) -> str:
        """
        Set all parameters in xml and convert it to the string.
        :return: xml in string format
        """
        # default name and stuff setup
        element_root, xml_tree = super()._add_basics()
        for element in list(element_root):
            try:
                if element.attrib['name'] == 'BeanShellSampler.resetInterpreter':
                    element.text = self.resetInterpreter
                elif element.attrib['name'] == 'BeanShellSampler.filename':
                    element.text = self.filename
                elif element.attrib['name'] == 'BeanShellSampler.parameters':
                    element.text = self.parameters
                elif element.attrib['name'] == 'BeanShellSampler.query':
                    element.text = self.query
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
