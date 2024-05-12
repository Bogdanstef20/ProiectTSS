import pytest
from tkinter import *
from calculator import app  # Assuming `calculator.py` contains your calculator class


@pytest.fixture
def gui():
    root = Tk()
    calculator = app(root)
    calculator.pack()
    return calculator


def click_button(gui, button):
    button.invoke()
    gui.update()


def test_display(gui):
    # Check if the display starts empty
    assert gui.display.get() == ""


def test_number_buttons(gui):
    # Test number buttons by clicking each one
    for num in range(10):
        click_button(gui, gui.number_buttons[num])
    assert gui.display.get() == '0123456789'


def test_operations(gui):
    # Test each operation button
    for op, button in zip(["+", "-", "*", "/"], gui.operation_buttons):
        click_button(gui, button)
        assert gui.operations == op


def test_clear_button(gui):
    # Test clear button
    click_button(gui, gui.button_clear)
    assert gui.display.get() == ''
    assert gui.operations == ''


def test_integer_calculation(gui):
    # Test calculation with integers
    click_button(gui, gui.number_buttons[2])
    click_button(gui, gui.number_buttons[5])
    click_button(gui, gui.get_button('+'))
    click_button(gui, gui.number_buttons[3])
    click_button(gui, gui.number_buttons[5])
    click_button(gui, gui.get_button('='))
    assert gui.display.get() == '60'


def test_float_calculation(gui):
    # Test calculation with floats
    click_button(gui, gui.button_clear)
    click_button(gui, gui.number_buttons[2])
    click_button(gui, gui.get_button('.'))
    click_button(gui, gui.number_buttons[5])
    click_button(gui, gui.get_button('+'))
    click_button(gui, gui.number_buttons[1])
    click_button(gui, gui.get_button('.'))
    click_button(gui, gui.number_buttons[5])
    click_button(gui, gui.get_button('='))
    assert gui.display.get() == '4.0'
