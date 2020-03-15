import xmltodict
import pytest

from jmeter_api.timers.uniform_random_timer.elements import UniformRandTimer
from jmeter_api.basics.utils import tag_wrapper


class TestUniformRandTimer:
    def test_args_type_check(self):
        # name type check
        with pytest.raises(TypeError):
            UniformRandTimer(name=123)
        # comments type check
        with pytest.raises(TypeError):
            UniformRandTimer(comments=123)
        # is_enabled type check
        with pytest.raises(TypeError, ):
            UniformRandTimer(is_enabled="True")
        # offset_delay type check (negative number input)
        with pytest.raises(TypeError):
            UniformRandTimer(offset_delay=-1)
        # offset_delay type check (wrong data type input)
        with pytest.raises(TypeError):
            UniformRandTimer(offset_delay='123')
        # rand_delay type check (negative number input)
        with pytest.raises(TypeError):
            UniformRandTimer(rand_delay=-1)
        # rand_delay type check (wrong data type input)
        with pytest.raises(TypeError):
            UniformRandTimer(rand_delay='123')


class TestUniformRandTimerXML:
    def test_render_testname(self) -> str:
        element = UniformRandTimer(name='My timer',
                                   comments='My comments',
                                   offset_delay=123,
                                   rand_delay=321,
                                   is_enabled=False)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        assert parsed_doc['test_results']['UniformRandomTimer']['@testname'] == 'My timer'

    def test_render_enabled(self) -> str:
        element = UniformRandTimer(name='My timer',
                                   comments='My comments',
                                   offset_delay=123,
                                   rand_delay=321,
                                   is_enabled=False)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        assert parsed_doc['test_results']['UniformRandomTimer']['@enabled'] == 'false'

    def test_render_stringProp(self) -> str:
        element = UniformRandTimer(name='My timer',
                                   comments='My comments',
                                   offset_delay=123,
                                   rand_delay=321,
                                   is_enabled=False)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        assert parsed_doc['test_results']['UniformRandomTimer']['stringProp'][0]['#text'] == '123'

    def test_render_stringProp1(self) -> str:
        element = UniformRandTimer(name='My timer',
                                   comments='My comments',
                                   offset_delay=123,
                                   rand_delay=321,
                                   is_enabled=False)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        assert parsed_doc['test_results']['UniformRandomTimer']['stringProp'][1]['#text'] == '321'

    def test_render_stringProp2(self) -> str:
        element = UniformRandTimer(name='My timer',
                                   comments='My comments',
                                   offset_delay=123,
                                   rand_delay=321,
                                   is_enabled=False)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        assert parsed_doc['test_results']['UniformRandomTimer']['stringProp'][2]['#text'] == 'My comments'

    def test_render_hashtree_contain(self) -> str:
        element = UniformRandTimer(name='My timer',
                                   comments='My comments',
                                   offset_delay=123,
                                   rand_delay=321,
                                   is_enabled=False)
        rendered_doc = element.to_xml()
        assert '<hashTree />' in rendered_doc
