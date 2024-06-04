import unittest

import quite6


class MyTestCase(unittest.TestCase):
    def test_line_edit_text(self):
        with quite6.EventLoop(0.1):
            line_edit = quite6.LineEdit()
            line_edit.show()
            times = []

            @quite6.connect_with(line_edit.string.changed)
            def text_changed(text):
                if len(times) == 0:
                    self.assertEqual(text, 'first')
                elif len(times) == 1:
                    self.assertEqual(text, 'second')
                times.append(len(times))

            line_edit.string.value = 'first'
            line_edit.string.value = 'second'
            self.assertEqual(len(times), 2)

    def test_line_edit_return_pressed(self):
        with quite6.EventLoop(0.1):
            line_edit = quite6.LineEdit()
            line_edit.show()
            times = []

            @quite6.connect_with(line_edit.excited)
            def return_pressed():
                times.append(len(times))

            line_edit.returnPressed.emit()
            line_edit.returnPressed.emit()
            self.assertEqual(len(times), 2)


if __name__ == '__main__':
    unittest.main()
