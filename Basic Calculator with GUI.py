import tkinter as tk

def calculate():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    operation = operation_var.get()

    if operation == "+":
        result.set(num1 + num2)
    elif operation == "-":
        result.set(num1 - num2)
    elif operation == "*":
        result.set(num1 * num2)
    elif operation == "/":
        if num2 != 0:
            result.set(num1 / num2)
        else:
            result.set("Error: Division by zero")

app = tk.Tk()
app.title("Calculator")

entry_num1 = tk.Entry(app)
entry_num1.pack()

entry_num2 = tk.Entry(app)
entry_num2.pack()

operation_var = tk.StringVar()
operation_choices = ["+", "-", "*", "/"]
operation_menu = tk.OptionMenu(app, operation_var, *operation_choices)
operation_menu.pack()

calculate_button = tk.Button(app, text="Calculate", command=calculate)
calculate_button.pack()

result = tk.StringVar()
result_label = tk.Label(app, textvariable=result)
result_label.pack()

app.mainloop()
