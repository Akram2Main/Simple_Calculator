import tkinter as tk
from tkinter import messagebox
import math
import cmath

class AdvancedCalculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b

    def power(self, a, b):
        return a ** b

    def sqrt(self, a):
        if a < 0:
            return cmath.sqrt(a)
        return math.sqrt(a)

    def factorial(self, a):
        if a < 0:
            return "Error: Negative value"
        return math.factorial(a)

    def log(self, a, base=math.e):
        if a <= 0:
            return "Error: Non-positive value"
        return math.log(a, base)

class CalculatorApp:
    def __init__(self, root):
        self.calc = AdvancedCalculator()
        self.root = root
        self.root.title("Advanced Calculator")
        
        self.entry = tk.Entry(root, width=50, borderwidth=5, font=('Arial', 18))
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        
        self.create_buttons()

    def create_buttons(self):
        button_texts = [
            '7', '8', '9', '/', 
            '4', '5', '6', '*', 
            '1', '2', '3', '-', 
            '0', '.', '=', '+', 
            'sqrt', 'pow', 'fact', 'log'
        ]
        row = 1
        col = 0

        for text in button_texts:
            button = tk.Button(self.root, text=text, padx=30, pady=20, font=('Arial', 14), command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def on_button_click(self, char):
        if char in '0123456789.':
            self.entry.insert(tk.END, char)
        elif char in '+-*/':
            self.entry.insert(tk.END, f' {char} ')
        elif char == '=':
            self.calculate()
        elif char == 'sqrt':
            self.calculate_single_arg_function(self.calc.sqrt)
        elif char == 'pow':
            self.entry.insert(tk.END, '**')
        elif char == 'fact':
            self.calculate_single_arg_function(self.calc.factorial)
        elif char == 'log':
            self.calculate_single_arg_function(self.calc.log)
    
    def calculate(self):
        try:
            result = eval(self.entry.get())
            self.entry.delete(0, tk.END)
            self.entry.insert(0, result)
        except Exception as e:
            messagebox.showerror("Error", f"Invalid input: {e}")

    def calculate_single_arg_function(self, func):
        try:
            value = float(self.entry.get())
            result = func(value)
            self.entry.delete(0, tk.END)
            self.entry.insert(0, result)
        except Exception as e:
            messagebox.showerror("Error", f"Invalid input: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
