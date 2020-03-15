import re
import xmltodict

from jmeter_api.configs.http_cache_manager.elements import HTTPCacheManager
from jmeter_api.thread_groups.common_thread_group.elements import CommonThreadGroup
from jmeter_api.basics.utils import tag_wrapper


class TestUtils:
    def test_tag_wrapper(self):
        wrapped_data = tag_wrapper('<a>testdata</a>', 'test_wrapper')
        parsed_data = xmltodict.parse(wrapped_data)
        assert parsed_data['test_wrapper']['a'] == 'testdata'

    def test_includes_elements_get_size(self):
        thread_group = CommonThreadGroup(continue_forever=True)
        elements_list = [HTTPCacheManager(), 
                         HTTPCacheManager(),
                         HTTPCacheManager()]
        for element in elements_list:
            thread_group.append(element)
        assert len(thread_group) == 3

    def test_includes_elements_test_render(self):
        thread_group = CommonThreadGroup(continue_forever=True)
        elements_list = [HTTPCacheManager(), 
                         HTTPCacheManager(),
                         HTTPCacheManager()]
        for element in elements_list:
            thread_group.append(element)
        xml_data = thread_group._render_inner_elements()
        assert len(re.findall('element_type', xml_data)) == 3

    def test_check_forbidden_symbols(self):
        thread_group = CommonThreadGroup(continue_forever=True)
        elements_list = [HTTPCacheManager(), 
                         HTTPCacheManager(),
                         HTTPCacheManager()]
        for element in elements_list:
            thread_group.append(element)
        xml_data = thread_group._render_inner_elements()
        assert "&lt;" not in xml_data
        assert "&gt;" not in xml_data
