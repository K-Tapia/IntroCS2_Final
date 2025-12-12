from PyQt6.QtWidgets import QTextEdit
from function_logic.adjust_grades_logic import GradesLogic

class PrintLogic:
    def __init__(self, ui,grades_logic: GradesLogic):
        self.ui = ui
        self.text_edit: QTextEdit = self.ui.textEdit
        self.grades_logic = grades_logic
    def relative_letter_grade(self, score: int) -> str:
        """
        this function takes the int score from the student's grades and
        converts to the abc scale
        :param: score:int
        :return:str
        """
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        else:
            return "F"

    def print_grades(self):
        """This function first clears the text widget.
        Wrapped in a try else, try: read the student_grades.txt file
        and saves it. if no file exist just return to prevent a crash.
        Since dictionary with inner dicitonary for loops to log informatin
        into the text widget.
         """
        self.text_edit.clear()
        try:
            student_data = self.grades_logic.read_grades()
            if not student_data:
                self.text_edit.setText("No student grades file found!")
                return
            for student_name, courses in student_data.items():
                self.text_edit.append(f"Student: {student_name}")
                for course_name, course_grade in courses.items():
                    letter = self.relative_letter_grade(course_grade)
                    self.text_edit.append(f"  {course_name}: {course_grade} ({letter})")
                self.text_edit.append("")
            with open("printed_grades.txt","w")as f:
                f.write(self.text_edit.toPlainText())
        except FileNotFoundError:
            self.text_edit.setText("No student grades file found!")
