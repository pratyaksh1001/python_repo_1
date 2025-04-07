import tkinter as tk

window=tk.Tk()

window.title("The first GUI")
window.minsize(800,400)
lab=tk.Label(text="i am a lable",font=("consolas",24,"bold"))
lab.pack(side="left",expand=True)










window.mainloop()