import xmltodict
import pytest

from jmeter_api.controllers.switch_controller.elements import SwitchController
from jmeter_api.basics.utils import tag_wrapper


class TestSwitchController:
    class TestSwitch:
        def test_check(self):
            with pytest.raises(TypeError):
                SwitchController(switchValue=123)

        def test_positive(self):
            SwitchController(switchValue="${value}")


class TestSwitchControllerRender:
    def test_condition(self):
        element = SwitchController(switchValue="some switch")
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        assert parsed_doc['test_results']['SwitchController']['stringProp']['#text'] == 'some switch'
