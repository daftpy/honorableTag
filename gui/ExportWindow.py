from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt
from ExportGuiFile import Ui_MainWindow
from PyQt5.QtCore import pyqtSignal


class ExportWindow(QMainWindow, Ui_MainWindow):
    csv_file_signal = pyqtSignal(str)

    def __init__(self, *args, obj=None, **kwargs):
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.SaveCSVButton.clicked.connect(self.emit_csv_save)


    def emit_csv_save(self):
        self.csv_file_signal.emit(
            self.CsvFileLineEdit.text()
        )
