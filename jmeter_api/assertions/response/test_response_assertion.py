import xmltodict
import pytest

from jmeter_api.assertions.response.elements import ResponseAssertion, Scope, TestField, TestType
from jmeter_api.basics.utils import tag_wrapper


class TestResponseAssertion:
    class TestScope:
        def test_check(self):
            with pytest.raises(TypeError):
                ResponseAssertion(scope=1)

        def test_check2(self):
            with pytest.raises(TypeError):
                ResponseAssertion(scope=True)

        def test_positive(self):
            ResponseAssertion(scope='Name')
            
        def test_positive1(self):
            ResponseAssertion(scope=Scope.MAIN)

    class TestTestField:
        def test_check(self):
            with pytest.raises(TypeError):
                ResponseAssertion(test_field="Assertion.response_data_as_document")

        def test_positive(self):
            ResponseAssertion(test_field=TestField.DOCUMENT)

    class TestTestType:
        def test_check(self):
            with pytest.raises(TypeError):
                ResponseAssertion(test_type=8)
                
        def test_check2(self):
            with pytest.raises(TypeError):
                ResponseAssertion(test_type="8")

        def test_positive(self):
            ra = ResponseAssertion(test_type=TestType.CONTAINS)
            assert ra.test_type == "2"

        def test_positive2(self):
            ra = ResponseAssertion(test_type=TestType.MATCHES, test_type_not=True)
            assert ra.test_type == "5"

        def test_positive3(self):
            ra = ResponseAssertion(test_type=TestType.EQUALS, test_type_or=True)
            assert ra.test_type == "40"

        def test_positive4(self):
            ra = ResponseAssertion(test_type=TestType.SUBSTRING, test_type_not=True, test_type_or=True)
            assert ra.test_type == "52"

    class TestIgnoreStatus:
        def test_check(self):
            with pytest.raises(TypeError):
                ResponseAssertion(ignore_status=1)
                
        def test_check2(self):
            with pytest.raises(TypeError):
                ResponseAssertion(ignore_status="True")

        def test_positive(self):
            ResponseAssertion(ignore_status=True)

    class TestTestTypeNot:
        def test_check(self):
            with pytest.raises(TypeError):
                ResponseAssertion(test_type_not=1)
                
        def test_check2(self):
            with pytest.raises(TypeError):
                ResponseAssertion(test_type_not="True")

        def test_positive(self):
            ResponseAssertion(test_type_not=True)

    class TestTestTypeOr:
        def test_check(self):
            with pytest.raises(TypeError):
                ResponseAssertion(test_type_or=1)
                
        def test_check2(self):
            with pytest.raises(TypeError):
                ResponseAssertion(test_type_or="True")

        def test_positive(self):
            ResponseAssertion(test_type_or=True)

    class TestPatterns:
        def test_check(self):
            with pytest.raises(TypeError):
                ResponseAssertion(patterns="pats")
                
        def test_check2(self):
            with pytest.raises(TypeError):
                ResponseAssertion(patterns=[1,2])

        def test_positive(self):
            ResponseAssertion(patterns=["par"])

    class TestCustomMessager:
        def test_check(self):
            with pytest.raises(TypeError):
                ResponseAssertion(custom_message=1)

        def test_positive(self):
            ResponseAssertion(custom_message="Message")

class TestResponseAssertionRender:
    def test_test_field(self):
        element = ResponseAssertion(test_field=TestField.REQUEST_DATA)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc,'test_result'))
        for tag in parsed_doc['test_result']['ResponseAssertion']['stringProp']:
            if tag['@name'] == 'Assertion.test_field':
                assert tag['#text'] == 'Assertion.request_data'

    def test_custom_message(self):
        element = ResponseAssertion(custom_message="Mes")
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc,'test_result'))
        for tag in parsed_doc['test_result']['ResponseAssertion']['stringProp']:
            if tag['@name'] == 'Assertion.custom_message':
                assert tag['#text'] == 'Mes'

    def test_patterns(self):
        element = ResponseAssertion(patterns=["Mes","mes"])
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc,'test_result'))
        assert parsed_doc['test_result']['ResponseAssertion']['collectionProp']['stringProp'][0]['#text'] == 'Mes'
                
    def test_test_type(self):
        element = ResponseAssertion(test_type=TestType.CONTAINS)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc,'test_result'))
        assert parsed_doc['test_result']['ResponseAssertion']['intProp']['#text'] == '2'

    def test_ignore_status(self):
        element = ResponseAssertion(ignore_status=True)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc,'test_result'))
        assert parsed_doc['test_result']['ResponseAssertion']['boolProp']['#text'] == 'true'

    def test_scope(self):
        element = ResponseAssertion(scope=Scope.SUB)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc,'test_result'))
        for tag in parsed_doc['test_result']['ResponseAssertion']['stringProp']:
            if tag['@name'] == 'Assertion.scope':
                assert tag['#text'] == 'children'

    def test_scope1(self):
        element = ResponseAssertion(scope=Scope.MAIN_AND_SUB)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc,'test_result'))
        for tag in parsed_doc['test_result']['ResponseAssertion']['stringProp']:
            if tag['@name'] == 'Assertion.scope':
                assert tag['#text'] == 'all'
                
    def test_scope2(self):
        element = ResponseAssertion(scope='var_name')
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc,'test_result'))
        for tag in parsed_doc['test_result']['ResponseAssertion']['stringProp']:
            if tag['@name'] == 'Assertion.scope':
                assert tag['#text'] == 'variable'
            if tag['@name'] == 'Scope.variable':
                assert tag['#text'] == 'var_name' 
