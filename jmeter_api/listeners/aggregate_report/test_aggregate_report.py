import pytest

from jmeter_api.listeners.aggregate_report.elements import AggregateReport


class TestAggregateReport:
    def test_empty(self):
        AggregateReport()

    def test_to_xml(self):
        AggregateReport().to_xml()

