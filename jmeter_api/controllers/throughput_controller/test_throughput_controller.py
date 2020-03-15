import xmltodict
import pytest

from jmeter_api.controllers.throughput_controller.elements import ThroughputController, ThroughputMode
from jmeter_api.basics.utils import tag_wrapper


class TestThroughputController:
    class TestThroughput:
        def test_total1(self):
            with pytest.raises(TypeError):
                ThroughputController(throughputMode=ThroughputMode.TOTAL, throughput=80.5)

        def test_total2(self):
            with pytest.raises(TypeError):
                ThroughputController(throughputMode=ThroughputMode.TOTAL, throughput="80")

        def test_total3(self):
            with pytest.raises(ValueError):
                ThroughputController(throughputMode=ThroughputMode.TOTAL, throughput=-1)

        def test_percent(self):
            with pytest.raises(TypeError):
                ThroughputController(throughputMode=ThroughputMode.PERCENT, throughput="80")

        def test_total3(self):
            with pytest.raises(ValueError):
                ThroughputController(throughputMode=ThroughputMode.PERCENT, throughput=-1)

        def test_total3(self):
            with pytest.raises(ValueError):
                ThroughputController(throughputMode=ThroughputMode.PERCENT, throughput=100.1)

        def test_positive_percent1(self):
            ThroughputController(throughputMode=ThroughputMode.PERCENT, throughput=80)

        def test_positive_percent2(self):
            ThroughputController(throughputMode=ThroughputMode.PERCENT, throughput=0)

        def test_positive_percent3(self):
            ThroughputController(throughputMode=ThroughputMode.PERCENT, throughput=100)

        def test_positive_total1(self):
            ThroughputController(throughputMode=ThroughputMode.TOTAL, throughput=102)

        def test_positive_total1(self):
            ThroughputController(throughputMode=ThroughputMode.TOTAL, throughput=2)

        def test_positive_total2(self):
            ThroughputController(throughputMode=ThroughputMode.TOTAL, throughput=0)

    class TestThroughputMode:
        def test_check(self):
            with pytest.raises(TypeError):
                ThroughputController(throughputMode="ThroughputMode.PERCENT")

    class TestPerThread:
        def test_check(self):
            with pytest.raises(TypeError):
                ThroughputController(perThread="True")

        def test_check2(self):
            with pytest.raises(TypeError):
                ThroughputController(perThread=1)

        def test_positive(self):
            ThroughputController(perThread=True)


class TestThroughputControllerRender:
    def test_loops(self):
        element = ThroughputController(throughputMode=ThroughputMode.PERCENT, throughput=80)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        assert parsed_doc['test_results']['ThroughputController']['FloatProperty']['value'] == '80.0'
