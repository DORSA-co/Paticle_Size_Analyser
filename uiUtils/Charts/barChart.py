from tkinter.messagebox import NO
from PySide6.QtCore import QMargins
from PySide6.QtGui import QPainter, QColor, QFont
from PySide6 import QtCharts

from uiUtils.Charts.chartUtils import Font

LABEL_POSITION = {
    'in_center': QtCharts.QAbstractBarSeries.LabelsPosition.LabelsCenter,
    'in_bottom': QtCharts.QAbstractBarSeries.LabelsPosition.LabelsInsideBase,
    'in_top': QtCharts.QAbstractBarSeries.LabelsPosition.LabelsInsideEnd,
    'out': QtCharts.QAbstractBarSeries.LabelsPosition.LabelsOutsideEnd,
    
}

class BarChart(QtCharts.QChartView):
    def __init__(self, 
                parent=None,
                chart_title: str = None,
                chart_title_color: str = None,
                chart_title_font: object = None,
                axisX_label: str = None,
                axisY_label: str = None,
                chart_background_color: str = None,
                bar_color: str = None,
                axis_color: str = None,
                axis_font: object = None,
                axisX_grid: bool = False,
                axisY_grid: bool = False,
                axisX_grid_color: str = None,
                axisY_grid_color: str = None,
                axisY_range: tuple = None,
                axisY_tickCount: str = 5,
                animation: bool = True,
                bar_width: float = 1,
                inner_margin = 20,
                visible_label = True,
                default_label_color = '#404040',
                label_position = 'out'
                ):

        self.chart_ = QtCharts.QChart()
        super().__init__(self.chart_, parent)

        self.default_label_color = default_label_color

        self.chart_.legend().setVisible(False)
        self.set_inner_margin(inner_margin)

        self.series = QtCharts.QBarSeries()
        self.series.setLabelsVisible(visible_label)
        self.series.setLabelsPosition(LABEL_POSITION[label_position])

        self.series.labelsPosition()

        self.chart_.addSeries(self.series)

        if chart_title:
            self.set_chart_title(chart_title)
        if chart_title_color:
            self.set_chart_title_color(chart_title_color)
        if chart_title_font:
            self.set_chart_title_font(chart_title_font)

        if chart_background_color:
            self.set_background_color(chart_background_color)

        self.set_bar_color(bar_color)

        self.set_axisX_label(axisX_label)
        self.set_axisY_label(axisY_label)

        self.set_axis_color(axis_color)
        self.set_axis_font(axis_font)
        self.set_axis_grid(axisX_grid, axisY_grid)
        self.set_axis_grid_color(axisX_grid_color, axisY_grid_color)

        self.set_axisY_range(axisY_range)

        self.set_axisY_tickCount(axisY_tickCount)

        if animation:
            self.set_animation(animation)

        self.set_bar_width(bar_width)

        self.setup_chart()

    def set_chart_title(self, title):
        self.chart_.setTitle(title)

    def set_chart_title_font(self, font):
        assert(isinstance(font, Font))
        font = QFont(font.font, font.font_size, QFont.Bold if font.bold else QFont.Normal)
        self.chart_.setTitleFont(font)

    def set_chart_title_color(self, color):
        self.chart_.setTitleBrush(QColor(color))

    def set_background_color(self, background_color: str) -> None:
        self.chart_.setBackgroundBrush(QColor(background_color))

    def __set_axisX(self, categories):
        self.axisX = QtCharts.QBarCategoryAxis()
        if self.axisX_label:
            self.axisX.setTitleText(self.axisX_label)
        if self.axis_color:
            self.axisX.setTitleBrush(QColor(self.axis_color))
            self.axisX.setLabelsColor(QColor(self.axis_color))
        if self.axis_font:
            assert(isinstance(self.axis_font, Font))
            font = QFont(self.axis_font.font, self.axis_font.font_size, QFont.Bold if self.axis_font.bold else QFont.Normal)
            self.axisX.setTitleFont(font)
        self.axisX.setGridLineVisible(self.axisX_grid)
        if self.axisX_grid_color:
            self.axisX.setGridLineColor(self.axisX_grid_color)
        self.axisX.append(categories)
        self.chart_.setAxisX(self.axisX, self.series)  

    def __set_axisY(self, values):
        self.axisY = QtCharts.QValueAxis()
        
        if self.axisY_label:
            self.axisY.setTitleText(self.axisY_label)

        if self.axis_color:
            self.axisY.setTitleBrush(QColor(self.axis_color))
            #self.axisY.setLabelsColor(QColor(self.axis_color))
        if self.axis_font:
            assert(isinstance(self.axis_font, Font))
            font = QFont(self.axis_font.font, self.axis_font.font_size, QFont.Bold if self.axis_font.bold else QFont.Normal)
            self.axisY.setTitleFont(font)
        self.axisY.setGridLineVisible(self.axisY_grid)
        if self.axisY_grid_color:
            self.axisY.setGridLineColor(self.axisY_grid_color)
        if self.axisY_range:
            self.axisY.setRange(*self.axisY_range)
        else:
            self.axisY.setRange(0, max(values))
        if self.axisY_tickCount:
            self.axisY.setTickCount(self.axisY_tickCount)
        self.chart_.setAxisY(self.axisY, self.series)

    def set_axisX_label(self, label):
        self.axisX_label = label
        if self.axisX_label and hasattr(self, 'axisX'):
            self.axisX.setTitleText(self.axisX_label)

    def set_axisY_label(self, label):
        self.axisY_label = label
        if self.axisY_label and hasattr(self, 'axisY'):
            self.axisY.setTitleText(self.axisY_label)

    def set_axis_color(self, color):
        self.axis_color = color
        if self.axis_color and hasattr(self, 'axisX') and hasattr(self, 'axisY'):
            self.axisX.setTitleBrush(QColor(self.axis_color))
            self.axisX.setLabelsColor(QColor(self.axis_color))
            self.axisY.setTitleBrush(QColor(self.axis_color))
            self.axisY.setLabelsColor(QColor(self.axis_color))

    def set_axis_font(self, font):
        self.axis_font = font
        if self.axis_font and hasattr(self, 'axisX') and hasattr(self, 'axisY'):
            assert(isinstance(self.axis_font, Font))
            font = QFont(self.axis_font.font, self.axis_font.font_size, QFont.Bold if self.axis_font.bold else QFont.Normal)
            self.axisX.setTitleFont(font)
            self.axisY.setTitleFont(font)

    def set_axis_grid(self, axisX_grid, axisY_grid):
        self.axisX_grid = axisX_grid
        self.axisY_grid = axisY_grid
        if self.axisX_grid and hasattr(self, 'axisX'):
            self.axisX.setGridLineVisible(self.axisX_grid)
        if self.axisY_grid and hasattr(self, 'axisY'):
            self.axisY.setGridLineVisible(self.axisY_grid)

    def set_axis_grid_color(self, axisX_grid_color, axisY_grid_color):
        self.axisX_grid_color = axisX_grid_color
        self.axisY_grid_color = axisY_grid_color
        if self.axisX_grid_color and hasattr(self, 'axisX'):
            self.axisX.setGridLineColor(self.axisX_grid_color)
        if self.axisY_grid and hasattr(self, 'axisY'):
            self.axisY.setGridLineColor(self.axisY_grid_color)

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
            self.chart_.setAnimationOptions(QtCharts.QChart.SeriesAnimations)
        else:
            self.chart_.setAnimationOptions(QtCharts.QChart.NoAnimation)

    def clear_chart(self):
        self.series.clear()

    def set_chart_y(self, axisY_values):
        self.clear_chart()

        self.__set_axisY(axisY_values)

        self.bar_set = QtCharts.QBarSet(self.axisY_label)
        self.bar_set.setLabelColor(QColor(self.default_label_color))
        for value in axisY_values:
            self.bar_set.append(value)
            
        self.series.append(self.bar_set)

        if self.bar_color:
            self.bar_set.setColor(QColor(self.bar_color))

        # Update the chart view
        self.update()
    
    def set_chart_x(self, axisX_ranges):
        self.__set_axisX(axisX_ranges)

    def setup_chart(self):
        self.chart_.setMargins(QMargins(0, 0, 0, 0))
        self.chart_.setBackgroundRoundness(0)
        self.chart_.setContentsMargins(-9, -9, -9, -9)
        self.chart_.legend().hide()
        self.setRenderHint(QPainter.Antialiasing)
        


    def set_inner_margin(self, border):
        if isinstance(border, int):
            self.chart_.layout().setContentsMargins(border, border, border, border)
        
        if isinstance(border, tuple):
            self.chart_.layout().setContentsMargins(*border)