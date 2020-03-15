import xmltodict
import pytest

from jmeter_api.thread_groups.ultimate_thread_group.elements import UltimateThreadGroup, ThreadGroupAction
from jmeter_api.basics.utils import tag_wrapper


class TestUltimateThreadGroupArgs:
    class TestSchedule:
        def test_check(self):
            with pytest.raises(TypeError):
                UltimateThreadGroup(schedule="1")

        def test_check2(self):
            with pytest.raises(TypeError):
                UltimateThreadGroup(schedule={"thread_count": 1, "delay": 0, "startup": 0,
                                                "hold": 10, "shotdown": 0})

        def test_check3(self):
            with pytest.raises(TypeError):
                UltimateThreadGroup(schedule=[{"thread_count": "1", "delay": 0, "startup": 0,
                                                "hold": 10, "shotdown": 0}])
                
        def test_check4(self):
            with pytest.raises(TypeError):
                UltimateThreadGroup(schedule=[{"thread_count": -1, "delay": 0, "startup": 0,
                                                "hold": 10, "shotdown": 0}])

        def test_check5(self):
            with pytest.raises(ValueError):
                UltimateThreadGroup(schedule=[{"thread_count": 1, "startup": 0,
                                                "hold": 10, "shotdown": 0}])

        def test_positive(self):
            UltimateThreadGroup(schedule=[{"thread_count": 1, "delay": 0, "startup": 0,
                                            "hold": 10, "shotdown": 0}])


class TestUltimateThreadGroupRender:
    def test_target_rate(self):
        element = UltimateThreadGroup(schedule=[{"thread_count": 3, "delay": 0, "startup": 5,
                                                      "hold": 10, "shotdown": 6}])
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        assert parsed_doc['test_results']['kg.apc.jmeter.threads.UltimateThreadGroup']['collectionProp']['collectionProp']['stringProp'][0]['#text'] == "3"
        assert parsed_doc['test_results']['kg.apc.jmeter.threads.UltimateThreadGroup']['collectionProp']['collectionProp']['stringProp'][1]['#text'] == "0"
        assert parsed_doc['test_results']['kg.apc.jmeter.threads.UltimateThreadGroup']['collectionProp']['collectionProp']['stringProp'][2]['#text'] == "5"
        assert parsed_doc['test_results']['kg.apc.jmeter.threads.UltimateThreadGroup']['collectionProp']['collectionProp']['stringProp'][3]['#text'] == "10"
        assert parsed_doc['test_results']['kg.apc.jmeter.threads.UltimateThreadGroup']['collectionProp']['collectionProp']['stringProp'][4]['#text'] == "6"

    def test_on_sample_error(self):
        element = UltimateThreadGroup(on_sample_error=ThreadGroupAction.START_NEXT_LOOP)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        assert parsed_doc['test_results']['kg.apc.jmeter.threads.UltimateThreadGroup']['stringProp']['#text'] == 'startnextloop'
