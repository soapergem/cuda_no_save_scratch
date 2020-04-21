from cudatext import *


class Command:
    def on_save_pre(self, ed_self):
        if ed_self.get_file_name() == "" and len(ed_self.get_text_all()) == 0:
            return False
