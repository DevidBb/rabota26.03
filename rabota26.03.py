from tkinter import *
f=False
def tehtudvalik():
    global f
    if f:
        texbox.configure(show="")
        f=False
    else:
        texbox.configure(show="*")
        f=True
def textpealkirjasse():
    t=texbox.get()
    pealkiri.configure(text=t)
    texbox.delete(0,END)
aken= Tk()
aken.geometry("500x500")
aken.title("Zagolovok")
aken.configure(bg="#03fc13")
aken.iconbitmap("eye.ico")
pealkiri=Label(aken,text="Põhielemendid", bg="#9edb8f",fg="#18420d",cursor="man",font="Times_New_Roman 16", justify=CENTER, height=3,width=26)
raam=Frame(aken)





texbox=Entry(raam,bg="#18420d", fg="#9edb8f", font="Times_New_Roman 16", width=20)
pilt=PhotoImage(file="scary.png")
var=BooleanVar() #IntVar(), StringVar()
valik=Checkbutton(raam, image=pilt,variable=var,onvalue=True,offvalue=False,command=tehtudvalik)
valik.deselect()
nupp=Button(raam,text="Vajuta mind",bg="#18420d", fg="#9edb8f",font="Times_New_Roman 16",width=16, command=textpealkirjasse)




pealkiri.pack()
raam.pack()
texbox.grid(row=0,column=0)
valik.grid(row=0, column=1)
nupp.grid(row=0, column=2)
aken.mainloop()
