import pytest

from jmeter_api.listeners.view_results_tree.elements import ViewResultsTree


class TestViewResultsTree:
    def test_empty(self):
        ViewResultsTree()

    def test_to_xml(self):
        ViewResultsTree().to_xml()

