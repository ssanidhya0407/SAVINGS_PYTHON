#From Tkinter
from tkinter import *
from tkinter import Frame as fr
from PIL import Image, ImageTk
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter.font import Font
from tkinter import messagebox
import tkinter as tk
from tkinter import StringVar
from tkinter import filedialog
from tkPDFViewer import tkPDFViewer as pdf
from cefpython3 import cefpython as cef

#Import Module
import getpass
import sqlite3
import itertools
import math
import time
import sys
import os
import random
import json
import calendar
from fpdf import FPDF
from selenium import webdriver
from django.shortcuts import render, redirect
from calendar import HTMLCalendar

#from DateTime
from datetime import datetime
from datetime import date
from datetime import datetime

#From Selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#ReportLab
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle, Frame, Paragraph, Spacer
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

#From dateutility
from dateutil import relativedelta

#From Flask
from flask import Flask, render_template, request


root = Tk()
root.geometry('1600x900+0+0')
root.title('Saving Details')
root.config(bg='gray')
root.state('zoomed')

#INSIDER WINDOWS CREATION

##SAVINGS ACCOUNT WINDOWS
def savings1():
    savings1 = Toplevel(root)
    savings1.title('Savings Account Details')
    savings1.config(bg='light yellow')
    savings1.geometry('1293x730+295+95')
    savings1.focus_force()


    def savings_pdf():
        pdf=FPDF()
        pdf.add_page()
        element_list = ["Account Number","Customer ID","Name(s)","Remark(s)","ATM Card Detail","Bank Name","Branch Name","A/C Open Date"]
        pdf.set_font("Times", style="BU", size=28)
        pdf.set_xy(x=3, y=2)
        pdf.cell(w=202, h=13, txt="Savings Report", border=1, align='C')
        pdf.set_font("Arial", style="", size=10)
        pdf.set_auto_page_break(auto=False, margin=2)
        con = sqlite3.connect(database=r'savings.db')
        cur = con.cursor()
        cur.execute('select * from savings')
        rows = cur.fetchall()
        y_pos=20
        num = -1
        count = len(rows)
        partn = int(count / 4)
        main_partn=int(count/partn)
        for i in rows:
            num+=1
            y_pos+=3
            for j, k in itertools.zip_longest(rows[num],element_list):
                pdf.set_xy(x=3, y=y_pos)
                pdf.cell(w=50, h=8, txt=k, border=1, align='L')
                pdf.set_xy(x=63, y=y_pos)
                pdf.cell(w=142, h=8, txt=j, border=1, align='R')
                y_pos = y_pos + 8
            if partn >= 1 and num == (main_partn-1):
                pdf.add_page()
                pdf.set_font("Arial", style="", size=10)
                pdf.set_auto_page_break(auto=False, margin=2)
                y_pos=10
                partn = partn - 1
                main_partn=main_partn+4
        pdf.output('Savings Report.pdf', 'F')

    # Creating the functions
    def counter():
        counter_tuple = 0
        counter_tuple1 = 0
        tuple = (
            var_Ac.get(), var_custID.get(), var_branch.get(), var_remark.get(), var_card.get(), var_opendate.get())
        for i in range(0, 5):
            if (tuple[i] == ""):
                counter_tuple += 1
            else:
                continue

        tuple2 = (var_Name.get(), var_bank.get())
        for i in range(0, 2):
            if (tuple2[i] == "Select"):
                counter_tuple1 += 1
            else:
                continue

        global finalcount_str, finalcount
        finalcount = counter_tuple + counter_tuple1
        finalcount_str = str(finalcount)


    def databaseOpen():
       con = sqlite3.connect(database=r'savings.db')
       cur = con.cursor()
       try:
           cur.execute('select * from savings')
           rows = cur.fetchall()
           database.delete(*database.get_children())
           for row in rows:
               database.insert("", END, values=row)

       except Exception as ex:
           messagebox.showerror("SQL Database", f"Error Details: {str(ex)}", parent=savings1)



    def save():
        con = sqlite3.connect(database=r'savings.db')
        cur = con.cursor()
        try:
            if (var_Ac.get() == "" and finalcount == 1):
                messagebox.showerror('SQL Database', "A/C No. Required", parent=savings1)
            elif (var_custID.get() == "" and finalcount == 1):
                messagebox.showerror('SQL Database', "Customer ID Required", parent=savings1)
            elif (var_remark.get() == "" and finalcount == 1):
                messagebox.showerror('SQL Database', "Remarks Required", parent=savings1)
            elif (var_bank.get() == "" and finalcount == 1):
                messagebox.showerror('SQL Database', "Bank Name Required", parent=savings1)
            elif (var_branch.get() == "" and finalcount == 1):
                messagebox.showerror('SQL Database', "Branch Name Required", parent=savings1)
            elif (var_Name.get() == "" and finalcount == 1):
                messagebox.showerror('SQL Database', "Name Of A/C Holders Required", parent=savings1)
            elif (var_card.get() == "" and finalcount == 1):
                messagebox.showerror('SQL Database', "ATM Card Number Required", parent=savings1)
            elif (var_opendate.get() == "" and finalcount == 1):
                messagebox.showerror('SQL Database', "A/C Open Date Required", parent=savings1)
            elif (finalcount >= 2):
                messagebox.showerror('SQL Database', f"{str(finalcount_str)} Fields Required", parent=savings1)
            elif (finalcount==0):
                cur.execute(
                    'Insert into savings(Ac, custID, Name, remark, card, bank, branch, opendate) values(?,?,?,?,?,?,?,?)',
                    (
                        var_Ac.get(),
                        var_custID.get(),
                        var_Name.get(),
                        var_remark.get(),
                        var_card.get(),
                        var_bank.get(),
                        var_branch.get(),
                        var_opendate.get(),
                ))
                con.commit()
                messagebox.showinfo('SQL Database', 'Account Details Added Successfully', parent=savings1)
                databaseOpen()

        except Exception as ex:
            messagebox.showerror("SQL Database", f"Error Details: {str(ex)}", parent=savings1)


    def update():
        con = sqlite3.connect(database=r'savings.db')
        cur = con.cursor()
        try:
            if (var_Ac.get() == "" and finalcount == 1):
                messagebox.showerror('SQL Database', "A/C No. Required", parent=savings1)
            elif (var_custID.get() == "" and finalcount == 1):
                messagebox.showerror('SQL Database', "Customer ID Required", parent=savings1)
            elif (var_remark.get() == "" and finalcount == 1):
                messagebox.showerror('SQL Database', "Remarks Required", parent=savings1)
            elif (var_bank.get() == "" and finalcount == 1):
                messagebox.showerror('SQL Database', "Bank Name Required", parent=savings1)
            elif (var_branch.get() == "" and finalcount == 1):
                messagebox.showerror('SQL Database', "Branch Name Required", parent=savings1)
            elif (var_Name.get() == "" and finalcount == 1):
                messagebox.showerror('SQL Database', "Name Of A/C Holders Required", parent=savings1)
            elif (var_card.get() == "" and finalcount == 1):
                messagebox.showerror('SQL Database', "ATM Card Details Required", parent=savings1)
            elif (var_opendate.get() == "" and finalcount == 1):
                messagebox.showerror('SQL Database', "A/C Open Date Required", parent=savings1)
            elif (finalcount >= 2):
                messagebox.showerror('SQL Database', f"{str(finalcount_str)} Fields Required", parent=savings1)
            elif (finalcount == 0):
                cur.execute('Select * from savings where Ac=?', (var_Ac.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("SQL Database", "Invalid Account Number", parent=savings1)
                else:
                    cur.execute(
                        'Update savings set remark=?, bank=?, branch=?, Name=?, card=?, custID=?, opendate=? where Ac=?',(
                            var_remark.get(),
                            var_bank.get(),
                            var_branch.get(),
                            var_Name.get(),
                            var_card.get(),
                            var_custID.get(),
                            var_opendate.get(),
                            var_Ac.get(),
                        ))
                    con.commit()
                    messagebox.showinfo('SQL Database', 'Account Details Updated Successfully', parent=savings1)
                    databaseOpen()
                    
        except Exception as ex:
                    messagebox.showerror("SQL Database", f"Error Details: {str(ex)}", parent=savings1)
    def delete():
        con = sqlite3.connect(database=r'savings.db')
        cur = con.cursor()
        try:
            if (var_Ac.get() == "" and finalcount == 1):
                messagebox.showerror('SQL Database', "A/C No. Required", parent=savings1)
            elif (var_custID.get() == "" and finalcount == 1):
                messagebox.showerror('SQL Database', "Customer ID Required", parent=savings1)
            elif (var_remark.get() == "" and finalcount == 1):
                messagebox.showerror('SQL Database', "Remarks Required", parent=savings1)
            elif (var_bank.get() == "" and finalcount == 1):
                messagebox.showerror('SQL Database', "Bank Name Required", parent=savings1)
            elif (var_branch.get() == "" and finalcount == 1):
                messagebox.showerror('SQL Database', "Branch Name Required", parent=savings1)
            elif (var_Name.get() == "" and finalcount == 1):
                messagebox.showerror('SQL Database', "Name Of A/C Holders Required", parent=savings1)
            elif (var_card.get() == "" and finalcount == 1):
                messagebox.showerror('SQL Database', "ATM Card Details Required", parent=savings1)
            elif (var_opendate.get() == "" and finalcount == 1):
                messagebox.showerror('SQL Database', "A/C Open Date Required", parent=savings1)
            elif (finalcount >= 2):
                messagebox.showerror('SQL Database', f"{str(finalcount_str)} Fields Required", parent=savings1)
            elif (finalcount == 0):
                cur.execute('Select * from savings where Ac=?', (var_Ac.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("SQL Database", "Invalid Account Number", parent=savings1)
                else:
                    op = messagebox.askyesno('SQL Database', "Do You Want To Delete The Selected Record?", parent=savings1)
                    if op == True:
                        cur.execute('delete from savings where Ac=?', (var_Ac.get(),))
                        con.commit()
                        messagebox.showinfo('SQL Database', 'Account Details Deleted Successfully', parent=savings1)
                        databaseOpen()



        except Exception as ex:
            messagebox.showerror("SQL Database", f"Error Details: {str(ex)}", parent=savings1)



    def passData(ev):
       f = database.focus()
       content = (database.item(f))
       row = content['values']
       var_Ac.set(row[0])
       var_custID.set(row[1])
       var_Name.set(row[2])
       var_remark.set(row[3])
       var_card.set(row[4])
       var_bank.set(row[5])
       var_branch.set(row[6])
       var_opendate.set(row[7])

    def clear():
        var_Ac.set("")
        var_custID.set("")
        var_Name.set("Select")
        var_remark.set("")
        var_card.set("")
        var_bank.set("Select")
        var_branch.set("")
        var_opendate.set("")



    # Additional Font
    font1 = Font(family='Helvetica', size=24, underline=1)

    # Title
    title = Label(savings1, text='Savings Account Details', compound=LEFT,
                  font=('courier', 40, 'bold'), bg='lightyellow', fg='black', anchor='n').place(x=2, y=10,
                                                                                                width=850,
                                                                                                height=70)
    generatesavingreportpdf=Button(savings1, text="Generate PDF", bg='red', fg='yellow',font=('courier', 20, 'bold'),
                                   bd=4, relief=RAISED, command=lambda: [savings_pdf()], cursor='hand2').place(x=1000,
                                                                                                         y=20,
                                                                                                         width=200,
                                                                                                         height=45)

    # Underline 1
    underline = Label(savings1,
                      text='                                                                                                                                                             ',
                      font=font1, bg='lightyellow', fg='black').place(x=0, y=64, width=1400)


    # Database
    database_Frame = fr(savings1, bd=3, relief=RIDGE)
    database_Frame.place(x=-2, y=100, relwidth=1, height=300)

    # ScrollBars
    scroll_xdir = Scrollbar(database_Frame, orient=HORIZONTAL)
    scroll_ydir = Scrollbar(database_Frame, orient=VERTICAL)

    # Table Creation
    database = ttk.Treeview(database_Frame,
                            columns=(
                                'Ac', 'custID', 'Name', 'remark', 'card', 'bank', 'branch', 'opendate'),
                            yscrollcommand=scroll_ydir.set, xscrollcommand=scroll_xdir.set)
    scroll_xdir.pack(side=BOTTOM, fill=X)
    scroll_ydir.pack(side=RIGHT, fill=Y)
    scroll_ydir.config(command=database.yview)
    scroll_xdir.config(command=database.xview)
    database.heading('Ac', text="A/C No.")
    database.heading('custID', text="CustID")
    database.heading('Name', text="Name(s)")
    database.heading('remark', text="Remarks")
    database.heading('card', text="ATM Card Details")
    database.heading('bank', text="Bank")
    database.heading('branch', text="Branch")
    database.heading('opendate', text="A/C Open Date")

    database['show'] = 'headings'

    database.column('Ac', width="100")
    database.column('custID', width="100")
    database.column('Name', width="200")
    database.column('remark', width="100")
    database.column('card', width="150")
    database.column('bank', width="100")
    database.column('branch', width="100")
    database.column('opendate', width="100")

    database.pack(fill=BOTH, expand=1)
    database.bind('<ButtonRelease-1>', passData)

    databaseOpen()

    # Declaring Savings Detail Variables
    var_Ac = StringVar()
    var_Name = StringVar()
    var_branch = StringVar()
    var_bank = StringVar()
    var_custID = StringVar()
    var_card = StringVar()
    var_remark = StringVar()
    var_opendate = StringVar()


    ###Buttons On The Savings A/C Page
    Save_Btn = Button(savings1, text='Save', command=lambda: [counter(), save(), clear()], cursor='hand2',
                       font=('helvetica', 30), bg='IndianRed2', fg='black', bd=4, relief=RAISED).place(x=1150, y=444,
                                                                                                       width=140,
                                                                                                       height=45)
    Update_Btn = Button(savings1, text='Update', command=lambda: [counter(), update(), clear()], cursor='hand2',
                         font=('helvetica', 30), bg='gold', fg='black', bd=4, relief=RAISED).place(x=1150, y=524,
                                                                                                   width=140,
                                                                                                   height=46)
    Delete_Btn = Button(savings1, text='Delete', command=lambda: [counter(), delete(), clear()], cursor='hand2',
                         font=('helvetica', 30), bg='OliveDrab2', fg='black', bd=4, relief=RAISED).place(x=1150,
                                                                                                         y=604,
                                                                                                         width=140,
                                                                                                         height=45)
    Clear_Btn = Button(savings1, text='Clear', command=lambda: [clear()], cursor='hand2', font=('helvetica', 30),
                        bg='DodgerBlue', fg='black', bd=4, relief=RAISED).place(x=1150, y=684, width=140, height=45)


    # Add Savings Details
    Ac_Lbl = Label(savings1, text='A/C No.', font=('goudy old style', 30, 'bold'), bg='lightyellow',
                      fg='black').place(x=-20, y=444, width=250, height=60)
    Ac_Entry = Entry(savings1, textvariable=var_Ac, font=('goudy old style', 15, 'bold'), bd=2, relief=SUNKEN,
                        bg='white', fg='black').place(x=230, y=449, width=150, height=50)

    custID_Lbl = Label(savings1, text='Cust ID', font=('goudy old style', 30, 'bold'), bg='lightyellow',
                     fg='black').place(
        x=380, y=444, width=250, height=60)
    custID_Entry = Entry(savings1, textvariable=var_custID, font=('goudy old style', 15, 'bold'), bd=2, relief=SUNKEN,
                       bg='white', fg='black').place(x=570, y=449, width=150, height=50)

    remark_Lbl = Label(savings1, text='Remarks', font=('goudy old style', 30, 'bold'), bg='lightyellow',
                       fg='black').place(
        x=-20, y=544, width=250, height=60)
    remark_Entry = Entry(savings1, textvariable=var_remark, font=('goudy old style', 15, 'bold'), bd=2,
                         relief=SUNKEN,
                         bg='white', fg='black').place(x=230, y=549, width=150, height=50)

    bank_Lbl = Label(savings1, text='Bank ', font=('goudy old style', 30, 'bold'), bg='lightyellow',
                       fg='black').place(
        x=380, y=544, width=250, height=60)
    bank_Combobox = ttk.Combobox(savings1, textvariable=var_bank,
                                   values=('Select', 'ICICI', 'SBI', 'BOB', 'HDFC', 'POST OFFICE'), state='readonly',
                                   justify=CENTER,
                                   font=('verdana', 15))
    bank_Combobox.place(x=570, y=560, width=150)
    bank_Combobox.current(0)

    Name_Lbl = Label(savings1, text='Name', font=('goudy old style', 30, 'bold'), bg='lightyellow',
                            fg='black').place(x=-20, y=644, width=250, height=60)
    Name_Combobox = ttk.Combobox(savings1, textvariable=var_Name,
                                        values=('Select', 'Shalini', 'SL+VK', 'Vinay', 'SL+VK+SS', 'VK+SS'), state='readonly', justify=CENTER,
                                        font=('verdana', 15))
    Name_Combobox.place(x=230, y=660, width=150)
    Name_Combobox.current(0)

    card_Lbl = Label(savings1, text='Card No.', font=('goudy old style', 30, 'bold'), bg='lightyellow',
                       fg='black').place(
        x=380, y=644, width=250, height=60)
    card_Entry = Entry(savings1, textvariable=var_card, font=('goudy old style', 15, 'bold'), bd=2, relief=SUNKEN,
                       bg='white', fg='black').place(x=590, y=660, width=400)

    branch_Lbl = Label(savings1, text='Branch', font=('goudy old style', 30, 'bold'), bg='lightyellow',
                      fg='black').place(
        x=720, y=444, width=250, height=60)
    branch_Entry = Entry(savings1, textvariable=var_branch, font=('goudy old style', 15, 'bold'), bd=2, relief=SUNKEN,
                        bg='white', fg='black').place(x=940, y=449, width=150, height=50)

    opendate_Lbl = Label(savings1, text='Open Date', font=('goudy old style', 30, 'bold'), bg='lightyellow',
                         fg='black').place(x=720, y=544, width=250, height=60)
    opendate_Entry = Entry(savings1, textvariable=var_opendate, font=('goudy old style', 15, 'bold'), bd=2,
                        relief=SUNKEN, bg='white', fg='black').place(x=940, y=549, width=150, height=50)


##MF WINDOWS
def mf():
    mf = Toplevel(root)
    mf.title('Mutual Fund Account Details')
    mf.config(bg='light yellow')
    mf.geometry('1293x730+295+95')
    mf.focus_force()

##NSC WINDOWS
def nsc():
    nsc = Toplevel(root)
    nsc.title('National Savings Certificates Account Details')
    nsc.config(bg='light yellow')
    nsc.geometry('1293x730+295+95')
    nsc.focus_force()

##PIN WINDOWS
def pin():
    pin = Toplevel(root)
    pin.title('PIN Account Details')
    pin.config(bg='light yellow')
    pin.geometry('1293x730+295+95')
    pin.focus_force()

##LIC WINDOWS
def lic():
    lic = Toplevel(root)
    lic.title('LIC Account Details')
    lic.config(bg='light yellow')
    lic.geometry('1293x730+295+95')
    lic.focus_force()

##INSURANCE DETAILS
def insurance():
    insurance = Toplevel(root)
    insurance.title('Insurance Account Details')
    insurance.config(bg='light yellow')
    insurance.geometry('1293x730+295+95')
    insurance.focus_force()

##PPF DETAILS
def ppf():
    ppf = Toplevel(root)
    ppf.title('Public Provident Fund Account Details')
    ppf.config(bg='light yellow')
    ppf.geometry('1293x730+295+95')
    ppf.focus_force()


#ROOT SETUP
# Title
logo_title10 = PhotoImage(file='images/Extras/R1.png')
title = Label(root, text=' Savings - Vinay & Shalini', image=logo_title10, compound=LEFT,
              font=('courier', 40, 'bold'), bg='#020b39', fg='white', anchor='w').place(x=0, y=0, relwidth=1,
                                                                                        height=70)


def logoutBtn():
    root.destroy()

# Remarks Button
Remarks_Btn = Button(root, text='Remarks', font=('lucid consolas', 28, 'bold'), bg='green', cursor='hand2',
                    fg='yellow').place(x=1190, y=12, height=47)

# Logout Button
Logout_Btn = Button(root, text='Logout', font=('lucid consolas', 28, 'bold'), bg='red', cursor='hand2',
                    command=logoutBtn,
                    fg='yellow').place(x=1420, y=12, height=47)

# Creating the Menu Side Bar
Left_Tabs = fr(root, bd=1, relief=RIDGE, bg='white')
Left_Tabs.place(x=0, y=72, width=301, height=780)

#Creating The Startup Image
StartupImage = fr(root, bd=1, relief=RIDGE, bg='white')
StartupImage.place(x=301, y=71, width=1300, height=765)

#Placing the Startup Image
startupimage= PhotoImage(file='images/Extras/SAVINGS_PYTHON_PIC.png')
Image = Label(StartupImage, image=startupimage,bg='light yellow', fg='black', anchor='center', bd=3)
Image.pack(fill=BOTH)

# Date Details
sandy1 = date.today().strftime("%d-%m-%Y")
Date = Label(Left_Tabs, relief=RAISED, text=sandy1, compound=LEFT, font=('times new roman', 30),
                 bg='light yellow', fg='black', anchor='center', bd=3).pack(side=TOP, fill=X)

# SAVINGS A/C Tab
Savings_Btn = Button(Left_Tabs, text='Savings A/C', compound=LEFT, command=savings1,
                      font=('times new roman', 30), bg='sky blue', fg='black', cursor='hand2', anchor='center',
                      bd=3).pack(side=TOP, fill=X)

# FD Tab
FD_Btn = Button(Left_Tabs, text='Fixed Deposit', compound=LEFT,
                      font=('times new roman', 30), bg='sky blue', fg='black', cursor='hand2', anchor='center',
                      bd=3).pack(side=TOP, fill=X)

# MF Tab
MF_Btn = Button(Left_Tabs, text='Mutual Fund', compound=LEFT,
                      font=('times new roman', 30), bg='sky blue', fg='black', cursor='hand2', anchor='center',
                      bd=3).pack(side=TOP, fill=X)

# NSC Tab
NSC_Btn = Button(Left_Tabs, text='Nat. Sav. Cert.', compound=LEFT,
                      font=('times new roman', 30), bg='sky blue', fg='black', cursor='hand2', anchor='center',
                      bd=3).pack(side=TOP, fill=X)

# PIN Tab
PIN_Btn = Button(Left_Tabs, text='Pin Details', compound=LEFT, font=('times new roman', 30), bg='sky blue', fg='black', cursor='hand2',
                            anchor='c', bd=3).pack(side=TOP, fill=X)

# LIC Tab
LIC_Btn = Button(Left_Tabs, text='LIC', compound=LEFT,
                     font=('times new roman', 30), bg='sky blue', fg='black', cursor='hand2', anchor='c',
                     bd=3).pack(
    side=TOP, fill=X)

# Insurance Tab
Insurance_Btn = Button(Left_Tabs, text='Insurance', compound=LEFT,
                  font=('times new roman', 30), bg='sky blue', fg='black', cursor='hand2', anchor='c', bd=3).pack(
    side=TOP, fill=X)

# PPF Tab
PPF_Btn = Button(Left_Tabs, text='Pub. Prov. Fund',compound=LEFT,
                      font=('times new roman', 30), bg='sky blue', fg='black', cursor='hand2', anchor='c',
                      bd=3).pack(
    side=TOP, fill=X)

# Time Details
current_time = datetime.now().strftime("%H:%M:%S")
Time = Button(Left_Tabs, relief=RAISED, text="GENERATE PDF", compound=LEFT, font=('times new roman', 30),
                 bg='red', fg='yellow', anchor='center', bd=3).pack(side=TOP, fill=X)

#ROOT ENDS

root.mainloop()