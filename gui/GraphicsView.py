from PyQt5.QtWidgets import QGraphicsView
from PyQt5.QtCore import Qt, QEvent, pyqtSignal, QRect
from PyQt5.QtGui import QPainter, QPen
from gui.GraphicsScene import GraphicsScene


class GraphicsView(QGraphicsView):
    mouse_pos_signal = pyqtSignal(int, int)
    def __init__(self, parent=None):
        super(GraphicsView, self).__init__(parent)
        # Create and set scene
        self.DrawScene = GraphicsScene()
        self.setScene(self.DrawScene)
        # Mouse position for the scene being displayed
        self.mouse_scene_pos = None
        # Mouse position used for drawing crosshairs
        self.mouse_view_pos = None
        # Mouse position storage used for drawing rects and moving viewport
        self.prev_pos = None
        self.selected_class = None


    def mouseMoveEvent(self, event):
        # Update mouse positions and update the viewport
        # to draw our crosshairs
        self.mouse_view_pos = event.pos()
        self.mouse_scene_pos = self.mapToScene(event.pos())
        self.mouse_pos_signal.emit(
            self.mouse_scene_pos.x(),
            self.mouse_scene_pos.y()
        )
        # Update the viewport on the GraphicsView to trigger
        # paint event for the crosshairs
        self.viewport().update()

    def mousePressEvent(self, event):
        # Set the prev_pos so we can start rendering a temp rec
        # for more accurate drawing for the user
        if event.button() == Qt.LeftButton:
            self.prev_pos = self.mapToScene(event.pos())

    def mouseReleaseEvent(self, event):
        # Reset the prev_pos so we stop drawing the temp rec
        # and render the new rect
        if event.button() == Qt.LeftButton:
            # Makes sure prev_pos is set before
            if self.prev_pos:
                new_rect = QRect(
                    self.prev_pos.toPoint(), self.mapToScene(event.pos()).toPoint()
                )
                self.DrawScene.new_rect(new_rect, self.selected_class)
                self.prev_pos = None
        self.viewport().update()

    def paintEvent(self, event):
        super().paintEvent(event)
        # Creates our crosshairs to help create more accurate bounding boxes
        painter = QPainter(self.viewport())
        if self.selected_class:
            painter.setPen(self.selected_class[1])
        else:
            painter.setPen(Qt.red)
        if self.mouse_view_pos:
            painter.drawLine(
                self.mouse_view_pos.x(),
                0,
                self.mouse_view_pos.x(),
                self.viewport().height()
            )
            painter.drawLine(
                0,
                self.mouse_view_pos.y(),
                self.viewport().width(),
                self.mouse_view_pos.y()
            )
        
        if self.prev_pos:
            painter.drawRect(QRect(
                self.prev_pos.toPoint(), self.mouse_scene_pos.toPoint()
            ))

    def update_selected_class(self, selected_class):
        self.selected_class = selected_class
        
