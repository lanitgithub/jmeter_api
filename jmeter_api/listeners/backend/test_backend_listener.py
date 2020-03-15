import xmltodict
import pytest

from jmeter_api.listeners.backend.elements import BackendListener
from jmeter_api.basics.utils import tag_wrapper


class TestHttpRequestArgsTypes:
    # name type check
    def test_name(self):
        with pytest.raises(TypeError):
            BackendListener(name=123)
    # comments type check

    def test_comments(self):
        with pytest.raises(TypeError):
            BackendListener(comments=123)
    # is_enabled type check

    def test_enabled(self):
        with pytest.raises(TypeError):
            BackendListener(is_enabled="True")

    def test_async_queue_size(self):
        with pytest.raises(TypeError):
            BackendListener(async_queue_size='1')
    # path type check (non string data input)

    def test_influx_db_url(self):
        with pytest.raises(TypeError):
            BackendListener(influx_db_url=13)
    # method type check (non Method data input)

    def test_application(self):
        with pytest.raises(TypeError):
            BackendListener(application=123)

    def test_measurement(self):
        with pytest.raises(TypeError):
            BackendListener(measurement=2)

    def test_summary_only(self):
        with pytest.raises(TypeError):
            BackendListener(summary_only='True')

    def test_samplers_regexp(self):
        with pytest.raises(Exception):
            BackendListener(samplers_regexp='[')

    def test_samplers_regexp2(self):
        with pytest.raises(TypeError):
            BackendListener(samplers_regexp=123)

    def test_percentilies(self):
        with pytest.raises(TypeError):
            BackendListener(percentilies=-1)

    def test_percentilies2(self):
        with pytest.raises(Exception):
            BackendListener(percentilies='102;100')

    def test_test_title(self):
        with pytest.raises(TypeError):
            BackendListener(BackendListener=-1)

    def test_event_tags(self):
        with pytest.raises(TypeError):
            BackendListener(event_tags=5)


class TestBackendListenerRender:
    root_tag = BackendListener.root_element_name

    def test_render_name(self):
        element = BackendListener(name='My backend')
        rendered_doc = tag_wrapper(element.to_xml(), self.root_tag)
        parsed_doc = xmltodict.parse(rendered_doc)[self.root_tag]
        assert parsed_doc[self.root_tag]['@testname'] == 'My backend'

    def test_render_comments(self):
        element = BackendListener(comments='My comment')
        rendered_doc = tag_wrapper(element.to_xml(), self.root_tag)
        parsed_doc = xmltodict.parse(rendered_doc)[self.root_tag]
        for tag in parsed_doc[self.root_tag]['stringProp']:
            if tag['@name'] == 'TestPlan.comments':
                assert tag['#text'] == 'My comment'

    def test_render_is_enabled(self):
        element = BackendListener(is_enabled=False)
        rendered_doc = tag_wrapper(element.to_xml(), self.root_tag)
        parsed_doc = xmltodict.parse(rendered_doc)[self.root_tag]
        assert parsed_doc[self.root_tag]['@enabled'] == 'false'

    def test_influx_db_url(self):
        element = BackendListener(influx_db_url='localhost')
        rendered_doc = tag_wrapper(element.to_xml(), self.root_tag)
        parsed_doc = xmltodict.parse(rendered_doc)[self.root_tag]
        temp = parsed_doc[self.root_tag]['elementProp']['collectionProp']['elementProp'][1]['stringProp'][1]
        for key in temp:
            if key == '#text':
                assert temp[key] == 'localhost'

    def test_application(self):
        element = BackendListener(application='my app')
        rendered_doc = tag_wrapper(element.to_xml(), self.root_tag)
        parsed_doc = xmltodict.parse(rendered_doc)[self.root_tag]
        temp = parsed_doc[self.root_tag]['elementProp']['collectionProp']['elementProp'][2]['stringProp'][1]
        for key in temp:
            if key == '#text':
                assert temp[key] == 'my app'

    def test_measurement(self):
        element = BackendListener(measurement='my mess')
        rendered_doc = tag_wrapper(element.to_xml(), self.root_tag)
        parsed_doc = xmltodict.parse(rendered_doc)[self.root_tag]
        temp = parsed_doc[self.root_tag]['elementProp']['collectionProp']['elementProp'][3]['stringProp'][1]
        for key in temp:
            if key == '#text':
                assert temp[key] == 'my mess'

    def test_summery_only(self):
        element = BackendListener(summary_only=False)
        rendered_doc = tag_wrapper(element.to_xml(), self.root_tag)
        parsed_doc = xmltodict.parse(rendered_doc)[self.root_tag]
        temp = parsed_doc[self.root_tag]['elementProp']['collectionProp']['elementProp'][4]['stringProp'][1]
        for key in temp:
            if key == '#text':
                assert temp[key] == 'false'

    def test_samplers_regexp(self):
        element = BackendListener(samplers_regexp='\d\w')
        rendered_doc = tag_wrapper(element.to_xml(), self.root_tag)
        parsed_doc = xmltodict.parse(rendered_doc)[self.root_tag]
        temp = parsed_doc[self.root_tag]['elementProp']['collectionProp']['elementProp'][5]['stringProp'][1]
        for key in temp:
            if key == '#text':
                assert temp[key] == '\d\w'

    def test_percentiles(self):
        element = BackendListener(percentiles='90;95')
        rendered_doc = tag_wrapper(element.to_xml(), self.root_tag)
        parsed_doc = xmltodict.parse(rendered_doc)[self.root_tag]
        temp = parsed_doc[self.root_tag]['elementProp']['collectionProp']['elementProp'][6]['stringProp'][1]
        for key in temp:
            if key == '#text':
                assert temp[key] == '90;95'

    def test_test_title(self):
        element = BackendListener(test_title='title for fun')
        rendered_doc = tag_wrapper(element.to_xml(), self.root_tag)
        parsed_doc = xmltodict.parse(rendered_doc)[self.root_tag]
        temp = parsed_doc[self.root_tag]['elementProp']['collectionProp']['elementProp'][7]['stringProp'][1]
        for key in temp:
            if key == '#text':
                assert temp[key] == 'title for fun'

    def test_event_tags(self):
        element = BackendListener(event_tags='tag for fun')
        rendered_doc = tag_wrapper(element.to_xml(), self.root_tag)
        parsed_doc = xmltodict.parse(rendered_doc)[self.root_tag]
        temp = parsed_doc[self.root_tag]['elementProp']['collectionProp']['elementProp'][8]['stringProp'][1]
        for key in temp:
            if key == '#text':
                assert temp[key] == 'tag for fun'
