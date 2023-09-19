from dataclasses import dataclass


@dataclass
class Person:
    """
    a person playing the lottery
    """
    givenname: str
    password: str
    balance: int

    @property
    def name(self):
        return self._givenname

    @givenname.setter
    def name(self, value):
        self._givenname = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value


if __name__ == '__main__':
    pass
