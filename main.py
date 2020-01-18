import sys
import copy
from PyQt5.QtWidgets import QApplication, QMainWindow
from GuiFile import Ui_MainWindow
from helpers.file_helpers import load_video_file, load_class_data

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

        # Set up signals essential for updating the gui
        self.FrameView.mouse_pos_signal.connect(
            self.update_coordinates_display
        )
        self.FrameView.DrawScene.current_frame_signal.connect(
            self.update_current_frame_display
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
        print(self.FrameView.selected_class)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
