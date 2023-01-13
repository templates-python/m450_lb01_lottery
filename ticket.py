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
        return self._num_draws

    @joker.setter
    def joker(self, value):
        self._num_draws = value

    @property
    def numbers(self):
        return self._numbers

    @numbers.setter
    def numbers(self, value):
        self._numbers = value


if __name__ == '__main__':
    pass
