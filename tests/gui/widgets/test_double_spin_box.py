import os
import quite6
import unittest


class MyTestCase(unittest.TestCase):
    def test_double_spin_box_integer_property(self):
        with quite6.EventLoop(.10):
            double_spin_box = quite6.DoubleSpinBox()
            double_spin_box.show()
            times = []

            @quite6.connect_with(double_spin_box.float.changed)
            def double_spin_box_double_changed(value: float):
                if len(times) == 0:
                    self.assertEqual(value, 1.1)
                elif len(times) == 1:
                    self.assertEqual(value, 10.2)
                elif len(times) == 2:
                    self.assertEqual(value, 99.3)
                elif len(times) == 3:
                    self.assertEqual(value, 0)
                times.append(len(times))

            double_spin_box.float.value = 1.1
            double_spin_box.float.value = 10.2
            double_spin_box.float.value = 99.3
            double_spin_box.float.value = -1.4
            self.assertEqual(len(times), 4)

    def test_double_spin_box_string_property(self):
        with quite6.EventLoop(0.1):
            double_spin_box = quite6.DoubleSpinBox()
            double_spin_box.show()
            times = []

            @quite6.connect_with(double_spin_box.string.changed)
            def double_spin_box_double_changed(value: str):
                if len(times) == 0:
                    self.assertEqual(value, '1.1')
                elif len(times) == 1:
                    self.assertEqual(value, '10.2')
                elif len(times) == 2:
                    self.assertEqual(value, '99.3')
                elif len(times) == 3:
                    self.assertEqual(value, '0.0')
                times.append(len(times))

            double_spin_box.string.value = '1.1'
            double_spin_box.string.value = '10.2'
            double_spin_box.string.value = '99.3'
            double_spin_box.string.value = '-1.4'
            self.assertEqual(len(times), 4)

    def test_double_spin_in_dialog(self):
        current_path = os.path.dirname(__file__)
        ui_file_path = os.path.join(current_path, 'res', '1.double.spin.dialog.ui')

        d = quite6.load_ui(None, ui_file_path)

        def add_by_step():
            for i in range(200, 400 + 1):
                d.number_double.float.value = i / 10.0
            d.close()

        times = []

        @quite6.connect_with(d.number_double.float.changed)
        def double_changed(value: float):
            self.assertEqual(min(len(times) / 10.0 + 20.0, 40.0), value)
            times.append(len(times))

        quite6.later(0.1, add_by_step)
        d.exec()
        self.assertEqual(len(times), 200 + 1)


if __name__ == '__main__':
    unittest.main()
