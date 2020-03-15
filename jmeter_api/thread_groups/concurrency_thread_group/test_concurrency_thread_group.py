import xmltodict
import pytest

from jmeter_api.thread_groups.concurrency_thread_group.elements import ConcurrencyThreadGroup, Unit, ThreadGroupAction
from jmeter_api.basics.utils import tag_wrapper


class TestConcurrencyThreadGroupArgs:
    class TestTargetRate:
        def test_check(self):
            with pytest.raises(TypeError):
                ConcurrencyThreadGroup(target_concurrency="1")

        def test_check2(self):
            with pytest.raises(TypeError):
                ConcurrencyThreadGroup(target_concurrency=-1)

        def test_positive(self):
            ConcurrencyThreadGroup(target_concurrency=10)

        def test_positive2(self):
            ConcurrencyThreadGroup(target_concurrency=0)

    class TestRampUp:
        def test_check(self):
            with pytest.raises(TypeError):
                ConcurrencyThreadGroup(ramp_up="1")

        def test_check2(self):
            with pytest.raises(TypeError):
                ConcurrencyThreadGroup(ramp_up=-1)

        def test_positive(self):
            ConcurrencyThreadGroup(ramp_up=10)

        def test_positive2(self):
            ConcurrencyThreadGroup(ramp_up=0)

    class TestSteps:
        def test_check(self):
            with pytest.raises(TypeError):
                ConcurrencyThreadGroup(steps="1")

        def test_check2(self):
            with pytest.raises(TypeError):
                ConcurrencyThreadGroup(steps=-1)

        def test_positive(self):
            ConcurrencyThreadGroup(steps=10)

        def test_positive2(self):
            ConcurrencyThreadGroup(steps=0)

    class TestHold:
        def test_check(self):
            with pytest.raises(TypeError):
                ConcurrencyThreadGroup(hold="1")

        def test_check2(self):
            with pytest.raises(TypeError):
                ConcurrencyThreadGroup(hold=-1)

        def test_positive(self):
            ConcurrencyThreadGroup(hold=10)

        def test_positive2(self):
            ConcurrencyThreadGroup(hold=0)

    class TestIterations:
        def test_check(self):
            with pytest.raises(TypeError):
                ConcurrencyThreadGroup(iterations="1")

        def test_check2(self):
            with pytest.raises(TypeError):
                ConcurrencyThreadGroup(iterations=-1)

        def test_positive(self):
            ConcurrencyThreadGroup(iterations=10)

        def test_positive2(self):
            ConcurrencyThreadGroup(iterations=0)


class TestConcurrencyThreadGroupRender:
    def test_ramp_up(self):
        element = ConcurrencyThreadGroup(ramp_up=50)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        for tag in parsed_doc['test_results']['com.blazemeter.jmeter.threads.concurrency.ConcurrencyThreadGroup']['stringProp']:
            if tag['@name'] == 'RampUp':
                assert tag['#text'] == '50'

    def test_target_rate(self):
        element = ConcurrencyThreadGroup(target_concurrency=50)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        for tag in parsed_doc['test_results']['com.blazemeter.jmeter.threads.concurrency.ConcurrencyThreadGroup']['stringProp']:
            if tag['@name'] == 'TargetLevel':
                assert tag['#text'] == '50'

    def test_steps(self):
        element = ConcurrencyThreadGroup(steps=50)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        for tag in parsed_doc['test_results']['com.blazemeter.jmeter.threads.concurrency.ConcurrencyThreadGroup']['stringProp']:
            if tag['@name'] == 'Steps':
                assert tag['#text'] == '50'
                
    def test_hold(self):
        element = ConcurrencyThreadGroup(hold=50)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        for tag in parsed_doc['test_results']['com.blazemeter.jmeter.threads.concurrency.ConcurrencyThreadGroup']['stringProp']:
            if tag['@name'] == 'Hold':
                assert tag['#text'] == '50'
                
    def test_iterations(self):
        element = ConcurrencyThreadGroup(iterations=50)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        for tag in parsed_doc['test_results']['com.blazemeter.jmeter.threads.concurrency.ConcurrencyThreadGroup']['stringProp']:
            if tag['@name'] == 'Iterations':
                assert tag['#text'] == '50'
                       
    def test_unit(self):
        element = ConcurrencyThreadGroup(unit=Unit.SECOND)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        for tag in parsed_doc['test_results']['com.blazemeter.jmeter.threads.concurrency.ConcurrencyThreadGroup']['stringProp']:
            if tag['@name'] == 'Unit':
                assert tag['#text'] == 'S'
                
    def test_filename(self):
        element = ConcurrencyThreadGroup(log_filename='file')
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        for tag in parsed_doc['test_results']['com.blazemeter.jmeter.threads.concurrency.ConcurrencyThreadGroup']['stringProp']:
            if tag['@name'] == 'LogFilename':
                assert tag['#text'] == 'file'

    def test_on_sample_error(self):
        element = ConcurrencyThreadGroup(on_sample_error=ThreadGroupAction.START_NEXT_LOOP)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        for tag in parsed_doc['test_results']['com.blazemeter.jmeter.threads.concurrency.ConcurrencyThreadGroup']['stringProp']:
            if tag['@name'] == 'ThreadGroup.on_sample_error':
                assert tag['#text'] == 'startnextloop'
