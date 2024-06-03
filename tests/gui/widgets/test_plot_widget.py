import os
import quite6
import unittest
import numpy as np


class TestPlotCase(unittest.TestCase):
    plot_widget = None

    def test_plot_data(self):
        with quite6.EventLoop(0.1):
            self.plot_widget = quite6.PlotWidget()
            x = np.random.random(10)
            y = np.random.random(10)
            self.plot_widget.plot(x=x, y=y)
            self.assertTrue((self.plot_widget.get_data() == np.array([x, y])).all())

            new_x = np.random.random(9)
            new_y = np.random.random(9)
            self.plot_widget.plot(x=new_x, y=new_y)
            self.assertTrue((self.plot_widget.get_data() == np.array([new_x, new_y])).all())

            add_x = np.random.random(5)
            add_y = np.random.random(5)
            old_data = self.plot_widget.get_data()
            self.plot_widget.append_plot(x=add_x, y=add_y)
            new_data = self.plot_widget.get_data()
            self.assertTrue((new_data == np.array(np.append(old_data[0], add_x)), np.append(old_data[1], add_y)))

    def test_error_plot_data(self):
        with quite6.EventLoop(0.1):
            self.plot_widget = quite6.PlotWidget()
            x = np.random.random(10)
            y = np.random.random(9)
            with self.assertRaises(Exception):
                self.plot_widget.plot(x=x, y=y)
                self.plot_widget.append_plot(x=x, y=y)

    def test_clear_data(self):
        with quite6.EventLoop(0.1):
            self.plot_widget = quite6.PlotWidget()
            x = np.random.random(10)
            y = np.random.random(10)
            self.plot_widget.plot(x=x, y=y)
            self.plot_widget.clear()
            self.assertEqual(self.plot_widget.get_data(), None)

    def test_set_labels(self):
        with quite6.EventLoop(0.1):
            self.plot_widget = quite6.PlotWidget()
            valid_labels = ['X', 'Y']
            valid_units = ['x', 'y']
            self.assertEqual(self.plot_widget.set_labels(text=valid_labels, units=valid_units), None)
            in_valid_labels = ['X', 'Y', 'Z']
            self.assertRaises(ValueError, self.plot_widget.set_labels, in_valid_labels)
            in_valid_units = ['x']
            self.assertRaises(ValueError, self.plot_widget.set_labels, valid_labels, in_valid_units)

    def test_load_plot_widget(self):
        current_path = os.path.dirname(__file__)
        ui_file_path = os.path.join(current_path, 'res', '2.plot_widget.ui')

        plot_widget_controller = quite6.DialogUiController(parent=None, ui_file=ui_file_path)
        plot_widget_controller.plot_widget('test').plot(x=np.random.random(10), y=np.random.random(10))
        timer = quite6.Timer()
        timer.timeout.connect(plot_widget_controller.close)
        timer.start(3000)
        plot_widget_controller.exec()

    def test_plot_widget_closed_signal(self):
        self.plot_widget = quite6.PlotWidget()
        executed = [False]

        @quite6.connect_with(self.plot_widget._closed)
        def is_closed():
            executed[0] = True

        quite6.later(0.01, self.plot_widget.close)
        self.plot_widget.exec()
        self.assertTrue(executed[0])


if __name__ == '__main__':
    unittest.main()
