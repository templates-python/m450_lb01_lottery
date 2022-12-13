from dataclasses import dataclass


@dataclass
class Person:
    """
    a person playing the lottery
    """
    name: str
    password: str
    balance: int

    @property
    def name(self):
        return self._firstname

    @name.setter
    def name(self, value):
        self._firstname = value

    @property
    def password(self):
        return self._lastname

    @password.setter
    def password(self, value):
        self._lastname = value

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value

if __name__ == '__main__':
    pass