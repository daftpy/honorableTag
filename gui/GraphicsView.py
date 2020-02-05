from PyQt5.QtWidgets import QGraphicsView
from PyQt5.QtCore import Qt, pyqtSignal, QRect
from PyQt5.QtGui import QPainter
from gui.GraphicsScene import GraphicsScene


class GraphicsView(QGraphicsView):
    mouse_pos_signal = pyqtSignal(int, int)
    remove_rect_signal = pyqtSignal(QRect)

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
        self.mouse_view_pos = event.pos()
        # Emit mouse pos relative to scene to gui for tracking
        self.mouse_scene_pos = self.mapToScene(event.pos())
        self.mouse_pos_signal.emit(
            self.mouse_scene_pos.x(),
            self.mouse_scene_pos.y()
        )

        if event.buttons() == Qt.MidButton:  # or Qt.MiddleButton
            offset = self.prev_pos - event.pos()  # get the offset
            self.prev_pos = event.pos()
            # Move the scene via the scrollbars
            self.verticalScrollBar().setValue(
                self.verticalScrollBar().value() + offset.y()
            )
            self.horizontalScrollBar().setValue(
                self.horizontalScrollBar().value() + offset.x()
            )
        else:
            super().mouseMoveEvent(event)

        # Update the viewport on the GraphicsView to trigger
        # paint event for the crosshairs
        self.viewport().update()

    def mousePressEvent(self, event):
        if event.button() == Qt.MidButton:  # or Qt.MiddleButton
            # Set pos used for moving around the pixmap
            self.prev_pos = event.pos()

        # Set the prev_pos so we can start rendering a temp rec
        elif event.button() == Qt.LeftButton:
            self.prev_pos = event.pos()

        elif event.button() == Qt.RightButton:
            item = self.itemAt(
                event.pos()
            )
            if item:
                if not hasattr(item, 'pixmap'):
                    rect = item.rect()
                    rect = rect.toRect()  # Convert the QRectF to a normal QRect
                    self.DrawScene.sql_storage.remove_rect(rect)
                    for row in self.DrawScene.rect_list:
                        # Find the row(list) that contains the rect
                        if rect in row:
                            # Remove from rect_list to not save it on get_frame
                            self.DrawScene.rect_list.remove(row)
                    self.remove_rect_signal.emit(rect)
                    item = self.DrawScene.removeItem(item)

    def mouseReleaseEvent(self, event):
        # Reset the prev_pos so we stop drawing the temp rec
        # and render the new rect
        if event.button() == Qt.LeftButton:
            if self.prev_pos:
                # Map the pos to the scene before rendering for accurate pos
                self.prev_pos = self.mapToScene(self.prev_pos)
                new_rect = QRect(
                    self.prev_pos.toPoint(),  # Round our pos to whole numbers
                    self.mapToScene(event.pos()).toPoint()
                )
                # Draw the rect
                if self.selected_class:
                    self.DrawScene.new_rect(new_rect, self.selected_class)
                self.prev_pos = None

        elif event.button() == Qt.MidButton:
            self.prev_pos = None

        self.viewport().update()

    def wheelEvent(self, event):
        # Scroll zoom mechanism
        adj = (event.angleDelta().y()) * 0.001
        self.scale(1+adj, 1+adj)

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self.viewport())
        # Creates our crosshairs to help create more accurate
        # bounding boxes
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
            # Draw temporary rect for accurate placement
            painter.drawRect(QRect(
                self.prev_pos, self.mouse_view_pos
            ))
