from numeric_input import read_float


def transfer_money(person):
    """
    deposit or withdraw an amount
    @param person: the person object
    """
    transaction = select_transaction()
    while transaction != 'Z':
        if transaction == 'A':
            prompt = 'Betrag Auszahlung > '
        else:
            prompt = 'Betrag Einzahlung > '
        amount = read_float(prompt, 10.00, 50.00)
        if transaction == 'A':
            amount *= -1
        person.balance += amount
        transaction = select_transaction()


def select_transaction():
    """
    select the type of the transaction
    """
    selection = ''
    while selection == '':
        selection = input('Auswahl (A, E oder Z) > ')
        if selection not in ['A', 'E', 'Z']:
            print('Geben Sie eine gültige Auswahl ein')
            selection = ''
    return selection