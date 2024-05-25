import quite6
from PySide6.QtGui import QFont


class CustomWidget(quite6.Widget):
    def paint(self, painter: quite6.Painter):
        painter.setFont(QFont('Courier New', 14))
        painter.draw_text_bottom_right(quite6.PointF(0, 0), 'Custom Widget')
        painter.end()


main_window = quite6.MainWindow()
custom_widget = CustomWidget(parent=main_window)
main_window.set_central_widget(custom_widget)
main_window.exec()
