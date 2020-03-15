import xmltodict
import pytest

from jmeter_api.post_processors.json_extractor.elements import JSONExtractor, Scope
from jmeter_api.basics.utils import tag_wrapper


class TestJSONExtractor:
    class TestReferenceNames:
        def test_check(self):
            with pytest.raises(TypeError):
                JSONExtractor(referenceNames=1)

        def test_positive(self):
            JSONExtractor(referenceNames='Name')

    class TestJsonPathExprs:
        def test_check(self):
            with pytest.raises(TypeError):
                JSONExtractor(jsonPathExprs=1)

        def test_positive(self):
            JSONExtractor(jsonPathExprs='Name')

    class TestMatchNumbers:
        def test_check(self):
            with pytest.raises(TypeError):
                JSONExtractor(match_numbers='1')
            with pytest.raises(TypeError):
                JSONExtractor(match_numbers=-2)

        def test_positive(self):
            JSONExtractor(match_numbers=1)
            JSONExtractor(match_numbers=0)
            JSONExtractor(match_numbers=-1)
    
    class TestDefaultValues:
        def test_check(self):
            with pytest.raises(TypeError):
                JSONExtractor(defaultValues=1)

        def test_positive(self):
            JSONExtractor(defaultValues='Name')

    class TestScope:
        def test_check(self):
            with pytest.raises(TypeError):
                JSONExtractor(scope=1)

        def test_check2(self):
            with pytest.raises(TypeError):
                JSONExtractor(scope=True)

        def test_positive(self):
            JSONExtractor(scope='Name')
            
        def test_positive1(self):
            JSONExtractor(scope=Scope.MAIN)

    class TestComputeConcat:
        def test_check(self):
            with pytest.raises(TypeError):
                JSONExtractor(compute_concat=1)
                
        def test_check1(self):
            with pytest.raises(TypeError):
                JSONExtractor(compute_concat="True")

        def test_positive(self):
            JSONExtractor(compute_concat=True)      


class TestJSONExtractorRender:
    def test_scope(self):
        element = JSONExtractor(scope=Scope.SUB)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc,'test_result'))
        for tag in parsed_doc['test_result']['JSONPostProcessor']['stringProp']:
            if tag['@name'] == 'Sample.scope':
                assert tag['#text'] == 'children'

    def test_scope1(self):
        element = JSONExtractor(scope=Scope.MAIN_AND_SUB)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc,'test_result'))
        for tag in parsed_doc['test_result']['JSONPostProcessor']['stringProp']:
            if tag['@name'] == 'Sample.scope':
                assert tag['#text'] == 'all'
                
    def test_scope2(self):
        element = JSONExtractor(scope='var_name')
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc,'test_result'))
        for tag in parsed_doc['test_result']['JSONPostProcessor']['stringProp']:
            if tag['@name'] == 'Sample.scope':
                assert tag['#text'] == 'variable'
            if tag['@name'] == 'Scope.variable':
                assert tag['#text'] == 'var_name' 

    def test_defaultValues(self):
        element = JSONExtractor(defaultValues='default')
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc,'test_result'))
        for tag in parsed_doc['test_result']['JSONPostProcessor']['stringProp']:
            if tag['@name'] == 'JSONPostProcessor.defaultValues':
                assert tag['#text'] == 'default'
                
    def test_referenceNames(self):
        element = JSONExtractor(referenceNames='name')
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc,'test_result'))
        for tag in parsed_doc['test_result']['JSONPostProcessor']['stringProp']:
            if tag['@name'] == 'JSONPostProcessor.referenceNames':
                assert tag['#text'] == 'name'
                
    def test_jsonPathExprs(self):
        element = JSONExtractor(jsonPathExprs='expr[*].result')
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc,'test_result'))
        for tag in parsed_doc['test_result']['JSONPostProcessor']['stringProp']:
            if tag['@name'] == 'JSONPostProcessor.jsonPathExprs':
                assert tag['#text'] == 'expr[*].result'
                
    def test_match_numbers(self):
        element = JSONExtractor(match_numbers=0)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc,'test_result'))
        for tag in parsed_doc['test_result']['JSONPostProcessor']['stringProp']:
            if tag['@name'] == 'JSONPostProcessor.match_numbers':
                assert tag['#text'] == '0'

    def test_compute_concat(self):
        element = JSONExtractor(compute_concat=True)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc,'test_result'))
        assert parsed_doc['test_result']['JSONPostProcessor']['boolProp']['#text'] == 'true'

    def test_hashtree_contain(self):
        element = JSONExtractor()
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        assert '<hashTree />' in rendered_doc
