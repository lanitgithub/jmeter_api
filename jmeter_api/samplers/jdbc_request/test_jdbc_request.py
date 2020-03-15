import pytest
import xmltodict

from jmeter_api.samplers.jdbc_request.elements import JdbcRequest, ResultSetHandler, QueryType


class TestJdbcRequestArgsTypes:

    def test_name(self):
        with pytest.raises(TypeError):
            JdbcRequest(name=123)

    def test_comments(self):
        with pytest.raises(TypeError):
            JdbcRequest(comments=123)

    def test_data_source(self):
        with pytest.raises(TypeError):
            JdbcRequest(data_source=123)

    def test_query_type(self):
        with pytest.raises(TypeError):
            JdbcRequest(query_type=123)

    def test_query(self):
        with pytest.raises(TypeError):
            JdbcRequest(query=123)

    def test_parameter_values1(self):
        with pytest.raises(TypeError):
            JdbcRequest(parameter_values=123)

    def test_parameter_values2(self):
        with pytest.raises(TypeError):
            JdbcRequest(parameter_values='123')

    def test_parameter_types1(self):
        with pytest.raises(TypeError):
            JdbcRequest(parameter_types=123)

    def test_parameter_types2(self):
        with pytest.raises(TypeError):
            JdbcRequest(parameter_types='123')

    def test_variable_names(self):
        with pytest.raises(TypeError):
            JdbcRequest(variable_names=123)

    def test_result_variable_name(self):
        with pytest.raises(TypeError):
            JdbcRequest(result_variable_name=123)

    def test_query_timeout1(self):
        with pytest.raises(ValueError):
            JdbcRequest(query_timeout=-1)

    def test_query_timeout2(self):
        with pytest.raises(TypeError):
            JdbcRequest(query_timeout='123')

    def test_handle_result_set1(self):
        with pytest.raises(TypeError):
            JdbcRequest(handle_result_set='123')

    def test_handle_result_set2(self):
        with pytest.raises(TypeError):
            JdbcRequest(handle_result_set=1)

    def test_is_enabled(self):
        with pytest.raises(TypeError):
            JdbcRequest(is_enabled=None)


class TestJdbcRequestRender:
    def test_name(self):
        element = JdbcRequest(name='jdbc')
        rendered_doc = element.to_xml().replace('<hashTree />', '')
        parsed_doc = xmltodict.parse(rendered_doc)
        assert parsed_doc['JDBCSampler']['@testname'] == 'jdbc'

    def test_is_enabled(self):
        element = JdbcRequest(is_enabled=False)
        rendered_doc = element.to_xml().replace('<hashTree />', '')
        parsed_doc = xmltodict.parse(rendered_doc)
        assert parsed_doc['JDBCSampler']['@enabled'] == 'false'

    def test_data_source(self):
        element = JdbcRequest(data_source='data source test')
        rendered_doc = element.to_xml().replace('<hashTree />', '')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['JDBCSampler']['stringProp']:
            if tag['@name'] == 'dataSource':
                assert tag['#text'] == 'data source test'

    def test_query_type(self):
        element = JdbcRequest(query_type=QueryType.AUTOCOMMIT)
        rendered_doc = element.to_xml().replace('<hashTree />', '')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['JDBCSampler']['stringProp']:
            if tag['@name'] == 'queryType':
                assert tag['#text'] == 'AutoCommit(false)'

    def test_query(self):
        q = """
        select * from table
        where col = '1'""".strip()
        element = JdbcRequest(query=q)
        rendered_doc = element.to_xml().replace('<hashTree />', '')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['JDBCSampler']['stringProp']:
            if tag['@name'] == 'query':
                assert tag['#text'] == q

    def test_parameter_values(self):
        element = JdbcRequest(parameter_values=['param-1', 'param-2'])
        rendered_doc = element.to_xml().replace('<hashTree />', '')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['JDBCSampler']['stringProp']:
            if tag['@name'] == 'queryArguments':
                assert tag['#text'] == '${param-1},${param-2}'

    def test_parameter_types(self):
        element = JdbcRequest(parameter_types=['varchar ', '    INTEGER'])
        rendered_doc = element.to_xml().replace('<hashTree />', '')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['JDBCSampler']['stringProp']:
            if tag['@name'] == 'queryArgumentsTypes':
                assert tag['#text'] == 'VARCHAR,INTEGER'

    def test_variable_names(self):
        element = JdbcRequest(variable_names='var name')
        rendered_doc = element.to_xml().replace('<hashTree />', '')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['JDBCSampler']['stringProp']:
            if tag['@name'] == 'variableNames':
                assert tag['#text'] == 'var name'

    def test_result_variable_name(self):
        element = JdbcRequest(result_variable_name='var name')
        rendered_doc = element.to_xml().replace('<hashTree />', '')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['JDBCSampler']['stringProp']:
            if tag['@name'] == 'resultVariable':
                assert tag['#text'] == 'var name'

    def test_query_timeout(self):
        element = JdbcRequest(query_timeout=500)
        rendered_doc = element.to_xml().replace('<hashTree />', '')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['JDBCSampler']['stringProp']:
            if tag['@name'] == 'queryTimeout':
                assert tag['#text'] == '500'

    def test_handle_result_set(self):
        element = JdbcRequest(handle_result_set=ResultSetHandler.COUNT_RECORDS)
        rendered_doc = element.to_xml().replace('<hashTree />', '')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['JDBCSampler']['stringProp']:
            if tag['@name'] == 'resultSetHandler':
                assert tag['#text'] == 'Count Records'

    def test_hashtree_contain(self):
        element = JdbcRequest(name='Jdbc',
                              handle_result_set=ResultSetHandler.COUNT_RECORDS,
                              query_timeout=20
                              )
        rendered_doc = element.to_xml()
        assert '<hashTree />' in rendered_doc

