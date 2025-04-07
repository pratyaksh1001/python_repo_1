import tkinter as tkr

window=tkr.Tk()

input=tkr.Entry()
input.grid(column=1,row=0,padx=5,pady=5)
l1=tkr.Label(text="Miles")
l1.grid(column=2,row=0,padx=5,pady=5)
l2=tkr.Label(text="Miles to KM is")
l2.grid(column=0,row=1)
l4=tkr.Label(text="KM")
l4.grid(column=1,row=2)
def press():
    txt=input.get()
    l3 = tkr.Label()
    l3.grid(column=1, row=1)
    l3.config(text=str(int(txt)*1.6)+" KM")

btn=tkr.Button(text="Calculate",command=press)
btn.grid(row=2,column=1)

window.mainloop()