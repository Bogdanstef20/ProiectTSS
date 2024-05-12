from tkinter import *
import math


def fCalc(src, side):
    appObj = Frame(src, borderwidth=4, bd=2, bg="#cccccc")
    appObj.pack(side=side, expand=YES, fill=BOTH)
    return appObj


def button(src, side, text, command=None):
    appObj = Button(src, text=text, command=command)
    appObj.pack(side=side, expand=YES, fill=BOTH)
    return appObj


class app(Frame):
    def __init__(self, root=Tk(), width=364, height=425):
        Frame.__init__(self)
        self.option_add("*Font", 'arial 20 bold')
        self.pack(expand=YES, fill=BOTH)
        self.master.title("Simple Calculator")
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        root.geometry('%dx%d+%d+%d' % (width, height, x, y))
        self.display = StringVar()
        Entry(self, relief=RIDGE,
              textvariable=self.display, state=DISABLED, justify='right', bd=20, bg="silver").pack(side=TOP, expand=YES,
                                                                                                   fill=BOTH)

        self.button_clear = Button(self, text="Clear", command=lambda: self.display.set(""))
        self.button_clear.pack(side=TOP, expand=YES, fill=BOTH)

        # Create buttons for all numbers
        self.numbers = fCalc(self, TOP)
        self.number_buttons = []
        for num in range(10):
            button_obj = Button(self.numbers, text=str(num),
                                command=lambda appObj=self.display, i=str(num): appObj.set(appObj.get() + i))
            button_obj.pack(side=LEFT, expand=YES, fill=BOTH)
            self.number_buttons.append(button_obj)

        # Create buttons for all operations
        self.operations = fCalc(self, TOP)
        self.operation_buttons = []
        for op in ["+", "-", "*", "/", "="]:
            if op == "=":
                btnEquals = Button(self.operations, text=op)
                btnEquals.bind('<ButtonRelease-1>', lambda e, s=self, appObj=self.display: s.result(appObj))
                btnEquals.pack(side=LEFT, expand=YES, fill=BOTH)
                self.operation_buttons.append(btnEquals)
            else:
                button_obj = Button(self.operations, text=op,
                                    command=lambda appObj=self.display, s=" %s " % op: appObj.set(appObj.get() + s))
                button_obj.pack(side=LEFT, expand=YES, fill=BOTH)
                self.operation_buttons.append(button_obj)

        self.button_dot = Button(self.numbers, text=".",
                                 command=lambda appObj=self.display, i=".": appObj.set(appObj.get() + i))
        self.button_dot.pack(side=LEFT, expand=YES, fill=BOTH)
        self.button_round = Button(self.numbers, text="round",
                                   command=lambda: self.round(2))
        self.button_round.pack(side=LEFT, expand=YES, fill=BOTH)

    def get_button(self, label):
        for widget in self.winfo_children():
            if isinstance(widget, Button) and widget['text'] == str(label):
                return widget
        raise ValueError(f"Button {label} not found")

    def get_dot_button(self):
        return self.get_button('.')

    def round(self, digits):
        try:
            value = float(self.display.get())
            rounded_value = round(value, digits)
            self.display.set(str(rounded_value))
        except:
            self.display.set("UNDEFINED")

    def result(self, display):
        try:
            result_value = eval(display.get())
            if result_value == float('inf'):
                display.set('Inf')
            else:
                display.set(str(result_value))
        except ZeroDivisionError:
            display.set('UNDEFINED')



if __name__ == '__main__':
    app().mainloop()
