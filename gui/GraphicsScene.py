from PyQt5.QtWidgets import QGraphicsScene
from PyQt5.QtGui import QImage, QPen, QPixmap
from PyQt5.QtCore import Qt, pyqtSignal


class GraphicsScene(QGraphicsScene):
    bbox_rect = pyqtSignal([list])
    current_frame_signal = pyqtSignal(int)
    def __init__(self, *args, **kwargs):
        super(QGraphicsScene, self).__init__(*args, **kwargs)
        self.frame_array = None
        self.current_frame = None
        self.rect_list = [] # Rect list for storage in sql

    def get_frame(self, n):
        # Make sure we have a frame array loaded and we do not go out of index
        if self.frame_array and len(self.frame_array)-1 >= n and n >= 0:
            frame = self.frame_array[n]
            # Load the frame into a QImage
            q_image = QImage (
                frame,
                frame.shape[1],
                frame.shape[0],
                QImage.Format_RGB888
            )
            # Clear the scene and draw the new pixmap
            self.current_frame = n
            self.current_frame_signal.emit(n) # Emit current frame to the gui
            self.clear()
            self.addPixmap(QPixmap(q_image))
            self.update()


    def new_rect(self, new_rect, selected_class):
        # Set the pen to the selected class color
        pen = QPen(selected_class[1], 2, Qt.DashLine)
        self.addRect(
            new_rect.topLeft().x(),
            new_rect.topLeft().y(),
            new_rect.width(),
            new_rect.height(),
            pen
        )
        # Add to the rect list for further sql storage
        self.rect_list.append(
            [new_rect, selected_class[0], selected_class[1]]
        )
        self.update()

    def mouseMoveEvent(self, event):
        print(event)