import unittest
from PySide6.QtCore import QRect, Qt
from PySide6.QtGui import QFont
from quite6 import *


class TestPainterChart(Widget):
    def __init__(self, *args):
        super().__init__(*args)
        self.label_x = '时间 [μs]'
        self.label_y = '电压 [V]'
        self.setMinimumSize(300, 150)

    def paint(self, painter: Painter):
        painter.setFont(QFont('微软雅黑', 13))
        w = self.width()
        h = self.height()
        text_width = int(30 * scaling.ratio)
        text_height = int(20 * scaling.ratio)

        # draw title and labels #
        painter.drawText(QRect(0, h - text_height, w, text_height), Qt.AlignmentFlag.AlignCenter, self.label_x)
        # translate and rotate for paint vertical text
        painter.save()
        painter.translate(0, h)
        painter.rotate(-90)
        painter.drawText(QRect(0, 0, h, text_height), Qt.AlignmentFlag.AlignCenter, self.label_y)
        painter.restore()

        painter.draw_text_bottom(PointF(w / 2, h / 2), "bottom", margin=2)
        painter.draw_text_bottom_left(PointF(w / 4, h / 2), "bottom_left", margin=2)
        painter.draw_text_bottom_right(PointF(3 * w / 4, h / 2), "bottom_right", margin=2)
        painter.draw_text_left(PointF(w / 4, h / 4), "left", margin=2)
        painter.draw_text_left(PointF(3 * w / 4, h / 4), "right", margin=2)
        painter.draw_text_top(PointF(w / 2, h / 8), "top", margin=2)
        painter.draw_text_top_left(PointF(w / 8, h / 8), "top", margin=2)


class MyTestCase(unittest.TestCase):
    def test_painter(self):
        try:
            with EventLoop(5):
                painter_chart = TestPainterChart()
                painter_chart.show()
        except Exception as e:
            self.fail(f"Failed to test painter, exception: {e}")


if __name__ == '__main__':
    unittest.main()
