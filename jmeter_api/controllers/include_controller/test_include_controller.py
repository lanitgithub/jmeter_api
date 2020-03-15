import xmltodict
import pytest

from jmeter_api.controllers.include_controller.elements import IncludeController
from jmeter_api.basics.utils import tag_wrapper


class TestIncludeController:
    class TestAppend:
        def test_check(self):
            with pytest.raises(RuntimeError):
                c = "jmeter_api/controllers/include_controller/include_test.jmx"
                IncludeController(includePath=c).append(IncludeController(includePath=c))
                
    class TestIncludePath:
        def test_check(self):
            with pytest.raises(TypeError):
                IncludeController(includePath=123)

        def test_check2(self):
            with pytest.raises(OSError):
                IncludeController(includePath="wrong file")
                
        def test_check4(self):
            with pytest.raises(OSError):
                IncludeController(includePath="")

        def test_check3(self):
            with pytest.raises(ValueError):
                IncludeController(includePath="jmeter_api/controllers/include_controller/elements.py")

        def test_positive(self):
            IncludeController(includePath="jmeter_api/controllers/include_controller/include_test.jmx")


class TestIncludeControllerRender:
    def test_condition(self):
        file = "jmeter_api/controllers/include_controller/include_test.jmx"
        element = IncludeController(includePath=file)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        assert parsed_doc['test_results']['IncludeController']['stringProp']['#text'] == file
