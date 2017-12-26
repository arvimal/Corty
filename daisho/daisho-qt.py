#!/usr/bin/env python3

__author__ = "Vimal A.R"
__version__ = "v0.1"
__license__ = "GNU GPL v2.0"
__copyright__ = "(c) 2015 Vimal A.R"
__email__ = "arvimal at yahoo dot in"

import sys
from PySide.QtCore import Qt
from PySide.QtGui import QApplication, QLabel


if __name__ == '__main__':
    myApp = QApplication(sys.argv)

    appLabel = QLabel()
    appLabel.setText(
        "Daisho - Your TO-DO manager\n")
    appLabel.setText("Daisho\n")
    appLabel.setAlignment(Qt.AlignCenter)
    appLabel.setWindowTitle("Daisho")
    appLabel.setGeometry(170, 100, 1200, 800)
    appLabel.show()

    myApp.exec_()
    sys.exit()
