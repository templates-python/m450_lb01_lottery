from numeric_input import read_int
from ticket import Ticket


def create_ticket(person):
    if person.balance >= 2.00:
        ticket = Ticket()
        select_numbers(ticket)
        print_ticket(ticket)
    else:
        print('Zuwenig Guthaben')


def select_numbers(ticket):
    """
    lets the user input his lottery numbers and joker number
    :param ticket:
    :return:
    """
    count = 0
    while count < 6:
        number = read_int(f'{count}. Zahl: Geben Sie eine Zahl von 1 bis 42 ein > ', 1, 42)
        if number not in ticket.numbers:
            ticket.numbers.append(number)
            count +=1

    ticket.joker = read_int('Jokerzahl: Geben Sie eine Zahl von 1 bis 6 ein > ')

def print_ticket(ticket):
    print('Lottoschein anzeigen')


if __name__ == '__main__':
    pass
