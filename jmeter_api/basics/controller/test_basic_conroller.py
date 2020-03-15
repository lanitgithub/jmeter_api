import pytest

from jmeter_api.basics.element.elements import BasicElement
from jmeter_api.basics.pre_processor.elements import BasicPreProcessor
from jmeter_api.basics.post_processor.elements import BasicPostProcessor
from jmeter_api.basics.controller.elements import BasicController
from jmeter_api.basics.config.elements import BasicConfig
from jmeter_api.basics.sampler.elements import BasicSampler
from jmeter_api.basics.assertion.elements import BasicAssertion
from jmeter_api.basics.listener.elements import BasicListener
from jmeter_api.basics.timer.elements import BasicTimer
from jmeter_api.basics.thread_group.elements import BasicThreadGroup
from jmeter_api.basics.non_test_elements.elements import NonTestElements
from jmeter_api.basics.test_fragment.elements import BasicTestFragment


class TestBasicTestFragmentAppend:
    def test_negative1(self):
        with pytest.raises(TypeError):
            BasicController().append(BasicTestFragment())
            
    def test_negative2(self):
        with pytest.raises(TypeError):
            BasicController().append(BasicThreadGroup())
            
    def test_negative3(self):
        with pytest.raises(TypeError):
            BasicController().append(NonTestElements())

    def test_positive1(self):
        BasicController().append(BasicPreProcessor())
        
    def test_positive2(self):
        BasicController().append(BasicPostProcessor())
        
    def test_positive3(self):
        BasicController().append(BasicController())
        
    def test_positive4(self):
        BasicController().append(BasicConfig())
        
    def test_positive5(self):
        BasicController().append(BasicSampler())
        
    def test_positive6(self):
        BasicController().append(BasicAssertion())
        
    def test_positive7(self):
        BasicController().append(BasicListener())
        
    def test_positive8(self):
        BasicController().append(BasicTimer())
