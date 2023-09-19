import main


# monkeypatch to replace the function 'create_ticket' in main
def dummy_ticket(person):
    print('dummy')
    pass


def test_main_exit(capsys, monkeypatch):
    inputs = iter(['geheim', 'Z'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main.main()
    output = capsys.readouterr().out
    assert output == 'Lotto\n---------\nA) Konto Ein- und Auszahlungen tätigen\nB) Lottotipps abgeben\n' \
                     'Z) Beenden\n'


def test_main_money(capsys, monkeypatch):
    inputs = iter(['geheim', 'A', 'Z', 'Z'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main.main()
    output = capsys.readouterr().out
    assert output == 'Lotto\n---------\nA) Konto Ein- und Auszahlungen tätigen\nB) Lottotipps abgeben\n' \
                     'Z) Beenden\nLotto\n---------\nA) Konto Ein- und Auszahlungen tätigen\nB) Lottotipps abgeben\n' \
                     'Z) Beenden\n'


def test_main_ticket(capsys, monkeypatch):
    inputs = iter(['geheim', 'B', 'Z', 'Z'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    monkeypatch.setattr(main, 'create_ticket', dummy_ticket)
    main.main()
    output = capsys.readouterr().out
    assert output == 'Lotto\n---------\nA) Konto Ein- und Auszahlungen tätigen\nB) Lottotipps abgeben\n' \
                     'Z) Beenden\ndummy\nLotto\n---------\nA) Konto Ein- und Auszahlungen tätigen\n' \
                     'B) Lottotipps abgeben\nZ) Beenden\n'