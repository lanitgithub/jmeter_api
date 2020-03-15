import xmltodict
import pytest

from jmeter_api.configs.user_defined_variables.elements import Argument, UserDefineVariables
from jmeter_api.basics.utils import tag_wrapper


class TestArgument:
    class TestName:
        def test_type_check(self):
            with pytest.raises(TypeError):
                Argument(name=123, value='1')

        def test_positive(self):
            Argument(name='var', value='1')
            
    class TestValue:
        def test_type_check(self):
            with pytest.raises(TypeError):
                Argument(name='var', value=1)

        def test_positive(self):
            Argument(name='var', value='1')

    class TestDesc:
        def test_type_check(self):
            with pytest.raises(TypeError):
                Argument(name='var', value='1', desc=1)

        def test_positive(self):
            Argument(name='var', value='1', desc='1')

    class TestMetadata:
        def test_type_check(self):
            with pytest.raises(TypeError):
                Argument(name='var', value='1', metadata=1)

        def test_positive(self):
            Argument(name='var', value='1', metadata='1')


class TestArgumentRender:
    def test_name(self):
        element = Argument(name='var', value='1')
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        assert parsed_doc['result']['elementProp']['@name'] == 'var'

    def test_name2(self):
        element = Argument(name='var', value='1')
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['result']['elementProp']['stringProp']:
            if tag['@name'] == 'Argument.name':
                assert tag['#text'] == 'var'

    def test_value(self):
        element = Argument(name='var', value='1')
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['result']['elementProp']['stringProp']:
            if tag['@name'] == 'Argument.value':
                assert tag['#text'] == '1'
                
    def test_description(self):
        element = Argument(name='var', value='1', desc='description')
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['result']['elementProp']['stringProp']:
            if tag['@name'] == 'Argument.desc':
                assert tag['#text'] == 'description'

    def test_metadata(self):
        element = Argument(name='var', value='1', metadata='+')
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['result']['elementProp']['stringProp']:
            if tag['@name'] == 'Argument.metadata':
                assert tag['#text'] == '+'
                

class TestUserDefineVariables:
    class TestArguments:
        def test_type_check(self):
            with pytest.raises(TypeError):
                UserDefineVariables(arguments=123)

        def test_type_check2(self):
            with pytest.raises(TypeError):
                UserDefineVariables(arguments='123')

        def test_type_check3(self):
            with pytest.raises(TypeError):
                UserDefineVariables(arguments=Argument(name='var', value='12'))
                
        def test_type_check4(self):
            with pytest.raises(TypeError):
                UserDefineVariables(arguments=['12', '23'])
                
        def test_type_check5(self):
            with pytest.raises(TypeError):
                UserDefineVariables(arguments=[Argument(name='var', value='12'), '23'])
                
        def test_type_check6(self):
            with pytest.raises(TypeError):
                UserDefineVariables(arguments=[{'var': '12'}, {'var2': '22'}])

        def test_positive(self):
            UserDefineVariables()

        def test_positive1(self):
            UserDefineVariables(arguments=[Argument(name='var', value='12'),\
                                            Argument(name='var2', value='22')])
            

class TestUserDefineVariablesRender:
    def test_argument(self):
        element = UserDefineVariables(arguments=[Argument(name='var', value='12'),\
                                                Argument(name='var2', value='22')])
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['result']['Arguments']['collectionProp']['elementProp']:
            if tag['@name'] == 'var':
                assert tag['stringProp'][0]['#text'] == 'var'
                assert tag['stringProp'][1]['#text'] == '12'

    def test_empty(self):
        element = UserDefineVariables()
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        assert not 'elementProp' in parsed_doc['result']['Arguments']['collectionProp']
                
    def test_hashtree_contain(self):
        element = UserDefineVariables(arguments=[Argument(name='var', value='12'),\
                                                Argument(name='var2', value='22')])
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        assert '<hashTree />' in rendered_doc
