import xmltodict
import pytest

from jmeter_api.configs.http_auth_manager.elements import AuthMechanism, Auth, HTTPAuthManager
from jmeter_api.basics.utils import tag_wrapper


class TestAuth:
    class TestUsername:
        def test_type_check(self):
            with pytest.raises(TypeError):
                Auth(username=123, password='1')

        def test_positive(self):
            Auth(username='var', password='1')
            
    class TestPassword:
        def test_type_check(self):
            with pytest.raises(TypeError):
                Auth(username='var', password=1)

        def test_positive(self):
            Auth(username='var', password='1')

    class TestDomain:
        def test_type_check(self):
            with pytest.raises(TypeError):
                Auth(username='var', password='1', domain=1)

        def test_positive(self):
            Auth(username='var', password='1', domain='1')

    class TestURL:
        def test_type_check(self):
            with pytest.raises(TypeError):
                Auth(username='var', password='1', url=1)

        def test_positive(self):
            Auth(username='var', password='1', url='https://google.com/')
            
    class TestRealm:
        def test_type_check(self):
            with pytest.raises(TypeError):
                Auth(username='var', password='1', realm=1)

        def test_positive(self):
            Auth(username='var', password='1', realm='s')
            
    class TestMechanism:
        def test_type_check(self):
            with pytest.raises(TypeError):
                Auth(username='var', password='1', mechanism='BASIC')

        def test_positive(self):
            Auth(username='var', password='1', mechanism=AuthMechanism.BASIC)

            
class TestAuthRender:
    def test_name(self):
        element = Auth(username='var', password='1')
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        assert parsed_doc['result']['elementProp']['@name'] == 'var'
        for tag in parsed_doc['result']['elementProp']['stringProp']:
            if tag['@name'] == 'Authorization.username':
                assert tag['#text'] == 'var'

    def test_pass(self):
        element = Auth(username='var', password='1')
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['result']['elementProp']['stringProp']:
            if tag['@name'] == 'Authorization.password':
                assert tag['#text'] == '1'
                
    def test_domain(self):
        element = Auth(username='var', password='1', domain='dom')
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['result']['elementProp']['stringProp']:
            if tag['@name'] == 'Authorization.domain':
                assert tag['#text'] == 'dom'

    def test_url(self):
        element = Auth(username='var', password='1', url='http://121.0.0.1:8097/request')
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['result']['elementProp']['stringProp']:
            if tag['@name'] == 'Authorization.url':
                assert tag['#text'] == 'http://121.0.0.1:8097/request'

    def test_realm(self):
        element = Auth(username='var', password='1', realm='realm')
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['result']['elementProp']['stringProp']:
            if tag['@name'] == 'Authorization.realm':
                assert tag['#text'] == 'realm'

    def test_mechanism(self):
        element = Auth(username='var', password='1', mechanism=AuthMechanism.KERBEROS)
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['result']['elementProp']['stringProp']:
            if tag['@name'] == 'Authorization.mechanism':
                assert tag['#text'] == 'KERBEROS'

                
class TestHTTPAuthManager:
    class TestAuths:
        def test_type_check(self):
            with pytest.raises(TypeError):
                HTTPAuthManager(auth_list=123)

        def test_type_check2(self):
            with pytest.raises(TypeError):
                HTTPAuthManager(auth_list='123')

        def test_type_check3(self):
            with pytest.raises(TypeError):
                HTTPAuthManager(auth_list=Auth(username='var', password='12'))
                
        def test_type_check4(self):
            with pytest.raises(TypeError):
                HTTPAuthManager(auth_list=['12', '23'])
                
        def test_type_check5(self):
            with pytest.raises(TypeError):
                HTTPAuthManager(auth_list=[Auth(username='var', password='12'), '23'])
                
        def test_type_check6(self):
            with pytest.raises(TypeError):
                HTTPAuthManager(auth_list=[{'var': '12'}, {'var2': '22'}])

        def test_positive(self):
            HTTPAuthManager()

        def test_positive1(self):
            HTTPAuthManager(auth_list=[Auth(username='var', password='12'),\
                                            Auth(username='var2', password='22')])
            
    class TestClearEachIter:
        def test_type_check(self):
            with pytest.raises(TypeError):
                HTTPAuthManager(clear_each_iter="True")

        def test_type_check1(self):
            with pytest.raises(TypeError):
                HTTPAuthManager(clear_each_iter=1)

        def test_positive(self):
            HTTPAuthManager(clear_each_iter=True)
            

class TestHTTPAuthManagerRender:
    def test_auth(self):
        element = HTTPAuthManager(auth_list=[Auth(username='var', password='12'),\
                                            Auth(username='var2', password='22')])
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['result']['AuthManager']['collectionProp']['elementProp']:
            if tag['@name'] == 'var':
                assert tag['stringProp'][1]['#text'] == 'var'
                assert tag['stringProp'][2]['#text'] == '12'

    def test_clear_each_iter(self):
        element = HTTPAuthManager(clear_each_iter=True)
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        assert parsed_doc['result']['AuthManager']['boolProp']['#text'] == 'true'

    def test_empty(self):
        element = HTTPAuthManager()
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        assert not 'elementProp' in parsed_doc['result']['AuthManager']['collectionProp']
                
    def test_hashtree_contain(self):
        element = HTTPAuthManager(auth_list=[Auth(username='var', password='12'),\
                                            Auth(username='var2', password='22')])
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        assert '<hashTree />' in rendered_doc
