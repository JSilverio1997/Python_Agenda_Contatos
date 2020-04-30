

class ContactGetSetter:

    @property
    def id_login(self):
        return self.__id_login

    @id_login.setter
    def id_login(self, id_login):
        if id_login is not None:
            self.__id_login = id_login

    @property
    def name(self):
        return self.__name.title()

    @name.setter
    def name(self, name):
        if name != "":
            self.__name = name.title()

    @property
    def name_recovered(self):
        return self.__name_recovered

    @name_recovered.setter
    def name_recovered(self, name_recovered):
        if name_recovered is not None:
            self.__name_recovered = name_recovered

    @property
    def main_number(self):
        return self.__main_number

    @main_number.setter
    def main_number(self, main_number):
        if main_number is not None and main_number.isdigit():
            self.__main_number = main_number

    @property
    def secundary_number(self):
        return self.__secundary_number

    @secundary_number.setter
    def secundary_number(self, secundary_number):
        if secundary_number.isdigit() or secundary_number is None or secundary_number == "":
            if secundary_number == "":
                secundary_number = None
            self.__secundary_number = secundary_number

