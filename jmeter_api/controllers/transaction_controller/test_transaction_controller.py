import xmltodict
import pytest

from jmeter_api.controllers.transaction_controller.elements import TransactionController
from jmeter_api.basics.utils import tag_wrapper


class TestTransactionController:
    class TestIncludeTimers:
        def test_check(self):
            with pytest.raises(TypeError):
                TransactionController(includeTimers="True")

        def test_check2(self):
            with pytest.raises(TypeError):
                TransactionController(includeTimers=1)

        def test_positive(self):
            TransactionController(includeTimers=True)

    class TestParent:
        def test_check(self):
            with pytest.raises(TypeError):
                TransactionController(parent="False")

        def test_check2(self):
            with pytest.raises(TypeError):
                TransactionController(parent=0)

        def test_positive(self):
            TransactionController(parent=True)


class TestTransactionControllerRender:
    def test(self):
        element = TransactionController()
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        assert parsed_doc['test_results']['TransactionController']['boolProp'][0]['#text'] == 'false'
