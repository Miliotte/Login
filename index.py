#Importação das Bibliotecas

from tkinter import *
from tkinter import messagebox
from turtle import left

# Criar Windows



win = Tk()
win.title("Miliotte System - Acess Panel")
win.geometry("600x300")
win.configure(background="white")
win.resizable(width=FALSE, height=False)

logo = PhotoImage(file="img/logo.png")

LeftFrame = Frame(win, width=200, height=300, bg="MIDNIGHTBLUE", relief="raise")
LeftFrame.pack(side=LEFT)

Rightrame = Frame(win, width=395, height=300, bg="MIDNIGHTBLUE", relief="raise")
Rightrame.pack(side=RIGHT)

LogoLabel = Label(LeftFrame, image=logo, bg='MIDNIGHTBLUE')
LogoLabel.place(x=50 , y=100)

win.mainloop()

