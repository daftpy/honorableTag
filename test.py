import sys
import unittest
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from main import MainWindow

app = QApplication(sys.argv)


class MainWindowTest(unittest.TestCase):
    def setUp(self):
        self.gui = MainWindow()
        self.gui.load_video('video.mp4')
        self.gui.load_classes('test.names')

    def test_window_title(self):
        self.assertEqual(self.gui.windowTitle(), 'HonorableTag')

    def test_frame_slider_values(self):
        # Frame slider max value should be the length of the frame_array
        self.assertEqual(
            len(self.gui.FrameView.DrawScene.frame_array),
            self.gui.FrameSlider.maximum()
        )

    def test_get_frame_retrieves_correct_frame(self):
        # get_scene retrieves the correct frame and sets current_Frame
        self.gui.FrameView.DrawScene.get_frame(5)
        self.assertEqual(self.gui.FrameView.DrawScene.current_frame, 5)

    def test_step_forward_btn_increments_one_frame(self):
        # Step forward takes the user forward one frame
        self.assertEqual(self.gui.FrameView.DrawScene.current_frame, 0)
        QTest.mouseClick(self.gui.StepForwardButton, Qt.LeftButton)
        self.assertEqual(self.gui.FrameView.DrawScene.current_frame, 1)

    def test_step_backward_btn_increments_one_frame(self):
        # Step backward takes the user back one frame
        self.gui.FrameView.DrawScene.get_frame(5)
        self.assertEqual(self.gui.FrameView.DrawScene.current_frame, 5)
        QTest.mouseClick(self.gui.StepBackwardButton, Qt.LeftButton)
        self.assertEqual(self.gui.FrameView.DrawScene.current_frame, 4)

    def test_big_step_forward_btn_increments_five_frames(self):
        # Big step forward takes  the user foraward 5 frames
        self.assertEqual(self.gui.FrameView.DrawScene.current_frame, 0)
        QTest.mouseClick(self.gui.BigStepForwardButton, Qt.LeftButton)
        self.assertEqual(self.gui.FrameView.DrawScene.current_frame, 5)

    def test_big_step_backward_btn_increments_five_frames(self):
        # Big step backward takes the user back 5 frames
        self.gui.FrameView.DrawScene.get_frame(5)
        self.assertEqual(self.gui.FrameView.DrawScene.current_frame, 5)
        QTest.mouseClick(self.gui.BigStepBackwardButton, Qt.LeftButton)
        self.assertEqual(self.gui.FrameView.DrawScene.current_frame, 0)

    def test_cannot_step_foward_out_of_index(self):
        # User cannot step forward out of index of frame_array
        self.gui.FrameView.DrawScene.get_frame(
            len(self.gui.FrameView.DrawScene.frame_array)-1
        )
        last_frame = self.gui.FrameView.DrawScene.current_frame
        QTest.mouseClick(self.gui.StepForwardButton, Qt.LeftButton)
        self.assertEqual(
            self.gui.FrameView.DrawScene.current_frame, last_frame
        )
        QTest.mouseClick(self.gui.BigStepForwardButton, Qt.LeftButton)
        self.assertEqual(
            self.gui.FrameView.DrawScene.current_frame, last_frame
        )

    def test_cannot_step_backward_out_index(self):
        # User cannot step backward out of index of frame_array
        self.assertEqual(self.gui.FrameView.DrawScene.current_frame, 0)
        QTest.mouseClick(self.gui.StepBackwardButton, Qt.LeftButton)
        self.assertEqual(self.gui.FrameView.DrawScene.current_frame, 0)
        QTest.mouseClick(self.gui.BigStepBackwardButton, Qt.LeftButton)
        self.assertEqual(self.gui.FrameView.DrawScene.current_frame, 0)

    def test_load_class_labels_loads_correct_number_of_labels(self):
        # User loads test.names which contains 3 classes
        self.gui.load_classes('test.names')
        self.assertEqual(self.gui.ClassLabelList.count(), 3)


if __name__ == "__main__":
    unittest.main()
