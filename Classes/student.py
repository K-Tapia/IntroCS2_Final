from PyQt6.QtWidgets import QMainWindow


class Student():
    def __init__(self, first_name:str, last_name:str, elective:str, math="Math", science="Science", english="English", )->None:
        self.__first_name = first_name
        self.__last_name = last_name
        self.__math = math
        self.__science = science
        self.__english = english
        self.__elective = elective
    def get_first_name(self):
        """
        get first name string
        :return: first name
        """
        return self.__first_name

    def get_last_name(self):
        """
        get last name string
        :return: last name
        """
        return self.__last_name
    def get_math(self):
        """
        get math string
        :return: math"""
        return self.__math
    def get_science(self):
        """
        get science string
        :return: science
        """
        return self.__science
    def get_english(self):
        """
        get english string
        :return: english
        """
        return self.__english
    def get_elective(self):
        """
        get elective string
        :return: elective
        """
        return self.__elective


