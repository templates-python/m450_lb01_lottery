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
    inputs = iter(['Z'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    monkeypatch.setattr(main, 'login', dummy_login)
    main.main()
    output = capsys.readouterr().out
    assert output == 'Lotto\n---------\nA) Konto Ein- und Auszahlungen tätigen\nB) Lottotipps abgeben\nZ) Beenden\n'


def test_main_money(capsys, monkeypatch):
    inputs = iter(['A', 'Z'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    monkeypatch.setattr(main, 'login', dummy_login)
    monkeypatch.setattr(main, 'transfer_money', dummy_transfer)
    main.main()
    output = capsys.readouterr().out
    assert output == 'Lotto\n---------\nA) Konto Ein- und Auszahlungen tätigen\nB) Lottotipps abgeben\nZ) Beenden\n' \
                     'Lotto\n---------\nA) Konto Ein- und Auszahlungen tätigen\nB) Lottotipps abgeben\nZ) Beenden\n'


def test_main_ticket(capsys, monkeypatch):
    inputs = iter(['B', 'Z'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    monkeypatch.setattr(main, 'login', dummy_login)
    monkeypatch.setattr(main, 'create_ticket', dummy_ticket)
    main.main()
    output = capsys.readouterr().out
    assert output == 'Lotto\n---------\nA) Konto Ein- und Auszahlungen tätigen\nB) Lottotipps abgeben\nZ) Beenden\n' \
                     'Lotto\n---------\nA) Konto Ein- und Auszahlungen tätigen\nB) Lottotipps abgeben\nZ) Beenden\n'