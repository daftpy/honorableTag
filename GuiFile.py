# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1032, 753)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.MainFrame = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MainFrame.sizePolicy().hasHeightForWidth())
        self.MainFrame.setSizePolicy(sizePolicy)
        self.MainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MainFrame.setObjectName("MainFrame")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.MainFrame)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.StepForwardButton = QtWidgets.QPushButton(self.MainFrame)
        self.StepForwardButton.setObjectName("StepForwardButton")
        self.gridLayout_4.addWidget(self.StepForwardButton, 4, 5, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 2, 2, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.MainFrame)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout_4.addWidget(self.pushButton_10, 2, 1, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(self.MainFrame)
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout_4.addWidget(self.pushButton_11, 2, 5, 1, 1)
        self.FrameSlider = QtWidgets.QSlider(self.MainFrame)
        self.FrameSlider.setMinimum(1)
        self.FrameSlider.setOrientation(QtCore.Qt.Horizontal)
        self.FrameSlider.setObjectName("FrameSlider")
        self.gridLayout_4.addWidget(self.FrameSlider, 4, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 1, 0, 1, 8)
        self.YCordLabel = QtWidgets.QLabel(self.MainFrame)
        self.YCordLabel.setObjectName("YCordLabel")
        self.gridLayout_4.addWidget(self.YCordLabel, 2, 7, 1, 1)
        self.CurrentFrameLabel = QtWidgets.QLabel(self.MainFrame)
        self.CurrentFrameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.CurrentFrameLabel.setObjectName("CurrentFrameLabel")
        self.gridLayout_4.addWidget(self.CurrentFrameLabel, 2, 3, 1, 1)
        self.StepBackwardButton = QtWidgets.QPushButton(self.MainFrame)
        self.StepBackwardButton.setObjectName("StepBackwardButton")
        self.gridLayout_4.addWidget(self.StepBackwardButton, 4, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem2, 4, 2, 1, 1)
        self.XCordLabel = QtWidgets.QLabel(self.MainFrame)
        self.XCordLabel.setObjectName("XCordLabel")
        self.gridLayout_4.addWidget(self.XCordLabel, 2, 6, 1, 1)
        self.BigStepForwardButton = QtWidgets.QPushButton(self.MainFrame)
        self.BigStepForwardButton.setObjectName("BigStepForwardButton")
        self.gridLayout_4.addWidget(self.BigStepForwardButton, 4, 6, 1, 2)
        self.BigStepBackwardButton = QtWidgets.QPushButton(self.MainFrame)
        self.BigStepBackwardButton.setObjectName("BigStepBackwardButton")
        self.gridLayout_4.addWidget(self.BigStepBackwardButton, 4, 0, 1, 1)
        self.FrameView = GraphicsView(self.MainFrame)
        self.FrameView.setMouseTracking(True)
        self.FrameView.setDragMode(QtWidgets.QGraphicsView.NoDrag)
        self.FrameView.setTransformationAnchor(QtWidgets.QGraphicsView.AnchorUnderMouse)
        self.FrameView.setResizeAnchor(QtWidgets.QGraphicsView.NoAnchor)
        self.FrameView.setObjectName("FrameView")
        self.gridLayout_4.addWidget(self.FrameView, 0, 0, 1, 8)
        spacerItem3 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem3, 4, 4, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem4, 2, 4, 1, 1)
        self.ColorIndicator = QtWidgets.QLabel(self.MainFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ColorIndicator.sizePolicy().hasHeightForWidth())
        self.ColorIndicator.setSizePolicy(sizePolicy)
        self.ColorIndicator.setMinimumSize(QtCore.QSize(0, 0))
        self.ColorIndicator.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.ColorIndicator.setAutoFillBackground(False)
        self.ColorIndicator.setStyleSheet("background-color: white;")
        self.ColorIndicator.setText("")
        self.ColorIndicator.setAlignment(QtCore.Qt.AlignCenter)
        self.ColorIndicator.setObjectName("ColorIndicator")
        self.gridLayout_4.addWidget(self.ColorIndicator, 2, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.gridLayout_5.addLayout(self.gridLayout_9, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.MainFrame, 0, 1, 1, 1)
        self.SideBarFrame = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SideBarFrame.sizePolicy().hasHeightForWidth())
        self.SideBarFrame.setSizePolicy(sizePolicy)
        self.SideBarFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SideBarFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SideBarFrame.setObjectName("SideBarFrame")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.SideBarFrame)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.LoadLabelsButton = QtWidgets.QPushButton(self.SideBarFrame)
        self.LoadLabelsButton.setObjectName("LoadLabelsButton")
        self.gridLayout_6.addWidget(self.LoadLabelsButton, 5, 0, 1, 1)
        self.LabelColorButton = QtWidgets.QPushButton(self.SideBarFrame)
        self.LabelColorButton.setObjectName("LabelColorButton")
        self.gridLayout_6.addWidget(self.LabelColorButton, 5, 1, 1, 1)
        self.ClassLabelList = QtWidgets.QListWidget(self.SideBarFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.ClassLabelList.sizePolicy().hasHeightForWidth())
        self.ClassLabelList.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ClassLabelList.setFont(font)
        self.ClassLabelList.setStyleSheet("")
        self.ClassLabelList.setObjectName("ClassLabelList")
        self.gridLayout_6.addWidget(self.ClassLabelList, 4, 0, 1, 2)
        self.TaggedFrameList = QtWidgets.QListWidget(self.SideBarFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.TaggedFrameList.sizePolicy().hasHeightForWidth())
        self.TaggedFrameList.setSizePolicy(sizePolicy)
        self.TaggedFrameList.setObjectName("TaggedFrameList")
        self.gridLayout_6.addWidget(self.TaggedFrameList, 8, 0, 1, 2)
        self.LoadVideoButton = QtWidgets.QPushButton(self.SideBarFrame)
        self.LoadVideoButton.setObjectName("LoadVideoButton")
        self.gridLayout_6.addWidget(self.LoadVideoButton, 10, 0, 1, 2)
        self.TotalFramesLabel = QtWidgets.QLabel(self.SideBarFrame)
        self.TotalFramesLabel.setTextFormat(QtCore.Qt.RichText)
        self.TotalFramesLabel.setObjectName("TotalFramesLabel")
        self.gridLayout_6.addWidget(self.TotalFramesLabel, 1, 0, 1, 2)
        self.pushButton_4 = QtWidgets.QPushButton(self.SideBarFrame)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_6.addWidget(self.pushButton_4, 11, 1, 1, 1)
        self.VideoPathLabel = QtWidgets.QLabel(self.SideBarFrame)
        self.VideoPathLabel.setTextFormat(QtCore.Qt.RichText)
        self.VideoPathLabel.setWordWrap(True)
        self.VideoPathLabel.setObjectName("VideoPathLabel")
        self.gridLayout_6.addWidget(self.VideoPathLabel, 0, 0, 1, 2)
        spacerItem5 = QtWidgets.QSpacerItem(40, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem5, 2, 0, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.SideBarFrame)
        self.label_3.setTextFormat(QtCore.Qt.RichText)
        self.label_3.setObjectName("label_3")
        self.gridLayout_6.addWidget(self.label_3, 3, 0, 1, 2)
        spacerItem6 = QtWidgets.QSpacerItem(40, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem6, 6, 0, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.SideBarFrame)
        self.label_4.setTextFormat(QtCore.Qt.RichText)
        self.label_4.setObjectName("label_4")
        self.gridLayout_6.addWidget(self.label_4, 7, 0, 1, 2)
        spacerItem7 = QtWidgets.QSpacerItem(40, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem7, 9, 0, 1, 2)
        self.ToolButton = QtWidgets.QToolButton(self.SideBarFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ToolButton.sizePolicy().hasHeightForWidth())
        self.ToolButton.setSizePolicy(sizePolicy)
        self.ToolButton.setObjectName("ToolButton")
        self.gridLayout_6.addWidget(self.ToolButton, 11, 0, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_6, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.SideBarFrame, 0, 0, 1, 1)
        self.TagsFrame = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TagsFrame.sizePolicy().hasHeightForWidth())
        self.TagsFrame.setSizePolicy(sizePolicy)
        self.TagsFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.TagsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.TagsFrame.setObjectName("TagsFrame")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.TagsFrame)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.pushButton = QtWidgets.QPushButton(self.TagsFrame)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_10.addWidget(self.pushButton, 4, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.TagsFrame)
        self.label.setObjectName("label")
        self.gridLayout_10.addWidget(self.label, 0, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem8, 2, 0, 1, 1)
        self.TagsFrameList = QtWidgets.QListWidget(self.TagsFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.TagsFrameList.sizePolicy().hasHeightForWidth())
        self.TagsFrameList.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.TagsFrameList.setFont(font)
        self.TagsFrameList.setAutoFillBackground(False)
        self.TagsFrameList.setStyleSheet("")
        self.TagsFrameList.setObjectName("TagsFrameList")
        self.gridLayout_10.addWidget(self.TagsFrameList, 1, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.TagsFrame)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_10.addWidget(self.pushButton_2, 5, 0, 1, 1)
        self.gridLayout_2.addWidget(self.TagsFrame, 0, 2, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1032, 18))
        self.menubar.setStyleSheet("")
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.actionOpen_Project = QtWidgets.QAction(MainWindow)
        self.actionOpen_Project.setObjectName("actionOpen_Project")
        self.actionCreate_Project = QtWidgets.QAction(MainWindow)
        self.actionCreate_Project.setObjectName("actionCreate_Project")
        self.actionOpen_Video = QtWidgets.QAction(MainWindow)
        self.actionOpen_Video.setObjectName("actionOpen_Video")
        self.actionSave_Project = QtWidgets.QAction(MainWindow)
        self.actionSave_Project.setObjectName("actionSave_Project")
        self.actionStep_Options = QtWidgets.QAction(MainWindow)
        self.actionStep_Options.setObjectName("actionStep_Options")
        self.actionVideo_Options = QtWidgets.QAction(MainWindow)
        self.actionVideo_Options.setObjectName("actionVideo_Options")
        self.actionExport_Options = QtWidgets.QAction(MainWindow)
        self.actionExport_Options.setObjectName("actionExport_Options")
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "HonorableTag"))
        self.StepForwardButton.setText(_translate("MainWindow", ">"))
        self.pushButton_10.setText(_translate("MainWindow", "Zoom +"))
        self.pushButton_11.setText(_translate("MainWindow", "- Zoom"))
        self.YCordLabel.setText(_translate("MainWindow", "<b>Y:</b>"))
        self.CurrentFrameLabel.setText(_translate("MainWindow", "Load a video . . ."))
        self.StepBackwardButton.setText(_translate("MainWindow", "<"))
        self.XCordLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">X:</span></p></body></html>"))
        self.BigStepForwardButton.setText(_translate("MainWindow", ">>"))
        self.BigStepBackwardButton.setText(_translate("MainWindow", "<<"))
        self.LoadLabelsButton.setText(_translate("MainWindow", "Load Labels"))
        self.LabelColorButton.setText(_translate("MainWindow", "Change Color"))
        self.LoadVideoButton.setText(_translate("MainWindow", "Load Video"))
        self.TotalFramesLabel.setText(_translate("MainWindow", "<b>Total Frames:</b>"))
        self.pushButton_4.setText(_translate("MainWindow", "Export"))
        self.VideoPathLabel.setText(_translate("MainWindow", "<b>Path:</b>"))
        self.label_3.setText(_translate("MainWindow", "<b>Class Labels: </b>"))
        self.label_4.setText(_translate("MainWindow", "<b>Tagged Frames: </b>"))
        self.ToolButton.setText(_translate("MainWindow", "..."))
        self.pushButton.setText(_translate("MainWindow", "Clear All"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Tags In Frame:</span></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "Hide"))
        self.actionOpen_Project.setText(_translate("MainWindow", "Open Project..."))
        self.actionCreate_Project.setText(_translate("MainWindow", "Create Project"))
        self.actionOpen_Video.setText(_translate("MainWindow", "Open Video..."))
        self.actionSave_Project.setText(_translate("MainWindow", "Save Project"))
        self.actionStep_Options.setText(_translate("MainWindow", "Project Options"))
        self.actionVideo_Options.setText(_translate("MainWindow", "Video Options"))
        self.actionExport_Options.setText(_translate("MainWindow", "Export Options"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))
from gui.GraphicsView import GraphicsView


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
