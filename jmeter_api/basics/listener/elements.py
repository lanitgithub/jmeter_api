import logging

from abc import ABC
from os import path

from jmeter_api.basics.element.elements import BasicElement
from jmeter_api.basics.utils import Renderable, tree_to_str


class BasicListener(BasicElement, ABC):

    def __init__(self,
                 name: str = 'BasicElement',
                 comments: str = '',
                 is_enabled: bool = True
                 ):
        super().__init__(name, comments, is_enabled)


class ResultCollector(BasicListener, Renderable, ABC):
    
    root_element_name = 'ResultCollector'
    TEMPLATE = 'result_collector_template.xml'

    def __init__(self,
                 guiclass: str,
                 error_logging: bool = False,
                 filename: str = None,
                 time: bool = True,
                 latency: bool = True,
                 timestamp: bool = True,
                 success: bool = True,
                 label: bool = True,
                 code: bool = True,
                 message: bool = True,
                 thread_name: bool = True,
                 data_type: bool = True,
                 encoding: bool = False,
                 assertions: bool = False,
                 subresults: bool = True,
                 response_data: bool = False,
                 sampler_data: bool = False,
                 xml: bool = False,
                 field_names: bool = True,
                 response_headers: bool = False,
                 request_headers: bool = False,
                 response_data_on_error: bool = False,
                 save_assertion_results_failure_message: bool = False,
                 bytes_: bool = True,
                 sent_bytes: bool = True,
                 url: bool = True,
                 thread_counts: bool = True,
                 idle_time: bool = True,
                 connect_time: bool = True,
                 name: str = 'BasicResultCollector',
                 comments: str = '',
                 is_enabled: bool = True
                 ):
        BasicListener.__init__(
            self, name=name, comments=comments, is_enabled=is_enabled)
        self.guiclass = guiclass
        self.error_logging = error_logging
        self.filename = filename
        self.time = time
        self.latency = latency
        self.timestamp = timestamp
        self.success = success
        self.label = label
        self.code = code
        self.message = message
        self.thread_name = thread_name
        self.data_type = data_type
        self.encoding = encoding
        self.assertions = assertions
        self.subresults = subresults
        self.response_data = response_data
        self.sampler_data = sampler_data
        self.xml = xml
        self.field_names = field_names
        self.response_headers = response_headers
        self.request_headers = request_headers
        self.response_data_on_error = response_data_on_error
        self.save_assertion_results_failure_message = save_assertion_results_failure_message
        self.bytes_ = bytes_
        self.sent_bytes = sent_bytes
        self.url = url
        self.thread_counts = thread_counts
        self.idle_time = idle_time
        self.connect_time = connect_time

    @property
    def guiclass(self) -> str:
        return self._guiclass

    @guiclass.setter
    def guiclass(self, value):
        if not isinstance(value, str):
            raise TypeError(
                f'guiclass must be str. {type(value).__name__} was given')
        self._guiclass = value
        
    @property
    def filename(self) -> str:
        return self._filename

    @filename.setter
    def filename(self, value):
        if not value is None:
            if not isinstance(value, str):
                raise TypeError(
                    f'filename must be str. {type(value).__name__} was given')
            if not path.isfile(value):
                raise ValueError(f'file {value} not exist')
            self._filename = value
        else:
            self._filename = ''      
        
    @property
    def error_logging(self) -> str:
        return self._error_logging

    @error_logging.setter
    def error_logging(self, value):
        if not isinstance(value, bool):
            raise TypeError(
                f'error_logging must be bool. {type(value).__name__} was given')
        self._error_logging = str(value).lower()

    @property
    def time(self) -> str:
        return self._time

    @time.setter
    def time(self, value):
        if not isinstance(value, bool):
            raise TypeError(
                f'time must be bool. {type(value).__name__} was given')
        self._time = str(value).lower()

    
    @property
    def latency(self) -> str:
        return self._latency

    @latency.setter
    def latency(self, value):
        if not isinstance(value, bool):
            raise TypeError(
                f'latency must be bool. {type(value).__name__} was given')
        self._latency = str(value).lower()
        
    @property
    def timestamp(self) -> str:
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value):
        if not isinstance(value, bool):
            raise TypeError(
                f'timestamp must be bool. {type(value).__name__} was given')
        self._timestamp = str(value).lower()
        
    @property
    def success(self) -> str:
        return self._success

    @success.setter
    def success(self, value):
        if not isinstance(value, bool):
            raise TypeError(
                f'success must be bool. {type(value).__name__} was given')
        self._success = str(value).lower()
        
    @property
    def label(self) -> str:
        return self._label

    @label.setter
    def label(self, value):
        if not isinstance(value, bool):
            raise TypeError(
                f'label must be bool. {type(value).__name__} was given')
        self._label = str(value).lower()
        
    @property
    def code(self) -> str:
        return self._code

    @code.setter
    def code(self, value):
        if not isinstance(value, bool):
            raise TypeError(
                f'per_user must be bool. {type(value).__name__} was given')
        self._code = str(value).lower()
        
    @property
    def message(self) -> str:
        return self._message

    @message.setter
    def message(self, value):
        if not isinstance(value, bool):
            raise TypeError(
                f'message must be bool. {type(value).__name__} was given')
        self._message = str(value).lower()
        
    @property
    def thread_name(self) -> str:
        return self._thread_name

    @thread_name.setter
    def thread_name(self, value):
        if not isinstance(value, bool):
            raise TypeError(
                f'thread_name must be bool. {type(value).__name__} was given')
        self._thread_name = str(value).lower()
        
    @property
    def data_type(self) -> str:
        return self._data_type

    @data_type.setter
    def data_type(self, value):
        if not isinstance(value, bool):
            raise TypeError(
                f'data_type must be bool. {type(value).__name__} was given')
        self._data_type = str(value).lower()
        
    @property
    def encoding(self) -> str:
        return self._encoding

    @encoding.setter
    def encoding(self, value):
        if not isinstance(value, bool):
            raise TypeError(
                f'encoding must be bool. {type(value).__name__} was given')
        self._encoding = str(value).lower()
        
    @property
    def assertions(self) -> str:
        return self._assertions

    @assertions.setter
    def assertions(self, value):
        if not isinstance(value, bool):
            raise TypeError(
                f'assertions must be bool. {type(value).__name__} was given')
        self._assertions = str(value).lower()
        
    @property
    def subresults(self) -> str:
        return self._subresults

    @subresults.setter
    def subresults(self, value):
        if not isinstance(value, bool):
            raise TypeError(
                f'subresults must be bool. {type(value).__name__} was given')
        self._subresults = str(value).lower()
        
    @property
    def response_data(self) -> str:
        return self._response_data

    @response_data.setter
    def response_data(self, value):
        if not isinstance(value, bool):
            raise TypeError(
                f'response_data must be bool. {type(value).__name__} was given')
        self._response_data = str(value).lower()
        
    @property
    def sampler_data(self) -> str:
        return self._sampler_data

    @sampler_data.setter
    def sampler_data(self, value):
        if not isinstance(value, bool):
            raise TypeError(
                f'sampler_data must be bool. {type(value).__name__} was given')
        self._sampler_data = str(value).lower()
        
    @property
    def xml(self) -> str:
        return self._xml

    @xml.setter
    def xml(self, value):
        if not isinstance(value, bool):
            raise TypeError(
                f'xml must be bool. {type(value).__name__} was given')
        self._xml = str(value).lower()
        
    @property
    def field_names(self) -> str:
        return self._field_names

    @field_names.setter
    def field_names(self, value):
        if not isinstance(value, bool):
            raise TypeError(
                f'field_names must be bool. {type(value).__name__} was given')
        self._field_names = str(value).lower()
        
    @property
    def response_headers(self) -> str:
        return self._response_headers

    @response_headers.setter
    def response_headers(self, value):
        if not isinstance(value, bool):
            raise TypeError(
                f'response_headers must be bool. {type(value).__name__} was given')
        self._response_headers = str(value).lower()
        
    @property
    def request_headers(self) -> str:
        return self._request_headers

    @request_headers.setter
    def request_headers(self, value):
        if not isinstance(value, bool):
            raise TypeError(
                f'request_headers must be bool. {type(value).__name__} was given')
        self._request_headers = str(value).lower()
        
    @property
    def response_data_on_error(self) -> str:
        return self._response_data_on_error

    @response_data_on_error.setter
    def response_data_on_error(self, value):
        if not isinstance(value, bool):
            raise TypeError(
                f'response_data_on_error must be bool. {type(value).__name__} was given')
        self._response_data_on_error = str(value).lower()
        
    @property
    def save_assertion_results_failure_message(self) -> str:
        return self._save_assertion_results_failure_message

    @save_assertion_results_failure_message.setter
    def save_assertion_results_failure_message(self, value):
        if not isinstance(value, bool):
            raise TypeError(
                f'save_assertion_results_failure_message must be bool. {type(value).__name__} was given')
        self._save_assertion_results_failure_message = str(value).lower()
        
    @property
    def bytes_(self) -> str:
        return self._bytes_

    @bytes_.setter
    def bytes_(self, value):
        if not isinstance(value, bool):
            raise TypeError(
                f'bytes_ must be bool. {type(value).__name__} was given')
        self._bytes_ = str(value).lower()
        
    @property
    def sent_bytes(self) -> str:
        return self._sent_bytes

    @sent_bytes.setter
    def sent_bytes(self, value):
        if not isinstance(value, bool):
            raise TypeError(
                f'sent_bytes must be bool. {type(value).__name__} was given')
        self._sent_bytes = str(value).lower()
        
    @property
    def url(self) -> str:
        return self._url

    @url.setter
    def url(self, value):
        if not isinstance(value, bool):
            raise TypeError(
                f'url must be bool. {type(value).__name__} was given')
        self._url = str(value).lower()
        
    @property
    def thread_counts(self) -> str:
        return self._thread_counts

    @thread_counts.setter
    def thread_counts(self, value):
        if not isinstance(value, bool):
            raise TypeError(
                f'thread_counts must be bool. {type(value).__name__} was given')
        self._thread_counts = str(value).lower()
        
    @property
    def idle_time(self) -> str:
        return self._idle_time

    @idle_time.setter
    def idle_time(self, value):
        if not isinstance(value, bool):
            raise TypeError(
                f'idle_time must be bool. {type(value).__name__} was given')
        self._idle_time = str(value).lower()
        
    @property
    def connect_time(self) -> str:
        return self._connect_time

    @connect_time.setter
    def connect_time(self, value):
        if not isinstance(value, bool):
            raise TypeError(
                f'connect_time must be bool. {type(value).__name__} was given')
        self._connect_time = str(value).lower()
 
    def to_xml(self) -> str:
        element_root, xml_tree = super()._add_basics()
        element_root.attrib['guiclass'] = self.guiclass
        
        for element in list(element_root):
            try:
                if element.tag == 'objProp':
                    for el in element[-1]:
                        if el.tag == 'time':
                            el.text = self.time
                        elif el.tag == 'latency':
                            el.text = self.latency
                        elif el.tag == 'timestamp':
                            el.text = self.timestamp
                        elif el.tag == 'success':
                            el.text = self.success
                        elif el.tag == 'label':
                            el.text = self.label
                        elif el.tag == 'code':
                            el.text = self.code
                        elif el.tag == 'message':
                            el.text = self.message
                        elif el.tag == 'threadName':
                            el.text = self.thread_name
                        elif el.tag == 'dataType':
                            el.text = self.data_type
                        elif el.tag == 'encoding':
                            el.text = self.encoding
                        elif el.tag == 'assertions':
                            el.text = self.assertions
                        elif el.tag == 'subresults':
                            el.text = self.subresults
                        elif el.tag == 'responseData':
                            el.text = self.response_data
                        elif el.tag == 'samplerData':
                            el.text = self.sampler_data
                        elif el.tag == 'xml':
                            el.text = self.xml
                        elif el.tag == 'fieldNames':
                            el.text = self.field_names
                        elif el.tag == 'responseHeaders':
                            el.text = self.response_headers
                        elif el.tag == 'requestHeaders':
                            el.text = self.request_headers
                        elif el.tag == 'responseDataOnError':
                            el.text = self.response_data_on_error
                        elif el.tag == 'saveAssertionResultsFailureMessage':
                            el.text = self.save_assertion_results_failure_message
                        elif el.tag == 'bytes':
                            el.text = self.bytes_
                        elif el.tag == 'sentBytes':
                            el.text = self.sent_bytes
                        elif el.tag == 'url':
                            el.text = self.url
                        elif el.tag == 'threadCounts':
                            el.text = self.thread_counts
                        elif el.tag == 'idleTime':
                            el.text = self.idle_time
                        elif el.tag == 'connectTime':
                            el.text = self.connect_time
                elif element.attrib['name'] == 'ResultCollector.error_logging':
                    element.text = self.error_logging
                elif element.attrib['name'] == 'filename':
                    element.text = self.filename
            except KeyError:
                logging.error(
                    f'Unable to properly convert {self.__class__} to xml.')
        return tree_to_str(xml_tree)
