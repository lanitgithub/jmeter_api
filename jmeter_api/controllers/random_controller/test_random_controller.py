import xmltodict
import pytest

from jmeter_api.controllers.random_controller.elements import RandomController
from jmeter_api.basics.utils import tag_wrapper


class TestRandomController:
    class TestIgnoreSubControllers:
        def test_check(self):
            with pytest.raises(TypeError):
                RandomController(ignoreSubControllers = "True")

        def test_check2(self):
            with pytest.raises(TypeError):
                RandomController(ignoreSubControllers = 1)

        def test_positive(self):
            RandomController(ignoreSubControllers = True)           


class TestRandomControllerRender:
    def test_ignore_sub_controllers(self):
        element = RandomController(ignoreSubControllers = True)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        assert parsed_doc['test_results']['RandomController']['intProp']['#text'] == '0'
