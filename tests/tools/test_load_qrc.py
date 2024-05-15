import os
import unittest

from PySide6.QtCore import QFile, QIODevice

import quite6


class MyTestCase(unittest.TestCase):
    def test_load_text_file_in_qrc(self):
        file_path = os.path.join(os.path.dirname(__file__), 'res/test.qrc')
        quite6.load_qrc(file_path)

        file_1 = QFile(':/text/test.txt')
        self.assertTrue(file_1.open(QIODevice.ReadOnly | QIODevice.Text))
        text_in_rc_file_1 = file_1.readAll()
        file_1.close()

        test_file_path = os.path.join(os.path.dirname(__file__), 'res/test.txt')
        file_2 = QFile(test_file_path)
        self.assertTrue(file_2.open(QIODevice.ReadOnly | QIODevice.Text))
        text_in_rc_file_2 = file_2.readAll()
        file_2.close()

        self.assertEqual(text_in_rc_file_1, text_in_rc_file_2)


if __name__ == '__main__':
    unittest.main()
