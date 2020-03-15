import xmltodict
import pytest

from jmeter_api.configs.counter.elements import Counter
from jmeter_api.basics.utils import tag_wrapper


class TestCounter:
    class TestVariableName:
        def test_type_check(self):
            with pytest.raises(TypeError):
                Counter(variable_name=123)

        def test_positive(self):
            Counter(variable_name="var")
            
    class TestFormat:
        def test_type_check(self):
            with pytest.raises(TypeError):
                Counter(variable_name="var", format_=123)

        def test_positive(self):
            Counter(variable_name="var", format_="user")
            
    class TestStart:
        def test_type_check(self):
            with pytest.raises(TypeError):
                Counter(variable_name="var", start="1")
                
        def test_type_check1(self):
            with pytest.raises(TypeError):
                Counter(variable_name="var", start=-1)

        def test_positive(self):
            Counter(variable_name="var", start=1)
            
    class TestEnd:
        def test_type_check(self):
            with pytest.raises(TypeError):
                Counter(variable_name="var", end="1")
                
        def test_type_check1(self):
            with pytest.raises(TypeError):
                Counter(variable_name="var", end=-1)
                
        def test_type_check2(self):
            with pytest.raises(ValueError):
                Counter(variable_name="var", start=2, end=1)

        def test_positive(self):
            Counter(variable_name="var", end=1)
            
    class TestIncrement:
        def test_type_check(self):
            with pytest.raises(TypeError):
                Counter(variable_name="var", incr="1")
                
        def test_type_check1(self):
            with pytest.raises(TypeError):
                Counter(variable_name="var", incr=0)

        def test_positive(self):
            Counter(variable_name="var", incr=10)

    class TestPerUser:
        def test_type_check(self):
            with pytest.raises(TypeError):
                Counter(variable_name="var", per_user="True")
                
        def test_type_check1(self):
            with pytest.raises(TypeError):
                Counter(variable_name="var", per_user=1)

        def test_positive(self):
            Counter(variable_name="var", per_user=True)

    class TestReset:
        def test_type_check(self):
            with pytest.raises(ValueError):
                Counter(variable_name="var", reset_on_tg_iteration=True)
                
        def test_type_check1(self):
            with pytest.raises(TypeError):
                Counter(variable_name="var", per_user=True, reset_on_tg_iteration=1)
                
        def test_type_check1(self):
            with pytest.raises(TypeError):
                Counter(variable_name="var", per_user=True, reset_on_tg_iteration="True")

        def test_positive(self):
            Counter(variable_name="var", per_user=True, reset_on_tg_iteration=True)


class TestCounterRender:
    def test_variable_name(self):
        element = Counter(variable_name="var")
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['result']['CounterConfig']['stringProp']:
            if tag['@name'] == 'CounterConfig.variable_name':
                assert tag['#text'] == 'var'

    def test_format(self):
        element = Counter(variable_name="var", format_="user")
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['result']['CounterConfig']['stringProp']:
            if tag['@name'] == 'CounterConfig.format':
                assert tag['#text'] == "user"
                
    def test_start(self):
        element = Counter(variable_name="var", start=1)
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['result']['CounterConfig']['stringProp']:
            if tag['@name'] == 'CounterConfig.start':
                assert tag['#text'] == '1'
                
    def test_end(self):
        element = Counter(variable_name="var", end=3)
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['result']['CounterConfig']['stringProp']:
            if tag['@name'] == 'CounterConfig.end':
                assert tag['#text'] == '3'
                
    def test_incr(self):
        element = Counter(variable_name="var", incr=2)
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['result']['CounterConfig']['stringProp']:
            if tag['@name'] == 'CounterConfig.incr':
                assert tag['#text'] == '2'

    def test_per_user(self):
        element = Counter(variable_name="var", per_user=True)
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        assert parsed_doc['result']['CounterConfig']['boolProp']['#text'] == 'true'
                
    def test_reset(self):
        element = Counter(variable_name="var", per_user=True, reset_on_tg_iteration=True)
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        
        for tag in parsed_doc['result']['CounterConfig']['boolProp']:
            if tag['@name'] == 'CounterConfig.reset_on_tg_iteration':
                assert tag['#text'] == 'true'
                
    def test_hashtree_contain(self):
        element = Counter(variable_name="var")
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        assert '<hashTree />' in rendered_doc
