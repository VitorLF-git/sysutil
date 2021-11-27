import psutil
import platform
from gui import *
from datetime import datetime

import utils

app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
app.exec_()