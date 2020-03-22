import xmltodict
import pytest

from jmeter_api.configs.csv_data_set_config.elements import CsvDataSetConfig, ShareMode
from jmeter_api.basics.utils import FileEncoding, tag_wrapper

exist_file = "./jmeter_api/configs/csv_data_set_config/test_csv_data_set_config.py"


class TestCsvDataSetConfigArgs:
    class TestFilePath:
        def test_type_check(self):
            with pytest.raises(FileNotFoundError, match=r".*is not file*"):
                CsvDataSetConfig(file_path='ErrorPath',
                                 variable_names=['var1', 'var2'])

        def test_type_check2(self):
            with pytest.raises(FileNotFoundError, match=r".*is not file*"):
                CsvDataSetConfig(file_path='./ErrorPath',
                                 variable_names=['var1', 'var2'])

        def test_positive(self):
            csvdata = CsvDataSetConfig(
                file_path=exist_file, variable_names=['var1', 'var2'])
            assert csvdata.file_path == exist_file

        def test_positive2(self):
            csvdata = CsvDataSetConfig(
                file_path=exist_file, variable_names=['var1', 'var2'])
            assert csvdata.file_path == exist_file

    class TestVariableNames:
        def test_type_check(self):
            with pytest.raises(TypeError, match=r".*variable_names must be List[str]*"):
                CsvDataSetConfig(file_path=exist_file,
                                 variable_names={'randkey': 'randvalue'})

        def test_content_type_check(self):
            with pytest.raises(TypeError, match=r".*All elements must be str*"):
                CsvDataSetConfig(file_path=exist_file,
                                 variable_names=['asdfg', 123, 'qwerty'])

        def test_content_type_check2(self):
            with pytest.raises(TypeError, match=r".*must contain chars*"):
                CsvDataSetConfig(file_path=exist_file,
                                 variable_names=['asdfg', '123', 'qwerty'])

        def test_positive(self):
            csvdata = CsvDataSetConfig(file_path=exist_file,
                                       variable_names=['asdfg', 'vbn', 'qwerty'])
            assert csvdata.variable_names == 'asdfg,vbn,qwerty'

    class TestDelimiter:
        def test_positive(self):
            csvdata = CsvDataSetConfig(file_path=exist_file,
                                       variable_names=['asdfg', 'vbn', 'qwerty'],
                                       delimiter='|')
            assert csvdata.variable_names == 'asdfg|vbn|qwerty'

    class TestFileEncoding:
        def test_type_check(self):
            with pytest.raises(TypeError, match=r".*must be FileEncoding*"):
                CsvDataSetConfig(file_path=exist_file,
                                 variable_names=['var1', 'var2'],
                                 file_encoding='UTF-8')

        def test_type_check2(self):
            with pytest.raises(TypeError, match=r".*must be FileEncoding*"):
                CsvDataSetConfig(file_path=exist_file,
                                 variable_names=['var1', 'var2'],
                                 file_encoding=100)

        def test_positive(self):
            csvdata = CsvDataSetConfig(file_path=exist_file,
                                       variable_names=['var1', 'var2'],
                                       file_encoding=FileEncoding.ISO8859)
            assert csvdata.file_encoding == FileEncoding.ISO8859

    class TestIgnoreFirstLine:
        def test_type_check(self):
            with pytest.raises(TypeError, match=r".*must be bool.*"):
                CsvDataSetConfig(file_path=exist_file,
                                 variable_names=['var1', 'var2'],
                                 ignore_first_line='True')

        def test_type_check2(self):
            with pytest.raises(TypeError, match=r".*must be bool.*"):
                CsvDataSetConfig(file_path=exist_file,
                                 variable_names=['var1', 'var2'],
                                 ignore_first_line=123456)

        def test_positive(self):
            csvdata = CsvDataSetConfig(file_path=exist_file,
                                       variable_names=['var1', 'var2'],
                                       ignore_first_line=True)
            assert csvdata.ignore_first_line == True

    class TestRecycle:
        def test_type_check(self):
            with pytest.raises(TypeError, match=r".*must be bool.*"):
                CsvDataSetConfig(file_path=exist_file,
                                 variable_names=['var1', 'var2'],
                                 recycle='True')

        def test_type_check2(self):
            with pytest.raises(TypeError, match=r".*must be bool.*"):
                CsvDataSetConfig(file_path=exist_file,
                                 variable_names=['var1', 'var2'],
                                 recycle=123456)

        def test_positive(self):
            csvdata = CsvDataSetConfig(file_path=exist_file,
                                       variable_names=['var1', 'var2'],
                                       recycle=True)
            assert csvdata.recycle == True

    class TestStopThread:
        def test_type_check(self):
            with pytest.raises(TypeError, match=r".*must be bool.*"):
                CsvDataSetConfig(file_path=exist_file,
                                 variable_names=['var1', 'var2'],
                                 stop_thread='True')

        def test_type_check2(self):
            with pytest.raises(TypeError, match=r".*must be bool.*"):
                CsvDataSetConfig(file_path=exist_file,
                                 variable_names=['var1', 'var2'],
                                 stop_thread=123456)

        def test_positive(self):
            csvdata = CsvDataSetConfig(file_path=exist_file,
                                       variable_names=['var1', 'var2'],
                                       stop_thread=True)
            assert csvdata.stop_thread == True

    class TestSharedMode:
        def test_type_check(self):
            with pytest.raises(TypeError, match=r".*must be ShareMode*"):
                CsvDataSetConfig(file_path=exist_file,
                                 variable_names=['var1', 'var2'],
                                 share_mode='True')

        def test_type_check2(self):
            with pytest.raises(TypeError, match=r".*must be ShareMode*"):
                CsvDataSetConfig(file_path=exist_file,
                                 variable_names=['var1', 'var2'],
                                 share_mode=123456)

        def test_positive(self):
            csvdata = CsvDataSetConfig(file_path=exist_file,
                                       variable_names=['var1', 'var2'],
                                       share_mode=ShareMode.ALL)
            assert csvdata.share_mode == ShareMode.ALL


class TestCsvDataSetConfigRender:
    def test_delimiter(self):
        element = CsvDataSetConfig(file_path=exist_file,
                                   variable_names=['var1', 'var2'],
                                   delimiter='|')
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        assert parsed_doc['result']['CSVDataSet']['stringProp'][1]['#text'] == '|'

    def test_file_encoding(self):
        element = CsvDataSetConfig(file_path=exist_file,
                                   variable_names=['var1', 'var2'],
                                   file_encoding=FileEncoding.UTF16)
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        assert parsed_doc['result']['CSVDataSet']['stringProp'][2]['#text'] == 'UTF-16'

    def test_file_path(self):
        element = CsvDataSetConfig(file_path=exist_file,
                                   variable_names=['var1', 'var2'],)
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        assert parsed_doc['result']['CSVDataSet']['stringProp'][3]['#text'] == exist_file

    def test_ignore_first_line(self):
        element = CsvDataSetConfig(file_path=exist_file,
                                   variable_names=['var1', 'var2'],
                                   ignore_first_line=True)
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        assert parsed_doc['result']['CSVDataSet']['boolProp'][0]['#text'] == 'true'

    def test_recycle(self):
        element = CsvDataSetConfig(file_path=exist_file,
                                   variable_names=['var1', 'var2'],
                                   recycle=True)
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        assert parsed_doc['result']['CSVDataSet']['boolProp'][2]['#text'] == 'true'

    def test_shared_mode(self):
        element = CsvDataSetConfig(file_path=exist_file,
                                   variable_names=['var1', 'var2'],
                                   share_mode=ShareMode.GROUP)
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        assert parsed_doc['result']['CSVDataSet']['stringProp'][4]['#text'] == 'shareMode.group'

    def test_stop_thread(self):
        element = CsvDataSetConfig(file_path=exist_file,
                                   variable_names=['var1', 'var2'],
                                   stop_thread=True)
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        assert parsed_doc['result']['CSVDataSet']['boolProp'][3]['#text'] == 'true'

    def test_variable_names(self):
        element = CsvDataSetConfig(file_path=exist_file,
                                   variable_names=['var1', 'var2', 'var3', 'var4'],)
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        assert parsed_doc['result']['CSVDataSet']['stringProp'][5]['#text'] == 'var1,var2,var3,var4'

    def test_header_contain(self):
        element = CsvDataSetConfig(file_path=exist_file,
                                   variable_names=['var1', 'var2'],)
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        is_contain = 'xml version' in rendered_doc
        assert is_contain is False

    def test_hashtree_contain(self):
        element = CsvDataSetConfig(file_path=exist_file,
                                   variable_names=['var1', 'var2'],)
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        assert '<hashTree />' in rendered_doc
