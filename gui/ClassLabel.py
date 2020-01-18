from PyQt5.QtWidgets import QListWidgetItem
from PyQt5.QtGui import QColor

class ClassLabel(QListWidgetItem):

    def __init__(self, class_label, color, rect=None, *args, **kwargs):
        super(QListWidgetItem, self).__init__(*args,**kwargs)
        self.label = class_label
        self.color = QColor(color)
        # Get the hue, sat, value so we can change value to 255
        h, s, v, a = self.color.getHsv()
        # This makes the black text more readable
        self.color.setHsv(h, s, 255)
        if rect is not None: # If the ClassLabel is going into TagsFrameList
            self.setText(f'{self.label}, {str(rect)}')
        else: # If the ClassLabel is going elsewhere
            self.setText(f'{self.label}')
        self.setBackground(self.color)

    def change_color(self):
        # Sets the background color
        self.setText(f'{self.label}')
        self.setBackground(self.color)

    def add_color_text(self):
        # Display the color name in the list
        self.setText(f'{self.label} - {self.color.getRgb()}')
