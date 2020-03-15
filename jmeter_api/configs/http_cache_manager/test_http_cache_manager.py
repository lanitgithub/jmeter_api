import xmltodict
import pytest

from jmeter_api.configs.http_cache_manager.elements import HTTPCacheManager
from jmeter_api.basics.utils import tag_wrapper


class TestHTTPCacheManagerArgs:
    class TestClearCacheEachIteration:
        def test_check(self):
            with pytest.raises(TypeError):
                HTTPCacheManager(clear_each_iteration="False")

        def test_check2(self):
            with pytest.raises(TypeError):
                HTTPCacheManager(clear_each_iteration=123456)

        def test_positive(self):
            cache_manager = HTTPCacheManager(clear_each_iteration=True)
            assert cache_manager.clear_each_iteration is True

    class TestUseCacheControl:
        def test_check(self):
            with pytest.raises(TypeError):
                HTTPCacheManager(use_cache_control="False")

        def test_check2(self):
            with pytest.raises(TypeError):
                HTTPCacheManager(use_cache_control=12345)

        def test_positive(self):
            cache_manager = HTTPCacheManager(use_cache_control=False)
            assert cache_manager.use_cache_control is False

    class TestMaxElementsInCache:
        def test_check(self):
            with pytest.raises(TypeError):
                HTTPCacheManager(max_elements_in_cache="test")

        def test_check2(self):
            with pytest.raises(TypeError):
                HTTPCacheManager(max_elements_in_cache="120")

        def test_positive(self):
            cache_manager = HTTPCacheManager(max_elements_in_cache=100)
            assert cache_manager.max_elements_in_cache == 100


class TestHTTPCacheManagerRender:

    def test_clear_each_iteration(self):
        element = HTTPCacheManager(clear_each_iteration=False,
                                   use_cache_control=True,
                                   max_elements_in_cache=100)
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        assert parsed_doc['result']['CacheManager']['boolProp'][0]['#text'] == 'false'

    def test_use_cache_control(self):
        element = HTTPCacheManager(clear_each_iteration=False,
                                   use_cache_control=True,
                                   max_elements_in_cache=100)
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        assert parsed_doc['result']['CacheManager']['boolProp'][1]['#text'] == 'true'

    def test_max_elements_in_cache(self):
        element = HTTPCacheManager(clear_each_iteration=False,
                                   use_cache_control=True,
                                   max_elements_in_cache=100)
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        assert parsed_doc['result']['CacheManager']['intProp']['#text'] == '100'
