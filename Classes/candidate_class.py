class Candidate:
    """
    Candidate class
     initilaized with first name, last name, party and votes
    """
    def __init__(self,first_name="",last_name="",party="",votes=0):
        self.__first_name=first_name
        self.__last_name=last_name
        self.__party=party
        self.__votes=votes
    def get_first_name(self)->str:
        """
        :return: first name as string
        """
        return self.__first_name
    def get_last_name(self)->str:
        """
        :return: last name as string
        """
        return self.__last_name
    def get_party(self)->str:
        """
        :return: party affiliation as string
        """
        return self.__party
    def get_votes(self)->int:
        """
        :return: number of votes as int: default(0)
        """
        return self.__votes
    def set_first_name(self,first_name)->None:
        """
        set first name
        :param first_name:
        """
        self.__first_name=first_name
    def set_last_name(self,last_name)->None:
        """
              set last name
              :param last_name:
              """
        self.__last_name=last_name
    def set_party(self,party)->None:
        """
              set party affiliation
              :param party:
              """
        self.__party=party
    def set_votes(self,votes)->None:
        """
              set votes
              :param votes:
              """
        self.__votes=votes

    def increase_votes(self)->None:
        """
        call to increment votes by 1
              """
        self.__votes=self.__votes+1