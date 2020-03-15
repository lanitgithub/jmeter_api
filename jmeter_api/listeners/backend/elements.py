import re

from jmeter_api.basics.listener.elements import BasicListener
from jmeter_api.basics.utils import Renderable, tree_to_str


class BackendListener(BasicListener, Renderable):

    root_element_name = 'BackendListener'

    def __init__(self, *,
                 name: str = 'Backend Listener',
                 async_queue_size: int = 5000,
                 influx_db_url: str = '',
                 application: str = '',
                 measurement: str = '',
                 summary_only: bool = True,
                 samplers_regexp: str = '',
                 percentiles: str = '',
                 test_title: str = '',
                 event_tags: str = '',
                 comments: str = '',
                 is_enabled: bool = True
                 ):
        super(BackendListener, self).__init__(name=name, comments=comments, is_enabled=is_enabled)
        self.async_queue_size = async_queue_size
        self.influx_db_url = influx_db_url
        self.application = application
        self.measurement = measurement
        self.summary_only = summary_only
        self.samplers_regexp = samplers_regexp
        self.percentiles = percentiles
        self.test_title = test_title
        self.event_tags = event_tags

    @property
    def async_queue_size(self) -> int:
        return self._async_queue_size

    @async_queue_size.setter
    def async_queue_size(self, value):
        if not isinstance(value, int):
            raise TypeError(f'arg: async_queue_size should be int. '
                            f'{type(value).__name__} was given')
        self._async_queue_size = value

    @property
    def influx_db_url(self):
        return self._influx_db_url

    @influx_db_url.setter
    def influx_db_url(self, value):
        if not isinstance(value, str):
            raise TypeError(f'arg: influx_db_url should be str. '
                            f'{type(value).__name__} was given')
        self._influx_db_url = value

    @property
    def application(self):
        return self._application

    @application.setter
    def application(self, value):
        if not isinstance(value, str):
            raise TypeError(f'arg: application should be str. '
                            f'{type(value).__name__} was given')
        self._application = value

    @property
    def measurement(self):
        return self._measurement

    @measurement.setter
    def measurement(self, value):
        if not isinstance(value, str):
            raise TypeError(f'arg: measurement should be str. '
                            f'{type(value).__name__} was given')
        self._measurement = value

    @property
    def summary_only(self):
        return self._summary_only

    @summary_only.setter
    def summary_only(self, value):
        if not isinstance(value, bool):
            raise TypeError(f'arg: summary_only should be bool. '
                            f'{type(value).__name__} was given')
        self._summary_only = value

    @property
    def samplers_regexp(self):
        return self._samplers_regexp

    @samplers_regexp.setter
    def samplers_regexp(self, value):
        if not isinstance(value, str):
            raise TypeError(f'arg: samplers_regexp should be str. '
                            f'{type(value).__name__} was given')
        try:
            re.compile(value)
        except Exception:
            raise Exception('Unable to compile reg exp')
        self._samplers_regexp = value

    @property
    def percentiles(self):
        return self._percentiles

    @percentiles.setter
    def percentiles(self, value):
        if not isinstance(value, str):
            raise TypeError(f'arg: percentiles should be str. '
                            f'{type(value).__name__} was given')
        if value:
            pers = value.split(';')
            for per in pers:
                try:
                    if int(per) > 101:
                        raise ValueError('Percentile should be less or equal than 100')
                except Exception:
                    raise Exception('Check percentilies format. Should be num;num;num...')
        self._percentiles = value

    @property
    def test_title(self):
        return self._test_title

    @test_title.setter
    def test_title(self, value):
        if not isinstance(value, str):
            raise TypeError(f'arg: test_title should be str. '
                            f'{type(value).__name__} was given')
        self._test_title = value

    @property
    def event_tags(self):
        return self._event_tags

    @event_tags.setter
    def event_tags(self, value):
        if not isinstance(value, str):
            raise TypeError(f'arg: event_tags should be str. '
                            f'{type(value).__name__} was given')
        self._event_tags = value

    def to_xml(self) -> str:
        """
        Set all parameters in xml and convert it to the string.
        :return: xml in string format
        """
        # default name and stuff setup
        element_root, xml_tree = super()._add_basics()
        element_root = element_root.find('elementProp')
        element_root = element_root.find('collectionProp')
        for element in list(element_root):
            try:
                if element.attrib['name'] == 'influxdbUrl':
                    for elem in list(element):
                        if elem.attrib['name'] == 'Argument.value' and self.influx_db_url:
                            elem.text = self.influx_db_url
                elif element.attrib['name'] == 'application':
                    for elem in list(element):
                        if elem.attrib['name'] == 'Argument.value' and self.application:
                            elem.text = self.application
                elif element.attrib['name'] == 'measurement':
                    for elem in list(element):
                        if elem.attrib['name'] == 'Argument.value' and self.measurement:
                            elem.text = self.application
                elif element.attrib['name'] == 'summaryOnly':
                    for elem in list(element):
                        if elem.attrib['name'] == 'Argument.value':
                            elem.text = str(self.summary_only).lower()
                elif element.attrib['name'] == 'samplersRegex':
                    for elem in list(element):
                        if elem.attrib['name'] == 'Argument.value' and self.samplers_regexp:
                            elem.text = self.samplers_regexp
                elif element.attrib['name'] == 'percentiles':
                    for elem in list(element):
                        if elem.attrib['name'] == 'Argument.value' and self.percentiles:
                            elem.text = self.percentiles
                elif element.attrib['name'] == 'testTitle':
                    for elem in list(element):
                        if elem.attrib['name'] == 'Argument.value' and self.test_title:
                            elem.text = self.test_title
                elif element.attrib['name'] == 'eventTags':
                    for elem in list(element):
                        if elem.attrib['name'] == 'Argument.value' and self.event_tags:
                            elem.text = self.event_tags
            except Exception:
                raise Exception(f'Unable to render xml from {type(self).__class__}')
        return tree_to_str(xml_tree, hashtree=True)
