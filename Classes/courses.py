class Courses():
    def __init__(self,course_name:str,course_grade:int=0):
        self.__course_name=course_name
        self.__course_grade=course_grade
    def get_course_name(self)->str:
        """
        course name is returned
        :return: course name
        """
        return self.__course_name
    def get_str_grade_to_int(self,grade:str)->int:
        """
        course grade conversion from str to int
        then return.
        :param grade:
        :return: grade
        """
        grade=int(grade)
        self.__course_grade=grade
        return self.__course_grade

