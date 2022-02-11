#Importação das Bibliotecas

from tkinter import *
from tkinter import messagebox
from tkinter import font
from tkinter import ttk
from turtle import left

# Criar Windows

win = Tk()
win.title("Miliotte System - Acess Panel")
win.geometry("600x300")
win.configure(background="white")
win.resizable(width=FALSE, height=False)
win.attributes("-alpha", 0.9)
win.iconbitmap(default="img/logoIcon.ico")

logo = PhotoImage(file="img/logo.png")

LeftFrame = Frame(win, width=200, height=300, bg="MIDNIGHTBLUE", relief="raise")
LeftFrame.pack(side=LEFT)

Rightrame = Frame(win, width=395, height=300, bg="MIDNIGHTBLUE", relief="raise")
Rightrame.pack(side=RIGHT)

LogoLabel = Label(LeftFrame, image=logo, bg='MIDNIGHTBLUE')
LogoLabel.place(x=50 , y=100)

#####Label User
UserLabel = Label(Rightrame, text="Username:", font=("Century Gothic", 20), bg='MIDNIGHTBLUE' , fg="White")
UserLabel.place(x=5, y=100)

UserEntry = ttk.Entry(Rightrame, width=30)
UserEntry.place(x=150, y=113)

#####Label Password

PassLabel = Label(Rightrame, text="Password:", font=("Century Gothic", 20), bg='MIDNIGHTBLUE' , fg="White")
PassLabel.place(x=6, y=150)

PassEntry = ttk.Entry(Rightrame, width=30, show="•")
PassEntry.place(x=150, y=160)

##Button

LoginButton = ttk.Button(Rightrame, text="Login", width=30)
LoginButton.place(x=100, y=225)

def Register():
    LoginButton.place(x=5000)
    RegisterButton.place(x=5000)

RegisterButton = ttk.Button(Rightrame, text="Register", width=20, command=Register)
RegisterButton.place(x=130, y=260)

win.mainloop()

