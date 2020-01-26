import random
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtGui import QColor
from PyQt5.QtCore import QRect
import pims
from av import AVError
from gui.ClassLabel import ClassLabel
from PIL import Image
from os import path, mkdir
import shutil


def load_video_file(self, videofile=None):
    if videofile:
        # For testing purposes
        frame_array = pims.Video(videofile)
        return(videofile, frame_array)
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
            # Return the file path and frame array
            frame_array = pims.Video(file_name)
            return (file_name, frame_array)
        except AVError as err:
            msg = QMessageBox()
            msg.setText(
                f'Try loading a different video file. \n{err}'
            )
            msg.exec_()
            return err


def load_class_data(self, class_file=None):
    if class_file:
        file_name = class_file
    else:
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "QFileDialog.getOpenFileName()",
            "",
            "All Files (*);;Python Files (*.py)"
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


def export_frames_yolo(self, sql_rows, class_list, frame_array):
    if not path.exists('output'):
        mkdir('output')
    else:
        shutil.rmtree('output')
        mkdir('output')
    # Get the number associated with the class_label for export format
    values = list(range(len(class_list)))
    # Break off the class name, remove color, zip it with its relative value
    value_list = {k.split(' - ')[0]: v for (k, v) in zip(class_list, values)}
    for row in sql_rows:
        img = Image.fromarray(frame_array[row[0]], 'RGB')
        img.save(f'output/{row[0]}_image.jpeg')
        # Turn it into a qrect for quick maths
        rect = QRect(row[2], row[3], row[4], row[5])
        frame = frame_array[row[0]]
        # Get yolo format from frame and rect dimensions
        yolo_format_text = yolo_format(frame, rect)
        f = open(f'output/{row[0]}.txt', 'a+')
        # row[1] is the class name. Use it as a key to get a value from
        # the value list for the corresponding class integer
        f.write(f'{value_list[row[1]]} {" ".join(yolo_format_text)}\n')
        f.close()


def yolo_format(frame, rect):
    x_center = float(
        (rect.topLeft().x() + rect.bottomRight().x()) / (2.0 * frame.shape[1])
    )
    y_center = float(
        (rect.topLeft().y() + rect.bottomRight().y()) / (2.0 * frame.shape[0])
    )
    x_width = float(rect.width()) / frame.shape[1]
    y_height = float(rect.height()) / frame.shape[0]
    items = map(str, [x_center, y_center, x_width, y_height])
    return list(items)
