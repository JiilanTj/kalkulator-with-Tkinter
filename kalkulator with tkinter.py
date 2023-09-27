import tkinter as tk

def on_click(event):
    text = event.widget.cget("text")
    
    if text == "=":
        try:
            expression = entry.get()
            result = eval(expression)
            entry.delete(0, tk.END)  # Hapus teks yang ada di entry
            entry.insert(0, result)  # Tampilkan hasil
        except Exception as e:
            entry.delete(0, tk.END)  # Hapus teks yang ada di entry
            entry.insert(0, "Error")
    elif text == "C":
        entry.delete(0, tk.END)  # Hapus teks yang ada di entry
    else:
        entry.insert(tk.END, text)

# Membuat jendela utama 
root = tk.Tk()
root.title("Kalkulator")

# Membuat entry untuk input
entry = tk.Entry(root, font=("Arial", 24), justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Tombol-tombol kalkulator
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row_val = 1
col_val = 0

for button_text in buttons:
    button = tk.Button(root, text=button_text, padx=20, pady=20, font=("Arial", 18))
    button.grid(row=row_val, column=col_val)
    button.bind("<Button-1>", on_click)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()
