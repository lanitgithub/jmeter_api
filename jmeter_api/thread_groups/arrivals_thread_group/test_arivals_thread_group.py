import xmltodict
import pytest

from jmeter_api.thread_groups.arrivals_thread_group.elements import ArrivalsThreadGroup, Unit, ThreadGroupAction
from jmeter_api.basics.utils import tag_wrapper


class TestArrivalsThreadGroupArgs:
    class TestTargetRate:
        def test_check(self):
            with pytest.raises(TypeError):
                ArrivalsThreadGroup(target_rate="1")

        def test_check2(self):
            with pytest.raises(TypeError):
                ArrivalsThreadGroup(target_rate=-1)

        def test_positive(self):
            ArrivalsThreadGroup(target_rate=10)

        def test_positive2(self):
            ArrivalsThreadGroup(target_rate=0)

    class TestRampUp:
        def test_check(self):
            with pytest.raises(TypeError):
                ArrivalsThreadGroup(ramp_up="1")

        def test_check2(self):
            with pytest.raises(TypeError):
                ArrivalsThreadGroup(ramp_up=-1)

        def test_positive(self):
            ArrivalsThreadGroup(ramp_up=10)

        def test_positive2(self):
            ArrivalsThreadGroup(ramp_up=0)

    class TestSteps:
        def test_check(self):
            with pytest.raises(TypeError):
                ArrivalsThreadGroup(steps="1")

        def test_check2(self):
            with pytest.raises(TypeError):
                ArrivalsThreadGroup(steps=-1)

        def test_positive(self):
            ArrivalsThreadGroup(steps=10)

        def test_positive2(self):
            ArrivalsThreadGroup(steps=0)

    class TestHold:
        def test_check(self):
            with pytest.raises(TypeError):
                ArrivalsThreadGroup(hold="1")

        def test_check2(self):
            with pytest.raises(TypeError):
                ArrivalsThreadGroup(hold=-1)

        def test_positive(self):
            ArrivalsThreadGroup(hold=10)

        def test_positive2(self):
            ArrivalsThreadGroup(hold=0)

    class TestIterations:
        def test_check(self):
            with pytest.raises(TypeError):
                ArrivalsThreadGroup(iterations="1")

        def test_check2(self):
            with pytest.raises(TypeError):
                ArrivalsThreadGroup(iterations=-1)

        def test_positive(self):
            ArrivalsThreadGroup(iterations=10)

        def test_positive2(self):
            ArrivalsThreadGroup(iterations=0)

    class TestConcurrencyLimit:
        def test_check(self):
            with pytest.raises(TypeError):
                ArrivalsThreadGroup(concurrency_limit="1")

        def test_check2(self):
            with pytest.raises(TypeError):
                ArrivalsThreadGroup(concurrency_limit=-1)

        def test_positive(self):
            ArrivalsThreadGroup(concurrency_limit=10)

        def test_positive2(self):
            ArrivalsThreadGroup(concurrency_limit=0)


class TestArrivalsThreadGroupRender:
    def test_ramp_up(self):
        element = ArrivalsThreadGroup(ramp_up=50)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        for tag in parsed_doc['test_results']['com.blazemeter.jmeter.threads.arrivals.ArrivalsThreadGroup']['stringProp']:
            if tag['@name'] == 'RampUp':
                assert tag['#text'] == '50'

    def test_target_rate(self):
        element = ArrivalsThreadGroup(target_rate=50)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        for tag in parsed_doc['test_results']['com.blazemeter.jmeter.threads.arrivals.ArrivalsThreadGroup']['stringProp']:
            if tag['@name'] == 'TargetLevel':
                assert tag['#text'] == '50'

    def test_steps(self):
        element = ArrivalsThreadGroup(steps=50)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        for tag in parsed_doc['test_results']['com.blazemeter.jmeter.threads.arrivals.ArrivalsThreadGroup']['stringProp']:
            if tag['@name'] == 'Steps':
                assert tag['#text'] == '50'
                
    def test_hold(self):
        element = ArrivalsThreadGroup(hold=50)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        for tag in parsed_doc['test_results']['com.blazemeter.jmeter.threads.arrivals.ArrivalsThreadGroup']['stringProp']:
            if tag['@name'] == 'Hold':
                assert tag['#text'] == '50'
                
    def test_iterations(self):
        element = ArrivalsThreadGroup(iterations=50)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        for tag in parsed_doc['test_results']['com.blazemeter.jmeter.threads.arrivals.ArrivalsThreadGroup']['stringProp']:
            if tag['@name'] == 'Iterations':
                assert tag['#text'] == '50'
                
    def test_concurrency_limit(self):
        element = ArrivalsThreadGroup(concurrency_limit=50)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        for tag in parsed_doc['test_results']['com.blazemeter.jmeter.threads.arrivals.ArrivalsThreadGroup']['stringProp']:
            if tag['@name'] == 'ConcurrencyLimit':
                assert tag['#text'] == '50'
                
    def test_unit(self):
        element = ArrivalsThreadGroup(unit=Unit.SECOND)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        for tag in parsed_doc['test_results']['com.blazemeter.jmeter.threads.arrivals.ArrivalsThreadGroup']['stringProp']:
            if tag['@name'] == 'Unit':
                assert tag['#text'] == 'S'
                
    def test_filename(self):
        element = ArrivalsThreadGroup(log_filename='file')
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        for tag in parsed_doc['test_results']['com.blazemeter.jmeter.threads.arrivals.ArrivalsThreadGroup']['stringProp']:
            if tag['@name'] == 'LogFilename':
                assert tag['#text'] == 'file'

    def test_on_sample_error(self):
        element = ArrivalsThreadGroup(on_sample_error=ThreadGroupAction.START_NEXT_LOOP)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        for tag in parsed_doc['test_results']['com.blazemeter.jmeter.threads.arrivals.ArrivalsThreadGroup']['stringProp']:
            if tag['@name'] == 'ThreadGroup.on_sample_error':
                assert tag['#text'] == 'startnextloop'
