from jmeter_api.basics.element.elements import BasicElement
from jmeter_api.basics.pre_processor.elements import BasicPreProcessor
from jmeter_api.basics.post_processor.elements import BasicPostProcessor
from jmeter_api.basics.controller.elements import BasicController
from jmeter_api.basics.config.elements import BasicConfig
from jmeter_api.basics.assertion.elements import BasicAssertion
from jmeter_api.basics.listener.elements import BasicListener
from jmeter_api.basics.sampler.elements import BasicSampler
from jmeter_api.basics.timer.elements import BasicTimer
from jmeter_api.basics.thread_group.elements import BasicThreadGroup
from jmeter_api.basics.non_test_elements.elements import NonTestElements
from jmeter_api.basics.test_fragment.elements import BasicTestFragment
import pytest

class TestBasicSamplerAppend:
    def test_negative1(self):
        with pytest.raises(TypeError):
            BasicSampler().append(BasicTestFragment())
    def test_negative2(self):
        with pytest.raises(TypeError):
            BasicSampler().append(BasicThreadGroup())
    def test_negative3(self):
        with pytest.raises(TypeError):
            BasicSampler().append(NonTestElements())
    def test_negative4(self):
        with pytest.raises(TypeError):
            BasicSampler().append(BasicController())
    def test_negative5(self):
        with pytest.raises(TypeError):
            BasicSampler().append(BasicSampler())

    def test_positive1(self):
        BasicSampler().append(BasicPreProcessor())
    def test_positive2(self):
        BasicSampler().append(BasicPostProcessor())
    def test_positive3(self):
        BasicSampler().append(BasicConfig())
    def test_positive4(self):
        BasicSampler().append(BasicAssertion())
    def test_positive5(self):
        BasicSampler().append(BasicListener())
    def test_positive6(self):
        BasicSampler().append(BasicTimer())
