from tkinter import *

f = True  # Изначально показывать пароль
user_credentials = {}  # Словарь для хранения учетных записей пользователей

def tehtudvalik():
    global f
    if f:
        texbox.configure(show="")
        valik.configure(image=pilt_hide)
        f = False
    else:
        texbox.configure(show="*")
        valik.configure(image=pilt_show)
        f = True

def textpealkirjasse():
    t = texbox.get()
    pealkiri.configure(text=t)
    texbox.delete(0, END)

def login():
    username = login_entry.get()
    password = texbox.get()

    if username in user_credentials:
        if user_credentials[username] == password:
            result_label.config(text="Успешный вход!", fg="green")
        else:
            result_label.config(text="Неправильный пароль!", fg="red")
    else:
        result_label.config(text="Пользователь не существует!", fg="red")

def register():
    username = login_entry.get()

    if username in user_credentials:
        result_label.config(text="Пользователь уже существует!", fg="red")
    else:
        user_credentials[username] = texbox.get()
        result_label.config(text="Успешно зарегистрирован!", fg="green")

def change_password():
    # Add code here to change the password
    pass

aken = Tk()
aken.geometry("500x500")
aken.title("Odnaklassniki")
aken.configure(bg="#F4D03F")

pealkiri = Label(aken, text="Добро пожаловать в однаклассники", bg="#9edb8f", fg="#18420d", cursor="man", font="Times_New_Roman 16", justify=CENTER, height=3, width=30)
raam = Frame(aken, bg="white")

login_label = Label(raam, text="Login:", font="Times_New_Roman 16", bg="white")  
login_entry = Entry(raam, font="Times_New_Roman 16")

password_label = Label(raam, text="Password:", font="Times_New_Roman 16", bg="white")  
texbox = Entry(raam, bg="white", fg="#18420d", font="Times_New_Roman 16", width=20)  

pilt_hide = PhotoImage(file="eyyee.png")  # Изображение закрытого глаза
pilt_show = PhotoImage(file="glaz.png")  # Изображение открытого глаза
var = BooleanVar()  
valik = Checkbutton(raam, image=pilt_show, variable=var, onvalue=True, offvalue=False, command=tehtudvalik)
valik.select()  # Галочка показывает, что пароль показывается изначально

login_button = Button(raam, text="Вход", bg="#007acc", fg="#9edb8f", font="Times_New_Roman 16", width=8, command=login)
register_button = Button(raam, text="Регистрация", bg="#007acc", fg="#9edb8f", font="Times_New_Roman 16", width=12, command=register)
change_password_button = Button(raam, text="Сменить пароль", bg="#007acc", fg="#9edb8f", font="Times_New_Roman 16", width=12, command=change_password)

result_label = Label(raam, text="", font="Times_New_Roman 12")

password_bottom_label = Label(raam, text="Password", font="Times_New_Roman 12", bg="white")  

pealkiri.pack()
raam.pack()

login_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")  
login_entry.grid(row=0, column=1, padx=10, pady=5, sticky="e")  

password_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")  
texbox.grid(row=1, column=1, padx=10, pady=5, sticky="e")  
valik.grid(row=1, column=2, padx=10, pady=5)

login_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5)
register_button.grid(row=2, column=1, columnspan=2, padx=10, pady=5)
change_password_button.grid(row=2, column=2, columnspan=2, padx=10, pady=5)
result_label.grid(row=3, columnspan=3, padx=10, pady=5)
aken.mainloop()
