import xmltodict
import pytest

from jmeter_api.assertions.size.elements import SizeAssertion, Scope, TestField, Operator
from jmeter_api.basics.utils import tag_wrapper


class TestSizeAssertion:
    class TestScope:
        def test_check(self):
            with pytest.raises(TypeError):
                SizeAssertion(scope=1, size=3)

        def test_check2(self):
            with pytest.raises(TypeError):
                SizeAssertion(scope=True, size=3)

        def test_positive(self):
            SizeAssertion(scope='Name', size=3)
            
        def test_positive1(self):
            SizeAssertion(scope=Scope.MAIN, size=3)

    class TestSize:
        def test_check(self):
            with pytest.raises(TypeError):
                SizeAssertion(size="30000")

        def test_positive(self):
            SizeAssertion(size=30000)

    class TestTestField:
        def test_check(self):
            with pytest.raises(TypeError):
                SizeAssertion(size=3, test_field="SizeAssertion.response_network_size")

        def test_positive(self):
            SizeAssertion(size=3, test_field=TestField.HEADER)

    class TestOperator:
        def test_check(self):
            with pytest.raises(TypeError):
                SizeAssertion(size=3, operator="4")

        def test_positive(self):
            SizeAssertion(size=3, operator=Operator.LESS)

class TestSizeAssertionRender:
    def test_size(self):
        element = SizeAssertion(size=30000)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc,'test_result'))
        for tag in parsed_doc['test_result']['SizeAssertion']['stringProp']:
            if tag['@name'] == 'SizeAssertion.size':
                assert tag['#text'] == '30000'

    def test_test_field(self):
        element = SizeAssertion(size=30000, test_field=TestField.HEADER)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc,'test_result'))
        for tag in parsed_doc['test_result']['SizeAssertion']['stringProp']:
            if tag['@name'] == 'Assertion.test_field':
                assert tag['#text'] == 'SizeAssertion.response_headers'

    def test_operator(self):
        element = SizeAssertion(size=30000, operator=Operator.NOT_EQUAL)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc,'test_result'))
        assert parsed_doc['test_result']['SizeAssertion']['intProp']['#text'] == '2'

    def test_scope(self):
        element = SizeAssertion(scope=Scope.SUB, size=3)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc,'test_result'))
        for tag in parsed_doc['test_result']['SizeAssertion']['stringProp']:
            if tag['@name'] == 'Assertion.scope':
                assert tag['#text'] == 'children'

    def test_scope1(self):
        element = SizeAssertion(scope=Scope.MAIN_AND_SUB, size=3)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc,'test_result'))
        for tag in parsed_doc['test_result']['SizeAssertion']['stringProp']:
            if tag['@name'] == 'Assertion.scope':
                assert tag['#text'] == 'all'
                
    def test_scope2(self):
        element = SizeAssertion(scope='var_name', size=3)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc,'test_result'))
        for tag in parsed_doc['test_result']['SizeAssertion']['stringProp']:
            if tag['@name'] == 'Assertion.scope':
                assert tag['#text'] == 'variable'
            if tag['@name'] == 'Scope.variable':
                assert tag['#text'] == 'var_name' 
