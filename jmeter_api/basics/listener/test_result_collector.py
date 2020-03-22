import xmltodict
import pytest

from jmeter_api.basics.listener.elements import ResultCollector
from jmeter_api.basics.utils import tag_wrapper

exist_file = "./jmeter_api/basics/listener/test_result_collector.py"


class TestResultCollector:
    class TestGUIClass:
        def test_type_check(self):
            with pytest.raises(TypeError):
                ResultCollector(guiclass=123)

        def test_positive(self):
            ResultCollector(guiclass="var")
            
    class TestFilename:
        def test_type_check(self):
            with pytest.raises(TypeError):
                ResultCollector(guiclass="var", filename=123)
                
        def test_type_check2(self):
            with pytest.raises(ValueError):
                ResultCollector(guiclass="var", filename='not existing file')

        def test_positive(self):
            ResultCollector(guiclass="var", filename=exist_file)
            
    class TestErrorLogging:
        def test_type_check(self):
            with pytest.raises(TypeError):
                ResultCollector(guiclass="var", error_logging="True")
                
        def test_type_check1(self):
            with pytest.raises(TypeError):
                ResultCollector(guiclass="var", error_logging=1)

        def test_positive(self):
            ResultCollector(guiclass="var", error_logging=True)
            
    class TestTime:
        def test_type_check(self):
            with pytest.raises(TypeError):
                ResultCollector(guiclass="var", time="True")
                
        def test_type_check1(self):
            with pytest.raises(TypeError):
                ResultCollector(guiclass="var", time=1)

        def test_positive(self):
            ResultCollector(guiclass="var", time=True)
                        
    class TestLatency:
        def test_type_check(self):
            with pytest.raises(TypeError):
                ResultCollector(guiclass="var", latency="True")
                
        def test_type_check1(self):
            with pytest.raises(TypeError):
                ResultCollector(guiclass="var", latency=1)

        def test_positive(self):
            ResultCollector(guiclass="var", latency=True)
                        
    class TestTimestamp:
        def test_type_check(self):
            with pytest.raises(TypeError):
                ResultCollector(guiclass="var", timestamp="True")
                
        def test_type_check1(self):
            with pytest.raises(TypeError):
                ResultCollector(guiclass="var", timestamp=1)

        def test_positive(self):
            ResultCollector(guiclass="var", timestamp=True)
                        
    class TestSuccess:
        def test_type_check(self):
            with pytest.raises(TypeError):
                ResultCollector(guiclass="var", success="True")
                
        def test_type_check1(self):
            with pytest.raises(TypeError):
                ResultCollector(guiclass="var", success=1)

        def test_positive(self):
            ResultCollector(guiclass="var", success=True)
                        
    class TestLabel:
        def test_type_check(self):
            with pytest.raises(TypeError):
                ResultCollector(guiclass="var", label="True")
                
        def test_type_check1(self):
            with pytest.raises(TypeError):
                ResultCollector(guiclass="var", label=1)

        def test_positive(self):
            ResultCollector(guiclass="var", label=True)
                        
    class TestCode:
        def test_type_check(self):
            with pytest.raises(TypeError):
                ResultCollector(guiclass="var", code="True")
                
        def test_type_check1(self):
            with pytest.raises(TypeError):
                ResultCollector(guiclass="var", code=1)

        def test_positive(self):
            ResultCollector(guiclass="var", code=True)
                        
    class TestMessage:
        def test_type_check(self):
            with pytest.raises(TypeError):
                ResultCollector(guiclass="var", message="True")
                
        def test_type_check1(self):
            with pytest.raises(TypeError):
                ResultCollector(guiclass="var", message=1)

        def test_positive(self):
            ResultCollector(guiclass="var", message=True)
                        
    class TestThreadName:
        def test_type_check(self):
            with pytest.raises(TypeError):
                ResultCollector(guiclass="var", thread_name="True")
                
        def test_type_check1(self):
            with pytest.raises(TypeError):
                ResultCollector(guiclass="var", thread_name=1)

        def test_positive(self):
            ResultCollector(guiclass="var", thread_name=True)
                        
    class TestDataType:
        def test_type_check(self):
            with pytest.raises(TypeError):
                ResultCollector(guiclass="var", data_type="True")
                
        def test_type_check1(self):
            with pytest.raises(TypeError):
                ResultCollector(guiclass="var", data_type=1)

        def test_positive(self):
            ResultCollector(guiclass="var", data_type=True)
                        
    class TestEncoding:
        def test_type_check(self):
            with pytest.raises(TypeError):
                ResultCollector(guiclass="var", encoding="True")
                
        def test_type_check1(self):
            with pytest.raises(TypeError):
                ResultCollector(guiclass="var", encoding=1)

        def test_positive(self):
            ResultCollector(guiclass="var", encoding=True)
                        
    class TestAssertions:
        def test_type_check(self):
            with pytest.raises(TypeError):
                ResultCollector(guiclass="var", assertions="True")
                
        def test_type_check1(self):
            with pytest.raises(TypeError):
                ResultCollector(guiclass="var", assertions=1)

        def test_positive(self):
            ResultCollector(guiclass="var", assertions=True)
                        
    class TestSubresults:
        def test_type_check(self):
            with pytest.raises(TypeError):
                ResultCollector(guiclass="var", subresults="True")
                
        def test_type_check1(self):
            with pytest.raises(TypeError):
                ResultCollector(guiclass="var", subresults=1)

        def test_positive(self):
            ResultCollector(guiclass="var", subresults=True)
                        
    class TestResponseData:
        def test_type_check(self):
            with pytest.raises(TypeError):
                ResultCollector(guiclass="var", response_data="True")
                
        def test_type_check1(self):
            with pytest.raises(TypeError):
                ResultCollector(guiclass="var", response_data=1)

        def test_positive(self):
            ResultCollector(guiclass="var", response_data=True)
                        
    class TestSamplerData:
        def test_type_check(self):
            with pytest.raises(TypeError):
                ResultCollector(guiclass="var", sampler_data="True")
                
        def test_type_check1(self):
            with pytest.raises(TypeError):
                ResultCollector(guiclass="var", sampler_data=1)

        def test_positive(self):
            ResultCollector(guiclass="var", sampler_data=True)
                        
    class TestXml:
        def test_type_check(self):
            with pytest.raises(TypeError):
                ResultCollector(guiclass="var", xml="True")
                
        def test_type_check1(self):
            with pytest.raises(TypeError):
                ResultCollector(guiclass="var", xml=1)

        def test_positive(self):
            ResultCollector(guiclass="var", xml=True)
                        
    class TestFieldNames:
        def test_type_check(self):
            with pytest.raises(TypeError):
                ResultCollector(guiclass="var", field_names="True")
                
        def test_type_check1(self):
            with pytest.raises(TypeError):
                ResultCollector(guiclass="var", field_names=1)

        def test_positive(self):
            ResultCollector(guiclass="var", field_names=True)
                        
    class TestResponseHeaders:
        def test_type_check(self):
            with pytest.raises(TypeError):
                ResultCollector(guiclass="var", response_headers="True")
                
        def test_type_check1(self):
            with pytest.raises(TypeError):
                ResultCollector(guiclass="var", response_headers=1)

        def test_positive(self):
            ResultCollector(guiclass="var", response_headers=True)
                        
    class TestRequestHeaders:
        def test_type_check(self):
            with pytest.raises(TypeError):
                ResultCollector(guiclass="var", request_headers="True")
                
        def test_type_check1(self):
            with pytest.raises(TypeError):
                ResultCollector(guiclass="var", request_headers=1)

        def test_positive(self):
            ResultCollector(guiclass="var", request_headers=True)
                        
    class TestResponseDataOnError:
        def test_type_check(self):
            with pytest.raises(TypeError):
                ResultCollector(guiclass="var", response_data_on_error="True")
                
        def test_type_check1(self):
            with pytest.raises(TypeError):
                ResultCollector(guiclass="var", response_data_on_error=1)

        def test_positive(self):
            ResultCollector(guiclass="var", response_data_on_error=True)
                        
    class TestSaveAssertion:
        def test_type_check(self):
            with pytest.raises(TypeError):
                ResultCollector(guiclass="var", save_assertion_results_failure_message="True")
                
        def test_type_check1(self):
            with pytest.raises(TypeError):
                ResultCollector(guiclass="var", save_assertion_results_failure_message=1)

        def test_positive(self):
            ResultCollector(guiclass="var", save_assertion_results_failure_message=True)
                        
    class TestBytes:
        def test_type_check(self):
            with pytest.raises(TypeError):
                ResultCollector(guiclass="var", bytes_="True")
                
        def test_type_check1(self):
            with pytest.raises(TypeError):
                ResultCollector(guiclass="var", bytes_=1)

        def test_positive(self):
            ResultCollector(guiclass="var", bytes_=True)
                        
    class TestSentBytes:
        def test_type_check(self):
            with pytest.raises(TypeError):
                ResultCollector(guiclass="var", sent_bytes="True")
                
        def test_type_check1(self):
            with pytest.raises(TypeError):
                ResultCollector(guiclass="var", sent_bytes=1)

        def test_positive(self):
            ResultCollector(guiclass="var", sent_bytes=True)
                        
    class TestURL:
        def test_type_check(self):
            with pytest.raises(TypeError):
                ResultCollector(guiclass="var", url="True")
                
        def test_type_check1(self):
            with pytest.raises(TypeError):
                ResultCollector(guiclass="var", url=1)

        def test_positive(self):
            ResultCollector(guiclass="var", url=True)
                        
    class TestThreadCounts:
        def test_type_check(self):
            with pytest.raises(TypeError):
                ResultCollector(guiclass="var", thread_counts="True")
                
        def test_type_check1(self):
            with pytest.raises(TypeError):
                ResultCollector(guiclass="var", thread_counts=1)

        def test_positive(self):
            ResultCollector(guiclass="var", thread_counts=True)
                        
    class TestIdleTime:
        def test_type_check(self):
            with pytest.raises(TypeError):
                ResultCollector(guiclass="var", idle_time="True")
                
        def test_type_check1(self):
            with pytest.raises(TypeError):
                ResultCollector(guiclass="var", idle_time=1)

        def test_positive(self):
            ResultCollector(guiclass="var", idle_time=True)
                        
    class TestConnectTime:
        def test_type_check(self):
            with pytest.raises(TypeError):
                ResultCollector(guiclass="var", connect_time="True")
                
        def test_type_check1(self):
            with pytest.raises(TypeError):
                ResultCollector(guiclass="var", connect_time=1)

        def test_positive(self):
            ResultCollector(guiclass="var", connect_time=True)


class TestResultCollectorRender:
    def test_filename(self):
        element = ResultCollector(guiclass="var", filename=exist_file)
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        assert parsed_doc['result']['ResultCollector']['stringProp']['#text'] == './jmeter_api/basics/listener/test_result_collector.py'

    def test_guiclass(self):
        element = ResultCollector(guiclass="var")
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        assert parsed_doc['result']['ResultCollector']['@guiclass'] == 'var'
                
    def test_error_logging(self):
        element = ResultCollector(guiclass="var", error_logging=True)
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        assert parsed_doc['result']['ResultCollector']['boolProp']['#text'] == 'true'
                
    def test_config_value(self):
        element = ResultCollector(guiclass="var", encoding=True)
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        parsed_doc = xmltodict.parse(rendered_doc)
        assert parsed_doc['result']['ResultCollector']['objProp']['value']['encoding'] == 'true'
                
    def test_hashtree_contain(self):
        element = ResultCollector(guiclass="var")
        rendered_doc = tag_wrapper(element.to_xml(), 'result')
        assert '<hashTree />' in rendered_doc
