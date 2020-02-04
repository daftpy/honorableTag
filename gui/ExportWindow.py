from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt
from ExportGuiFile import Ui_MainWindow
from PyQt5.QtCore import pyqtSignal


class ExportWindow(QMainWindow, Ui_MainWindow):
    csv_file_signal = pyqtSignal(str)
    csv_load = pyqtSignal(str)

    def __init__(self, *args, obj=None, **kwargs):
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.SaveCsvButton.clicked.connect(self.emit_csv_save)
        self.LoadCsvButton.clicked.connect(self.emit_load_csv)


    def emit_csv_save(self):
        self.csv_file_signal.emit(
            self.CsvFileLineEdit.text()
        )

    def emit_load_csv(self):
        self.csv_load.emit(
            self.CsvFileLineEdit.text()
        )
