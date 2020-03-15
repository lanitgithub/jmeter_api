import xmltodict
import pytest

from jmeter_api.samplers.debug.elements import DebugSampler
from jmeter_api.basics.utils import tag_wrapper


class TestDebugSampler:
    class TestDisplayProps:
        def test_check(self):
            with pytest.raises(TypeError):
                DebugSampler(display_props="True")

        def test_check2(self):
            with pytest.raises(TypeError):
                DebugSampler(display_props="1")

        def test_positive(self):
            DebugSampler(display_props=True)
            
    class TestDisplayVars:
        def test_check(self):
            with pytest.raises(TypeError):
                DebugSampler(display_vars="True")

        def test_check2(self):
            with pytest.raises(TypeError):
                DebugSampler(display_vars="1")

        def test_positive(self):
            DebugSampler(display_vars=True)
                        
    class TestDisplaySysProps:
        def test_check(self):
            with pytest.raises(TypeError):
                DebugSampler(display_sys_props="True")

        def test_check2(self):
            with pytest.raises(TypeError):
                DebugSampler(display_sys_props="1")

        def test_positive(self):
            DebugSampler(display_sys_props=True)
    

class TestDebugSamplerRender:                
    def test_display_props(self):
        element = DebugSampler(display_props=True)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc,'test_result'))
        for tag in parsed_doc['test_result']['DebugSampler']['boolProp']:
            if tag['@name'] == 'displayJMeterProperties':
                assert tag['#text'] == 'true'
                
    def test_display_vars(self):
        element = DebugSampler(display_vars=False)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc,'test_result'))
        for tag in parsed_doc['test_result']['DebugSampler']['boolProp']:
            if tag['@name'] == 'displayJMeterVariables':
                assert tag['#text'] == 'false'
                
    def test_display_sys_props(self):
        element = DebugSampler(display_sys_props=True)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc,'test_result'))
        for tag in parsed_doc['test_result']['DebugSampler']['boolProp']:
            if tag['@name'] == 'displaySystemProperties':
                assert tag['#text'] == 'true'
                
    def test_hashtree_contain(self):
        element = DebugSampler()
        rendered_doc = element.to_xml()
        assert '<hashTree />' in rendered_doc
