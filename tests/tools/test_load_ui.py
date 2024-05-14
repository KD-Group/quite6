import os
import quite6
import unittest


class MyTestCase(unittest.TestCase):
    def test_load_simple_ui(self):
        current_path = os.path.dirname(__file__)
        ui_file_path = os.path.join(current_path, 'res', '2.simple.ui.file.ui')

        addresses = set()
        for i in range(3):
            w = quite6.load_ui(None, ui_file_path)
            addresses.add(w)
            self.assertTrue(isinstance(w, quite6.Widget))

            t = quite6.Timer()
            t.timeout.connect(w.close)
            t.start(100)

            w.show()
            w.exec()
        self.assertEqual(len(addresses), 3)


if __name__ == '__main__':
    unittest.main()
