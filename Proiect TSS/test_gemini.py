import pytest
from tkinter import Tk
from calculator import app  # Replace with the path to your calculator file


@pytest.fixture
def calculator():
    return app()


def test_addition(calculator):
    # Test adding with different numbers
    calculator.display.set("7")
    calculator.get_button("+").invoke()
    calculator.display.set("4")
    calculator.result(calculator.display)
    assert calculator.display.get() == "11"


def test_subtraction(calculator):
    # Test subtracting with different numbers
    calculator.display.set("9")
    calculator.get_button("-").invoke()
    calculator.display.set("2")
    calculator.result(calculator.display)
    assert calculator.display.get() == "7"


def test_multiplication(calculator):
    calculator.display.set("3")
    calculator.get_button("*").invoke()
    calculator.display.set("8")
    calculator.result(calculator.display)
    assert calculator.display.get() == "24"


def test_division(calculator):
    calculator.display.set("12")
    calculator.get_button("/").invoke()
    calculator.display.set("3")
    calculator.result(calculator.display)
    assert calculator.display.get() == "4"

    # Test division by zero (unchanged)
    calculator.display.set("3")
    calculator.get_button("/").invoke()
    calculator.display.set("0")
    calculator.result(calculator.display)
    assert calculator.display.set() == "UNDEFINED"


def test_decimal(calculator):
    calculator.display.set("1.8")
    calculator.get_dot_button().invoke()
    calculator.display.set("7")
    calculator.get_button("+").invoke()
    calculator.display.set("5.2")
    calculator.result(calculator.display)
    assert calculator.display.get() == "7.7"


def test_round(calculator):
    calculator.display.set("2.6532")
    calculator.button_round.invoke()
    assert calculator.display.get() == "2.7"  # Round to one decimal place


def test_invalid_expression(calculator):
    calculator.display.set("xyz")
    calculator.result(calculator.display)
    assert calculator.display.get() == "ERROR"