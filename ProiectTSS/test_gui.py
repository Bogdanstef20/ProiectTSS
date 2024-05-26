import pytest
from tkinter import *
from calculator import app  

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
    # Verificam daca display-ul incepe gol
    assert gui.display.get() == ""

def test_number_buttons(gui):
    # Testam butoanele de numere apasande pe ele pe rand
    for num in range(10):
        click_button(gui, gui.number_buttons[num])
    assert gui.display.get() == '0123456789'

def test_operations(gui):
    # Testam butoanele de operatii
    for op, button in zip(["+", "-", "*", "/"], gui.operation_buttons[:-1]):
        click_button(gui, gui.button_clear)  # Clear the display before each test
        click_button(gui, gui.number_buttons[1])  # Enter a number
        click_button(gui, button)  # Click the operation button
        assert gui.display.get() == f"1 {op} "  # Check if the operation is displayed correctly

def test_clear_button(gui):
    # Testam butonul de Clear
    click_button(gui, gui.number_buttons[1])  # Enter a number to ensure there's something to clear
    click_button(gui, gui.button_clear)  # Click the clear button
    assert gui.display.get() == ''  # Verify that the display is cleared

