"""

@authors Saveliy Yusufov and Kohtaro Yamakawa
"""

import sys
import json
import queue

import numpy as np
from PyQt5 import QtWidgets, QtCore
import pyqtgraph as pg

# from network import Client


class MyWidget(pg.GraphicsWindow):
    """Wrapper class for the pyqtgraph scatterplot"""

    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.mainLayout = QtWidgets.QVBoxLayout()
        self.setLayout(self.mainLayout)

        self.plotItem = self.addPlot(title="Configuration Space")
        self.plotDataItem = self.plotItem.plot([], pen=None, symbolBrush=(255, 0, 0), symbolSize=5, symbolPen=None)

        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(100)
        self.timer.start()
        self.timer.timeout.connect(self.on_new_data)

    def set_data(self, x, y):
        """Sets the new data points on the scatterplot"""
        self.plotDataItem.setData(x, y)

    def on_new_data(self):
        """Updates the scatterplot on the timer interval"""
        n = 100
        x = np.random.normal(size=n)
        y = np.random.normal(size=n)
        self.set_data(x, y)


def main():
    app = QtWidgets.QApplication([])
    pg.setConfigOptions(antialias=True)

    win = MyWidget()
    win.show()
    win.resize(800, 600)
    win.raise_()
    app.exec_()

if __name__ == "__main__":

    # Set white background and black foreground
    pg.setConfigOption('background', 'k')
    pg.setConfigOption('foreground', 'k')
    main()
