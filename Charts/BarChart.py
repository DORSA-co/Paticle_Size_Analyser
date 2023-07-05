from PySide6.QtCore import QMargins
from PySide6.QtGui import QPainter, QColor, QCursor
from PySide6.QtWidgets import QToolTip
from PySide6 import QtCharts



class BarChart(QtCharts.QChartView):
    def __init__(self, 
                parent=None,
                chart_title: str = None,
                chart_title_color: str = None,
                axisX_label: str = None,
                axisY_label: str = None,
                chart_background_color: str = None,
                bar_color: str = None,
                axis_color: str = None,
                axis_grid: bool = False,
                axisY_range: tuple = None,
                axisY_tickCount: str = 5,
                animation: bool = True,
                bar_width: float = 1,
                ):

        self.chart = QtCharts.QChart()
        super().__init__(self.chart, parent)


        self.axisX_label = axisX_label
        self.axisY_label = axisX_label
        
        self.chart.legend().setVisible(False)

        self.series = QtCharts.QBarSeries()
        self.chart.addSeries(self.series)

        if chart_title:
            self.set_chart_title(chart_title)
        if chart_title_color:
            self.set_chart_title_color(chart_title_color)

        if chart_background_color:
            self.set_background_color(chart_background_color)

        self.set_bar_color(bar_color)

        self.set_axisX_label(axisX_label)
        self.set_axisY_label(axisY_label)

        self.set_axis_color(axis_color)
        self.set_axis_grid(axis_grid)

        self.set_axisY_range(axisY_range)

        self.set_axisY_tickCount(axisY_tickCount)

        if animation:
            self.set_animation(animation)

        self.set_bar_width(bar_width)

        self.setup_chart()

    def set_chart_title(self, title):
        self.chart.setTitle(title)

    def set_chart_title_color(self, color):
        self.chart.setTitleBrush(QColor(color))

    def set_background_color(self, background_color: str) -> None:
        self.chart.setBackgroundBrush(QColor(background_color))

    def __set_axisX(self, categories):
        self.axisX = QtCharts.QBarCategoryAxis()
        if self.axisX_label:
            self.axisX.setTitleText(self.axisX_label)
        if self.axis_color:
            self.axisX.setTitleBrush(QColor(self.axis_color))
            self.axisX.setLabelsColor(QColor(self.axis_color))
        self.axisX.setGridLineVisible(self.axis_grid)
        self.axisX.append(categories)
        self.chart.setAxisX(self.axisX, self.series)  

    def __set_axisY(self, values):
        self.axisY = QtCharts.QValueAxis()
        if self.axisY_label:
            self.axisY.setTitleText(self.axisY_label)
        if self.axis_color:
            self.axisY.setTitleBrush(QColor(self.axis_color))
            self.axisY.setLabelsColor(QColor(self.axis_color))
        self.axisY.setGridLineVisible(self.axis_grid)
        if self.axisY_range:
            self.axisY.setRange(*self.axisY_range)
        else:
            self.axisY.setRange(0, max(values))
        if self.axisY_tickCount:
            self.axisY.setTickCount(self.axisY_tickCount)
        self.chart.setAxisY(self.axisY, self.series)

    def set_axisX_label(self, label):
        if label and hasattr(self, 'axisX'):
            self.axisX.setTitleText(label)

    def set_axisY_label(self, label):
        if label and hasattr(self, 'axisY'):
            self.axisY.setTitleText(label)

    def set_axis_color(self, color):
        self.axis_color = color
        if self.axis_color and hasattr(self, 'axisX') and hasattr(self, 'axisY'):
            self.axisX.setTitleBrush(QColor(self.axis_color))
            self.axisX.setLabelsColor(QColor(self.axis_color))
            self.axisY.setTitleBrush(QColor(self.axis_color))
            self.axisY.setLabelsColor(QColor(self.axis_color))

    def set_axis_grid(self, grid):
        self.axis_grid = grid
        if self.axis_grid and hasattr(self, 'axisX') and hasattr(self, 'axisY'):
            self.axisX.setGridLineVisible(self.axis_grid)
            self.axisY.setGridLineVisible(self.axis_grid)

    def set_axisY_range(self, range):
        self.axisY_range = range
        if self.axisY_range and hasattr(self, 'axisY'):
            self.axisY.setRange(*self.axisY_range)

    def set_axisY_tickCount(self, tickCount):
        self.axisY_tickCount = tickCount
        if self.axisY_tickCount and hasattr(self, 'axisY'):
            self.axisY.setTickCount(self.axisY_tickCount)

    def set_bar_width(self, bar_width):
        self.series.setBarWidth(bar_width)

    def set_bar_color(self, color):
        self.bar_color = color
        if self.bar_color and hasattr(self, 'bar_set'):
            self.bar_set.setColor(QColor(self.bar_color))

    def set_animation(self, animation):
        if animation:
            self.chart.setAnimationOptions(QtCharts.QChart.SeriesAnimations)
        else:
            self.chart.setAnimationOptions(QtCharts.QChart.NoAnimation)

    def clear_chart(self):
        self.series.clear()

    def update_chart(self, axisX_ranges, axisY_values):
        self.clear_chart()

        self.__set_axisX(axisX_ranges)
        self.__set_axisY(axisY_values)

        self.bar_set = QtCharts.QBarSet(self.axisY_label)
        for value in axisY_values:
            self.bar_set.append(value)
        self.series.append(self.bar_set)

        if self.bar_color:
            self.bar_set.setColor(QColor(self.bar_color))

        # Update the chart view
        self.update()

    def setup_chart(self):
        self.chart.setMargins(QMargins(0, 0, 0, 0))
        self.chart.setBackgroundRoundness(0)
        self.chart.setContentsMargins(-9, -9, -9, -9)
        self.chart.legend().hide()
        self.setRenderHint(QPainter.Antialiasing)
        