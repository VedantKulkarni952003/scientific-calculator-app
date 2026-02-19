import tkinter as tk
from tkinter import messagebox
import math
import re

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")    
        self.root.geometry("400x450")

        
        self.frame = tk.Frame(root, bg="skyblue", padx=10)
        self.frame.pack(fill="both", expand=True)


        self.entry = tk.Entry(self.frame, relief=tk.SUNKEN, borderwidth=3, width=60)
        self.entry.grid(row=0, column=0, columnspan=4, ipady=2, pady=2)
        self.root.bind("<Return>", lambda e: self.equal())
        self.entry.bind("<BackSpace>", self.handle_backspace)

        self.create_buttons()
    def handle_backspace(self, event):
        self.backspace()
        return "break"   

    def click(self, value):
        current = self.entry.get()
        ops = '+-*/'
        if current and current[-1] in ops and value in ops:
            return
        self.entry.insert(tk.END, value)

    def equal(self):
        try:
            result = str(eval(self.entry.get()))
            self.entry.delete(0, tk.END)
            self.entry.insert(0, result)
        except Exception:
            messagebox.showerror("Error", "Invalid Expression")

    def clear(self):
        self.entry.delete(0, tk.END)
    def backspace(self):
        current = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(0, current[:-1])


    def create_buttons(self):
        buttons = [
            ('(', 1, 0), (')', 1, 1), 
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2),('/', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2),('*', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
            ('0', 5, 0), ('.', 5, 1),('+', 5, 3), 
        ]

        for txt, r, c in buttons:
            for i in range(4):
                self.frame.columnconfigure(i, weight=1)

            for i in range(6):
                self.frame.rowconfigure(i, weight=1)
            tk.Button(
                self.frame,
                text=txt,
                width=5,
                command=lambda t=txt: self.click(t)
            ).grid(row=r, column=c, pady=2, padx=2,sticky="nsew")

        tk.Button(self.frame, text="AC", width=5, command=self.clear)\
            .grid(row=1, column=3, columnspan=1, pady=2,padx=2,sticky="nsew")
        tk.Button(self.frame, text="⌫", width=5, command=self.backspace)\
            .grid(row=1, column=2, columnspan=1, pady=2,padx=2,sticky="nsew")

        tk.Button(self.frame, text="=", width=5, command=self.equal)\
            .grid(row=5, column=2, columnspan=1, pady=2,padx=2,sticky="nsew")
        tk.Button(self.frame, text="Scientific Calculator", width=5, command=self.switch_scientific)\
            .grid(row=6, column=0, columnspan=4, pady=2,padx=2,sticky="nsew")
        

    def switch_scientific(self):
        self.root.destroy()
        new_root = tk.Tk()
        Scientific_Calculator(new_root)
        new_root.mainloop()

class Scientific_Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")    
        self.root.geometry("500x500")

        
        self.frame = tk.Frame(root, bg="skyblue", padx=10)
        self.frame.pack(fill="both", expand=True)


        self.entry = tk.Entry(self.frame, relief=tk.SUNKEN, borderwidth=3, width=60)
        self.entry.grid(row=0, column=0, columnspan=4, ipady=2, pady=2)
        self.root.bind("<Return>", lambda e: self.equal())
        self.entry.bind("<BackSpace>", self.handle_backspace)

        self.create_buttons()
    def handle_backspace(self, event):
        self.backspace()
        return "break"   

    def click(self, value):
        current = self.entry.get()
        ops = '+-*/'
        if current and current[-1] in ops and value in ops:
            return
        self.entry.insert(tk.END, value)

    def equal(self):
        try:
            expr = self.entry.get()
            expr = re.sub(r'(\d+)%', r'(\1/100)', expr)
            expr = re.sub(r'(\d+\.?\d*)R(\d+\.?\d*)', r'(\2**(1/\1))', expr)
            allowed = {
            'log': math.log10,
            'ln': math.log,
            'sin': math.sin,
            'cos': math.cos,
            'tan': math.tan,
            'sqrt': math.sqrt,
            'factorial':math.factorial,
            'P':math.perm,
            'C':math.comb,
            'asin':math.asin,
            'acos':math.acos,
            'atan':math.atan,
            'π':math.pi,
            'e':math.e
        }
            result = eval(expr, {"__builtins__": None}, allowed)
            self.entry.delete(0, tk.END)
            self.entry.insert(0, result)
        except Exception:
            messagebox.showerror("Error", "Invalid Expression")

    def clear(self):
        self.entry.delete(0, tk.END)
    def backspace(self):
        current = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(0, current[:-1])

    def switch_calculator(self):
        self.root.destroy()
        new_root = tk.Tk()
        Calculator(new_root)
        new_root.mainloop()
    
    def click_log(self):
        self.entry.insert(tk.END, "log(")  # insert as text, user enters number
    def click_ln(self):
        self.entry.insert(tk.END, "ln(")
    def click_factorial(self):
        self.entry.insert(tk.END, "factorial(")  
    def power_button(self):
        self.entry.insert(tk.END, "**")
    def npr(self):
        self.entry.insert(tk.END,'P(')
    def ncr(self):
        self.entry.insert(tk.END,'C(')
    def sin_function(self):
        self.entry.insert(tk.END, 'sin(')
    def cos_function(self):
        self.entry.insert(tk.END, 'cos(')
    def tan_function(self):
        self.entry.insert(tk.END, 'tan(')
    def inverse_sin_function(self):
        self.entry.insert(tk.END, 'asin(')
    def inverse_cos_function(self):
        self.entry.insert(tk.END, 'acos(')
    def inverse_tan_function(self):
        self.entry.insert(tk.END, 'atan(')
    def pi_button(self):
        self.entry.insert(tk.END, 'π')
    def e_button(self):
        self.entry.insert(tk.END, 'e')
    def percent_button(self):
        self.entry.insert(tk.END, '%')
    def epower(self):
            self.entry.insert(tk.END, 'e**')
    def tenpower(self):
        self.entry.insert(tk.END, '10**')
    def root_button(self):
        self.entry.insert(tk.END, 'R')
    def create_buttons(self):
        buttons = [
            ('(', 1, 0), (')', 1, 1), 
            ('7', 5, 0), ('8', 5, 1), ('9', 5, 2),('/', 5, 3),
            ('4', 6, 0), ('5', 6, 1), ('6', 6, 2),('*', 6, 3),
            ('1', 7, 0), ('2', 7, 1), ('3', 7, 2), ('-', 7, 3),
            ('0', 8, 0), ('.', 8, 1),('+', 8, 3), (',',8,4)
        ]

        for txt, r, c in buttons:
            for i in range(6):
                self.frame.columnconfigure(i, weight=1)

            for i in range(6):
                self.frame.rowconfigure(i, weight=1)
            tk.Button(
                self.frame,
                text=txt,
                width=5,
                command=lambda t=txt: self.click(t)
            ).grid(row=r, column=c, pady=2, padx=2,sticky="nsew")

        tk.Button(self.frame, text="AC", width=5, command=self.clear)\
            .grid(row=1, column=3, columnspan=1, pady=2,padx=2,sticky="nsew")
        tk.Button(self.frame, text="⌫", width=5, command=self.backspace)\
            .grid(row=1, column=2, columnspan=1, pady=2,padx=2,sticky="nsew")

        tk.Button(self.frame, text="=", width=5, command=self.equal)\
            .grid(row=8, column=2, columnspan=1, pady=2,padx=2,sticky="nsew")
        tk.Button(self.frame, text="xʸ", width=5, command=self.power_button)\
            .grid(row=2, column=3, columnspan=1, pady=2,padx=2,sticky="nsew")
        tk.Button(self.frame, text="log10", width=5, command=self.click_log)\
            .grid(row=2, column=2, columnspan=1, pady=2,padx=2,sticky="nsew")
        tk.Button(self.frame, text="ln", width=5, command=self.click_ln)\
            .grid(row=2, column=1, columnspan=1, pady=2,padx=2,sticky="nsew")
        tk.Button(self.frame, text="!", width=5, command=self.click_factorial)\
            .grid(row=2, column=0, columnspan=1, pady=2,padx=2,sticky="nsew")
        tk.Button(self.frame, text="Basic Calculator", width=5, command=self.switch_calculator)\
            .grid(row=10, column=0, columnspan=5, pady=2,padx=2,sticky="nsew")
        
        tk.Button(self.frame, text="%", width=5, command=self.percent_button)\
            .grid(row=3, column=0, columnspan=1, pady=2,padx=2,sticky="nsew")
        tk.Button(self.frame, text="e^x", width=5, command=self.epower)\
            .grid(row=3, column=1, columnspan=1, pady=2,padx=2,sticky="nsew")
        tk.Button(self.frame, text="10^x", width=5, command=self.tenpower)\
            .grid(row=3, column=2, columnspan=1, pady=2,padx=2,sticky="nsew")
        tk.Button(self.frame, text="root", width=5, command=self.root_button)\
            .grid(row=3, column=3, columnspan=1, pady=2,padx=2,sticky="nsew")
        
        # Math Values
        tk.Button(self.frame, text="π", width=5, command=self.pi_button)\
            .grid(row=4, column=0, columnspan=1, pady=2,padx=2,sticky="nsew")
        tk.Button(self.frame, text="e", width=5, command=self.e_button)\
            .grid(row=4, column=1, columnspan=1, pady=2,padx=2,sticky="nsew")
        
        # Combinations
        tk.Button(self.frame, text="P(n,r)", width=5, command=self.npr)\
            .grid(row=4, column=2, columnspan=1, pady=2,padx=2,sticky="nsew")
        tk.Button(self.frame, text="C(n,r)", width=5, command=self.ncr)\
            .grid(row=4, column=3, columnspan=1, pady=2,padx=2,sticky="nsew")
        
        # Trig Functions
        tk.Button(self.frame, text="sin", width=5, command=self.sin_function)\
            .grid(row=2, column=4, columnspan=1, pady=2,padx=2,sticky="nsew")
        tk.Button(self.frame, text="cos", width=5, command=self.cos_function)\
            .grid(row=3, column=4, columnspan=1, pady=2,padx=2,sticky="nsew")
        tk.Button(self.frame, text="tan", width=5, command=self.tan_function)\
            .grid(row=4, column=4, columnspan=1, pady=2,padx=2,sticky="nsew")
        tk.Button(self.frame, text="Sin-1", width=5, command=self.inverse_sin_function)\
            .grid(row=5, column=4, columnspan=1, pady=2,padx=2,sticky="nsew")
        tk.Button(self.frame, text="Cos-1", width=5, command=self.inverse_cos_function)\
            .grid(row=6, column=4, columnspan=1, pady=2,padx=2,sticky="nsew")
        tk.Button(self.frame, text="Tan-1", width=5, command=self.inverse_tan_function)\
            .grid(row=7, column=4, columnspan=1, pady=2,padx=2,sticky="nsew")



if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()