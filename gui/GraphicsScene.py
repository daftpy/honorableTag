from sqlite3 import IntegrityError
from PyQt5.QtWidgets import QGraphicsScene
from PyQt5.QtGui import QImage, QPen, QPixmap, QColor
from PyQt5.QtCore import Qt, pyqtSignal, QRect
from SqlStorage import SqlStorage


class GraphicsScene(QGraphicsScene):
    current_frame_signal = pyqtSignal(int)
    new_tag_signal = pyqtSignal(list)

    def __init__(self, *args, **kwargs):
        super(QGraphicsScene, self).__init__(*args, **kwargs)
        self.frame_array = None
        self.current_frame = None
        self.rect_list = []  # Rect list for storage in sql
        self.sql_storage = SqlStorage()

    def get_frame(self, n):
        if len(self.rect_list) > 0:
            self.store_rects()

        # Clear the rect list for a new scene
        self.rect_list = []
        # Make sure we have a frame array loaded and we do not go out of index
        if self.frame_array and len(self.frame_array)-1 >= n and n >= 0:
            frame = self.frame_array[n]
            # Load the frame into a QImage
            q_image = QImage(
                frame,
                frame.shape[1],
                frame.shape[0],
                QImage.Format_RGB888
            )
            # Clear the scene and draw the new pixmap
            self.current_frame = n
            self.current_frame_signal.emit(n)  # Emit current frame to the gui
            self.clear()
            self.addPixmap(QPixmap(q_image))
            self.load_rects()  # Load any rects that should be in the scene
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
        # selected_class[0], class label selected_class[1] color
        self.new_tag_signal.emit(
            [new_rect, selected_class[0], selected_class[1]]
        )
        self.update()

    def load_rects(self):
        # Information is from the SQL query, so load them into widgets
        rects = self.sql_storage.get_rects(self.current_frame)
        if rects:
            for rect in rects:
                loaded_rect = QRect(
                    rect[2],
                    rect[3],
                    rect[4],
                    rect[5]
                )

                # Set pen color
                pen = QPen(QColor(rect[6]), 2, Qt.DashLine)
                self.addRect(
                    rect[2],
                    rect[3],
                    rect[4],
                    rect[5],
                    pen
                )
                # Load the rect color from the sql query
                color = QColor(rect[6])
                # rect[1] is class label
                self.new_tag_signal.emit([loaded_rect, rect[1], color])

    def store_rects(self):
        try:  # try except to skip duplicates
            for rect in self.rect_list:
                # Insert any frames in rect list into sql storage
                self.sql_storage.insert_rect_record(
                    self.current_frame,
                    rect[1],
                    rect[0].topLeft().x(),
                    rect[0].topLeft().y(),
                    rect[0].width(),
                    rect[0].height(),
                    rect[2].name()
                )
        except IntegrityError as err:
            print(err)