import xmltodict
import pytest

from jmeter_api.thread_groups.common_thread_group.elements import CommonThreadGroup, ThreadGroupAction
from jmeter_api.basics.utils import tag_wrapper


class TestCommonThreadGroupArgs:
    class TestDelayedStart:
        def test_check(self):
            with pytest.raises(TypeError):
                CommonThreadGroup(delayed_start="True")

        def test_check2(self):
            with pytest.raises(TypeError):
                CommonThreadGroup(delayed_start=1)

        def test_positive(self):
            CommonThreadGroup(delayed_start=True)


class TestCommonThreadGroupRender:
    def test_loops(self):
        element = CommonThreadGroup(loops=55)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        assert parsed_doc['test_results']['ThreadGroup']['elementProp']['stringProp']['#text'] == '55'
        
    def test_is_sheduler_enable(self):
        element = CommonThreadGroup(is_sheduler_enable=True)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        assert parsed_doc['test_results']['ThreadGroup']['boolProp']['#text'] == 'true'

    def test_sheduler_duration(self):
        element = CommonThreadGroup(is_sheduler_enable=True, sheduler_duration=1000, sheduler_delay=2000)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        for tag in parsed_doc['test_results']['ThreadGroup']['stringProp']:
            if tag['@name'] == 'ThreadGroup.duration':
                assert tag['#text'] == '1000'

    def test_sheduler_delay(self):
        element = CommonThreadGroup(is_sheduler_enable=True, sheduler_duration=1000, sheduler_delay=2000)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        for tag in parsed_doc['test_results']['ThreadGroup']['stringProp']:
            if tag['@name'] == 'ThreadGroup.delay':
                assert tag['#text'] == '2000'

    def test_ramp_time(self):
        element = CommonThreadGroup(ramp_time=50)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        for tag in parsed_doc['test_results']['ThreadGroup']['stringProp']:
            if tag['@name'] == 'ThreadGroup.ramp_time':
                assert tag['#text'] == '50'

    def test_num_threads(self):
        element = CommonThreadGroup(num_threads=50)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        for tag in parsed_doc['test_results']['ThreadGroup']['stringProp']:
            if tag['@name'] == 'ThreadGroup.num_threads':
                assert tag['#text'] == '50'

    def test_on_sample_error(self):
        element = CommonThreadGroup(on_sample_error=ThreadGroupAction.START_NEXT_LOOP)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        for tag in parsed_doc['test_results']['ThreadGroup']['stringProp']:
            if tag['@name'] == 'ThreadGroup.on_sample_error':
                assert tag['#text'] == 'startnextloop'
