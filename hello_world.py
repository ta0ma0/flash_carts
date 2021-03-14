import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import time
import sys
import configparser
config = configparser.ConfigParser()
config.read('config.py')
x = int(config['WINDGEOMETRY']['x_win'])
y = int(config['WINDGEOMETRY']['y_win'])
width = int(config['WINDGEOMETRY']['width'])
height = int(config['WINDGEOMETRY']['height'])


def window():
   app = QApplication(sys.argv)
   widget = QWidget()

   textLabel = QLabel(widget)
   textLabel.setText("Hello World!")
   textLabel.move(110,85)

   widget.setGeometry(x, y, width, height)
   widget.setWindowTitle("This word")
   widget.setWindowOpacity(0.8)
   widget.show()
   sys.exit(app.exec_())


if __name__ == '__main__':
   window()