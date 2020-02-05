from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt
from gui.ExportGuiFile import Ui_MainWindow
from PyQt5.QtCore import pyqtSignal


class ExportWindow(QMainWindow, Ui_MainWindow):
    csv_file_signal = pyqtSignal(str)
    csv_load_signal = pyqtSignal(str)
    save_to_web_signal = pyqtSignal(list)

    def __init__(self, *args, obj=None, **kwargs):
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.SaveCsvButton.clicked.connect(self.emit_csv_save)
        self.LoadCsvButton.clicked.connect(self.emit_load_csv)
        self.SaveToWebButton.clicked.connect(self.emit_save_to_web)


    def emit_csv_save(self):
        self.csv_file_signal.emit(
            self.CsvFileLineEdit.text()
        )

    def emit_load_csv(self):
        self.csv_load_signal.emit(
            self.CsvFileLineEdit.text()
        )

    def emit_save_to_web(self):
        address = self.ServerAddressLineEdit.text()
        username = self.ServerUsernameLineEdit.text()
        password = self.ServerPasswordLineEdit.text()
        repo_title = self.RepoNameLineEdit.text()
        self.save_to_web_signal.emit(
            [address, username, password, repo_title]
        )
