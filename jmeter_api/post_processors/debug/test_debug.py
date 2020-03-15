import xmltodict
import pytest

from jmeter_api.post_processors.debug.elements import DebugPostProcessor
from jmeter_api.basics.utils import tag_wrapper


class TestDebugPostProcessor:
    class TestDisplayProps:
        def test_check(self):
            with pytest.raises(TypeError):
                DebugPostProcessor(display_props="True")

        def test_check2(self):
            with pytest.raises(TypeError):
                DebugPostProcessor(display_props="1")

        def test_positive(self):
            DebugPostProcessor(display_props=True)
            
    class TestDisplaySamplerProps:
        def test_check(self):
            with pytest.raises(TypeError):
                DebugPostProcessor(display_sampler_props="True")

        def test_check2(self):
            with pytest.raises(TypeError):
                DebugPostProcessor(display_sampler_props="1")

        def test_positive(self):
            DebugPostProcessor(display_sampler_props=True)
            
    class TestDisplayVars:
        def test_check(self):
            with pytest.raises(TypeError):
                DebugPostProcessor(display_vars="True")

        def test_check2(self):
            with pytest.raises(TypeError):
                DebugPostProcessor(display_vars="1")

        def test_positive(self):
            DebugPostProcessor(display_vars=True)
                        
    class TestDisplaySysProps:
        def test_check(self):
            with pytest.raises(TypeError):
                DebugPostProcessor(display_sys_props="True")

        def test_check2(self):
            with pytest.raises(TypeError):
                DebugPostProcessor(display_sys_props="1")

        def test_positive(self):
            DebugPostProcessor(display_sys_props=True)
    

class TestDebugPostProcessorRender:                
    def test_display_props(self):
        element = DebugPostProcessor(display_props=True)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc,'test_result'))
        for tag in parsed_doc['test_result']['DebugPostProcessor']['boolProp']:
            if tag['@name'] == 'displayJMeterProperties':
                assert tag['#text'] == 'true'
                
    def test_display_vars(self):
        element = DebugPostProcessor(display_vars=False)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc,'test_result'))
        for tag in parsed_doc['test_result']['DebugPostProcessor']['boolProp']:
            if tag['@name'] == 'displayJMeterVariables':
                assert tag['#text'] == 'false'
                
    def test_display_sampler_props(self):
        element = DebugPostProcessor(display_sampler_props=False)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc,'test_result'))
        for tag in parsed_doc['test_result']['DebugPostProcessor']['boolProp']:
            if tag['@name'] == 'displaySamplerProperties':
                assert tag['#text'] == 'false'
                
    def test_display_sys_props(self):
        element = DebugPostProcessor(display_sys_props=True)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc,'test_result'))
        for tag in parsed_doc['test_result']['DebugPostProcessor']['boolProp']:
            if tag['@name'] == 'displaySystemProperties':
                assert tag['#text'] == 'true'
                
    def test_hashtree_contain(self):
        element = DebugPostProcessor()
        rendered_doc = element.to_xml()
        assert '<hashTree />' in rendered_doc
