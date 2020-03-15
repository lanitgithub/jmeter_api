import xmltodict
import pytest

from jmeter_api.controllers.if_controller.elements import IfController
from jmeter_api.basics.utils import tag_wrapper


class TestIfController:
    class TestCondition:
        def test_check(self):
            with pytest.raises(TypeError):
                IfController(condition=True)

        def test_check2(self):
            with pytest.raises(TypeError):
                IfController(condition=123)

        def test_positive(self):
            IfController(condition="True")

    class TestEvaluateAll:
        def test_check(self):
            with pytest.raises(TypeError):
                IfController(condition="True", evaluateAll="True")

        def test_check2(self):
            with pytest.raises(TypeError):
                IfController(condition="True", evaluateAll=1)

        def test_positive(self):
            IfController(condition="True", evaluateAll=True)

    class TestUseExpression:
        def test_check(self):
            with pytest.raises(TypeError):
                IfController(condition="True", useExpression="False")

        def test_check2(self):
            with pytest.raises(TypeError):
                IfController(condition="True", useExpression=0)

        def test_positive(self):
            IfController(condition="True", useExpression=False)


class TestIfControllerRender:
    def test_condition(self):
        element = IfController(condition="some expression")
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        assert parsed_doc['test_results']['IfController']['stringProp']['#text'] == 'some expression'
