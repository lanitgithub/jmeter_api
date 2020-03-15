import pytest

from jmeter_api.listeners.summary_report.elements import SummaryReport


class TestSummaryReport:
    def test_empty(self):
        SummaryReport()

    def test_to_xml(self):
        SummaryReport().to_xml()

