import tkinter as tk

def on_click(button_value):
    current_text = result_var.get()
    if button_value == '=':
        try:
            result_var.set(eval(current_text))
        except Exception as e:
            result_var.set("Error")
    elif button_value == "C":
        result_var.set('')
    else:
        result_var.set(current_text + str(button_value))

root = tk.Tk()
root.title("Colorful Calculator")
root.geometry("310x510")
root.configure(bg='#282828')

result_var = tk.StringVar()

result_entry = tk.Entry(root, textvariable=result_var, font=('Arial', 20), bd=10, insertwidth=4, width=18, justify='right', bg='#1e1e1e', fg='white')
result_entry.grid(row=0, column=0, columnspan=8, pady=10)

button_colors = [
    ('#444444', '#ffffff'), ('#444444', '#ffffff'), ('#444444', '#ffffff'), ('#f08080', '#ffffff'),
    ('#444444', '#ffffff'), ('#444444', '#ffffff'), ('#444444', '#ffffff'), ('#f08080', '#ffffff'),
    ('#444444', '#ffffff'), ('#444444', '#ffffff'), ('#444444', '#ffffff'), ('#f08080', '#ffffff'),
    ('#444444', '#ffffff'), ('#444444', '#ffffff'), ('#4caf50', '#ffffff'), ('#f08080', '#ffffff'),
    ('#444444', '#ffffff')
]

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    "C"
]

row_val = 1
col_val = 0

for i, button in enumerate(buttons):
    color = button_colors[i]
    tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 14), command=lambda b=button: on_click(b),
              bg=color[0], fg=color[1]).grid(row=row_val, column=col_val, pady=5, padx=5)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Start the Tkinter main loop
root.mainloop()