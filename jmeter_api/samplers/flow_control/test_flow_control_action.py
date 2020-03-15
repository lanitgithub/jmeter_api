import xmltodict
import pytest

from jmeter_api.samplers.flow_control.elements import FlowControlAction, ActionOnThread, Target
from jmeter_api.basics.utils import tag_wrapper


class TestFlowControlAction:
    # name type check
    def test_name(self):
        with pytest.raises(TypeError):
            FlowControlAction(name=123)
    # comments type check

    def test_comments(self):
        with pytest.raises(TypeError):
            FlowControlAction(comments=123)
    # is_enabled type check

    def test_enabled(self):
        with pytest.raises(TypeError):
            FlowControlAction(is_enabled="True")

    def test_logical_action_on_thread(self):
        with pytest.raises(TypeError):
            FlowControlAction(logical_action_on_thread=1)

    def test_pause(self):
        with pytest.raises(TypeError):
            FlowControlAction(pause='123')

    def test_pause2(self):
        with pytest.raises(ValueError):
            FlowControlAction(pause=-1)

    def test_target(self):
        with pytest.raises(TypeError):
            FlowControlAction(target=-1)


class TestFlowActionControlRender:
    root_tag = FlowControlAction.root_element_name

    def test_name(self):
        element = FlowControlAction(name='My flow')
        rendered_doc = tag_wrapper(element.to_xml(), self.root_tag)
        parsed_doc = xmltodict.parse(rendered_doc)[self.root_tag]
        assert parsed_doc[self.root_tag]['@testname'] == 'My flow'

    def test_comments(self):
        element = FlowControlAction(comments='My flow')
        rendered_doc = tag_wrapper(element.to_xml(), self.root_tag)
        parsed_doc = xmltodict.parse(rendered_doc)[self.root_tag]
        for tag in parsed_doc[self.root_tag]['stringProp']:
            if tag['@name'] == 'TestPlan.comments':
                assert tag['#text'] == 'My flow'

    def test_is_enabled(self):
        element = FlowControlAction(is_enabled=False)
        rendered_doc = tag_wrapper(element.to_xml(), self.root_tag)
        parsed_doc = xmltodict.parse(rendered_doc)[self.root_tag]
        assert parsed_doc[self.root_tag]['@enabled'] == 'false'

    def test_logical_action(self):
        element = FlowControlAction(
            logical_action_on_thread=ActionOnThread.STOP)
        rendered_doc = tag_wrapper(element.to_xml(), self.root_tag)
        parsed_doc = xmltodict.parse(rendered_doc)[self.root_tag]
        for tag in parsed_doc[self.root_tag]['intProp']:
            if tag['@name'] == 'ActionProcessor.action':
                assert tag['#text'] == '0'

    def test_target(self):
        element = FlowControlAction(logical_action_on_thread=ActionOnThread.STOP,
                                    target=Target.ALL_THREAD)
        rendered_doc = tag_wrapper(element.to_xml(), self.root_tag)
        parsed_doc = xmltodict.parse(rendered_doc)[self.root_tag]
        for tag in parsed_doc[self.root_tag]['intProp']:
            if tag['@name'] == 'ActionProcessor.target':
                assert tag['#text'] == '2'
