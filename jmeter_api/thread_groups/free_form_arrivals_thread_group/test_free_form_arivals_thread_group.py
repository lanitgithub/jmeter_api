import xmltodict
import pytest

from jmeter_api.thread_groups.free_form_arrivals_thread_group.elements import FreeFormArrivalsThreadGroup, Unit, ThreadGroupAction
from jmeter_api.basics.utils import tag_wrapper


class TestFreeFormArrivalsThreadGroupArgs:
    class TestSchedule:
        def test_check(self):
            with pytest.raises(TypeError):
                FreeFormArrivalsThreadGroup(schedule="1")

        def test_check2(self):
            with pytest.raises(TypeError):
                FreeFormArrivalsThreadGroup(schedule={"start": 1, "end": 1, "duration": 1})

        def test_check3(self):
            with pytest.raises(TypeError):
                FreeFormArrivalsThreadGroup(schedule=[{"start": "1", "end": 1, "duration": 1}])
                
        def test_check4(self):
            with pytest.raises(TypeError):
                FreeFormArrivalsThreadGroup(schedule=[{"start": -1, "end": 1, "duration": 1}])

        def test_check5(self):
            with pytest.raises(ValueError):
                FreeFormArrivalsThreadGroup(schedule=[{"start": 1, "end": 1}])

        def test_positive(self):
            FreeFormArrivalsThreadGroup(schedule=[{"start": 1, "end": 1, "duration": 1}])

    class TestIterations:
        def test_check(self):
            with pytest.raises(TypeError):
                FreeFormArrivalsThreadGroup(iterations="1")

        def test_check2(self):
            with pytest.raises(TypeError):
                FreeFormArrivalsThreadGroup(iterations=-1)

        def test_positive(self):
            FreeFormArrivalsThreadGroup(iterations=10)

        def test_positive2(self):
            FreeFormArrivalsThreadGroup(iterations=0)

    class TestConcurrencyLimit:
        def test_check(self):
            with pytest.raises(TypeError):
                FreeFormArrivalsThreadGroup(concurrency_limit="1")

        def test_check2(self):
            with pytest.raises(TypeError):
                FreeFormArrivalsThreadGroup(concurrency_limit=-1)

        def test_positive(self):
            FreeFormArrivalsThreadGroup(concurrency_limit=10)

        def test_positive2(self):
            FreeFormArrivalsThreadGroup(concurrency_limit=0)


class TestFreeFormArrivalsThreadGroupRender:
    def test_target_rate(self):
        element = FreeFormArrivalsThreadGroup(schedule=[{"start": 1, "end": 2, "duration": 3}])
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        for tag in parsed_doc['test_results']['com.blazemeter.jmeter.threads.arrivals.FreeFormArrivalsThreadGroup']['collectionProp']['collectionProp']['stringProp']:
            if tag['@name'] == '49':
                assert tag['#text'] == '1'
                
    def test_iterations(self):
        element = FreeFormArrivalsThreadGroup(iterations=50)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        for tag in parsed_doc['test_results']['com.blazemeter.jmeter.threads.arrivals.FreeFormArrivalsThreadGroup']['stringProp']:
            if tag['@name'] == 'Iterations':
                assert tag['#text'] == '50'
                
    def test_concurrency_limit(self):
        element = FreeFormArrivalsThreadGroup(concurrency_limit=50)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        for tag in parsed_doc['test_results']['com.blazemeter.jmeter.threads.arrivals.FreeFormArrivalsThreadGroup']['stringProp']:
            if tag['@name'] == 'ConcurrencyLimit':
                assert tag['#text'] == '50'
                
    def test_unit(self):
        element = FreeFormArrivalsThreadGroup(unit=Unit.SECOND)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        for tag in parsed_doc['test_results']['com.blazemeter.jmeter.threads.arrivals.FreeFormArrivalsThreadGroup']['stringProp']:
            if tag['@name'] == 'Unit':
                assert tag['#text'] == 'S'
                
    def test_filename(self):
        element = FreeFormArrivalsThreadGroup(log_filename='file')
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        for tag in parsed_doc['test_results']['com.blazemeter.jmeter.threads.arrivals.FreeFormArrivalsThreadGroup']['stringProp']:
            if tag['@name'] == 'LogFilename':
                assert tag['#text'] == 'file'

    def test_on_sample_error(self):
        element = FreeFormArrivalsThreadGroup(on_sample_error=ThreadGroupAction.START_NEXT_LOOP)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        for tag in parsed_doc['test_results']['com.blazemeter.jmeter.threads.arrivals.FreeFormArrivalsThreadGroup']['stringProp']:
            if tag['@name'] == 'ThreadGroup.on_sample_error':
                assert tag['#text'] == 'startnextloop'
