import xmltodict
import pytest

from jmeter_api.timers.constant_timer.elements import ConstantTimer
from jmeter_api.basics.utils import tag_wrapper


class TestConstantTimerArgs:
    def test_args_type_check(self):
        # name type check
        with pytest.raises(TypeError):
            ConstantTimer(name=123)
        # comments type check
        with pytest.raises(TypeError):
            ConstantTimer(comments=123)
        # is_enabled type check
        with pytest.raises(TypeError):
            ConstantTimer(is_enabled="True")
        # delay type check (negative number input)
        with pytest.raises(TypeError):
            ConstantTimer(delay=-1)
        # delay type check (wrong data type input)
        with pytest.raises(TypeError):
            ConstantTimer(delay='123')


class TestConstantTimerRender:
    def test_testname(self):
        element = ConstantTimer(name='My timer',
                                comments='My comments',
                                delay=123,
                                is_enabled=False)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        assert parsed_doc['test_results']['ConstantTimer']['@testname'] == 'My timer'

    def test_enabled(self):
        element = ConstantTimer(name='My timer',
                                comments='My comments',
                                delay=123,
                                is_enabled=False)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        assert parsed_doc['test_results']['ConstantTimer']['@enabled'] == 'false'

    def test_stringProp(self):
        element = ConstantTimer(name='My timer',
                                comments='My comments',
                                delay=123,
                                is_enabled=False)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        assert parsed_doc['test_results']['ConstantTimer']['stringProp'][0]['#text'] == 'My comments'

    def test_stringProp1(self):
        element = ConstantTimer(name='My timer',
                                comments='My comments',
                                delay=123,
                                is_enabled=False)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        assert parsed_doc['test_results']['ConstantTimer']['stringProp'][1]['#text'] == '123'

    def test_hashtree_contain(self):
        element = ConstantTimer(name='My timer',
                                comments='My comments',
                                delay=123,
                                is_enabled=False)
        rendered_doc = element.to_xml()
        assert '<hashTree />' in rendered_doc
