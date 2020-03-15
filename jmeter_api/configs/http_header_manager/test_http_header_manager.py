import xmltodict
import pytest

from jmeter_api.configs.http_header_manager.elements import Header, HTTPHeaderManager
from jmeter_api.basics.utils import tag_wrapper


class TestHeader:
    class TestName:
        def test_type_check(self):
            with pytest.raises(TypeError):
                Header(name=123, value='1')

        def test_positive(self):
            Header(name='var', value='1')
            
    class TestValue:
        def test_type_check(self):
            with pytest.raises(TypeError):
                Header(name='var', value=1)

        def test_positive(self):
            Header(name='var', value='1')
            
            
class TestHeaderRender:
    def test_name(self):
        element = Header(name='var', value='1')
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        assert parsed_doc['result']['elementProp']['@name'] == 'var'
        for tag in parsed_doc['result']['elementProp']['stringProp']:
            if tag['@name'] == 'Header.name':
                assert tag['#text'] == 'var'

    def test_value(self):
        element = Header(name='var', value='1')
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['result']['elementProp']['stringProp']:
            if tag['@name'] == 'Header.value':
                assert tag['#text'] == '1'

                
class TestHTTPHeaderManager:
    class TestHeaderss:
        def test_type_check(self):
            with pytest.raises(TypeError):
                HTTPHeaderManager(headers=123)

        def test_type_check2(self):
            with pytest.raises(TypeError):
                HTTPHeaderManager(headers='123')

        def test_type_check3(self):
            with pytest.raises(TypeError):
                HTTPHeaderManager(headers=Header(name='var', value='12'))
                
        def test_type_check4(self):
            with pytest.raises(TypeError):
                HTTPHeaderManager(headers=['12', '23'])
                
        def test_type_check5(self):
            with pytest.raises(TypeError):
                HTTPHeaderManager(headers=[Header(name='var', value='12'), '23'])
                
        def test_positive2(self):
            HTTPHeaderManager(headers=[{'var': '12'}, {'var2': '22'}])

        def test_positive(self):
            HTTPHeaderManager()

        def test_positive1(self):
            HTTPHeaderManager(headers=[Header(name='var', value='12'),\
                                        Header(name='var2', value='22')])


class TestHTTPAuthManagerRender:
    def test_header(self):
        element = HTTPHeaderManager(headers=[Header(name='var', value='12'),\
                                            Header(name='var2', value='22')])
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['result']['HeaderManager']['collectionProp']['elementProp']:
            if tag['@name'] == 'var':
                assert tag['stringProp'][0]['#text'] == 'var'
                assert tag['stringProp'][1]['#text'] == '12'
                
    def test_header2(self):
        element = HTTPHeaderManager(headers=[{'var': '12'}, {'var2': '22'}])
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['result']['HeaderManager']['collectionProp']['elementProp']:
            if tag['@name'] == 'var':
                assert tag['stringProp'][0]['#text'] == 'var'
                assert tag['stringProp'][1]['#text'] == '12'

    def test_empty(self):
        element = HTTPHeaderManager()
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        assert not 'elementProp' in parsed_doc['result']['HeaderManager']['collectionProp']
                
    def test_hashtree_contain(self):
        element = HTTPHeaderManager(headers=[Header(name='var', value='12'),\
                                            Header(name='var2', value='22')])
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        assert '<hashTree />' in rendered_doc
