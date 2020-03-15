import xmltodict
import pytest

from jmeter_api.configs.http_cookie_manager.elements import CookiePolicy, Cookie, HTTPCookieManager
from jmeter_api.basics.utils import tag_wrapper


class TestCookie:
    class TestName:
        def test_type_check(self):
            with pytest.raises(TypeError):
                Cookie(name=123, value='1')

        def test_positive(self):
            Cookie(name='var', value='1')
            
    class TestValue:
        def test_type_check(self):
            with pytest.raises(TypeError):
                Cookie(name='var', value=1)

        def test_positive(self):
            Cookie(name='var', value='1')

    class TestDomain:
        def test_type_check(self):
            with pytest.raises(TypeError):
                Cookie(name='var', value='1', domain=1)

        def test_positive(self):
            Cookie(name='var', value='1', domain='1')

    class TestPath:
        def test_type_check(self):
            with pytest.raises(TypeError):
                Cookie(name='var', value='1', path=1)

        def test_positive(self):
            Cookie(name='var', value='1', path='1')
            
    class TestExpires:
        def test_type_check(self):
            with pytest.raises(TypeError):
                Cookie(name='var', value='1', expires='1')

        def test_positive(self):
            Cookie(name='var', value='1', expires=12345678)
            
    class TestSecure:
        def test_type_check(self):
            with pytest.raises(TypeError):
                Cookie(name='var', value='1', secure='True')

        def test_type_check1(self):
            with pytest.raises(TypeError):
                Cookie(name='var', value='1', secure=1)

        def test_positive(self):
            Cookie(name='var', value='1', secure=True)
            
    class TestPathSpecified:
        def test_type_check(self):
            with pytest.raises(TypeError):
                Cookie(name='var', value='1', path_specified='True')

        def test_type_check1(self):
            with pytest.raises(TypeError):
                Cookie(name='var', value='1', path_specified=1)

        def test_positive(self):
            Cookie(name='var', value='1', path_specified=True)
            
    class TestDomainSpecified:
        def test_type_check(self):
            with pytest.raises(TypeError):
                Cookie(name='var', value='1', domain_specified='True')

        def test_type_check1(self):
            with pytest.raises(TypeError):
                Cookie(name='var', value='1', domain_specified=1)

        def test_positive(self):
            Cookie(name='var', value='1', domain_specified=True)

            
class TestCookieRender:
    def test_name(self):
        element = Cookie(name='var', value='1')
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        assert parsed_doc['result']['elementProp']['@name'] == 'var'
        assert parsed_doc['result']['elementProp']['@testname'] == 'var'

    def test_value(self):
        element = Cookie(name='var', value='1')
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['result']['elementProp']['stringProp']:
            if tag['@name'] == 'Cookie.value':
                assert tag['#text'] == '1'
                
    def test_domain(self):
        element = Cookie(name='var', value='1', domain='dom')
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['result']['elementProp']['stringProp']:
            if tag['@name'] == 'Cookie.domain':
                assert tag['#text'] == 'dom'

    def test_path(self):
        element = Cookie(name='var', value='1', path='pa')
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['result']['elementProp']['stringProp']:
            if tag['@name'] == 'Cookie.path':
                assert tag['#text'] == 'pa'

    def test_expire(self):
        element = Cookie(name='var', value='1', expires=12345678)
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        assert parsed_doc['result']['elementProp']['longProp']['#text'] == '12345678'
                
    def test_bool(self):
        element = Cookie(name='var', value='1')
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['result']['elementProp']['boolProp']:
            if tag['@name'] == 'Cookie.secure':
                assert tag['#text'] == 'false'
            elif tag['@name'] == 'Cookie.path_specified':
                assert tag['#text'] == 'true'
            elif tag['@name'] == 'Cookie.domain_specified':
                assert tag['#text'] == 'true'


class TestHTTPCookieManager:
    class TestCookies:
        def test_type_check(self):
            with pytest.raises(TypeError):
                HTTPCookieManager(cookies=123)

        def test_type_check2(self):
            with pytest.raises(TypeError):
                HTTPCookieManager(cookies='123')

        def test_type_check3(self):
            with pytest.raises(TypeError):
                HTTPCookieManager(cookies=Cookie(name='var', value='12'))
                
        def test_type_check4(self):
            with pytest.raises(TypeError):
                HTTPCookieManager(cookies=['12', '23'])
                
        def test_type_check5(self):
            with pytest.raises(TypeError):
                HTTPCookieManager(cookies=[Cookie(name='var', value='12'), '23'])
                
        def test_type_check6(self):
            with pytest.raises(TypeError):
                HTTPCookieManager(cookies=[{'var': '12'}, {'var2': '22'}])

        def test_positive(self):
            HTTPCookieManager()

        def test_positive1(self):
            HTTPCookieManager(cookies=[Cookie(name='var', value='12'),\
                                            Cookie(name='var2', value='22')])
            
    class TestClearEachIter:
        def test_type_check(self):
            with pytest.raises(TypeError):
                HTTPCookieManager(clear_each_iter="True")

        def test_type_check1(self):
            with pytest.raises(TypeError):
                HTTPCookieManager(clear_each_iter=1)

        def test_positive(self):
            HTTPCookieManager(clear_each_iter=True)

    class TestPolicy:
        def test_type_check(self):
            with pytest.raises(TypeError):
                HTTPCookieManager(policy="standard")

        def test_positive(self):
            HTTPCookieManager(policy=CookiePolicy.DEFAULT)
            

class TestHTTPCookieManagerRender:
    def test_cookie(self):
        element = HTTPCookieManager(cookies=[Cookie(name='var', value='12'),\
                                            Cookie(name='var2', value='22')])
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['result']['CookieManager']['collectionProp']['elementProp']:
            if tag['@name'] == 'var':
                assert tag['@testname'] == 'var'
                assert tag['stringProp'][0]['#text'] == '12'

    def test_clear_each_iter(self):
        element = HTTPCookieManager(clear_each_iter=True)
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        assert parsed_doc['result']['CookieManager']['boolProp']['#text'] == 'true'

    def test_policy(self):
        element = HTTPCookieManager(policy=CookiePolicy.DEFAULT)
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        assert parsed_doc['result']['CookieManager']['stringProp']['#text'] == 'default'

    def test_empty(self):
        element = HTTPCookieManager()
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        assert not 'elementProp' in parsed_doc['result']['CookieManager']['collectionProp']
                
    def test_hashtree_contain(self):
        element = HTTPCookieManager(cookies=[Cookie(name='var', value='12'),\
                                            Cookie(name='var2', value='22')])
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        assert '<hashTree />' in rendered_doc
