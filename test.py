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

    def test_window_title(self):
        self.assertEqual(self.gui.windowTitle(), 'HonorableTag')

    def test_get_frame_retrieves_correct_frame(self):
        self.gui.FrameView.DrawScene.get_frame(5)
        self.assertEqual(self.gui.FrameView.DrawScene.current_frame, 5)

    def test_step_forward_btn_increments_one_frame(self):
        self.assertEqual(self.gui.FrameView.DrawScene.current_frame, 0)
        QTest.mouseClick(self.gui.StepForwardButton, Qt.LeftButton)
        self.assertEqual(self.gui.FrameView.DrawScene.current_frame, 1)

    def test_step_backwards_btn_increments_one_frame(self):
        self.gui.FrameView.DrawScene.get_frame(5)
        self.assertEqual(self.gui.FrameView.DrawScene.current_frame, 5)
        QTest.mouseClick(self.gui.StepBackwardButton, Qt.LeftButton)
        self.assertEqual(self.gui.FrameView.DrawScene.current_frame, 4)

    def test_big_step_forward_btn_increments_five_frames(self):
        self.assertEquals(self.gui.FrameView.DrawScene.current_frame, 0)
        QTest.mouseClick(self.gui.BigStepForwardButton, Qt.LeftButton)
        self.assertEquals(self.gui.FrameView.DrawScene.current_frame, 5)


if __name__ == "__main__":
    unittest.main()
