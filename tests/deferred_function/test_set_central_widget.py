import unittest
import quite6


class MyTestCase(unittest.TestCase):
    def test_set_main_window_central_widget(self):
        before_central_widget = quite6.Widget()
        after_central_widget = quite6.Widget()
        main_window = quite6.MainWindow()
        main_window.set_central_widget(before_central_widget)
        self.assertEqual(id(before_central_widget), id(main_window.center_widget))
        main_window.set_central_widget(after_central_widget)
        self.assertEqual(id(after_central_widget), id(main_window.center_widget))

    def test_set_dock_window_central_widget(self):
        before_central_widget = quite6.Widget()
        after_central_widget = quite6.Widget()
        dock_widget = quite6.DockWidget()
        dock_widget.set_central_widget(before_central_widget)
        self.assertEqual(id(before_central_widget), id(dock_widget.center_widget))
        dock_widget.set_central_widget(after_central_widget)
        self.assertEqual(id(after_central_widget), id(dock_widget.center_widget))

    def test_set_widget_central_widget(self):
        before_central_widget = quite6.Widget()
        after_central_widget = quite6.Widget()
        contain_widget = quite6.Widget()
        contain_widget.set_central_widget(before_central_widget)
        self.assertEqual(id(before_central_widget), id(contain_widget.center_widget))
        contain_widget.set_central_widget(after_central_widget)
        self.assertEqual(id(after_central_widget), id(contain_widget.center_widget))
