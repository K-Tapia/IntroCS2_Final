from PyQt6.QtWidgets import QMessageBox
from Classes.student import Student

class StudentLogic:
    def __init__(self, ui):
        """Initialize with UI reference"""
        self.ui = ui

    def read_student(self)->list:
        """This function reads student from student.txt and saves a list
            of student classes.
            :return: List
        """
        with open('student.txt', 'a+') as file:
            file.seek(0)
            student_list = []
            for line in file:
                line = line.strip()
                parts = line.split("|")
                firstname = parts[0]
                lastname = parts[1]
                elective_class = parts[2]
                math_class = parts[3]
                english_class = parts[4]
                science_class = parts[5]
                student = Student(
                    firstname, lastname, elective_class,
                    math_class, english_class, science_class
                )
                student_list.append(student)
            return student_list

    def validate_name(self, name: str)->str:
        """
        Check if student name is valid by using is alpha, excludes any numbers and spaces.
        capitalize name in return.
        :param name:
        :return: name
        """
        if not name.isalpha():
            QMessageBox.warning(None,"Invalid Name","Please enter a valid name (letters only)")
            return None
        return name.capitalize()

    def save_student(self, student: Student) -> None:
        """
        This function appends student object data to student.txt file. The information is gathered.
        :param student: Student object
        :return: None
        """
        with open('student.txt', 'a') as file:
            file.write(
                f'{student.get_first_name()}|'
                f'{student.get_last_name()}|'
                f'{student.get_elective()}|'
                f'{student.get_math()}|'
                f'{student.get_english()}|'
                f'{student.get_science()}\n'
            )

    def add_student_btn(self) -> None:
        """
        This function creates functionality for adding student in gui.
        First it checks if the first and last names are valid, then it checks for
        elective choice, if elective choice isnt picked it will display an error message.
        lastly student object is created and saved into student.txt file and shows a success message.
        :return: None
        """
        first_name = self.validate_name(self.ui.first_name_input.text())
        if first_name is None:
            return

        last_name = self.validate_name(self.ui.last_name_input.text())
        if last_name is None:
            return
        #ai usage for line 77
        elective_choice = self.ui.elective_btn_group.checkedButton()
        if elective_choice is None:
            QMessageBox.warning(None, "Error", "Please select an elective")
            return
        elective = elective_choice.text()
        list=self.read_student()
        for student in list:
            if student.get_first_name() == first_name and student.get_last_name() == last_name:
                QMessageBox.warning(None, "Error", "Student already exists")
                return
        student = Student(first_name, last_name, elective)
        self.save_student(student)
        QMessageBox.information(None, "Success", "Student added successfully")