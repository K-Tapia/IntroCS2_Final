class User:
    """
    User class, initialized with username, voted defaults to false
    """
    def __init__(self,username,voted=False):
        self.__username=username
        self.__voted=voted
    def get_username(self)->str:
        """
        :return: username as string
        """
        return self.__username
    def get_voted(self)->bool:
        """
        :return: voted as boolean, default as false
        """
        return self.__voted
    def set_username(self,username:str)->None:
        """
        set username
        :param username:
        """
        self.__username=username
    def set_voted(self,voted:bool)->None:
        """
        set voted
        :param voted:
        """
        self.__voted=voted
    def user_voted(self)->None:
        """
        change boolean value of voted to True if user places vote
        """
        self.__voted=True