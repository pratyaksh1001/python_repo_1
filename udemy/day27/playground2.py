import tkinter as tk

window=tk.Tk()
window.minsize(800,400)
l1=tk.Label(text="hello world")
l1.pack()
inp=tk.Entry(width=30)
inp.pack()
def change():
    l1["text"]=inp.get()

button=tk.Button(text="Click Me",command=change)
button.pack()

window.mainloop()