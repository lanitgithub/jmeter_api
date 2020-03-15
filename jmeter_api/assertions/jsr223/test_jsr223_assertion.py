import xmltodict
import pytest

from jmeter_api.assertions.jsr223.elements import JSR223Assertion, ScriptLanguage
from jmeter_api.basics.utils import tag_wrapper


class TestJSR223AssertionRender:
    def test_script_language(self):
        element = JSR223Assertion(script_language=ScriptLanguage.JAVA)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc,'test_result'))
        for tag in parsed_doc['test_result']['JSR223Assertion']['stringProp']:
            if tag['@name'] == 'scriptLanguage':
                assert tag['#text'] == 'java'
                
    def test_cache_key(self):
        element = JSR223Assertion(cache_key=False)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc,'test_result'))
        for tag in parsed_doc['test_result']['JSR223Assertion']['stringProp']:
            if tag['@name'] == 'cacheKey':
                assert tag['#text'] == 'false'
                
    def test_filename(self):
        element = JSR223Assertion(filename="./jmeter_api/basics/jsr223_test.groovy")
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc,'test_result'))
        for tag in parsed_doc['test_result']['JSR223Assertion']['stringProp']:
            if tag['@name'] == 'filename':
                assert tag['#text'] == "./jmeter_api/basics/jsr223_test.groovy"

    def test_script(self):
        sc = """var a=2
vars.put("some value",a)
log("value added")"""
        element = JSR223Assertion(script=sc)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc,'test_result'))
        for tag in parsed_doc['test_result']['JSR223Assertion']['stringProp']:
            if tag['@name'] == 'script':
                assert tag['#text'] == sc
                
    def test_hashtree_contain(self):
        element = JSR223Assertion()
        rendered_doc = element.to_xml()
        assert '<hashTree />' in rendered_doc
