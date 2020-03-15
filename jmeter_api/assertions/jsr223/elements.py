import logging

from jmeter_api.basics.jsr223 import JSR223, ScriptLanguage
from jmeter_api.basics.assertion.elements import BasicAssertion
from jmeter_api.basics.utils import Renderable, tree_to_str


class JSR223Assertion(BasicAssertion, JSR223, Renderable):

    root_element_name = 'JSR223Assertion'

    def __init__(self, *,
                 cache_key: bool = True,
                 filename: str = '',
                 parameters: str = '',
                 script: str = '',
                 script_language: ScriptLanguage = ScriptLanguage.GROOVY,
                 name: str = 'JSR223 Assertion',
                 comments: str = '',
                 is_enabled: bool = True
                 ):
        """

        :type source_type: object
        """
        JSR223.__init__(self,
            cache_key=cache_key,
            filename=filename,
            parameters=parameters,
            script=script,
            script_language=script_language)
        BasicAssertion.__init__(
            self, name=name, comments=comments, is_enabled=is_enabled)

    def to_xml(self) -> str:
        element_root, xml_tree = super()._add_basics()
        for element in list(element_root):
            try:
                if element.attrib['name'] == 'cacheKey':
                    element.text = self.cache_key
                elif element.attrib['name'] == 'filename':
                    element.text = self.filename
                elif element.attrib['name'] == 'parameters':
                    element.text = self.parameters
                elif element.attrib['name'] == 'script':
                    element.text = self.script
                elif element.attrib['name'] == 'scriptLanguage':
                    element.text = self.script_language.value
            except KeyError:
                logging.error('Unable to set xml parameters')

        return tree_to_str(xml_tree)
