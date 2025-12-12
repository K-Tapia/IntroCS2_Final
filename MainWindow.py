from PyQt6.QtWidgets import QMainWindow
from GUIs.gui import Ui_MainWindow

from function_logic.add_student_logic import StudentLogic
from function_logic.adjust_grades_logic import GradesLogic
from function_logic.print_grades_functionality import PrintLogic


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #page nav
        self.ui.btn_page1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page))
        self.ui.btn_page2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
        self.ui.btn_page3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))
        self.student_logic = StudentLogic(self.ui)
        self.grades_logic = GradesLogic(self.ui, self.student_logic)
        # btn functionality
        self.ui.save_btn.clicked.connect(self.add_student_and_refresh)
        self.ui.list_students.itemClicked.connect(self.grades_logic.student_courses)
        self.ui.save_btn_2.clicked.connect(self.grades_logic.save_grades_to_file)
        self.print_logic = PrintLogic(self.ui,self.grades_logic)
        self.ui.print_button.clicked.connect(self.print_logic.print_grades)

        self.grades_logic.student_list()
    def add_student_and_refresh(self):
        self.student_logic.add_student_btn()
        self.grades_logic.student_list()