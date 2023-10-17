from money import transfer_money
from person import Person


def test_transfer_A(monkeypatch):
    person = Person('Inga', 'geheim', 14.00)
    inputs = iter(['A', '12.00', 'Z'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    transfer_money(person)
    assert person.balance == 2.00

def test_transfer_B(monkeypatch):
    person = Person('Inga', 'geheim', 15.00)
    inputs = iter(['E', '25.00', 'Z'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    transfer_money(person)
    assert person.balance == 40.00