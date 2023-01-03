import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QComboBox, QWidget


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.btn = QPushButton('Start', self)
        self.btn.clicked.connect(self.on_click)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(50, 50)

        self.combo = QComboBox(self)
        self.combo.addItem("driftveil_city")
        self.combo.addItem("other")
        self.combo.addItem("other2")
        self.combo.move(50, 100)

        self.combo2 = QComboBox(self)
        self.combo2.addItem("hordes")
        self.combo2.addItem("singles")
        self.combo2.addItem("fishing")
        self.combo2.move(50, 150)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('PKMN-AI')


    def on_click(self):
        if self.btn.text() == 'Start':
            self.btn.setText('Stop')
        else:
            self.btn.setText('Start')

"""if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    sys.exit(app.exec_())"""
