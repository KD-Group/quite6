import st
import quite6
import unittest


class MyTestCase(unittest.TestCase):
    def test_tab_widget_index(self):
        with quite6.EventLoop(0.1):
            tab_widget = quite6.TabWidget()
            widget_1 = quite6.Widget()
            widget_2 = quite6.Widget()
            tab_widget.addTab(widget_1, "tab_1")
            tab_widget.addTab(widget_2, "tab_2")
            tab_widget.show()
            executed = [False]

            @quite6.connect_with(tab_widget.index.changed)
            def index_changed(index):
                self.assertEqual(index, 1)
                executed[0] = True

            tab_widget.index.value = 1
            self.assertTrue(executed[0])
            tab_widget.install_check_before_switch(lambda index: index != 0)
            self.assertEqual(tab_widget.index_item.count, 2)
            self.assertEqual(tab_widget.index_item.tab_text(0), "tab_1")
            self.assertEqual(tab_widget.index_item.tab_text(1), "tab_2")


if __name__ == '__main__':
    unittest.main()
