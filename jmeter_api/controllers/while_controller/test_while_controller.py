import xmltodict
import pytest

from jmeter_api.controllers.while_controller.elements import WhileController
from jmeter_api.basics.utils import tag_wrapper


class TestWhileController:
    class TestCondition:
        def test_check(self):
            with pytest.raises(TypeError):
                WhileController(condition=True)

        def test_check2(self):
            with pytest.raises(TypeError):
                WhileController(condition=123)

        def test_positive(self):
            WhileController(condition="True")


class TestWhileControllerRender:
    def test_condition(self):
        element = WhileController(condition="some condition")
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        assert parsed_doc['test_results']['WhileController']['stringProp']['#text'] == 'some condition'
