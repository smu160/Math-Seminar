"""

@authors Saveliy Yusufov and Kohtaro Yamakawa
"""

import sys
import json
import queue

import numpy as np
from PyQt5 import QtWidgets, QtCore
import pyqtgraph as pg
from network import Client


class MyWidget(pg.GraphicsWindow):
    """Wrapper class for the pyqtgraph scatterplot"""

    def __init__(self, data_queue, parent=None):
        super().__init__(parent=parent)

        self.mainLayout = QtWidgets.QVBoxLayout()
        self.setLayout(self.mainLayout)

        self.plotItem = self.addPlot(title="Configuration Space")

        # Adjust plot to only show [0, 2pi] on both axes
        self.plotItem.setRange(xRange=[0, 6.3], yRange=[0, 6.3])

        self.plotItem.showGrid(x=True, y=True, alpha=None)

        self.plotDataItem = self.plotItem.plot([], pen=None, symbolBrush=(255, 0, 0), symbolSize=10, symbolPen=None)

        self.data_queue = data_queue

        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(10)
        self.timer.start()
        self.timer.timeout.connect(self.on_new_data)

    def set_data(self, data):
        """Sets the new data points on the scatterplot"""
        x, y = data
        x = [x]
        y = [y]
        self.plotDataItem.setData(x, y)

    def on_new_data(self):
        """Updates the scatterplot on the timer interval"""
        try:
            data = self.data_queue.get(block=False)
        except queue.Empty:
            return

        data = json.loads(data)
        self.set_data(data)


def main():
    app = QtWidgets.QApplication([])
    pg.setConfigOptions(antialias=True)

    data_queue = queue.Queue()
    _ = Client("localhost", 10000, data_queue)

    win = MyWidget(data_queue)
    win.show()
    win.resize(800, 600)
    win.raise_()
    sys.exit(app.exec_())

if __name__ == "__main__":

    # Set white background and black foreground
    pg.setConfigOption('background', 'k')
    pg.setConfigOption('foreground', 'w')
    main()
