import os
import unittest

import quite6


class MyTestCase(unittest.TestCase):
    def test_create_dialog_dialog(self):
        current_path = os.path.dirname(__file__)
        ui_file_path = os.path.join(current_path, 'res', '4.dialog.controller.ui')

        c = quite6.DialogUiController(None, ui_file_path)
        self.assertTrue(isinstance(c.w, quite6.Dialog))
        self.assertTrue(isinstance(c.button('quit'), quite6.PushButton))
        quite6.later(0.1, c.close)
        c.exec()

    def test_create_dialog_by_widget_ui(self):
        current_path = os.path.dirname(__file__)
        ui_file_path = os.path.join(current_path, 'res', '3.widget.controller.ui')

        class WidgetDialogController(quite6.DialogUiController):
            def __init__(self, parent=None):
                super().__init__(parent, ui_file_path)

                @quite6.connect_with(self.button('add').excited)
                def new_dialog():
                    d = WidgetDialogController(self.w)
                    quite6.later(.1, d.close)
                    d.exec()

        c = WidgetDialogController()
        self.assertTrue(isinstance(c.button('add'), quite6.PushButton))
        self.assertTrue(isinstance(c.combo('index'), quite6.ComboBox))
        self.assertTrue(isinstance(c.edit('number'), quite6.LineEdit))
        self.assertTrue(isinstance(c.list('numbers'), quite6.ListWidget))
        quite6.later(.4, c.close)
        quite6.later(.1, c.button('add').click)
        c.exec()


if __name__ == '__main__':
    unittest.main()
