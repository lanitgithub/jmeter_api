import xmltodict
import pytest

from jmeter_api.assertions.json.elements import JSONAssertion
from jmeter_api.basics.utils import tag_wrapper


class TestJSONAssertion:
    class TestJSONPath:
        def test_check(self):
            with pytest.raises(TypeError):
                JSONAssertion(json_path = 1)

        def test_positive(self):
            JSONAssertion(json_path = "data[*].value")
            
    class TestExpectedValue:
        def test_check(self):
            with pytest.raises(TypeError):
                JSONAssertion(expected_value = 1)

        def test_positive(self):
            JSONAssertion(expected_value = "value")

    class TestValidation:
        def test_check(self):
            with pytest.raises(TypeError):
                JSONAssertion(validation = "True")

        def test_check2(self):
            with pytest.raises(TypeError):
                JSONAssertion(validation = 1)

        def test_positive(self):
            JSONAssertion(validation = True)
            
    class TestExpectNull:
        def test_check(self):
            with pytest.raises(TypeError):
                JSONAssertion(expect_null = "True")

        def test_check2(self):
            with pytest.raises(TypeError):
                JSONAssertion(expect_null = 1)

        def test_positive(self):
            JSONAssertion(expect_null = True)
            
    class TestInvert:
        def test_check(self):
            with pytest.raises(TypeError):
                JSONAssertion(invert = "True")

        def test_check2(self):
            with pytest.raises(TypeError):
                JSONAssertion(invert = 1)

        def test_positive(self):
            JSONAssertion(invert = True)
            
    class TestIsRegex:
        def test_check(self):
            with pytest.raises(TypeError):
                JSONAssertion(is_regex = "True")

        def test_check2(self):
            with pytest.raises(TypeError):
                JSONAssertion(is_regex = 1)

        def test_positive(self):
            JSONAssertion(is_regex = True)
            

class TestJSONAssertionRender:
    def test_validation(self):
        element = JSONAssertion(validation=True)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc,'test_result'))
        for tag in parsed_doc['test_result']['JSONPathAssertion']['boolProp']:
            if tag['@name'] == 'JSONVALIDATION':
                assert tag['#text'] == 'true'

    def test_expect_null(self):
        element = JSONAssertion(expect_null=True)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc,'test_result'))
        for tag in parsed_doc['test_result']['JSONPathAssertion']['boolProp']:
            if tag['@name'] == 'EXPECT_NULL':
                assert tag['#text'] == 'true'

    def test_invert(self):
        element = JSONAssertion(invert=True)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc,'test_result'))
        for tag in parsed_doc['test_result']['JSONPathAssertion']['boolProp']:
            if tag['@name'] == 'INVERT':
                assert tag['#text'] == 'true'

    def test_is_regex(self):
        element = JSONAssertion(is_regex=False)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc,'test_result'))
        for tag in parsed_doc['test_result']['JSONPathAssertion']['boolProp']:
            if tag['@name'] == 'ISREGEX':
                assert tag['#text'] == 'false'

    def test_json_path(self):
        element = JSONAssertion(json_path="data[*].value")
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc,'test_result'))
        for tag in parsed_doc['test_result']['JSONPathAssertion']['stringProp']:
            if tag['@name'] == 'JSON_PATH':
                assert tag['#text'] == "data[*].value"

    def test_expected_value(self):
        element = JSONAssertion(expected_value="value")
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc,'test_result'))
        for tag in parsed_doc['test_result']['JSONPathAssertion']['stringProp']:
            if tag['@name'] == 'EXPECTED_VALUE':
                assert tag['#text'] == "value"                
