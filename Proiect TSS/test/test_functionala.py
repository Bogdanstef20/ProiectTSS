import unittest
from tkinter import Tk
from calculator import app  # Asigură-te că acest import corespunde locației codului tău

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.root = Tk()
        self.app = app(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_button_press(self):
        for num in range(10):
            self.app.display.set("")
            self.app.number_buttons[num].invoke()
            self.assertEqual(self.app.display.get(), str(num))

    def test_operator_press(self):
        operators = {'+': self.app.operation_buttons[0], '-': self.app.operation_buttons[1],
                     '*': self.app.operation_buttons[2], '/': self.app.operation_buttons[3]}
        for op, button in operators.items():
            self.app.display.set("")
            button.invoke()
            self.assertIn(op, self.app.display.get())

    def test_calculation(self):
        #Test adunare 
        self.app.display.set("")
        self.app.number_buttons[2].invoke()
        self.app.operation_buttons[0].invoke() 
        self.app.number_buttons[3].invoke()
        self.app.result(self.app.display)
        self.assertEqual(self.app.display.get(), "5")
        
         #Test scadere
        self.app.display.set("")
        self.app.number_buttons[1].invoke()
        self.app.number_buttons[0].invoke()
        self.app.operation_buttons[1].invoke() 
        self.app.number_buttons[7].invoke()
        self.app.result(self.app.display)
        self.assertEqual(self.app.display.get(), "3")
        
         #Test inmultire 
        self.app.display.set("")  
        self.app.number_buttons[1].invoke()
        self.app.number_buttons[7].invoke()
        self.app.operation_buttons[2].invoke() 
        self.app.number_buttons[5].invoke()
        self.app.result(self.app.display)
        self.assertEqual(self.app.display.get(), "85")
        
         #Test impartire
        self.app.display.set("") 
        self.app.number_buttons[1].invoke()
        self.app.number_buttons[0].invoke()
        self.app.number_buttons[5].invoke()
        self.app.operation_buttons[3].invoke() 
        self.app.number_buttons[5].invoke()
        self.app.result(self.app.display)
        self.assertEqual(self.app.display.get(), "21.0")
        

    def test_clear(self):
        self.app.display.set("123")
        self.app.button_clear.invoke()
        self.assertEqual(self.app.display.get(), "")

    def test_decimal(self):
        self.app.display.set("")
        self.app.button_dot.invoke()
        self.assertEqual(self.app.display.get(), ".")

    def test_round(self):
        self.app.display.set("3.14159")
        self.app.button_round.invoke()
        self.assertEqual(self.app.display.get(), "3.14")

    def test_division_by_zero(self):
        self.app.number_buttons[1].invoke()
        self.app.operation_buttons[3].invoke()  
        self.app.number_buttons[0].invoke()  
        self.app.result(self.app.display)
        self.assertEqual(self.app.display.get(), "UNDEFINED")
        
    def test_invalid_expresion(self):
        self.app.display.set("")
        self.app.display.set("2 + +")  
        self.app.result(self.app.display)
        self.assertEqual(self.app.display.get(), "ERROR")
        
if __name__ == '__main__':
    unittest.main()
