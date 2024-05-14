import os
import quite6


class CustomWidget(quite6.Widget):
    def paint(self, painter: quite6.Painter):
        w, _ = self.size
        painter.setFont(quite6.QFont('Courier New', 14.0))
        painter.draw_text_bottom_right(quite6.PointF(0, 0), 'So Cool!')
        painter.draw_text_bottom_left(quite6.PointF(w, 0), 'From Custom Widget')
        painter.end()


main_window = quite6.load_ui(filename=os.path.join(os.path.dirname(__file__), 'main_window.ui'))
main_window.set_central_widget(CustomWidget(parent=main_window))
main_window.exec()
