from email.charset import QP
import time
from PySide6.QtWidgets import QMainWindow, QApplication, QFrame, QVBoxLayout, QPushButton
from Charts.BarChart import BarChart
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.bar_chart_widget = BarChart(
                    chart_title = 'TEST',
                    chart_title_color = 'white',
                    axisX_label = 'Rages',
                    axisY_label = 'Percents',
                    chart_background_color = 'black',
                    bar_color = '#0c1a66',
                    axis_color = 'white',
                    axis_grid=False,
                    axisY_range = (0, 100),
                    axisY_tickCount = 10,
                    animation = True,
                    bar_width = 1,
                )

        self.frame = QFrame()
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.bar_chart_widget)
        self.frame.setLayout(self.layout)
        self.setCentralWidget(self.frame)
        self.resize(800, 600)

        categoris = ['a', 'b', 'c', 'd', 'e', 'f']
        values = [5, 10, 20, 40, 60, 80]

        self.bar_chart_widget.update_chart(axisX_ranges=categoris, axisY_values=values)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())