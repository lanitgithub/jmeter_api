import pytest

from jmeter_api.basics.thread_group.bzm_elements import BasicBzmThreadGroup, Unit


class TestBasicBzmThreadGroupArgs:
    class TestLogFilename:
        def test_positive(self):
            BasicBzmThreadGroup(log_filename="file")

        def test_check(self):
            with pytest.raises(TypeError):
                BasicBzmThreadGroup(log_filename=123)

    class TestUnit:
        def test_positive(self):
            BasicBzmThreadGroup(unit=Unit.SECOND)

        def test_check(self):
            with pytest.raises(TypeError):
                BasicBzmThreadGroup(unit=1)
        def test_check1(self):
            with pytest.raises(TypeError):
                BasicBzmThreadGroup(unit="S")
