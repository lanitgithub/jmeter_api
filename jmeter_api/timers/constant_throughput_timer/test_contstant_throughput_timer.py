import xmltodict
import pytest

from jmeter_api.timers.constant_throughput_timer.elements import ConstantThroughputTimer, BasedOn
from jmeter_api.basics.utils import tag_wrapper


class TestConstantThroughputTimerArgs:
    def test_args_type_check(self):
        # name type check
        with pytest.raises(TypeError):
            ConstantThroughputTimer(name=123)

        # comments type check
        with pytest.raises(TypeError):
            ConstantThroughputTimer(comments=123)

        # is_enabled type check
        with pytest.raises(TypeError):
            ConstantThroughputTimer(is_enabled="True")

        # targ_throughput type check (negative number input)
        with pytest.raises(TypeError, match=r".*arg: targ_throughput should be positive int or float.*"):
            ConstantThroughputTimer(targ_throughput=-1)

        # arg: targ_throughput should be positive int or float. (wrong data type input)
        with pytest.raises(TypeError, match=r".*arg: targ_throughput should be positive int or float.*"):
            ConstantThroughputTimer(targ_throughput='123')

        # based_on type check (wrong data type input)
        with pytest.raises(TypeError, match=r".*arg: based_on should be BasedOn.*"):
            ConstantThroughputTimer(based_on=123)


class TestConstantThroughputTimerRender:
    def test_intProp(self):
        element = ConstantThroughputTimer(name='My tp timer',
                                          targ_throughput=2,
                                          based_on=BasedOn.THIS_THREAD_ONLY,
                                          comments='My comments',
                                          is_enabled=False)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        assert parsed_doc['test_results']['ConstantThroughputTimer']['intProp']['#text'] == '0'

    def test_testname(self):
        element = ConstantThroughputTimer(name='My tp timer',
                                          targ_throughput=2,
                                          based_on=BasedOn.THIS_THREAD_ONLY,
                                          comments='My comments',
                                          is_enabled=False)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        assert parsed_doc['test_results']['ConstantThroughputTimer']['@testname'] == 'My tp timer'

    def test_enabled(self):
        element = ConstantThroughputTimer(name='My tp timer',
                                          targ_throughput=2,
                                          based_on=BasedOn.THIS_THREAD_ONLY,
                                          comments='My comments',
                                          is_enabled=False)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        assert parsed_doc['test_results']['ConstantThroughputTimer']['@enabled'] == 'false'

    def test_value(self):
        element = ConstantThroughputTimer(name='My tp timer',
                                          targ_throughput=2,
                                          based_on=BasedOn.THIS_THREAD_ONLY,
                                          comments='My comments',
                                          is_enabled=False)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        assert parsed_doc['test_results']['ConstantThroughputTimer']['doubleProp']['value'] == '2'

    def test_value_stringProp(self):
        element = ConstantThroughputTimer(name='My tp timer',
                                          targ_throughput=2,
                                          based_on=BasedOn.THIS_THREAD_ONLY,
                                          comments='My comments',
                                          is_enabled=False)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        assert parsed_doc['test_results']['ConstantThroughputTimer']['stringProp']['#text'] == 'My comments'

    def test_hashtree_contain(self):
        element = ConstantThroughputTimer(name='My tp timer',
                                          targ_throughput=2,
                                          based_on=BasedOn.THIS_THREAD_ONLY,
                                          comments='My comments',
                                          is_enabled=False)
        rendered_doc = element.to_xml()
        assert '<hashTree />' in rendered_doc
