import pytest
from calculator import app
from decimal import Decimal

@pytest.fixture(scope="module")
def calculator():
    return app()

def test_addition(calculator):
    calculator.display.set('5+2')
    calculator.result(calculator.display)
    assert calculator.display.get() == '7'

def test_subtraction(calculator):
    calculator.display.set('10-2')
    calculator.result(calculator.display)
    assert calculator.display.get() == '8'

def test_multiplication(calculator):
    calculator.display.set('10*5')
    calculator.result(calculator.display)
    assert calculator.display.get() == '50'

def test_division(calculator):
    calculator.display.set('20/4')
    calculator.result(calculator.display)
    assert calculator.display.get() == '5.0'

def test_clear(calculator):
    calculator.display.set('12345')  #setam desplay-ul cu un numar random
    calculator.button_clear.invoke()  #simulam apasarea butonului de clear
    assert calculator.display.get() == ''

def test_negative_numbers():
    calculator = app()
    calculator.display.set("-5+3")
    calculator.result(calculator.display)
    assert calculator.display.get() == "-2"

def test_decimal_numbers():
    calculator = app()
    calculator.display.set("2.5+3.7")
    calculator.result(calculator.display)
    assert calculator.display.get() == "6.2"

def test_multiple_numbers():
    calculator = app()
    calculator.display.set("2+3+4")
    calculator.result(calculator.display)
    assert calculator.display.get() == "9"

def test_operator_priority():
    calculator = app()
    calculator.display.set("2+3*4-5")
    calculator.result(calculator.display)
    assert calculator.display.get() == "9"

def test_large_numbers():
    calculator = app()
    calculator.display.set("1000000000000000000000000000000000000000000000000000000000000+1")
    calculator.result(calculator.display)
    expected = Decimal("1e+60")
    actual = Decimal(calculator.display.get()).normalize()
    assert actual == expected

def test_small_numbers():
    calculator = app()
    calculator.display.set("0.0000000000000000000000000000000000000000000000000000000000001+0.0000000000000000000000000000000000000000000000000000000000002")
    calculator.result(calculator.display)
    assert calculator.display.get() == "3e-61"

def test_float_operations():
    calculator = app()
    #Test Adunare
    calculator.display.set("2.5+1.25")
    calculator.result(calculator.display)
    assert Decimal(calculator.display.get()) == Decimal("3.75")
    #Test Scadere   
    calculator.display.set("2.5-1.25")
    calculator.result(calculator.display)
    assert Decimal(calculator.display.get()) == Decimal("1.25")
    #Test Inmultire
    calculator.display.set("2.5*1.25")
    calculator.result(calculator.display)
    assert Decimal(calculator.display.get()) == Decimal("3.125")
    #Test impartire
    calculator.display.set("2.5/1.25")
    calculator.result(calculator.display)
    assert Decimal(calculator.display.get()) == Decimal("2")

def test_nan_inf_operations():
    calculator = app()
    #Test Impartire cu 0
    calculator.display.set("1/0")
    calculator.result(calculator.display)
    assert calculator.display.get() == "UNDEFINED"

    calculator.display.set("0/0")
    calculator.result(calculator.display)
    assert calculator.display.get() == "UNDEFINED"

def test_float_overflow():
    calculator = app()
    #Test dapasire limita float
    calculator.display.set(str(Decimal('1e400') * Decimal('1e400')))
    calculator.result(calculator.display)
    assert calculator.display.get() == "inf"

def test_round_float():
    calculator = app()
    #Testam rotunjirea la 2 zecimale
    calculator.display.set("1.23456789")
    calculator.round(2)
    assert calculator.display.get() == "1.23"
    #Testam rotunjirea la 5 zecimale
    calculator.display.set("1.23456789")
    calculator.round(5)
    assert calculator.display.get() == "1.23457"
