import pytest

from jmeter_api.basics.thread_group.elements import BasicStandartThreadGroup


class TestBasicStandartThreadGroupArgs:
    class TestNumThreads:
        def test_positive(self):
            btg = BasicStandartThreadGroup(num_threads=10)
            assert btg.num_threads == 10

        def test_check(self):
            with pytest.raises(TypeError):
                BasicStandartThreadGroup(num_threads='123')

        def test_less_more_check(self):
            with pytest.raises(TypeError):
                BasicStandartThreadGroup(num_threads=-5)

        def test_null_check(self):
            with pytest.raises(TypeError):
                BasicStandartThreadGroup(num_threads=0)

    class TestRampTime:
        def test_positive(self):
            btg = BasicStandartThreadGroup(ramp_time=25)
            assert btg.ramp_time == 25

        def test_check(self):
            with pytest.raises(TypeError):
                BasicStandartThreadGroup(ramp_time='25')

    class TestContinueForever:
        def test_check(self):
            with pytest.raises(TypeError):
                BasicStandartThreadGroup(continue_forever="True")

        def test_check2(self):
            with pytest.raises(TypeError):
                BasicStandartThreadGroup(continue_forever=1)

        def test_positive(self):
            BasicStandartThreadGroup(continue_forever=True)

    class TestConditions:
        def test_check(self):
            with pytest.raises(ValueError):
                BasicStandartThreadGroup(continue_forever=True, loops=1)

        def test_check2(self):
            with pytest.raises(ValueError):
                BasicStandartThreadGroup(loops=-1)

    class TestLoops:
        def test_check(self):
            with pytest.raises(TypeError):
                BasicStandartThreadGroup(loops="1")

        def test_check2(self):
            with pytest.raises(TypeError):
                BasicStandartThreadGroup(loops="a")

        def test_positive(self):
            BasicStandartThreadGroup(loops=23)

        def test_zero(self):
            BasicStandartThreadGroup(loops=0)

        def test_negative(self):
            with pytest.raises(TypeError):
                BasicStandartThreadGroup(loops=-4)

    class TestIsShedulerEnable:
        def test_check(self):
            with pytest.raises(TypeError):
                BasicStandartThreadGroup(is_sheduler_enable="True")

        def test_check2(self):
            with pytest.raises(TypeError):
                BasicStandartThreadGroup(is_sheduler_enable=1)

        def test_positive(self):
            BasicStandartThreadGroup(is_sheduler_enable=True)
            
    class TestConditionSheduler:
        def test_check(self):
            with pytest.raises(ValueError):
                BasicStandartThreadGroup(sheduler_duration=23)

        def test_check2(self):
            with pytest.raises(ValueError):
                BasicStandartThreadGroup(sheduler_delay=1)

        def test_positive(self):
            BasicStandartThreadGroup(is_sheduler_enable=True, sheduler_delay=1)
            
        def test_positive1(self):
            BasicStandartThreadGroup(is_sheduler_enable=True, sheduler_duration=1)

    class TestShedulerDuration:
        def test_check(self):
            with pytest.raises(TypeError):
                BasicStandartThreadGroup(is_sheduler_enable=True, sheduler_duration="1")

        def test_positive(self):
            BasicStandartThreadGroup(is_sheduler_enable=True, sheduler_duration=23)

    class TestShedulerDelay:
        def test_check(self):
            with pytest.raises(TypeError):
                BasicStandartThreadGroup(is_sheduler_enable=True, sheduler_delay="1")

        def test_positive(self):
            BasicStandartThreadGroup(is_sheduler_enable=True, sheduler_delay=23)
