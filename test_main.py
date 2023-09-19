import main
# monkeypatch to replace the function 'create_ticket' in main
def dummy_ticket(person):
    pass

# monkeypatch to replace the function 'login' in main
def dummy_login():
    pass

# monkeypatch to replace the function 'transfer_money' in main
def dummy_transfer(person):
    pass

def test_main_exit(capsys, monkeypatch):
    inputs = iter(['geheim', 'Z'])
    inputs = iter(['Z'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    monkeypatch.setattr(main, 'login', dummy_login)
    main.main()
    output = capsys.readouterr().out
    assert output == 'Lotto\n---------\nA) Konto Ein- und Auszahlungen tätigen\nB) Lottotipps abgeben\n' \
                     'Z) Beenden\n'


def test_main_money(capsys, monkeypatch):
    inputs = iter(['geheim', 'A', 'Z', 'Z'])
    inputs = iter(['A', 'Z'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    monkeypatch.setattr(main, 'login', dummy_login)
    monkeypatch.setattr(main, 'transfer_money', dummy_transfer)
    main.main()
    output = capsys.readouterr().out
    assert output == 'Lotto\n---------\nA) Konto Ein- und Auszahlungen tätigen\nB) Lottotipps abgeben\n' \


def test_main_ticket(capsys, monkeypatch):
    inputs = iter(['geheim', 'B', 'Z', 'Z'])
    inputs = iter(['B', 'Z'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    monkeypatch.setattr(main, 'login', dummy_login)
    monkeypatch.setattr(main, 'create_ticket', dummy_ticket)
    main.main()
    output = capsys.readouterr().out
    assert output == 'Lotto\n---------\nA) Konto Ein- und Auszahlungen tätigen\nB) Lottotipps abgeben\n' \
                     'Z) Beenden\ndummy\nLotto\n---------\nA) Konto Ein- und Auszahlungen tätigen\n' \
                     'Z) Beenden\nLotto\n---------\nA) Konto Ein- und Auszahlungen tätigen\n' \
                     'B) Lottotipps abgeben\nZ) Beenden\n'