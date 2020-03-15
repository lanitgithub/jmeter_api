import xmltodict
import pytest

from jmeter_api.configs.random_variable.elements import RandomVariable
from jmeter_api.basics.utils import tag_wrapper


class TestRandomVariable:
    class TestVariableName:
        def test_type_check(self):
            with pytest.raises(TypeError):
                RandomVariable(variable_name=123)

        def test_positive(self):
            RandomVariable(variable_name="var")
            
    class TestFormat:
        def test_type_check(self):
            with pytest.raises(TypeError):
                RandomVariable(variable_name="var", output_format=123)

        def test_positive(self):
            RandomVariable(variable_name="var", output_format="user")
            
    class TestMin:
        def test_type_check(self):
            with pytest.raises(TypeError):
                RandomVariable(variable_name="var", minimum_value="1")

        def test_positive(self):
            RandomVariable(variable_name="var", minimum_value=1)
            
    class TestMax:
        def test_type_check(self):
            with pytest.raises(TypeError):
                RandomVariable(variable_name="var", maximum_value="1")
                
        def test_type_check2(self):
            with pytest.raises(ValueError):
                RandomVariable(variable_name="var", minimum_value=2, maximum_value=1)

        def test_positive(self):
            RandomVariable(variable_name="var", maximum_value=1)
            
    class TestSeed:
        def test_type_check(self):
            with pytest.raises(TypeError):
                RandomVariable(variable_name="var", random_seed="1")

        def test_positive(self):
            RandomVariable(variable_name="var", random_seed=10)

    class TestPerThread:
        def test_type_check(self):
            with pytest.raises(TypeError):
                RandomVariable(variable_name="var", per_thread="True")
                
        def test_type_check1(self):
            with pytest.raises(TypeError):
                RandomVariable(variable_name="var", per_thread=1)

        def test_positive(self):
            RandomVariable(variable_name="var", per_thread=True)


class TestCsvDataSetConfigRender:
    def test_variable_name(self):
        element = RandomVariable(variable_name="var")
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['result']['RandomVariableConfig']['stringProp']:
            if tag['@name'] == 'CounterConfig.variable_name':
                assert tag['#text'] == 'var'

    def test_format(self):
        element = RandomVariable(variable_name="var", output_format="user")
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['result']['RandomVariableConfig']['stringProp']:
            if tag['@name'] == 'outputFormat':
                assert tag['#text'] == "user"
                
    def test_min(self):
        element = RandomVariable(variable_name="var", minimum_value=1)
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['result']['RandomVariableConfig']['stringProp']:
            if tag['@name'] == 'minimumValue':
                assert tag['#text'] == '1'
                
    def test_max(self):
        element = RandomVariable(variable_name="var", maximum_value=3)
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['result']['RandomVariableConfig']['stringProp']:
            if tag['@name'] == 'maximumValue':
                assert tag['#text'] == '3'
                
    def test_seed(self):
        element = RandomVariable(variable_name="var", random_seed=2)
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['result']['RandomVariableConfig']['stringProp']:
            if tag['@name'] == 'randomSeed':
                assert tag['#text'] == '2'

    def test_per_thread(self):
        element = RandomVariable(variable_name="var", per_thread=True)
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        assert parsed_doc['result']['RandomVariableConfig']['boolProp']['#text'] == 'true'
                
    def test_hashtree_contain(self):
        element = RandomVariable(variable_name="var")
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        assert '<hashTree />' in rendered_doc
