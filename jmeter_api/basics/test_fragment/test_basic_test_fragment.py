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

class TestBasicTestFragmentAppend:
    def test_negative1(self):
        with pytest.raises(TypeError):
            BasicTestFragment().append(BasicTestFragment())
    def test_negative2(self):
        with pytest.raises(TypeError):
            BasicTestFragment().append(BasicThreadGroup())
    def test_negative3(self):
        with pytest.raises(TypeError):
            BasicTestFragment().append(NonTestElements())

    def test_positive1(self):
        BasicTestFragment().append(BasicPreProcessor())
    def test_positive2(self):
        BasicTestFragment().append(BasicPostProcessor())
    def test_positive3(self):
        BasicTestFragment().append(BasicController())
    def test_positive4(self):
        BasicTestFragment().append(BasicConfig())
    def test_positive5(self):
        BasicTestFragment().append(BasicSampler())
    def test_positive6(self):
        BasicTestFragment().append(BasicAssertion())
    def test_positive7(self):
        BasicTestFragment().append(BasicListener())
    def test_positive8(self):
        BasicTestFragment().append(BasicTimer())
