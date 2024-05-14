import unittest
import quite6


class MyTestCase(unittest.TestCase):
    def test_signal(self):
        signal = quite6.SignalSender()
        executed = [False]

        def slot():
            self.assertEqual(True, True)
            executed[0] = True

        signal.connect(slot)

        signal.emit()
        self.assertTrue(executed[0])

    def test_signal_with_parameters(self):
        signal = quite6.SignalSender()
        executed = [False]

        def slot(a: int, b: int, c: int):
            self.assertEqual(a, 1)
            self.assertEqual(b, 2)
            self.assertEqual(c, 3)
            executed[0] = True

        signal.connect(slot)

        signal.emit(1, 2, 3)
        self.assertTrue(executed[0])

    def test_connect_with(self):
        signal = quite6.SignalSender()
        executed = [False]

        @quite6.connect_with(signal, 1, 2)
        def slot(a: int, b: int, c: int):
            self.assertEqual(a, 1)
            self.assertEqual(b, 2)
            self.assertEqual(c, 3)
            executed[0] = True

        signal.emit(3)
        self.assertTrue(executed[0])

        slot(1, 2, 3)


if __name__ == '__main__':
    unittest.main()
