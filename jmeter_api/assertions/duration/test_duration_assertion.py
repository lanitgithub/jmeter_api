import xmltodict
import pytest

from jmeter_api.assertions.duration.elements import DurationAssertion, Scope
from jmeter_api.basics.utils import tag_wrapper


class TestDurationAssertion:
    class TestScope:
        def test_check(self):
            with pytest.raises(TypeError):
                DurationAssertion(scope=1, duration=3)

        def test_check2(self):
            with pytest.raises(TypeError):
                DurationAssertion(scope=True, duration=3)

        def test_check3(self):
            with pytest.raises(TypeError):
                DurationAssertion(scope='main', duration=3)
            
        def test_positive1(self):
            DurationAssertion(scope=Scope.MAIN, duration=3)

    class TestDuration:
        def test_check(self):
            with pytest.raises(TypeError):
                DurationAssertion(duration="30000")

        def test_positive(self):
            DurationAssertion(duration=30000)
            

class TestDurationAssertionRender:
    def test_validation(self):
        element = DurationAssertion(duration=30000)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc,'test_result'))
        assert parsed_doc['test_result']['DurationAssertion']['stringProp']['#text'] == '30000'

    def test_scope(self):
        element = DurationAssertion(scope=Scope.SUB, duration=3)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc,'test_result'))
        for tag in parsed_doc['test_result']['DurationAssertion']['stringProp']:
            if tag['@name'] == 'Assertion.scope':
                assert tag['#text'] == 'children'

    def test_scope1(self):
        element = DurationAssertion(scope=Scope.MAIN_AND_SUB, duration=3)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc,'test_result'))
        for tag in parsed_doc['test_result']['DurationAssertion']['stringProp']:
            if tag['@name'] == 'Assertion.scope':
                assert tag['#text'] == 'all'
