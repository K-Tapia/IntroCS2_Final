from PyQt6.QtWidgets import QMainWindow
from GUIs.gui import Ui_MainWindow
from function_logic.add_student_logic import *

#I got the idea to create a custom class for main window and inherit,
#the gui with my functionality using ai.
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_page1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page))
        self.ui.btn_page2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
        self.ui.btn_page3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))
        self.student_logic = StudentLogic(self.ui)
        self.ui.save_btn.clicked.connect(self.student_logic.add_student_btn)