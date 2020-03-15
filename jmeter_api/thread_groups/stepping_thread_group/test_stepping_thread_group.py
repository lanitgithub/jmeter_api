import xmltodict
import pytest

from jmeter_api.thread_groups.stepping_thread_group.elements import SteppingThreadGroup, ThreadGroupAction
from jmeter_api.basics.utils import tag_wrapper


class TestSteppingThreadGroupArgs:
    class TestNumThreads:
        def test_check(self):
            with pytest.raises(TypeError):
                SteppingThreadGroup(num_threads="1")

        def test_check(self):
            with pytest.raises(TypeError):
                SteppingThreadGroup(num_threads=-1)

        def test_positive(self):
            SteppingThreadGroup(num_threads=1)

    class TestInitialDelay:
        def test_check(self):
            with pytest.raises(TypeError):
                SteppingThreadGroup(initial_delay="1")

        def test_check(self):
            with pytest.raises(TypeError):
                SteppingThreadGroup(initial_delay=-1)

        def test_positive(self):
            SteppingThreadGroup(initial_delay=1)
            
    class TestStartUsersCount:
        def test_check(self):
            with pytest.raises(TypeError):
                SteppingThreadGroup(start_users_count="1")

        def test_check(self):
            with pytest.raises(TypeError):
                SteppingThreadGroup(start_users_count=-1)

        def test_positive(self):
            SteppingThreadGroup(start_users_count=1)
            
    class TestStartUsersCountBurst:
        def test_check(self):
            with pytest.raises(TypeError):
                SteppingThreadGroup(start_users_count_burst="1")

        def test_check(self):
            with pytest.raises(TypeError):
                SteppingThreadGroup(start_users_count_burst=-1)

        def test_positive(self):
            SteppingThreadGroup(start_users_count_burst=1)

    class TestStartUsersPeriod:
        def test_check(self):
            with pytest.raises(TypeError):
                SteppingThreadGroup(start_users_period="1")

        def test_check(self):
            with pytest.raises(TypeError):
                SteppingThreadGroup(start_users_period=-1)

        def test_positive(self):
            SteppingThreadGroup(start_users_period=1)
            
    class TestStopUsersCount:
        def test_check(self):
            with pytest.raises(TypeError):
                SteppingThreadGroup(stop_users_count="1")

        def test_check(self):
            with pytest.raises(TypeError):
                SteppingThreadGroup(stop_users_count=-1)

        def test_positive(self):
            SteppingThreadGroup(stop_users_count=1)
            
    class TestStopUsersPeriod:
        def test_check(self):
            with pytest.raises(TypeError):
                SteppingThreadGroup(stop_users_period="1")

        def test_check(self):
            with pytest.raises(TypeError):
                SteppingThreadGroup(stop_users_period=-1)

        def test_positive(self):
            SteppingThreadGroup(stop_users_period=1)
            
    class TestHold:
        def test_check(self):
            with pytest.raises(TypeError):
                SteppingThreadGroup(hold="1")

        def test_check(self):
            with pytest.raises(TypeError):
                SteppingThreadGroup(hold=-1)

        def test_positive(self):
            SteppingThreadGroup(hold=1)
            
    class TestRampUp:
        def test_check(self):
            with pytest.raises(TypeError):
                SteppingThreadGroup(ramp_up="1")

        def test_check(self):
            with pytest.raises(TypeError):
                SteppingThreadGroup(ramp_up=-1)

        def test_positive(self):
            SteppingThreadGroup(ramp_up=1)


class TestSteppingThreadGroupRender:
    def test_num_threads(self):
        element = SteppingThreadGroup(num_threads=1)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        for tag in parsed_doc['test_results']['kg.apc.jmeter.threads.SteppingThreadGroup']['stringProp']:
            if tag['@name'] == 'ThreadGroup.num_threads':
                assert tag['#text'] == '1'
                
    def test_initial_delay(self):
        element = SteppingThreadGroup(initial_delay=1)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        for tag in parsed_doc['test_results']['kg.apc.jmeter.threads.SteppingThreadGroup']['stringProp']:
            if tag['@name'] == 'Threads initial delay':
                assert tag['#text'] == '1'
                
    def test_start_users_count(self):
        element = SteppingThreadGroup(start_users_count=1)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        for tag in parsed_doc['test_results']['kg.apc.jmeter.threads.SteppingThreadGroup']['stringProp']:
            if tag['@name'] == 'Start users count':
                assert tag['#text'] == '1'
                
    def test_start_users_count_burst(self):
        element = SteppingThreadGroup(start_users_count_burst=1)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        for tag in parsed_doc['test_results']['kg.apc.jmeter.threads.SteppingThreadGroup']['stringProp']:
            if tag['@name'] == 'Start users count burst':
                assert tag['#text'] == '1'
                
    def test_start_users_period(self):
        element = SteppingThreadGroup(start_users_period=1)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        for tag in parsed_doc['test_results']['kg.apc.jmeter.threads.SteppingThreadGroup']['stringProp']:
            if tag['@name'] == 'Start users period':
                assert tag['#text'] == '1'
                
    def test_stop_users_count(self):
        element = SteppingThreadGroup(stop_users_count=1)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        for tag in parsed_doc['test_results']['kg.apc.jmeter.threads.SteppingThreadGroup']['stringProp']:
            if tag['@name'] == 'Stop users count':
                assert tag['#text'] == '1'
                
    def test_stop_users_period(self):
        element = SteppingThreadGroup(stop_users_period=1)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        for tag in parsed_doc['test_results']['kg.apc.jmeter.threads.SteppingThreadGroup']['stringProp']:
            if tag['@name'] == 'Stop users period':
                assert tag['#text'] == '1'
                
    def test_hold(self):
        element = SteppingThreadGroup(hold=1)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        for tag in parsed_doc['test_results']['kg.apc.jmeter.threads.SteppingThreadGroup']['stringProp']:
            if tag['@name'] == 'flighttime':
                assert tag['#text'] == '1'
                
    def test_ramp_up(self):
        element = SteppingThreadGroup(ramp_up=1)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        for tag in parsed_doc['test_results']['kg.apc.jmeter.threads.SteppingThreadGroup']['stringProp']:
            if tag['@name'] == 'rampUp':
                assert tag['#text'] == '1'
                
    def test_on_sample_error(self):
        element = SteppingThreadGroup(on_sample_error=ThreadGroupAction.START_NEXT_LOOP)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        for tag in parsed_doc['test_results']['kg.apc.jmeter.threads.SteppingThreadGroup']['stringProp']:
            if tag['@name'] == 'ThreadGroup.on_sample_error':
                assert tag['#text'] == 'startnextloop'
                
