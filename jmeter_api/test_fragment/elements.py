from jmeter_api.basics.test_fragment.elements import BasicTestFragment
from jmeter_api.basics.utils import Renderable, IncludesElements, tree_to_str


class TestFragment(BasicTestFragment, Renderable):

    root_element_name = 'TestFragmentController'
    TEMPLATE = 'test_fragment_template.xml'

    def __init__(self, *,
                 name: str = 'Test Fragment',
                 comments: str = '',
                 is_enabled: bool = False,):
        BasicTestFragment.__init__(self, name=name, comments=comments, is_enabled=is_enabled)         

    def to_xml(self) -> str:
        element_root, xml_tree = super()._add_basics()
        content_root = xml_tree.find('hashTree')
        content_root.text = self._render_inner_elements()
        return tree_to_str(xml_tree)
