import pytest

from jmeter_api.listeners.simple_data_writer.elements import SimpleDataWriter


class TestSimpleDataWriter:
    def test_empty(self):
        SimpleDataWriter()

    def test_to_xml(self):
        SimpleDataWriter().to_xml()

