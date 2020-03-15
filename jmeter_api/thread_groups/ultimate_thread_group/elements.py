from xml.etree.ElementTree import Element
from typing import List
from random import random

from jmeter_api.basics.thread_group.elements import BasicThreadGroup, ThreadGroupAction
from jmeter_api.basics.utils import Renderable, IncludesElements, tree_to_str


class UltimateThreadGroup(BasicThreadGroup, Renderable):

    root_element_name = 'kg.apc.jmeter.threads.UltimateThreadGroup'

    def __init__(self, *,
                 schedule: List[dict] = [],
                 on_sample_error: ThreadGroupAction = ThreadGroupAction.CONTINUE,
                 name: str = 'jp@gc - Ultimate Thread Group',
                 comments: str = '',
                 is_enabled: bool = True):
        self.schedule = schedule
        BasicThreadGroup.__init__(self,
                                  on_sample_error=on_sample_error,
                                  name=name,
                                  comments=comments,
                                  is_enabled=is_enabled)

    @property
    def schedule(self):
        return self._schedule

    @schedule.setter
    def schedule(self, value: int):
        if not isinstance(value, List):
            raise TypeError(
                f'schedule must be List[dict]. schedule {type(value)} = {value}')
        else:
            for v in value:
                if not isinstance(value, List):
                    raise TypeError(
                        f'schedule must be List[dict]. schedule {type(value)} = {value}')
                if 'thread_count' not in v or 'delay' not in v or 'startup' not in v or 'hold' not in v or 'shotdown' not in v:
                    raise ValueError(
                        f'schedule dict must contain "thread_count", "delay", "startup", "hold" and "shotdown" feilds')
                else:
                    for field in ("thread_count", "delay", "startup", "hold", "shotdown"):
                        if not isinstance(v[field], int) or v[field] < 0:
                            raise TypeError(
                                f"{field} must be positive int. {field} {type(v[field])} = {v[field]}")
            self._schedule = value
            
    def to_xml(self) -> str:
        element_root, xml_tree = super()._add_basics()

        for element in list(element_root):
            try:
                if element.attrib['name'] == 'ThreadGroup.on_sample_error':
                    element.text = self.on_sample_error.value
                elif element.attrib['name'] == 'ultimatethreadgroupdata':
                    for row in self.schedule:
                        el = Element("collectionProp", attrib={"name": str(int(random()*10000000000))})
                        for field in ("thread_count", "delay", "startup", "hold", "shotdown"):
                            sub_el = Element("stringProp", attrib={"name": str(int(random()*100000))})
                            sub_el.text = str(row[field])
                            el.append(sub_el)
                        element.append(el)
            except KeyError:
                continue
        content_root = xml_tree.find('hashTree')
        content_root.text = self._render_inner_elements()
        return tree_to_str(xml_tree)
