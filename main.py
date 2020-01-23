import sys
import re
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem
from PyQt5.QtCore import Qt
from GuiFile import Ui_MainWindow
from helpers.file_helpers import load_video_file, load_class_data, export_frames_yolo
from gui.ClassLabel import ClassLabel

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, *args, obj=None, **kwargs):
        QMainWindow.__init__(self)
        
        self.setupUi(self)

        # Set up gui connections
        self.LoadVideoButton.clicked.connect(self.load_video)
        self.LoadLabelsButton.clicked.connect(self.load_classes)
        self.StepForwardButton.clicked.connect(
            lambda: self.step_forward(1)
        )
        self.BigStepForwardButton.clicked.connect(
            lambda: self.step_forward(5)
        )
        self.StepBackwardButton.clicked.connect(
            lambda: self.step_backwards(1)
        )
        self.BigStepBackwardButton.clicked.connect(
            lambda: self.step_backwards(5)
        )
        self.FrameSlider.valueChanged.connect(
            lambda n: self.update_current_frame_display(n-1)
        )
        self.FrameSlider.sliderReleased.connect(
            lambda: self.FrameView.DrawScene.get_frame(
                self.FrameSlider.value()-1
            )
        )
        self.ClassLabelList.itemClicked.connect(self.select_class)
        self.TaggedFrameList.itemClicked.connect(self.get_tagged_frame)
        self.ExportFramesButton.clicked.connect(self.export_frames)

        # Set up signals essential for updating the gui
        self.FrameView.mouse_pos_signal.connect(
            self.update_coordinates_display
        )
        self.FrameView.DrawScene.current_frame_signal.connect(
            self.update_current_frame_display
        )
        self.FrameView.DrawScene.new_tag_signal.connect(
            self.update_tags_list
        )
        self.FrameView.remove_rect_signal.connect(
            self.remove_from_tags_list
        )

    def load_video(self):
        try:
            # None type returned if failed to load file
            f_path, frame_array = load_video_file(self)
        except:
            # Error handled in the helper.
            return
        self.VideoPathLabel.setText(
            f'<b>Path: </b> {f_path}'
        )
        self.TotalFramesLabel.setText(
            f'<b>Total Frames: </b> {len(frame_array)}'
        )
        self.FrameSlider.setMaximum(len(frame_array))
        self.FrameView.DrawScene.frame_array = frame_array
        self.FrameView.DrawScene.get_frame(0)

    def load_classes(self):
        # None type is returned if failed to load file
        class_labels = load_class_data(self)
        if class_labels:
            # Iterate through class_labels and activate each label
            for label in class_labels:
                # Add the color name to the label text and add it to the list
                label.add_color_text()
                self.ClassLabelList.addItem(label)
        return

    def update_coordinates_display(self, x, y):
        # Slot for xy_coords, updates x,y coord display every mouse_pos emit
        self.XCordLabel.setText(f'<b>X:</b> {x}')
        self.YCordLabel.setText(f'<b>Y:</b> {y}')

    def update_current_frame_display(self, n):
        # Updates our frame counter every current_frame_signal emit
        self.CurrentFrameLabel.setText(
            f'{n+1}/{len(self.FrameView.DrawScene.frame_array)}'
        )
        self.TagsFrameList.clear()
        

    def step_forward(self, n):
        self.FrameView.DrawScene.get_frame(
            self.FrameView.DrawScene.current_frame + n
        )

    def step_backwards(self, n):
        self.FrameView.DrawScene.get_frame(
            self.FrameView.DrawScene.current_frame - n
        )

    def select_class(self, class_label):
        # Take the color off the label text and give it to the frame view
        # to make sure the right color is being drawn
        class_name = class_label.text().split(' - ')
        selected_class = (class_name[0], class_label.color)
        self.FrameView.selected_class = selected_class

    def update_tags_list(self, rect):
        # Add rect to tags in frame list
        exists = self.TagsFrameList.findItems(
            f'{rect[1][0]}, {str(rect[0].getRect())}', Qt.MatchExactly
        )
        if len(exists) == 0:
            self.TagsFrameList.addItem(
                ClassLabel(
                    class_label=str(rect[1]),
                    color=(rect[2].name()),
                    rect=(rect[0].getRect())
                )
            )
        # If frame is not in the TaggedFrameList already, add it
        exists = self.TaggedFrameList.findItems(
            f'Frame: {self.FrameView.DrawScene.current_frame + 1}', Qt.MatchExactly
        )
        if len(exists) == 0:
            self.TaggedFrameList.addItem(
                QListWidgetItem(f'Frame: {self.FrameView.DrawScene.current_frame + 1}')
            )
        # Order items in TaggedFrameList
        exists = self.TaggedFrameList.findItems(
            'Frame:', Qt.MatchContains
        )
        frame_list = [str(frame_title.text()) for frame_title in exists]
        ordered_frame_list = sorted(frame_list, key=lambda h: int(h[7:]))
        self.TaggedFrameList.clear()
        self.TaggedFrameList.addItems(ordered_frame_list)

    def remove_from_tags_list(self, rect):
        # Find the tag in the TagsFrameList by finding the rect shape
        exists = self.TagsFrameList.findItems(
            f'({rect.topLeft().x()}, {rect.topLeft().y()}, {rect.width()}, {rect.height()})', Qt.MatchContains
        )
        if len(exists) != 0:
            # If the tag exists, grab the item row and remove it
            item = self.TagsFrameList.row(exists[0])
            self.TagsFrameList.takeItem(
                item
            )
        if self.TagsFrameList.count() == 0:
            exists = self.TaggedFrameList.findItems(
                f'Frame: {self.FrameView.DrawScene.current_frame + 1}', Qt.MatchExactly
            )
            if exists:
                item = self.TaggedFrameList.row(exists[0])
                self.TaggedFrameList.takeItem(item)

    def get_tagged_frame(self, frame_item):
        frame = int(re.search(r'\d+', frame_item.text()).group()) - 1
        self.FrameView.DrawScene.get_frame(frame)

    def export_frames(self):
        rows = self.FrameView.DrawScene.sql_storage.get_all_rects()
        class_list = [str(self.ClassLabelList.item(i).text()) for i in range(self.ClassLabelList.count())]
        export_frames_yolo(self, rows, class_list, self.FrameView.DrawScene.frame_array)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
