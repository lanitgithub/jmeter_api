import pytest

from jmeter_api.basics.element.elements import BasicElement


class TestBasicElementArgs:
    class TestIsEnable:
        def test_check_type(self):
            with pytest.raises(TypeError):
                BasicElement(is_enabled='True')

        def test_check_type2(self):
            with pytest.raises(TypeError):
                BasicElement(is_enabled=847378)

        def test_positive(self):
            element = BasicElement(is_enabled=True)
            assert element.is_enabled is True

    class TestName:
        def test_check_type(self):
            with pytest.raises(TypeError, match=r".*must be str.*"):
                BasicElement(name=847378)

        def test_positive(self):
            element = BasicElement(name='MyName')
            assert element.name == 'MyName'
