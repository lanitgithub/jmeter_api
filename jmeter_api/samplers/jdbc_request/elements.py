import logging

from enum import Enum
from typing import Union, List

from jmeter_api.basics.sampler.elements import BasicSampler
from jmeter_api.basics.utils import IncludesElements, Renderable, tree_to_str


class QueryType(Enum):
    SELECT_STATEMENT = 'Select Statement'
    UPDATE_STATEMENT = 'Update Statement'
    CALLABLE_STATEMENT = 'Callable Statement'
    PREPARED_SELECT_STATEMENT = 'Prepared Select Statement'
    PREPARED_UPDATE_STATEMENT = 'Prepared Update Statement'
    COMMIT = 'Commit'
    ROLLBACK = 'Rollback'
    AUTOCOMMIT = 'AutoCommit(false)'


class ResultSetHandler(Enum):
    STORE_AS_STRING = 'Store as String'
    STORE_AS_OBJECT = 'Store as Object'
    COUNT_RECORDS = 'Count Records'
    EDIT = '${}'


class JdbcRequest(BasicSampler, Renderable):

    root_element_name = 'JDBCSampler'

    def __init__(self,
                 name: str = 'JDBC Request',
                 data_source: str = '',
                 query_type: QueryType = QueryType.SELECT_STATEMENT,
                 query: str = '',
                 parameter_values: Union[List[str], None] = None,
                 parameter_types: Union[List[str], None] = None,
                 variable_names: str = '',
                 result_variable_name: str = '',
                 query_timeout: Union[int, None] = None,
                 handle_result_set: ResultSetHandler = ResultSetHandler.STORE_AS_STRING,
                 comments: str = '',
                 is_enabled: bool = True
                 ):
        BasicSampler.__init__(self, name=name, comments=comments, is_enabled=is_enabled)
        self.handle_result_set = handle_result_set
        self.result_variable_name = result_variable_name
        self.variable_names = variable_names
        self.parameter_types = parameter_types
        self.parameter_values = parameter_values
        self.query_timeout = query_timeout
        self.query = query
        self.query_type = query_type
        self.data_source = data_source

    @property
    def data_source(self) -> str:
        return self._data_source

    @data_source.setter
    def data_source(self, value) -> None:
        if not isinstance(value, str):
            raise TypeError(f'arg: data_source should be str. {type(value).__name__} was given')
        self._data_source = value

    @property
    def query_type(self) -> QueryType:
        return self._query_type

    @query_type.setter
    def query_type(self, value) -> None:
        if not isinstance(value, QueryType):
            raise TypeError(f'arg: query_type should be QueryType. {type(value).__name__} was given')
        self._query_type = value

    @property
    def query(self) -> str:
        return self._query

    @query.setter
    def query(self, value) -> None:
        if not isinstance(value, str):
            raise TypeError(f'arg: query should be str. {type(value).__name__} was given')
        self._query = value

    @property
    def query_timeout(self) -> Union[int, None]:
        return self._query_timeout

    @query_timeout.setter
    def query_timeout(self, value) -> None:
        if value is not None and not isinstance(value, int):
            raise TypeError(f'arg: query_timeout should be int. {type(value).__name__} was given')
        if value is not None and value < 0:
            raise ValueError(f'arg: query_timeout should be positive.')
        self._query_timeout = value

    @property
    def parameter_values(self) -> Union[List[str], None]:
        return self._parameter_values

    @parameter_values.setter
    def parameter_values(self, value) -> None:
        if value is not None and not isinstance(value, List):
            raise TypeError(f'arg: parameter_values should be str. {type(value).__name__} was given')
        self._parameter_values = value

    @property
    def parameter_types(self) -> Union[List[str], None]:
        return self._parameter_types

    @parameter_types.setter
    def parameter_types(self, value) -> None:
        if value is not None and not isinstance(value, List):
            raise TypeError(f'arg: parameter_types should be str. {type(value).__name__} was given')
        self._parameter_types = value

    @property
    def variable_names(self) -> str:
        return self._variable_names

    @variable_names.setter
    def variable_names(self, value) -> None:
        if not isinstance(value, str):
            raise TypeError(f'arg: variable_names should be str. {type(value).__name__} was given')
        self._variable_names = value

    @property
    def result_variable_name(self) -> str:
        return self._result_variable_name

    @result_variable_name.setter
    def result_variable_name(self, value) -> None:
        if not isinstance(value, str):
            raise TypeError(f'arg: result_variable_name should be str. {type(value).__name__} was given')
        self._result_variable_name = value

    @property
    def handle_result_set(self) -> ResultSetHandler:
        return self._handle_result_set

    @handle_result_set.setter
    def handle_result_set(self, value) -> None:
        if not isinstance(value, ResultSetHandler):
            raise TypeError(f'arg: handle_result_set should be ResultSetHandler. {type(value).__name__} was given')
        self._handle_result_set = value

    def to_xml(self) -> str:
        element_root, xml_tree = super()._add_basics()
        for element in list(element_root):
            try:
                if element.attrib['name'] == 'dataSource':
                    element.text = self.data_source
                elif element.attrib['name'] == 'queryType':
                    element.text = self.query_type.value
                elif element.attrib['name'] == 'query':
                    element.text = self.query
                elif element.attrib['name'] == 'queryArguments':
                    if self.parameter_values is not None:
                        element.text = ','.join(['${%s}' % i for i in self.parameter_values])
                    else:
                        element.text = self.parameter_values
                elif element.attrib['name'] == 'queryArgumentsTypes':
                    if self.parameter_types is not None:
                        element.text = ','.join(list(map(lambda x: x.upper().strip(), self.parameter_types)))
                    else:
                        element.text = ''
                elif element.attrib['name'] == 'variableNames':
                    element.text = self.variable_names
                elif element.attrib['name'] == 'resultVariable':
                    element.text = self.result_variable_name
                elif element.attrib['name'] == 'queryTimeout':
                    if self.query_timeout is not None:
                        element.text = str(self.query_timeout)
                    else:
                        element.text = ''
                elif element.attrib['name'] == 'resultSetHandler':
                    element.text = self.handle_result_set.value
            except KeyError:
                logging.error('Unable to set xml parameters')

        if len(self) == 1:
            content_root = xml_tree.find('hashTree')
            content_root.text = self._render_inner_elements().replace('<hashTree />', '')
        elif len(self) > 1:
            content_root = xml_tree.find('hashTree')
            content_root.text = self._render_inner_elements()
        return tree_to_str(xml_tree)

