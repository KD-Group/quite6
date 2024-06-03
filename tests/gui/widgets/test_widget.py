import unittest
import quite6


class MyTestCase(unittest.TestCase):
    def test_widget_closed_signal(self):
        w = quite6.Widget()
        executed = [False]

        @quite6.connect_with(w.quite_closed)
        def is_closed():
            executed[0] = True

        quite6.later(0.01, w.close)
        w.exec()
        self.assertTrue(executed[0])


if __name__ == '__main__':
    unittest.main()
