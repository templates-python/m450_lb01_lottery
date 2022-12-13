from authenticate import login
from menu import select_menu
from money import transfer_money


def main():
    people_list = list()
    person = login(people_list)
    item = ''
    while item != 'Z':
        item = select_menu()
        if item == 'A':
            transfer_money(person)
        elif item == 'B':
            pass





if __name__ == '__main__':
    main()