import random
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtGui import QColor
import pims
from av import AVError
from gui.ClassLabel import ClassLabel

def load_video_file(self):
    file_name, _ = QFileDialog.getOpenFileName(
        self,
        'QFileDialog.getOpenFileName()',
        '',
        'All Files(*);;PythonFiles(*.py)'
    )
    # Convert the file to an array of frames
    if file_name:
        frame_array = None
        try:
            frame_array = pims.Video(file_name)
        except AVError as err:
            msg = QMessageBox()
            msg.setText(
                f'Try loading a different video file. \n{err}'
            )
            msg.exec_()
            return
    
    # Return the file path and frame array
    return (file_name, frame_array)

def load_class_data(self):
    file_name, _ = QFileDialog.getOpenFileName(
        self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)"
    )
    class_labels = []
    if file_name:
        try:
            with open(file_name) as f:
                self.class_labels = [line.rstrip() for line in f.readlines()]
                for label in self.class_labels:
                    # Assign a random color
                    color = (
                        random.randrange(255),
                        random.randrange(255),
                        random.randrange(255)
                    )
                    color = QColor(color[0], color[1], color[2])
                    class_labels.append(ClassLabel(label, color=color))
        except UnicodeDecodeError as err:
            msg = QMessageBox()
            msg.setText(
                f'Try loading a different label file. \n{err}'
            )
            msg.exec_()
            return
    return class_labels
