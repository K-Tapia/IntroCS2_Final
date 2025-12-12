from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QTableWidgetItem, QMessageBox
from Classes.courses import Courses

class GradesLogic:
    def __init__(self, ui, student_logic)->None:
        """
        This is a base initialization for the gui, it also contains
        an initialization for student_logic to read from student.txt
        and setups table widget functionality
        :param ui:
        :param student_logic:
        """
        self.ui = ui
        self.student_logic = student_logic
        self.ui.grades_table_widget.cellChanged.connect(self.grades_column_validation)

    def student_list(self)->None:
        """
        This function read student.txt file, and collects all students and puts them in the
        list widget with first and last name combined.
        """
        self.ui.list_students.clear()
        students = self.student_logic.read_student()
        for student in students:
            full = f"{student.get_first_name()} {student.get_last_name()}"
            self.ui.list_students.addItem(full)

    def student_courses(self, widget_list_item)->None:
        """
        This function takes the contents of the list widget and compares
        with the contents of student.txt file. If the full name put together in
        student.txt is equal to the full name in the list widget, add content to the table
        widget
        :param widget_list_item:
        :return: None
        """
        student_name = widget_list_item.text()
        students = self.student_logic.read_student()
        for student in students:
            full = f"{student.get_first_name()} {student.get_last_name()}"
            if full == student_name:
                self.populate_table(student)
                break

    def grades_column_validation(self, row, column)->None:
        """
        This function is a validater for input in the table widget.
        First it retrieves the table widget, it checks if the column being edited is not 1
        if so end function. Then it retrieves the content of row and column 1, if empty end function.
        When there is content take the text of that table.item. check to see if the edited content is a number
        if not set to 0. If number entered is less than 0 set the text to 0, and if it is greater than 100 set the text
        to 100 (percentage grade values).
        :param row:
        :param column:
        :return:None
        """
        table = self.ui.grades_table_widget
        if column != 1:
            return

        item = table.item(row, column)
        if item is None:
            return

        text = item.text()
        if not text.isdigit():
            item.setText("0")
        else:
            value = int(text)
            if value < 0:
                item.setText("0")
            elif value > 100:
                item.setText("100")

    def populate_table(self, student,):
        """T
         edited this a little later after creating. The function first checks to see if there are students with grades existing already
            than it saves it to courses for the course/grade column. this function get a student object passed and saves it in the dictionary called courses.
            then set the number of rows equal to the length of courses. Columns is always set to a max of 2 columns
            Then iterate throught the dictionary, set course names in column 1 as uneditable.
            for grade column set grades and make column editable.

        """
        all_grades = self.read_grades()

        fullname = f"{student.get_first_name()} {student.get_last_name()}"
        if fullname in all_grades:
            courses = all_grades[fullname]
        else:
            courses = {
                student.get_math(): 0,
                student.get_science(): 0,
                student.get_english(): 0,
                student.get_elective(): 0
            }

        table = self.ui.grades_table_widget
        table.setRowCount(len(courses))
        table.setColumnCount(2)

        row = 0
        for course_name, grade in courses.items():

            name_item = QTableWidgetItem(course_name)
            #ai use line 100 and line 103
            name_item.setFlags(name_item.flags() & ~Qt.ItemFlag.ItemIsEditable)
            table.setItem(row, 0, name_item)
            grade_item = QTableWidgetItem(str(grade))
            grade_item.setFlags(grade_item.flags() | Qt.ItemFlag.ItemIsEditable)
            table.setItem(row, 1, grade_item)
            row += 1

    def save_grades_to_file(self)->None:
        """
        This function first gets the table widget, it than checks to see if their is content
        inside the list widget. If there is it will save the current list widget content in student name.
        get row count from tables than for loop get content from the columns and if both exist convert the grade
        content from a string into an int. Save course as a course object and append to the course list.
        from there students along with courses/grades gets saved to a txt file using a cusotm string format.
        :return:
        """
        table = self.ui.grades_table_widget
        current_item = self.ui.list_students.currentItem()
        if current_item is None:
            return

        student_name = current_item.text()
        course_list = []
        row_count = table.rowCount()

        for row in range(row_count):
            course_item = table.item(row, 0)
            grade_item = table.item(row, 1)
            if course_item and grade_item:
                try:
                    grade = int(grade_item.text())
                except ValueError:
                    grade = 0
                course = Courses(course_item.text(), grade)
                course_list.append(course)

        string = f'{student_name}|{course_list[0].get_course_name()}|{course_list[0]._Courses__course_grade}|' \
                 f'{course_list[1].get_course_name()}|{course_list[1]._Courses__course_grade}|' \
                 f'{course_list[2].get_course_name()}|{course_list[2]._Courses__course_grade}|' \
                 f'{course_list[3].get_course_name()}|{course_list[3]._Courses__course_grade}'
        lines=[]

        with open("student_grades.txt", "r") as f:
            for line in f:
                #ai usage line 143-145
                if not line.startswith(student_name + '|'):
                    lines.append(line.strip())
            lines.append(string)

        with open("student_grades.txt", "w") as f:
            for line in lines:
                f.write(line + "\n")

        QMessageBox.information(self.ui.grades_table_widget, "Saved", f"Grades for {student_name} saved!")
    def read_names(self)->list:
        """
        this functiosn read just the names in each line for student_grades.txt
        :return: list of student names
        """
        student_names = []
        with open("student_grades.txt", "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    parts = line.split('|')
                    student_names.append(parts[0])
        return student_names

    def read_grades(self) -> dict:
        """
        Created this function so grades will show in the table widget if they already exist
        read student_grades.txt and
        """
        student_grades_data = {}
        with open("student_grades.txt", "a+") as f:
            f.seek(0)
            for line in f:
                line = line.strip()
                if line:
                    parts = line.split('|')
                    fullname= parts[0]
                    course1=parts[1]
                    course1_grade = int(parts[2])
                    course2=parts[3]
                    course2_grade = int(parts[4])
                    course3=parts[5]
                    course3_grade = int(parts[6])
                    course4=parts[7]
                    course4_grade = int(parts[8])
                    courses={course1:course1_grade,course2:course2_grade,course3:course3_grade,course4:course4_grade}
                    student_grades_data[fullname] = courses

        return student_grades_data

