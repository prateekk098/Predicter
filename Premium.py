# import tkinter as tk
from tkinter import *
import numpy as np
import joblib
from tkinter import messagebox

mydata = joblib.load("premium_predicter.joblib")

root = Tk()
root.title("Premium Checker")
root.geometry("600x300")
root.config(bg = "#fcba03")

def ent_clear():
    ent1.delete(0,END)

def ent_submit():
    # if ent1 == "":
    #     messagebox.showerror("Error","Field Can't be Empty")
        user_input = float(ent1.get())
        user_input1 = np.array(user_input)
        reshape_data = user_input1.reshape(-1,1)
        premium = mydata.predict(reshape_data)[0]
        
        res.config(text = f"Your predicted Premium is : {str(premium)[:8]}")
        ent1.delete(0,END)
        
    
lab1 = Label(text="Premium Predicter",font="robort 28 bold",bg="#fcba03",fg="red").pack(ipady=22)
ent1 = Entry(root,font="robort 28",fg="#e6e3dc")
ent1.insert(0,"Please Enter the Age")

ent1.pack()

btn1 = Button(text="Clear",fg="#fcba03",bg="red",font="robort 17 bold",border=5,command = ent_clear).place(x = 210,y=150)
btn1 = Button(text="Submit",fg="#fcba03",bg="red",font="robort 17 bold",border=5,command = ent_submit).place(x = 300,y=150)
res = Label(text="",bg="#fcba03",font="robort 12 bold")
res.place(x=180,y=230)
root.mainloop( )