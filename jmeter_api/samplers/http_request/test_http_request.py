import xmltodict
import pytest

from jmeter_api.samplers.http_request.elements import HttpRequest, Method, Protocol, Implement, Source


class TestHttpRequestArgsTypes:
    # name type check
    def test_name(self):
        with pytest.raises(TypeError):
            HttpRequest(name=123)
    # comments type check

    def test_comments(self):
        with pytest.raises(TypeError):
            HttpRequest(comments=123)
    # is_enabled type check

    def test_enabled(self):
        with pytest.raises(TypeError):
            HttpRequest(is_enabled="True")
    # host type check (non string data input)

    def test_host(self):
        with pytest.raises(TypeError):
            HttpRequest(host=1)
    # path type check (non string data input)

    def test_path(self):
        with pytest.raises(TypeError):
            HttpRequest(path=-1)
    # method type check (non Method data input)

    def test_method(self):
        with pytest.raises(TypeError):
            HttpRequest(method=-1)

    def test_protocol(self):
        with pytest.raises(TypeError):
            HttpRequest(protocol=2)

    def test_port(self):
        with pytest.raises(ValueError):
            HttpRequest(port=-1)

    def test_port2(self):
        with pytest.raises(TypeError):
            HttpRequest(port='123')

    def test_content_encoding(self):
        with pytest.raises(TypeError):
            HttpRequest(content_encoding=-1)

    def test_auto_redirect(self):
        with pytest.raises(TypeError):
            HttpRequest(auto_redirect=-1)

    def test_keep_alive(self):
        with pytest.raises(TypeError):
            HttpRequest(keep_alive=5)

    def test_do_multipart_post(self):
        with pytest.raises(TypeError):
            HttpRequest(do_multipart_post=5)

    def test_browser_comp_headers(self):
        with pytest.raises(TypeError):
            HttpRequest(browser_comp_headers=-9)

    def test_implementation(self):
        with pytest.raises(TypeError):
            HttpRequest(implementation='52')

    def test_connect_timeout(self):
        with pytest.raises(TypeError):
            HttpRequest(connect_timeout='5')

    def test_connect_timeout2(self):
        with pytest.raises(ValueError):
            HttpRequest(connect_timeout=-1)

    def test_response_timeout(self):
        with pytest.raises(TypeError):
            HttpRequest(response_timeout='5')

    def test_response_timeout2(self):
        with pytest.raises(ValueError):
            HttpRequest(response_timeout=-1)

    def test_retrieve_all_emb_resources(self):
        with pytest.raises(TypeError):
            HttpRequest(retrieve_all_emb_resources='5')

    def test_parallel_downloads(self):
        with pytest.raises(TypeError):
            HttpRequest(parallel_downloads='5')

    def test_parallel_downloads_no(self):
        with pytest.raises(TypeError):
            HttpRequest(parallel_downloads_no='5')

    def test_parallel_downloads_no2(self):
        with pytest.raises(ValueError):
            HttpRequest(parallel_downloads_no=-1)

    def test_parallel_downloads_no(self):
        with pytest.raises(TypeError):
            HttpRequest(parallel_downloads_no='5')

    def test_url_must_match(self):
        with pytest.raises(TypeError):
            HttpRequest(url_must_match=True)

    def test_source_type(self):
        with pytest.raises(TypeError):
            HttpRequest(source_type=5)

    def test_source_address(self):
        with pytest.raises(TypeError):
            HttpRequest(source_address=5)

    def test_proxy_scheme(self):
        with pytest.raises(TypeError):
            HttpRequest(proxy_scheme=5)

    def test_proxy_host(self):
        with pytest.raises(TypeError):
            HttpRequest(proxy_host=5)

    def test_proxy_port(self):
        with pytest.raises(TypeError):
            HttpRequest(proxy_port='5')

    def test_proxy_port2(self):
        with pytest.raises(ValueError):
            HttpRequest(proxy_port=-1)

    def test_proxy_username(self):
        with pytest.raises(TypeError):
            HttpRequest(proxy_username=-1)

    def test_proxy_password(self):
        with pytest.raises(TypeError):
            HttpRequest(proxy_password=-1)

    def test_text(self):
        with pytest.raises(TypeError):
            HttpRequest(text=-1)


class TestHttpRequestRender:
    def test_name(self):
        element = HttpRequest(name='My http')
        rendered_doc = element.to_xml().replace('<hashTree />', '')
        parsed_doc = xmltodict.parse(rendered_doc)
        assert parsed_doc['HTTPSamplerProxy']['@testname'] == 'My http'

    def test_comments(self):
        element = HttpRequest(comments='My http')
        rendered_doc = element.to_xml().replace('<hashTree />', '')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['HTTPSamplerProxy']['stringProp']:
            if tag['@name'] == 'TestPlan.comments':
                assert tag['#text'] == 'My http'

    def test_is_enabled(self):
        element = HttpRequest(is_enabled=False)
        rendered_doc = element.to_xml().replace('<hashTree />', '')
        parsed_doc = xmltodict.parse(rendered_doc)
        assert parsed_doc['HTTPSamplerProxy']['@enabled'] == 'false'

    def test_host(self):
        element = HttpRequest(host='localhost')
        rendered_doc = element.to_xml().replace('<hashTree />', '')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['HTTPSamplerProxy']['stringProp']:
            if tag['@name'] == 'HTTPSampler.domain':
                assert tag['#text'] == 'localhost'

    def test_path(self):
        element = HttpRequest(path='/search')
        rendered_doc = element.to_xml().replace('<hashTree />', '')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['HTTPSamplerProxy']['stringProp']:
            if tag['@name'] == 'HTTPSampler.path':
                assert tag['#text'] == '/search'

    def test_method(self):
        element = HttpRequest(method=Method.HEAD)
        rendered_doc = element.to_xml().replace('<hashTree />', '')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['HTTPSamplerProxy']['stringProp']:
            if tag['@name'] == 'HTTPSampler.method':
                assert tag['#text'] == 'HEAD'

    def test_protocol(self):
        element = HttpRequest(protocol=Protocol.FTP)
        rendered_doc = element.to_xml().replace('<hashTree />', '')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['HTTPSamplerProxy']['stringProp']:
            if tag['@name'] == 'HTTPSampler.protocol':
                assert tag['#text'] == 'ftp'

    def test_port(self):
        element = HttpRequest(port=123)
        rendered_doc = element.to_xml().replace('<hashTree />', '')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['HTTPSamplerProxy']['stringProp']:
            if tag['@name'] == 'HTTPSampler.port':
                assert tag['#text'] == '123'

    def test_port2(self):
        element = HttpRequest(port=None)
        rendered_doc = element.to_xml().replace('<hashTree />', '')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['HTTPSamplerProxy']['stringProp']:
            if tag['@name'] == 'HTTPSampler.port':
                assert '#text' not in tag.keys()

    def test_content_encoding(self):
        element = HttpRequest(content_encoding='utf-8')
        rendered_doc = element.to_xml().replace('<hashTree />', '')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['HTTPSamplerProxy']['stringProp']:
            if tag['@name'] == 'HTTPSampler.contentEncoding':
                assert tag['#text'] == 'utf-8'

    def test_auto_redirect(self):
        element = HttpRequest(auto_redirect=True)
        rendered_doc = element.to_xml().replace('<hashTree />', '')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['HTTPSamplerProxy']['boolProp']:
            if tag['@name'] == 'HTTPSampler.auto_redirects':
                assert tag['#text'] == 'true'

    def test_keep_alive(self):
        element = HttpRequest(keep_alive=False)
        rendered_doc = element.to_xml().replace('<hashTree />', '')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['HTTPSamplerProxy']['boolProp']:
            if tag['@name'] == 'HTTPSampler.use_keepalive':
                assert tag['#text'] == 'false'

    def test_do_multipart_post(self):
        element = HttpRequest(do_multipart_post=True)
        rendered_doc = element.to_xml().replace('<hashTree />', '')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['HTTPSamplerProxy']['boolProp']:
            if tag['@name'] == 'HTTPSampler.DO_MULTIPART_POST':
                assert tag['#text'] == 'true'

    def test_browser_comp_headers(self):
        element = HttpRequest(browser_comp_headers=True)
        rendered_doc = element.to_xml().replace('<hashTree />', '')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['HTTPSamplerProxy']['boolProp']:
            if tag['@name'] == 'HTTPSampler.BROWSER_COMPATIBLE_MULTIPART':
                assert tag['#text'] == 'true'

    def test_implementation(self):
        element = HttpRequest(implementation=Implement.JAVA)
        rendered_doc = element.to_xml().replace('<hashTree />', '')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['HTTPSamplerProxy']['stringProp']:
            if tag['@name'] == 'HTTPSampler.implementation':
                assert tag['#text'] == 'Java'

    def test_connect_timeout(self):
        element = HttpRequest(connect_timeout=123)
        rendered_doc = element.to_xml().replace('<hashTree />', '')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['HTTPSamplerProxy']['stringProp']:
            if tag['@name'] == 'HTTPSampler.connect_timeout':
                assert tag['#text'] == '123'

    def test_connect_timeout2(self):
        element = HttpRequest(connect_timeout=None)
        rendered_doc = element.to_xml().replace('<hashTree />', '')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['HTTPSamplerProxy']['stringProp']:
            if tag['@name'] == 'HTTPSampler.connect_timeout':
                assert '#text' not in tag.keys()

    def test_response_timeout(self):
        element = HttpRequest(response_timeout=321)
        rendered_doc = element.to_xml().replace('<hashTree />', '')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['HTTPSamplerProxy']['stringProp']:
            if tag['@name'] == 'HTTPSampler.response_timeout':
                assert tag['#text'] == '321'

    def test_response_timeout2(self):
        element = HttpRequest(response_timeout=None)
        rendered_doc = element.to_xml().replace('<hashTree />', '')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['HTTPSamplerProxy']['stringProp']:
            if tag['@name'] == 'HTTPSampler.response_timeout':
                assert '#text' not in tag.keys()

    def test_retrieve_all_emb_resources(self):
        element = HttpRequest(
            retrieve_all_emb_resources=True)
        rendered_doc = element.to_xml().replace('<hashTree />', '')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['HTTPSamplerProxy']['boolProp']:
            if tag['@name'] == 'HTTPSampler.image_parser':
                assert tag['#text'] == 'true'

    def test_parallel_downloads(self):
        element = HttpRequest(parallel_downloads=True)
        rendered_doc = element.to_xml().replace('<hashTree />', '')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['HTTPSamplerProxy']['boolProp']:
            if tag['@name'] == 'HTTPSampler.concurrentDwn':
                assert tag['#text'] == 'true'

    def test_parallel_downloads_no(self):
        element = HttpRequest(parallel_downloads_no=6)
        rendered_doc = element.to_xml().replace('<hashTree />', '')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['HTTPSamplerProxy']['stringProp']:
            if tag['@name'] == 'HTTPSampler.concurrentPool':
                assert tag['#text'] == '6'

    def test_parallel_downloads_no2(self):
        element = HttpRequest(parallel_downloads_no=None)
        rendered_doc = element.to_xml().replace('<hashTree />', '')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['HTTPSamplerProxy']['stringProp']:
            if tag['@name'] == 'HTTPSampler.concurrentPool':
                assert '#text' not in tag.keys()

    def test_url_must_match(self):
        element = HttpRequest(url_must_match='url_match')
        rendered_doc = element.to_xml().replace('<hashTree />', '')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['HTTPSamplerProxy']['stringProp']:
            if tag['@name'] == 'HTTPSampler.embedded_url_re':
                assert tag['#text'] == 'url_match'

    def test_source_type(self):
        element = HttpRequest(source_type=Source.IPV4)
        rendered_doc = element.to_xml().replace('<hashTree />', '')
        parsed_doc = xmltodict.parse(rendered_doc)
        assert parsed_doc['HTTPSamplerProxy']['intProp']['#text'] == '2'

    def test_source_address(self):
        element = HttpRequest(source_address='test_source')
        rendered_doc = element.to_xml().replace('<hashTree />', '')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['HTTPSamplerProxy']['stringProp']:
            if tag['@name'] == 'HTTPSampler.ipSource':
                assert tag['#text'] == 'test_source'

    def test_source_scheme(self):
        element = HttpRequest(proxy_scheme='test_scheme')
        rendered_doc = element.to_xml().replace('<hashTree />', '')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['HTTPSamplerProxy']['stringProp']:
            if tag['@name'] == 'HTTPSampler.proxyScheme':
                assert tag['#text'] == 'test_scheme'

    def test_proxy_host(self):
        element = HttpRequest(proxy_host='proxy_localhost')
        rendered_doc = element.to_xml().replace('<hashTree />', '')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['HTTPSamplerProxy']['stringProp']:
            if tag['@name'] == 'HTTPSampler.proxyHost':
                assert tag['#text'] == 'proxy_localhost'

    def test_proxy_port(self):
        element = HttpRequest(proxy_port=443)
        rendered_doc = element.to_xml().replace('<hashTree />', '')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['HTTPSamplerProxy']['stringProp']:
            if tag['@name'] == 'HTTPSampler.proxyPort':
                assert tag['#text'] == '443'

    def test_proxy_port2(self):
        element = HttpRequest(proxy_port=None)
        rendered_doc = element.to_xml().replace('<hashTree />', '')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['HTTPSamplerProxy']['stringProp']:
            if tag['@name'] == 'HTTPSampler.proxyPort':
                assert '#text' not in tag.keys()

    def test_proxy_username(self):
        element = HttpRequest(
            proxy_username='proxy_username')
        rendered_doc = element.to_xml().replace('<hashTree />', '')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['HTTPSamplerProxy']['stringProp']:
            if tag['@name'] == 'HTTPSampler.proxyUser':
                assert tag['#text'] == 'proxy_username'

    def test_proxy_password(self):
        element = HttpRequest(proxy_password='pass')
        rendered_doc = element.to_xml().replace('<hashTree />', '')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['HTTPSamplerProxy']['stringProp']:
            if tag['@name'] == 'HTTPSampler.proxyPass':
                assert tag['#text'] == 'pass'

    def test_hashtree_contain(self):
        element = HttpRequest(name='My http',
                              host='localhost',
                              path='/',
                              method=Method.POST,
                              comments='My comments',
                              is_enabled=False)
        rendered_doc = element.to_xml()
        assert '<hashTree />' in rendered_doc
