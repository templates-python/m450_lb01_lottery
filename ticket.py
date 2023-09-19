from dataclasses import dataclass


@dataclass
class Ticket:
    """
    a lottery ticket
    """
    joker: int
    numbers: list

    @property
    def joker(self):
        return self._joker

    @joker.setter
    def joker(self, value):
        self._joker = int(value)

    @property
    def numbers(self):
        return self._numbers

    @numbers.setter
    def numbers(self, value):
        if isinstance(value, list):
            self._numbers = value
        else:
            raise ValueError


if __name__ == '__main__':
    pass
