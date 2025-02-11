# PyQt5 intoduction

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My cool first GUI")
        self.setGeometry(500, 500, 500, 500) # first two arguments - where, second two how big
        self.setWindowIcon(QIcon('C:/Users/diefi/Documents/GitHub/Python_learn/icon_giliszta.png'))

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_()) # app execute method

if __name__ == "__main__":
    main()