import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(str(screen.get())))
            screen.set(result)
        except:
            screen.set("Error")
    elif text == "C":
        screen.set("")
    else:
        screen.set(screen.get() + text)

root = tk.Tk()
root.geometry("400x600")
root.title("Simple Calculator")

screen = tk.StringVar()
entry = tk.Entry(root, textvar=screen, font="Arial 20", justify='right')
entry.pack(fill="both", ipadx=8, ipady=20, padx=10, pady=10)

# Calculator button layout
buttons = [
    ['%', 'CE', 'C', '⌫'],
    ['1/x', 'x²', '√', '÷'],
    ['7', '8', '9', '*'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '+'],
    ['±', '0', '.', '=']
]

for row in buttons:
    frame = tk.Frame(root)
    for btn in row:
        b = tk.Button(frame, text=btn, font="Arial 18", height=2, width=6)
        b.pack(side="left", padx=5, pady=5)
        b.bind("<Button-1>", click)
    frame.pack()

root.mainloop()