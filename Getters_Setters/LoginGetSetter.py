

class LoginGetSetter:

    @property
    def id_login(self):
        return self.__id_login

    @id_login.setter
    def id_login(self, id_login):
        self.__id_login = id_login

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name is not None:
            self.__name = name.title()

    @property
    def nickname(self):
        return self.__nickname

    @nickname.setter
    def nickname(self, nickname):
        if nickname is not None and len(nickname) >= 3:
            self.__nickname = nickname

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        if len(password) > 3:
            self.__password = password

    @property
    def question(self):
        return self.__question

    @question.setter
    def question(self, question):
        if question is not None:
            self.__question = question

    @property
    def answer(self):
        return self.__answer

    @answer.setter
    def answer(self, answer):
        if answer is not None:
            self.__answer = answer

    @property
    def desactive_flag(self):
        return self.__desactive_flag

    @desactive_flag.setter
    def desactive_flag(self, desactive_flag):
        if desactive_flag in ('Y', 'N'):
            self.__desactive_flag = desactive_flag
