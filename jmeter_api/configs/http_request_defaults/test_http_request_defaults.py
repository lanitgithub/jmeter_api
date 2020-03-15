import xmltodict
import pytest

from jmeter_api.configs.http_request_defaults.elements import Implementation,\
     IpSourceType, PostBodyRaw, Argument, HTTPRequestDefaults
from jmeter_api.basics.utils import tag_wrapper
from jmeter_api.basics.utils import FileEncoding


class TestPostBodyRaw:
    class TestMetadata:
        def test_type_check(self):
            with pytest.raises(TypeError):
                PostBodyRaw(value='1', metadata=1)

        def test_positive(self):
            PostBodyRaw(value='1', metadata='1')
            
    class TestValue:
        def test_type_check(self):
            with pytest.raises(TypeError):
                PostBodyRaw(value=1)

        def test_positive(self):
            PostBodyRaw(value='1')
            
    class TestEncode:
        def test_type_check(self):
            with pytest.raises(TypeError):
                PostBodyRaw(value='1', encode='True')
                
        def test_type_check1(self):
            with pytest.raises(TypeError):
                PostBodyRaw(value='1', encode=1)

        def test_positive(self):
            PostBodyRaw(value='1', encode=True)
            
            
class TestPostBodyRawRender:
    def test_metadata(self):
        element = PostBodyRaw(value='1', metadata='1')
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['result']['elementProp']['stringProp']:
            if tag['@name'] == 'Argument.metadata':
                assert tag['#text'] == '1'

    def test_value(self):
        element = PostBodyRaw(value='1')
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['result']['elementProp']['stringProp']:
            if tag['@name'] == 'Argument.value':
                assert tag['#text'] == '1'
                
    def test_encode(self):
        element = PostBodyRaw(value='1', encode=True)
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        assert parsed_doc['result']['elementProp']['boolProp']['#text'] == 'true'


class TestArgument:
    class TestName:
        def test_type_check(self):
            with pytest.raises(TypeError):
                Argument(value='1', name=1)

        def test_positive(self):
            Argument(value='1', name='1')
            
    class TestValue:
        def test_type_check(self):
            with pytest.raises(TypeError):
                Argument(value=1, name='1')

        def test_positive(self):
            Argument(value='1', name='1')
            
    class TestEncode:
        def test_type_check(self):
            with pytest.raises(TypeError):
                Argument(name='1', value='1', encode='True')
                
        def test_type_check1(self):
            with pytest.raises(TypeError):
                Argument(name='1', value='1', encode=1)

        def test_positive(self):
            Argument(name='1', value='1', encode=True)

    class TestUseEquals:
        def test_type_check(self):
            with pytest.raises(TypeError):
                Argument(name='1', value='1', use_equals='True')
                
        def test_type_check1(self):
            with pytest.raises(TypeError):
                Argument(name='1', value='1', use_equals=1)

        def test_positive(self):
            arg = Argument(name='1', value='1', use_equals=False)
            assert arg.metadata == ''
            
        def test_positive1(self):
            arg = Argument(name='1', value='1', use_equals=True)
            assert arg.metadata == '='

    class TestContentType:
        def test_type_check(self):
            with pytest.raises(TypeError):
                Argument(name='1', value='1', content_type=1)

        def test_positive(self):
            Argument(name='1', value='1', content_type='text')
            
            
class TestArgumentRender:
    def test_name(self):
        element = Argument(name='1', value='2')
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['result']['elementProp']['stringProp']:
            if tag['@name'] == 'Argument.name':
                assert tag['#text'] == '1'
                
    def test_use_equals(self):
        element = Argument(name='1', value='1')
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['result']['elementProp']['boolProp']:
            if tag['@name'] == 'HTTPArgument.use_equals':
                assert tag['#text'] == 'true'
        for tag in parsed_doc['result']['elementProp']['stringProp']:
            if tag['@name'] == 'Argument.metadata':
                assert tag['#text'] == '='

    def test_value(self):
        element = Argument(name='1', value='2')
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['result']['elementProp']['stringProp']:
            if tag['@name'] == 'Argument.value':
                assert tag['#text'] == '2'
                
    def test_encode(self):
        element = Argument(name='1', value='1', encode=True)
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['result']['elementProp']['boolProp']:
            if tag['@name'] == 'HTTPArgument.always_encode':
                assert tag['#text'] == 'true'

        
class TestHTTPRequestDefaults:
    # basic fields
    class TestArguments:
        def test_type_check(self):
            with pytest.raises(TypeError):
                HTTPRequestDefaults(arguments=123)

        def test_type_check2(self):
            with pytest.raises(TypeError):
                HTTPRequestDefaults(arguments=[{'var': '12'}, {'var2': '22'}])

        def test_type_check3(self):
            with pytest.raises(TypeError):
                HTTPRequestDefaults(arguments=Argument(name='var', value='12'))
                
        def test_type_check4(self):
            with pytest.raises(TypeError):
                HTTPRequestDefaults(arguments=['12', '23'])
                
        def test_type_check5(self):
            with pytest.raises(TypeError):
                HTTPRequestDefaults(arguments=[Argument(name='var', value='12'), '23'])
                
        def test_positive2(self):
            HTTPRequestDefaults(arguments='123456')

        def test_positive(self):
            HTTPRequestDefaults()

        def test_positive1(self):
            HTTPRequestDefaults(arguments=[Argument(name='var', value='12'),\
                                        Argument(name='var2', value='22')])
    
    class TestDomain:
        def test_type_check(self):
            with pytest.raises(TypeError):
                HTTPRequestDefaults(domain=123)
                
        def test_positive(self):
            HTTPRequestDefaults(domain='123')

    class TestPort:
        def test_type_check(self):
            with pytest.raises(TypeError):
                HTTPRequestDefaults(port='123')
                
        def test_type_check2(self):
            with pytest.raises(TypeError):
                HTTPRequestDefaults(port=-1)
                
        def test_positive(self):
            HTTPRequestDefaults(port=123)
            
    class TestProtocol:
        def test_type_check(self):
            with pytest.raises(TypeError):
                HTTPRequestDefaults(protocol=123)
                
        def test_positive(self):
            HTTPRequestDefaults(protocol='123')
            
    class TestFileEncoding:
        def test_type_check(self):
            with pytest.raises(TypeError):
                HTTPRequestDefaults(encoding='UTF-8')
                
        def test_positive(self):
            HTTPRequestDefaults(encoding=FileEncoding.UTF8)
            
    class TestPath:
        def test_type_check(self):
            with pytest.raises(TypeError):
                HTTPRequestDefaults(path=123)
                
        def test_positive(self):
            HTTPRequestDefaults(path='123')

    class TestConcurrentPool:
        def test_type_check(self):
            with pytest.raises(TypeError):
                HTTPRequestDefaults(concurrent_pool='12')
                
        def test_type_check2(self):
            with pytest.raises(TypeError):
                HTTPRequestDefaults(concurrent_pool=-1)
                
        def test_positive(self):
            HTTPRequestDefaults(concurrent_pool=12)

    class TestConnectTimeout:
        def test_type_check(self):
            with pytest.raises(TypeError):
                HTTPRequestDefaults(connect_timeout='12')
                
        def test_type_check2(self):
            with pytest.raises(TypeError):
                HTTPRequestDefaults(connect_timeout=-1)
                
        def test_positive(self):
            HTTPRequestDefaults(connect_timeout=12)

    class TestResponseTimeout:
        def test_type_check(self):
            with pytest.raises(TypeError):
                HTTPRequestDefaults(response_timeout='12')
                
        def test_type_check2(self):
            with pytest.raises(TypeError):
                HTTPRequestDefaults(response_timeout=-1)
                
        def test_positive(self):
            HTTPRequestDefaults(response_timeout=12)

    # advanced fields
    class TestImageParser:
        def test_type_check(self):
            with pytest.raises(TypeError):
                HTTPRequestDefaults(image_parser='True')
                
        def test_type_check2(self):
            with pytest.raises(TypeError):
                HTTPRequestDefaults(image_parser=1)
                
        def test_positive(self):
            HTTPRequestDefaults(image_parser=True)

    class TestConcurrentDwn:
        def test_type_check(self):
            with pytest.raises(TypeError):
                HTTPRequestDefaults(concurrent_dwn='True')
                
        def test_type_check2(self):
            with pytest.raises(TypeError):
                HTTPRequestDefaults(concurrent_dwn=1)
                
        def test_positive(self):
            HTTPRequestDefaults(concurrent_dwn=True)

    class TestMD5:
        def test_type_check(self):
            with pytest.raises(TypeError):
                HTTPRequestDefaults(md5='True')
                
        def test_type_check2(self):
            with pytest.raises(TypeError):
                HTTPRequestDefaults(md5=1)
                
        def test_positive(self):
            HTTPRequestDefaults(md5=True)

    class TestProxyPort:
        def test_type_check(self):
            with pytest.raises(TypeError):
                HTTPRequestDefaults(proxy_port='123')
                
        def test_type_check2(self):
            with pytest.raises(TypeError):
                HTTPRequestDefaults(proxy_port=-1)
                
        def test_positive(self):
            HTTPRequestDefaults(proxy_port=123)
            
    class TestEmbedded:
        def test_type_check(self):
            with pytest.raises(TypeError):
                HTTPRequestDefaults(embedded_url_re=123)
                
        def test_positive(self):
            HTTPRequestDefaults(embedded_url_re='123')
            
    class TestIpSource:
        def test_type_check(self):
            with pytest.raises(TypeError):
                HTTPRequestDefaults(ip_source=123)
                
        def test_positive(self):
            HTTPRequestDefaults(ip_source='123')

    class TestProxyScheme:
        def test_type_check(self):
            with pytest.raises(TypeError):
                HTTPRequestDefaults(proxy_scheme=123)
                
        def test_positive(self):
            HTTPRequestDefaults(proxy_scheme='123')

    class TestProxyHost:
        def test_type_check(self):
            with pytest.raises(TypeError):
                HTTPRequestDefaults(proxy_host=123)
                
        def test_positive(self):
            HTTPRequestDefaults(proxy_host='123')

    class TestProxyUser:
        def test_type_check(self):
            with pytest.raises(TypeError):
                HTTPRequestDefaults(proxy_user=123)
                
        def test_positive(self):
            HTTPRequestDefaults(proxy_user='123')

    class TestProxyPass:
        def test_type_check(self):
            with pytest.raises(TypeError):
                HTTPRequestDefaults(proxy_pass=123)
                
        def test_positive(self):
            HTTPRequestDefaults(proxy_pass='123')

    class TestIpSourceType:
        def test_type_check(self):
            with pytest.raises(TypeError):
                HTTPRequestDefaults(ip_source_type=1)

        def test_type_check2(self):
            with pytest.raises(TypeError):
                HTTPRequestDefaults(ip_source_type='1')
                
        def test_positive(self):
            HTTPRequestDefaults(ip_source_type=IpSourceType.IP)

    class TestImplementation:
        def test_type_check2(self):
            with pytest.raises(TypeError):
                HTTPRequestDefaults(implementation='HttpClient4')
                
        def test_positive(self):
            HTTPRequestDefaults(implementation=Implementation.HTTP)
            
class TestHTTPRequestDefaultsRender:
    def test_args(self):
        element = HTTPRequestDefaults(arguments=[Argument(name='var', value='12'),\
                                            Argument(name='var2', value='22')])
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['result']['ConfigTestElement']['elementProp']['collectionProp']['elementProp']:
            if tag['@name'] == 'var':
                assert tag['stringProp'][0]['#text'] == '12'
                assert tag['stringProp'][2]['#text'] == 'var'
          
    def test_body(self):
        element = HTTPRequestDefaults(arguments='132456')
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        assert parsed_doc['result']['ConfigTestElement']['boolProp']['#text'] == 'true'
        for tag in parsed_doc['result']['ConfigTestElement']['elementProp']['collectionProp']['elementProp']['stringProp']:
            if tag['@name'] == 'Argument.value':
                assert tag['#text'] == '132456'
                    
    # basic fields              
    def test_domain(self):
        element = HTTPRequestDefaults(domain='123')
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['result']['ConfigTestElement']['stringProp']:
            if tag['@name'] == 'HTTPSampler.domain':
                assert tag['#text'] == '123'

    def test_port(self):
        element = HTTPRequestDefaults(port=123)
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['result']['ConfigTestElement']['stringProp']:
            if tag['@name'] == 'HTTPSampler.port':
                assert tag['#text'] == '123'

    def test_protocol(self):
        element = HTTPRequestDefaults(protocol='123')
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['result']['ConfigTestElement']['stringProp']:
            if tag['@name'] == 'HTTPSampler.protocol':
                assert tag['#text'] == '123' 

    def test_encoding(self):
        element = HTTPRequestDefaults(encoding=FileEncoding.UTF8)
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['result']['ConfigTestElement']['stringProp']:
            if tag['@name'] == 'HTTPSampler.contentEncoding':
                assert tag['#text'] == 'UTF-8'
                
    def test_path(self):
        element = HTTPRequestDefaults(path='123')
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['result']['ConfigTestElement']['stringProp']:
            if tag['@name'] == 'HTTPSampler.path':
                assert tag['#text'] == '123'
                
    def test_concurrent_pool(self):
        element = HTTPRequestDefaults(concurrent_pool=123)
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['result']['ConfigTestElement']['stringProp']:
            if tag['@name'] == 'HTTPSampler.concurrentPool':
                assert tag['#text'] == '123'
                
    def test_connect_timeout(self):
        element = HTTPRequestDefaults(connect_timeout=123)
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['result']['ConfigTestElement']['stringProp']:
            if tag['@name'] == 'HTTPSampler.connect_timeout':
                assert tag['#text'] == '123'

    def test_response_timeout(self):
        element = HTTPRequestDefaults(response_timeout=123)
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['result']['ConfigTestElement']['stringProp']:
            if tag['@name'] == 'HTTPSampler.response_timeout':
                assert tag['#text'] == '123'

    # advanced fields
    def test_image_parser(self):
        element = HTTPRequestDefaults(image_parser=True)
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['result']['ConfigTestElement']['stringProp']:
            if tag['@name'] == 'HTTPSampler.image_parser':
                assert tag['#text'] == 'true'

    def test_concurrent_dwn(self):
        element = HTTPRequestDefaults(concurrent_dwn=True)
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['result']['ConfigTestElement']['stringProp']:
            if tag['@name'] == 'HTTPSampler.concurrentDwn':
                assert tag['#text'] == 'true'

    def test_md5(self):
        element = HTTPRequestDefaults(md5=True)
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['result']['ConfigTestElement']['stringProp']:
            if tag['@name'] == 'HTTPSampler.md5':
                assert tag['#text'] == 'true'

    def test_proxy_port(self):
        element = HTTPRequestDefaults(proxy_port=123)
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['result']['ConfigTestElement']['stringProp']:
            if tag['@name'] == 'HTTPSampler.proxyPort':
                assert tag['#text'] == '123'

    def test_embedded_url_re(self):
        element = HTTPRequestDefaults(embedded_url_re='123')
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['result']['ConfigTestElement']['stringProp']:
            if tag['@name'] == 'HTTPSampler.embedded_url_re':
                assert tag['#text'] == '123'

    def test_ip_source(self):
        element = HTTPRequestDefaults(ip_source='123')
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['result']['ConfigTestElement']['stringProp']:
            if tag['@name'] == 'HTTPSampler.ipSource':
                assert tag['#text'] == '123'

    def test_proxy_scheme(self):
        element = HTTPRequestDefaults(proxy_scheme='123')
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['result']['ConfigTestElement']['stringProp']:
            if tag['@name'] == 'HTTPSampler.proxyScheme':
                assert tag['#text'] == '123'
                
    def test_proxy_host(self):
        element = HTTPRequestDefaults(proxy_host='123')
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['result']['ConfigTestElement']['stringProp']:
            if tag['@name'] == 'HTTPSampler.proxyHost':
                assert tag['#text'] == '123'
                
    def test_proxy_user(self):
        element = HTTPRequestDefaults(proxy_user='123')
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['result']['ConfigTestElement']['stringProp']:
            if tag['@name'] == 'HTTPSampler.proxyUser':
                assert tag['#text'] == '123'
                
    def test_proxy_pass(self):
        element = HTTPRequestDefaults(proxy_pass='123')
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['result']['ConfigTestElement']['stringProp']:
            if tag['@name'] == 'HTTPSampler.proxyPass':
                assert tag['#text'] == '123'
                
    def test_ip_source_type(self):
        element = HTTPRequestDefaults(ip_source_type=IpSourceType.IP)
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['result']['ConfigTestElement']['stringProp']:
            if tag['@name'] == 'HTTPSampler.ipSourceType':
                assert tag['#text'] == '0'
                
    def test_implementation(self):
        element = HTTPRequestDefaults(implementation=Implementation.HTTP)
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['result']['ConfigTestElement']['stringProp']:
            if tag['@name'] == 'HTTPSampler.implementation':
                assert tag['#text'] == 'HttpClient4'
                
    def test_empty(self):
        element = HTTPRequestDefaults()
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        assert not 'elementProp' in parsed_doc['result']['ConfigTestElement']['elementProp']['collectionProp']
        assert not 'intProp' in parsed_doc['result']['ConfigTestElement']
                
    def test_hashtree_contain(self):
        element = HTTPRequestDefaults(arguments=[Argument(name='var', value='12'),\
                                            Argument(name='var2', value='22')])
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        assert '<hashTree />' in rendered_doc
