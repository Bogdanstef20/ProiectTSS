import pytest
from calculator import app


def test_statement_coverage():
    test_app = app()
    test_app.button_clear.invoke()
    assert test_app.display.get() == ""

    # testam toate butoanele de numere
    for i in range(10):
        test_app.button_clear.invoke()
        test_app.number_buttons[i].invoke()
        assert test_app.display.get() == str(i)

    # testam butonul .
    test_app.button_clear.invoke()
    test_app.button_dot.invoke()
    assert test_app.display.get() == "."

    # testam butonul de round
    test_app.button_clear.invoke()
    test_app.button_round.invoke()
    assert test_app.display.get() == "UNDEFINED"

    # testam adunarea
    test_app.button_clear.invoke()
    test_app.number_buttons[1].invoke()
    test_app.operation_buttons[0].invoke()
    test_app.number_buttons[2].invoke()
    test_app.operation_buttons[4].invoke()
    assert test_app.display.get() == "1 + 2"

    # testam scaderea
    test_app.button_clear.invoke()
    test_app.number_buttons[5].invoke()
    test_app.operation_buttons[1].invoke()
    test_app.number_buttons[2].invoke()
    test_app.operation_buttons[4].invoke()
    assert test_app.display.get() == "5 - 2"

    # testam inmultirea
    test_app.button_clear.invoke()
    test_app.number_buttons[3].invoke()
    test_app.operation_buttons[2].invoke()
    test_app.number_buttons[4].invoke()
    test_app.operation_buttons[4].invoke()
    assert test_app.display.get() == "3 * 4"

    # testam impartirea
    test_app.button_clear.invoke()
    test_app.number_buttons[4].invoke()
    test_app.operation_buttons[3].invoke()
    test_app.number_buttons[2].invoke()
    test_app.operation_buttons[4].invoke()
    assert test_app.display.get() == "4 / 2"

    # testam impartirea cu 0
    test_app.button_clear.invoke()
    test_app.number_buttons[4].invoke()
    test_app.operation_buttons[3].invoke()
    test_app.number_buttons[0].invoke()
    test_app.operation_buttons[4].invoke()
    assert test_app.display.get() == "4 / 0"
