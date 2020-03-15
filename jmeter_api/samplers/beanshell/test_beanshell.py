from jmeter_api.samplers.beanshell.elements import BeanShell
from jmeter_api.basics.utils import tag_wrapper
import xmltodict
import pytest

class TestBeanShell:
    class TestResetInterpreter:
        def test_check(self):
            with pytest.raises(TypeError):
                BeanShell(resetInterpreter="True")

        def test_check2(self):
            with pytest.raises(TypeError):
                BeanShell(resetInterpreter=1)

        def test_positive(self):
            BeanShell(resetInterpreter=True)

    class TestFilename:
        def test_check(self):
            with pytest.raises(TypeError):
                BeanShell(filename=1)

        def test_check2(self):
            with pytest.raises(OSError):
                BeanShell(filename="notExestingFile")

        def test_check3(self):
            with pytest.raises(ValueError):
                BeanShell(filename="./jmeter_api/samplers/beanshell/elements.py")

        def test_positive(self):
            BeanShell(filename="./jmeter_api/samplers/beanshell/beanshell_test.bsh")

    class TestQuery:
        def test_check(self):
            with pytest.raises(TypeError):
                BeanShell(query=1)
                
        def test_check2(self):
            with pytest.raises(TypeError):
                BeanShell(query=False)

        def test_positive(self):
            BeanShell(query="var a=0")
            
    class TestParameters:
        def test_check(self):
            with pytest.raises(TypeError):
                BeanShell(parameters=1)
                
        def test_check2(self):
            with pytest.raises(TypeError):
                BeanShell(parameters=False)

        def test_positive(self):
            BeanShell(parameters="some parameters")
            
class TestBeanShellRender:                
    def test_resetInterpreter(self):
        element = BeanShell(resetInterpreter=True)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc,'test_result'))
        assert parsed_doc['test_result']['BeanShellSampler']['boolProp']['#text'] == 'true'
                
    def test_fileName(self):
        element = BeanShell(filename="./jmeter_api/samplers/beanshell/beanshell_test.bsh")
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc,'test_result'))
        for tag in parsed_doc['test_result']['BeanShellSampler']['stringProp']:
            if tag['@name'] == 'filename':
                assert tag['#text'] == "./jmeter_api/samplers/beanshell/beanshell_test.bsh"

    def test_query(self):
        sc = """var a=2
vars.put("some value",a)
log("value added")"""
        element = BeanShell(query=sc)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc,'test_result'))
        for tag in parsed_doc['test_result']['BeanShellSampler']['stringProp']:
            if tag['@name'] == 'query':
                assert tag['#text'] == sc
                
    def test_hashtree_contain(self):
        element = BeanShell()
        rendered_doc = element.to_xml()
        assert '<hashTree />' in rendered_doc
