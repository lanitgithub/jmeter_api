import xmltodict
import pytest

from jmeter_api.configs.random_csv_data_set_config.elements import RandomCsvDataSetConfig
from jmeter_api.basics.utils import FileEncoding, tag_wrapper

file = './jmeter_api/configs/random_csv_data_set_config/random_csv_data_set_config_test.csv'


class TestRandomCsvDataSetConfigArgs:
    class TestFilename:
        def test_type_check(self):
            with pytest.raises(FileNotFoundError, match=r".*is not file*"):
                RandomCsvDataSetConfig(filename='ErrorPath',
                                    variable_names=['var1', 'var2'])

        def test_type_check2(self):
            with pytest.raises(FileNotFoundError, match=r".*is not file*"):
                RandomCsvDataSetConfig(filename='./ErrorPath',
                                    variable_names=['var1', 'var2'])

        def test_positive(self):
            csvdata = RandomCsvDataSetConfig(filename=file,
                                           variable_names=['var1', 'var2'])
            assert csvdata.filename == file

    class TestVariableNames:
        def test_type_check(self):
            with pytest.raises(TypeError, match=r".*variable_names must be List[str]*"):
                RandomCsvDataSetConfig(filename=file,
                                    variable_names={'randkey': 'randvalue'})

        def test_content_type_check(self):
            with pytest.raises(TypeError, match=r".*All elements must be str*"):
                RandomCsvDataSetConfig(filename=file,
                                    variable_names=['asdfg', 123, 'qwerty'])

        def test_content_type_check2(self):
            with pytest.raises(TypeError, match=r".*must contain chars*"):
                RandomCsvDataSetConfig(filename=file,
                                    variable_names=['asdfg', '123', 'qwerty'])

        def test_positive(self):
            csvdata = RandomCsvDataSetConfig(filename=file,
                                           variable_names=['asdfg', 'vbn', 'qwerty'])
            assert csvdata.variable_names == 'asdfg,vbn,qwerty'

    class TestDelimiter:
        def test_positive(self):
            csvdata = RandomCsvDataSetConfig(filename=file,
                                           variable_names=['asdfg', 'vbn', 'qwerty'],
                                           delimiter='|')
            assert csvdata.variable_names == 'asdfg|vbn|qwerty'

    class TestFileEncoding:
        def test_type_check(self):
            with pytest.raises(TypeError, match=r".*must be FileEncoding*"):
                RandomCsvDataSetConfig(filename=file,
                                    variable_names=['var1', 'var2'],
                                    file_encoding='UTF-8')

        def test_type_check2(self):
            with pytest.raises(TypeError, match=r".*must be FileEncoding*"):
                RandomCsvDataSetConfig(filename=file,
                                    variable_names=['var1', 'var2'],
                                    file_encoding=100)

        def test_positive(self):
            csvdata = RandomCsvDataSetConfig(filename=file,
                                           variable_names=['var1', 'var2'],
                                           file_encoding=FileEncoding.ISO8859)
            assert csvdata.file_encoding == FileEncoding.ISO8859

    class TestIgnoreFirstLine:
        def test_type_check(self):
            with pytest.raises(TypeError, match=r".*must be bool.*"):
                RandomCsvDataSetConfig(filename=file,
                                 variable_names=['var1', 'var2'],
                                 ignore_first_line='True')

        def test_type_check2(self):
            with pytest.raises(TypeError, match=r".*must be bool.*"):
                RandomCsvDataSetConfig(filename=file,
                                 variable_names=['var1', 'var2'],
                                 ignore_first_line=123456)

        def test_positive(self):
            csvdata = RandomCsvDataSetConfig(filename=file,
                                       variable_names=['var1', 'var2'],
                                       ignore_first_line=True)
            assert csvdata.ignore_first_line == True

    class TestRecycle:
        def test_type_check(self):
            with pytest.raises(TypeError, match=r".*must be bool.*"):
                RandomCsvDataSetConfig(filename=file,
                                        variable_names=['var1', 'var2'],
                                        recycle='True')

        def test_type_check2(self):
            with pytest.raises(TypeError, match=r".*must be bool.*"):
                RandomCsvDataSetConfig(filename=file,
                                        variable_names=['var1', 'var2'],
                                        recycle=123456)

        def test_positive(self):
            csvdata = RandomCsvDataSetConfig(filename=file,
                                       variable_names=['var1', 'var2'],
                                       recycle=True)
            assert csvdata.recycle == True

    class TestRandomOrder:
        def test_type_check(self):
            with pytest.raises(TypeError, match=r".*must be bool.*"):
                RandomCsvDataSetConfig(filename=file,
                                        variable_names=['var1', 'var2'],
                                        random_order='True')

        def test_type_check2(self):
            with pytest.raises(TypeError, match=r".*must be bool.*"):
                RandomCsvDataSetConfig(filename=file,
                                        variable_names=['var1', 'var2'],
                                        random_order=123456)

        def test_positive(self):
            csvdata = RandomCsvDataSetConfig(filename=file,
                                            variable_names=['var1', 'var2'],
                                            random_order=True)
            assert csvdata.random_order == True
            
    class TestIndependent:
        def test_type_check(self):
            with pytest.raises(TypeError, match=r".*must be bool.*"):
                RandomCsvDataSetConfig(filename=file,
                                        variable_names=['var1', 'var2'],
                                        independent_per_thread='True')

        def test_type_check2(self):
            with pytest.raises(TypeError, match=r".*must be bool.*"):
                RandomCsvDataSetConfig(filename=file,
                                        variable_names=['var1', 'var2'],
                                        independent_per_thread=123456)

        def test_positive(self):
            csvdata = RandomCsvDataSetConfig(filename=file,
                                            variable_names=['var1', 'var2'],
                                            independent_per_thread=True)
            assert csvdata.independent_per_thread == True


class TestCsvDataSetConfigRender:
    def test_delimiter(self):
        element = RandomCsvDataSetConfig(filename=file,
                                        variable_names=['var1', 'var2'],
                                        delimiter='|')
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['result']['com.blazemeter.jmeter.RandomCSVDataSetConfig']['stringProp']:
            if tag['@name'] == 'delimiter':
                assert tag['#text'] == '|'

    def test_file_encoding(self):
        element = RandomCsvDataSetConfig(filename=file,
                                        variable_names=['var1', 'var2'],
                                        file_encoding=FileEncoding.UTF16)
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['result']['com.blazemeter.jmeter.RandomCSVDataSetConfig']['stringProp']:
            if tag['@name'] == 'fileEncoding':
                assert tag['#text'] == 'UTF-16'

    def test_filename(self):
        element = RandomCsvDataSetConfig(filename=file,
                                        variable_names=['var1', 'var2'],)
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['result']['com.blazemeter.jmeter.RandomCSVDataSetConfig']['stringProp']:
            if tag['@name'] == 'filename':
                assert tag['#text'] == file

    def test_ignore_first_line(self):
        element = RandomCsvDataSetConfig(filename=file,
                                        variable_names=['var1', 'var2'],
                                        ignore_first_line=True)
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['result']['com.blazemeter.jmeter.RandomCSVDataSetConfig']['boolProp']:
            if tag['@name'] == 'ignoreFirstLine':
                assert tag['#text'] == 'true'

    def test_recycle(self):
        element = RandomCsvDataSetConfig(filename=file,
                                        variable_names=['var1', 'var2'],
                                        recycle=False)
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['result']['com.blazemeter.jmeter.RandomCSVDataSetConfig']['boolProp']:
            if tag['@name'] == 'rewindOnTheEndOfList':
                assert tag['#text'] == 'false'

    def test_random_order(self):
        element = RandomCsvDataSetConfig(filename=file,
                                        variable_names=['var1', 'var2'],
                                        random_order=False)
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['result']['com.blazemeter.jmeter.RandomCSVDataSetConfig']['boolProp']:
            if tag['@name'] == 'randomOrder':
                assert tag['#text'] == 'false'
                
    def test_independent_per_thread(self):
        element = RandomCsvDataSetConfig(filename=file,
                                        variable_names=['var1', 'var2'],
                                        independent_per_thread=True)
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['result']['com.blazemeter.jmeter.RandomCSVDataSetConfig']['boolProp']:
            if tag['@name'] == 'independentListPerThread':
                assert tag['#text'] == 'true'

    def test_variable_names(self):
        element = RandomCsvDataSetConfig(filename=file,
                                        variable_names=['var1', 'var2', 'var3', 'var4'],)
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        for tag in parsed_doc['result']['com.blazemeter.jmeter.RandomCSVDataSetConfig']['stringProp']:
            if tag['@name'] == 'variableNames':
                assert tag['#text'] == 'var1,var2,var3,var4'

    def test_header_contain(self):
        element = RandomCsvDataSetConfig(filename=file,
                                        variable_names=['var1', 'var2'],)
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        is_contain = 'xml version' in rendered_doc
        assert is_contain is False

    def test_hashtree_contain(self):
        element = RandomCsvDataSetConfig(filename=file,
                                        variable_names=['var1', 'var2'],)
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        assert '<hashTree />' in rendered_doc
