import xmltodict
import pytest

from jmeter_api.thread_groups.teardown_thread_group.elements import TearDownThreadGroup, ThreadGroupAction
from jmeter_api.basics.utils import tag_wrapper


class TestTearDownThreadGroupRender:
    def test_loops(self):
        element = TearDownThreadGroup(loops=55)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        assert parsed_doc['test_results']['PostThreadGroup']['elementProp']['stringProp']['#text'] == '55'
        
    def test_is_sheduler_enable(self):
        element = TearDownThreadGroup(is_sheduler_enable=True)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        assert parsed_doc['test_results']['PostThreadGroup']['boolProp']['#text'] == 'true'

    def test_sheduler_duration(self):
        element = TearDownThreadGroup(is_sheduler_enable=True, sheduler_duration=1000, sheduler_delay=2000)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        for tag in parsed_doc['test_results']['PostThreadGroup']['stringProp']:
            if tag['@name'] == 'ThreadGroup.duration':
                assert tag['#text'] == '1000'

    def test_sheduler_delay(self):
        element = TearDownThreadGroup(is_sheduler_enable=True, sheduler_duration=1000, sheduler_delay=2000)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        for tag in parsed_doc['test_results']['PostThreadGroup']['stringProp']:
            if tag['@name'] == 'ThreadGroup.delay':
                assert tag['#text'] == '2000'

    def test_ramp_time(self):
        element = TearDownThreadGroup(ramp_time=50)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        for tag in parsed_doc['test_results']['PostThreadGroup']['stringProp']:
            if tag['@name'] == 'ThreadGroup.ramp_time':
                assert tag['#text'] == '50'

    def test_num_threads(self):
        element = TearDownThreadGroup(num_threads=50)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        for tag in parsed_doc['test_results']['PostThreadGroup']['stringProp']:
            if tag['@name'] == 'ThreadGroup.num_threads':
                assert tag['#text'] == '50'

    def test_on_sample_error(self):
        element = TearDownThreadGroup(on_sample_error=ThreadGroupAction.START_NEXT_LOOP)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        for tag in parsed_doc['test_results']['PostThreadGroup']['stringProp']:
            if tag['@name'] == 'ThreadGroup.on_sample_error':
                assert tag['#text'] == 'startnextloop'
