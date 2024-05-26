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
        click_button(gui, gui.button_clear)  # Stergem display-ul inainte de fiecare test
        click_button(gui, gui.number_buttons[1])  # Punem un numar
        click_button(gui, button)  # Apasam un operator
        assert gui.display.get() == f"1 {op} "  # Verificam daca operatia este corect afisata

def test_clear_button(gui):
    # Testam butonul de Clear
    click_button(gui, gui.number_buttons[1])  # Introducem un numar pentru a avea ceva de sters
    click_button(gui, gui.button_clear)  # Apasam butonul de clear
    assert gui.display.get() == ''  # Verificam daca dsiplay-ul este gol

