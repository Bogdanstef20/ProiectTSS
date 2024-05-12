from calculator import app
import pytest

@pytest.fixture
def calculator():
    calc = app()
    yield calc

def test_clear(calculator):
    calculator.display.set("987")
    calculator.button_clear.invoke()
    assert calculator.display.get() == ""

def test_addition(calculator):
    calculator.display.set("15+7")
    calculator.result(calculator.display)
    assert calculator.display.get() == "22"

def test_subtraction(calculator):
    calculator.display.set("20-8")
    calculator.result(calculator.display)
    assert calculator.display.get() == "12"

def test_multiplication(calculator):
    calculator.display.set("10*6")
    calculator.result(calculator.display)
    assert calculator.display.get() == "60"

def test_division(calculator):
    calculator.display.set("30/5")
    calculator.result(calculator.display)
    assert calculator.display.get() == "6.0"

def test_division_by_zero(calculator):
    calculator.display.set("15/0")
    calculator.result(calculator.display)
    assert calculator.display.get() == "UNDEFINED"

def test_round(calculator):
    calculator.display.set("1.61803398875")
    calculator.round(3)
    assert calculator.display.get() == "1.618"

def test_round_with_invalid_input(calculator):
    calculator.display.set("invalid_input")
    calculator.round(2)
    assert calculator.display.get() == "UNDEFINED"

def test_get_dot_button_not_found(calculator):
    with pytest.raises(ValueError):
        calculator.get_button("non-existent button")
