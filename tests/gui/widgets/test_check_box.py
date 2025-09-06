import unittest
import quite6


class MyTestCase(unittest.TestCase):
    def test_check_box_text(self):
        with quite6.EventLoop(0.1):
            check_box = quite6.CheckBox()
            check_box.show()
            times = []

            @quite6.connect_with(check_box.string.changed)
            def text_changed(text):
                if len(times) == 0:
                    self.assertEqual(text, 'first')
                elif len(times) == 1:
                    self.assertEqual(text, 'second')
                times.append(len(times))

            check_box.string.value = 'first'
            check_box.string.value = 'second'
            self.assertEqual(len(times), 2)

    def test_check_box_triggered(self):
        with quite6.EventLoop(0.1):
            check_box = quite6.CheckBox()
            check_box.show()
            times = []

            @quite6.connect_with(check_box.excited)
            def check_box_clicked():
                if len(times) == 0:
                    self.assertEqual(check_box.index.value, 1)
                    self.assertTrue(check_box.isChecked())
                elif len(times) == 1:
                    self.assertEqual(check_box.index.value, 0)
                    self.assertFalse(check_box.isChecked())
                times.append(len(times))

            check_box.click()
            check_box.click()
            self.assertEqual(len(times), 2)


if __name__ == '__main__':
    unittest.main()
