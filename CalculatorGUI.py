import tkinter as tk

class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return x / y

    def modulus(self, x, y):
        return x % y

    def power(self, x, y):
        return x ** y

    def operate(self, x, op, y):
        if op == '+':
            return self.add(x, y)
        elif op == '-':
            return self.subtract(x, y)
        elif op == '*':
            return self.multiply(x, y)
        elif op == '/':
            return self.divide(x, y)
        elif op == '%':
            return self.modulus(x, y)
        elif op == '**':
            return self.power(x, y)
        else:
            raise ValueError("Invalid operator.")

# Minimal Tkinter UI
class CalculatorUI:
    def __init__(self, master):
        self.master = master
        self.master.title("SpartanCalc GUI")
        self.calc = Calculator()

        self.display = tk.Entry(master, width=30, font=('Arial', 16))
        self.display.grid(row=0, column=0, columnspan=4)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('/', 4, 3),
            ('=', 5, 0, 4)
        ]

        for (text, row, col, cs) in [b if len(b) == 4 else (*b, 1) for b in buttons]:
            tk.Button(master, text=text, width=7, height=2, font=('Arial', 14),
                      command=lambda t=text: self.on_click(t)).grid(row=row, column=col, columnspan=cs)

    def on_click(self, char):
        if char == 'C':
            self.display.delete(0, tk.END)
        elif char == '=':
            try:
                expression = self.display.get()
                for op in ['**', '+', '-', '*', '/', '%']:
                    if op in expression:
                        x, y = map(float, expression.split(op))
                        result = self.calc.operate(x, op, y)
                        self.display.delete(0, tk.END)
                        self.display.insert(tk.END, str(result))
                        return
                self.display.insert(tk.END, ' Error')
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, f"Error")
        else:
            self.display.insert(tk.END, char)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorUI(root)
    root.mainloop()
