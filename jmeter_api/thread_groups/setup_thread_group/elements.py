from jmeter_api.basics.thread_group.elements import BasicStandartThreadGroup, ThreadGroupAction
from jmeter_api.basics.utils import Renderable, IncludesElements, tree_to_str


class SetupThreadGroup(BasicStandartThreadGroup, Renderable):

    root_element_name = 'SetupThreadGroup'

    def __init__(self, *,
                 num_threads: int = 1,
                 ramp_time: int = 0,
                 continue_forever: bool = False,
                 loops: int = None,
                 is_sheduler_enable: bool = False,
                 sheduler_duration: int = None,
                 sheduler_delay: int = None,
                 on_sample_error: ThreadGroupAction = ThreadGroupAction.CONTINUE,
                 name: str = 'setUp Thread Group',
                 comments: str = '',
                 is_enabled: bool = True,):
        BasicStandartThreadGroup.__init__(self, name=name,
                                          comments=comments,
                                          is_enabled=is_enabled,
                                          num_threads=num_threads,
                                          ramp_time=ramp_time,
                                          continue_forever=continue_forever,
                                          loops=loops,
                                          is_sheduler_enable=is_sheduler_enable,
                                          sheduler_duration=sheduler_duration,
                                          sheduler_delay=sheduler_delay,
                                          on_sample_error=on_sample_error)

    def to_xml(self) -> str:
        element_root, xml_tree = super()._add_basics()

        for element in list(element_root):
            try:
                if element.attrib['name'] == 'ThreadGroup.on_sample_error':
                    element.text = self.on_sample_error.value
                elif element.attrib['name'] == 'ThreadGroup.num_threads':
                    element.text = str(self.num_threads)
                elif element.attrib['name'] == 'ThreadGroup.ramp_time':
                    element.text = str(self.ramp_time)
                elif element.attrib['name'] == 'ThreadGroup.scheduler':
                    element.text = str(self.is_sheduler_enable).lower()
                elif element.attrib['name'] == 'ThreadGroup.duration' and self.is_sheduler_enable:
                    element.text = self.sheduler_duration
                elif element.attrib['name'] == 'ThreadGroup.delay' and self.is_sheduler_enable:
                    element.text = self.sheduler_delay
                elif element.attrib['name'] == 'ThreadGroup.main_controller':
                    for main_controller_element in list(element):
                        if main_controller_element.attrib['name'] == 'LoopController.continue_forever':
                            main_controller_element.text = str(self.continue_forever).lower()
                        elif main_controller_element.attrib['name'] == 'LoopController.loops':
                            main_controller_element.text = str(self.loops)
            except KeyError:
                continue
        content_root = xml_tree.find('hashTree')
        content_root.text = self._render_inner_elements()
        return tree_to_str(xml_tree)
