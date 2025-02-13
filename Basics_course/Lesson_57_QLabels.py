# PyQt5 QLabels

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)

        label = QLabel("Hello", self)
        label.setFont(QFont("Arial", 30))
        label.setGeometry(0, 0, 500, 500)
        label.setStyleSheet("color: #cf4cac;"
                            "background-color: #84f0e9;"
                            "font_weight: bold;"
                            "font_style: italic;"
                            "text_decoration: underline;")
        
        # label.setAlignment(Qt.alignTop) - Vertically top
        # label.setAlignment(Qt.AlignBottom)  - Vertically bottom
        # label.setAlignment(Qt.AlignVCenter) - Vertically Center

        # label.setAlignment(Qt.AlignRight) - Horizontally right
        # label.setAlignment(Qt.AlignLeft) - Horizontally left
        # label.setAlignment(Qt.AlignHCenter) - Horizontally center

        # label.setAlignment(Qt.AlignHCenter | Qt.AlignTop) - Center & Top
        # label.setAlignment(Qt.AlignHCenter | Qt. AlignBottom) - Center & Bottom
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) - Center - middle of screen
        label.setAlignment(Qt.AlignCenter)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()