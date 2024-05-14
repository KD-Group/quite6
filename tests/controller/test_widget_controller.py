import os
import unittest

import quite6


class MyTestCase(unittest.TestCase):
    def test_create_widget_dialog(self):
        current_path = os.path.dirname(__file__)
        ui_file_path = os.path.join(current_path, 'res', '3.widget.controller.ui')

        with quite6.EventLoop(timeout=.10):
            c = quite6.WidgetUiController(None, ui_file_path)
            c.show()
            self.assertTrue(isinstance(c.w, quite6.Widget))

            self.assertTrue(isinstance(c.button('add'), quite6.PushButton))
            self.assertTrue(isinstance(c.combo('index'), quite6.ComboBox))
            self.assertTrue(isinstance(c.edit('number'), quite6.LineEdit))
            self.assertTrue(isinstance(c.list('numbers'), quite6.ListWidget))


if __name__ == '__main__':
    unittest.main()
