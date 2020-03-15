import xmltodict
import pytest

from jmeter_api.controllers.loop_controller.elements import LoopController
from jmeter_api.basics.utils import tag_wrapper


class TestLoopController:
    class TestContinueForever:
        def test_check(self):
            with pytest.raises(TypeError):
                LoopController(continue_forever="True")

        def test_check2(self):
            with pytest.raises(TypeError):
                LoopController(continue_forever="123")

        def test_positive(self):
            LoopController(continue_forever=True)

    class TestConditions:
        def test_check(self):
            with pytest.raises(ValueError):
                LoopController(continue_forever=True, loops=1)

        def test_check2(self):
            with pytest.raises(ValueError):
                LoopController(loops=-1)

    class TestLoops:
        def test_check(self):
            with pytest.raises(TypeError):
                LoopController(loops="1")

        def test_check2(self):
            with pytest.raises(TypeError):
                LoopController(loops="a")

        def test_positive(self):
            LoopController(loops=23)

        def test_zero(self):
            LoopController(loops=0)

        def test_negative(self):
            with pytest.raises(TypeError):
                LoopController(loops=-4)


class TestLoopControllerRender:
    def test_loops(self):
        element = LoopController(loops=55)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        assert parsed_doc['test_results']['LoopController']['stringProp']['#text'] == '55'
