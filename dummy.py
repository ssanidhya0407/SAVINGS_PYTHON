
##FD WINDOWS
def fd1():
    fd1 = Toplevel(root)
    fd1.title('Fixed Deposit Details')
    fd1.config(bg='light yellow')
    fd1.geometry('1293x730+295+95')
    fd1.focus_force()

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

        tuple2 = (var_bank.get(),var_branch.get(),var_autorenewal.get(),var_autoclosure.get())
        for i in range(0, 2):
            if (tuple2[i] == "Select"):
                counter_tuple1 += 1
            else:
                continue

        global finalcount_str, finalcount
        finalcount = counter_tuple + counter_tuple1
        finalcount_str = str(finalcount)

    def databaseOpen():
         con = sqlite3.connect(database=r'fixeddeposit.db')
         cur = con.cursor()
         try:
             cur.execute('select * from fixeddeposit')
             rows = cur.fetchall()
             database.delete(*database.get_children())
             for row in rows:
                 database.insert("", END, values=row)

         except Exception as ex:
             messagebox.showerror("SQL Database", f"Error Details: {str(ex)}", parent=fd1)

    def save():
         con = sqlite3.connect(database=r'fixeddeposit.db')
         cur = con.cursor()
         try:
             if (var_name.get() == "" and finalcount == 1):
                 messagebox.showerror('SQL Database', "Name Required", parent=fd1)
             elif (var_principal.get() == "" and finalcount == 1):
                 messagebox.showerror('SQL Database', "Principal Amount Required", parent=fd1)
             elif (var_operationtype.get() == "" and finalcount == 1):
                 messagebox.showerror('SQL Database', "Operation Type Required", parent=fd1)
             elif (var_period.get() == "" and finalcount == 1):
                 messagebox.showerror('SQL Database', "Period Required", parent=fd1)
             elif (var_autorenewal.get() == "" and finalcount == 1):
                 messagebox.showerror('SQL Database', "Auto Renewal Required", parent=fd1)
             elif (var_autoclosure.get() == "" and finalcount == 1):
                 messagebox.showerror('SQL Database', "Auto Closure Required", parent=fd1)
             elif (var_nomineename.get() == "" and finalcount == 1):
                 messagebox.showerror('SQL Database', "Nominee Name Required", parent=fd1)
             elif (var_bank.get() == "" and finalcount == 1):
                 messagebox.showerror('SQL Database', "Bank Name Required", parent=fd1)
             elif (var_branch.get() == "" and finalcount == 1):
                 messagebox.showerror('SQL Database', "Branch Name Required", parent=fd1)
             elif (var_dateofdeposit.get() == "" and finalcount == 1):
                 messagebox.showerror('SQL Database', "Date Of Deposit Required", parent=fd1)
             elif (var_ac.get() == "" and finalcount == 1):
                 messagebox.showerror('SQL Database', "A/C No. Required", parent=fd1)
             elif (var_cifid.get() == "" and finalcount == 1):
                 messagebox.showerror('SQL Database', "CIF ID Required", parent=fd1)
             elif (var_remark.get() == "" and finalcount == 1):
                 messagebox.showerror('SQL Database', "Remark(s) Required", parent=fd1)
             elif (finalcount >= 2):
                 messagebox.showerror('SQL Database', f"{str(finalcount_str)} Fields Required", parent=fd1)
             elif (finalcount == 0):
                 cur.execute(
                     'Insert into fixeddeposit(Name,Principal Amount,Operation Type,Period,Maturity Amount,Auto Renewal,Auto Closure,Nominee Name,Bank,Branch,Date Of Deposit,Account Number,CIF ID,Remark(s), Maturity Date) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
                     (
                         var_name.get(),
                         var_principal.get(),
                         var_operationtype.get(),
                         var_period.get(),
                         var_maturityamount.get(),
                         var_autorenewal.get(),
                         var_autoclosure.get(),
                         var_nomineename.get(),
                         var_bank.get(),
                         var_branch.get(),
                         var_dateofdeposit.get(),
                         var_ac.get(),
                         var_cifid.get(),
                         var_remark.get(),
                         var_maturitydate.get(),
                     ))
                 con.commit()
                 messagebox.showinfo('SQL Database', 'Account Details Added Successfully', parent=fd1)
                 databaseOpen()

         except Exception as ex:
             messagebox.showerror("SQL Database", f"Error Details: {str(ex)}", parent=fd1)

    def update():
         con = sqlite3.connect(database=r'fixeddeposit.db')
         cur = con.cursor()
         try:
             if (var_name.get() == "" and finalcount == 1):
                 messagebox.showerror('SQL Database', "Name Required", parent=fd1)
             elif (var_principal.get() == "" and finalcount == 1):
                 messagebox.showerror('SQL Database', "Principal Amount Required", parent=fd1)
             elif (var_operationtype.get() == "" and finalcount == 1):
                 messagebox.showerror('SQL Database', "Operation Type Required", parent=fd1)
             elif (var_period.get() == "" and finalcount == 1):
                 messagebox.showerror('SQL Database', "Period Required", parent=fd1)
             elif (var_autorenewal.get() == "" and finalcount == 1):
                 messagebox.showerror('SQL Database', "Auto Renewal Required", parent=fd1)
             elif (var_autoclosure.get() == "" and finalcount == 1):
                 messagebox.showerror('SQL Database', "Auto Closure Required", parent=fd1)
             elif (var_nomineename.get() == "" and finalcount == 1):
                 messagebox.showerror('SQL Database', "Nominee Name Required", parent=fd1)
             elif (var_bank.get() == "" and finalcount == 1):
                 messagebox.showerror('SQL Database', "Bank Name Required", parent=fd1)
             elif (var_branch.get() == "" and finalcount == 1):
                 messagebox.showerror('SQL Database', "Branch Name Required", parent=fd1)
             elif (var_dateofdeposit.get() == "" and finalcount == 1):
                 messagebox.showerror('SQL Database', "Date Of Deposit Required", parent=fd1)
             elif (var_ac.get() == "" and finalcount == 1):
                 messagebox.showerror('SQL Database', "A/C No. Required", parent=fd1)
             elif (var_cifid.get() == "" and finalcount == 1):
                 messagebox.showerror('SQL Database', "CIF ID Required", parent=fd1)
             elif (var_remark.get() == "" and finalcount == 1):
                 messagebox.showerror('SQL Database', "Remark(s) Required", parent=fd1)
             elif (finalcount >= 2):
                 messagebox.showerror('SQL Database', f"{str(finalcount_str)} Fields Required", parent=fd1)
             elif (finalcount == 0):
                 cur.execute('Select * from fixeddeposit where Name=?', (var_name.get(),))
                 row = cur.fetchone()
                 if row == None:
                     messagebox.showerror("SQL Database", "Invalid Account Number", parent=fd1)
                 else:
                     cur.execute(
                         'Update fixeddeposit set Principal Amount=?, Operation Type=?, Period=?, Maturity Amount=?, Auto Renewal=?, Auto Closure=?, Nominee Name=?, Bank=?, Branch=?, Date Of Deposit=?, Account Number=?, CIF ID=?, Remark(s)=?,  Maturity Date=? where Name=?',(
                             var_principal.get(),
                             var_operationtype.get(),
                             var_period.get(),
                             var_maturityamount.get(),
                             var_autorenewal.get(),
                             var_autoclosure.get(),
                             var_nomineename.get(),
                             var_bank.get(),
                             var_branch.get(),
                             var_dateofdeposit.get(),
                             var_ac.get(),
                             var_cifid.get(),
                             var_remark.get(),
                             var_maturitydate.get(),
                             var_name.get(),
                         ))
                     con.commit()
                     messagebox.showinfo('SQL Database', 'Account Details Updated Successfully', parent=fd1)
                     databaseOpen()

         except Exception as ex:
             messagebox.showerror("SQL Database", f"Error Details: {str(ex)}", parent=fd1)

    def delete():
         con = sqlite3.connect(database=r'fixeddeposit.db')
         cur = con.cursor()
         try:
             if (var_name.get() == "" and finalcount == 1):
                 messagebox.showerror('SQL Database', "Name Required", parent=fd1)
             elif (var_principal.get() == "" and finalcount == 1):
                 messagebox.showerror('SQL Database', "Principal Amount Required", parent=fd1)
             elif (var_operationtype.get() == "" and finalcount == 1):
                 messagebox.showerror('SQL Database', "Operation Type Required", parent=fd1)
             elif (var_period.get() == "" and finalcount == 1):
                 messagebox.showerror('SQL Database', "Period Required", parent=fd1)
             elif (var_autorenewal.get() == "" and finalcount == 1):
                 messagebox.showerror('SQL Database', "Auto Renewal Required", parent=fd1)
             elif (var_autoclosure.get() == "" and finalcount == 1):
                 messagebox.showerror('SQL Database', "Auto Closure Required", parent=fd1)
             elif (var_nomineename.get() == "" and finalcount == 1):
                 messagebox.showerror('SQL Database', "Nominee Name Required", parent=fd1)
             elif (var_bank.get() == "" and finalcount == 1):
                 messagebox.showerror('SQL Database', "Bank Name Required", parent=fd1)
             elif (var_branch.get() == "" and finalcount == 1):
                 messagebox.showerror('SQL Database', "Branch Name Required", parent=fd1)
             elif (var_dateofdeposit.get() == "" and finalcount == 1):
                 messagebox.showerror('SQL Database', "Date Of Deposit Required", parent=fd1)
             elif (var_ac.get() == "" and finalcount == 1):
                 messagebox.showerror('SQL Database', "A/C No. Required", parent=fd1)
             elif (var_cifid.get() == "" and finalcount == 1):
                 messagebox.showerror('SQL Database', "CIF ID Required", parent=fd1)
             elif (var_remark.get() == "" and finalcount == 1):
                 messagebox.showerror('SQL Database', "Remark(s) Required", parent=fd1)
             elif (finalcount >= 2):
                 messagebox.showerror('SQL Database', f"{str(finalcount_str)} Fields Required", parent=fd1)
             elif (finalcount == 0):
                 cur.execute('Select * from fixeddeposit where Name=?', (var_name.get(),))
                 row = cur.fetchone()
                 if row == None:
                     messagebox.showerror("SQL Database", "Invalid Account Number", parent=fd1)
                 else:
                     op = messagebox.askyesno('SQL Database', "Do You Want To Delete The Selected Record?",
                                              parent=fd1)
                     if op == True:
                         cur.execute('delete from fixeddeposit where Name=?', (var_name.get(),))
                         con.commit()
                         messagebox.showinfo('SQL Database', 'Account Details Deleted Successfully', parent=fd1)
                         databaseOpen()

         except Exception as ex:
             messagebox.showerror("SQL Database", f"Error Details: {str(ex)}", parent=fd1)

    #def passData()

    def clear():
        var_principal.set('')
        var_operationtype.set('')
        var_period.set('')
        var_autorenewal.set('Select')
        var_autoclosure.set('Select')
        var_nomineename.set('')
        var_bank.set('Select')
        var_branch.set('Select')
        var_dateofdeposit.set('')
        var_ac.set('')
        var_cifid.set('')
        var_remark.set('')
        var_name.set('')


    # Additional Font
    font1 = Font(family='Helvetica', size=24, underline=1)

    # Title
    title = Label(fd1, text='Fixed Deposit Details', compound=LEFT,
                  font=('courier', 40, 'bold'), bg='lightyellow', fg='black', anchor='n').place(x=2, y=10,
                                                                                                width=850,
                                                                                                height=70)
    generatesavingreportpdf=Button(fd1, text="Generate PDF", bg='red', fg='yellow',font=('courier', 20, 'bold'),
                                   bd=4, relief=RAISED, command=lambda: [fixeddeposit_pdf()], cursor='hand2').place(x=1000,
                                                                                                         y=20,
                                                                                                         width=200,
                                                                                                         height=45)

    # Underline 1
    underline = Label(fd1,
                      text='                                                                                                                                                             ',
                      font=font1, bg='lightyellow', fg='black').place(x=0, y=64, width=1400)


    # Database
    database_Frame = fr(fd1, bd=3, relief=RIDGE)
    database_Frame.place(x=-2, y=100, relwidth=1, height=300)

    # ScrollBars
    scroll_xdir = Scrollbar(database_Frame, orient=HORIZONTAL)
    scroll_ydir = Scrollbar(database_Frame, orient=VERTICAL)

    # Table Creation
    database = ttk.Treeview(database_Frame,
                            columns=(
    'Name','Principal Amount','Operation Type','Period','Maturity Amount','Auto Renewal','Auto Closure','Nominee Name','Bank','Branch','Date Of Deposit','Account Number','CIF ID','Remark(s)','Maturity Date'),
                            yscrollcommand=scroll_ydir.set, xscrollcommand=scroll_xdir.set)
    scroll_xdir.pack(side=BOTTOM, fill=X)
    scroll_ydir.pack(side=RIGHT, fill=Y)
    scroll_ydir.config(command=database.yview)
    scroll_xdir.config(command=database.xview)
    database.heading('Name', text="Name")
    database.heading('Principal Amount', text="Principal Amount")
    database.heading('Operation Type', text="Operation Type")
    database.heading('Period', text="Period")
    database.heading('Maturity Amount', text="Maturity Amount")
    database.heading('Auto Renewal', text="Auto Renewal")
    database.heading('Auto Closure', text="Auto Closure")
    database.heading('Nominee Name', text="Nominee Name")
    database.heading('Bank', text="Bank")
    database.heading('Branch', text="Branch")
    database.heading('Date Of Deposit', text="Date Of Deposit")
    database.heading('Account Number', text="Account Number")
    database.heading('CIF ID', text="CIF ID")
    database.heading('Remark(s)', text="Remark(s)")
    database.heading('Maturity Date', text="Maturity Date")



    database['show'] = 'headings'
    database.column('Name', width="100")
    database.column('Principal Amount', width="100")
    database.column('Operation Type', width="100")
    database.column('Period', width="100")
    database.column('Maturity Amount', width="100")
    database.column('Auto Renewal', width="200")
    database.column('Auto Closure', width="100")
    database.column('Nominee Name', width="150")
    database.column('Bank', width="100")
    database.column('Branch', width="100")
    database.column('Date Of Deposit', width="100")
    database.column('Account Number', width="100")
    database.column('CIF ID', width="100")
    database.column('Remark(s)', width="100")
    database.column('Maturity Date', width="100")



    database.pack(fill=BOTH, expand=1)

    databaseOpen()

    # Declaring fixeddeposit Detail Variables
    var_principal = IntVar()
    var_operationtype = StringVar()
    var_period = StringVar()
    var_autorenewal = StringVar()
    var_autoclosure = StringVar()
    var_nomineename = StringVar()
    var_bank = StringVar()
    var_branch = StringVar()
    var_dateofdeposit = StringVar()
    var_ac = StringVar()
    var_cifid = StringVar()
    var_remark = StringVar()
    var_name = StringVar()
    var_maturitydate = StringVar()
    var_maturityamount = IntVar()

    ###Buttons On The fixeddeposit A/C Page
    Save_Btn = Button(fd1, text='Save', command=lambda: [counter(), save(), clear()], cursor='hand2',
                       font=('helvetica', 30), bg='IndianRed2', fg='black', bd=4, relief=RAISED).place(x=1150, y=444,
                                                                                                       width=140,
                                                                                                       height=45)
    Update_Btn = Button(fd1, text='Update', command=lambda: [counter(), update(), clear()], cursor='hand2',
                         font=('helvetica', 30), bg='gold', fg='black', bd=4, relief=RAISED).place(x=1150, y=524,
                                                                                                   width=140,
                                                                                                   height=46)
    Delete_Btn = Button(fd1, text='Delete', command=lambda: [counter(), delete(), clear()], cursor='hand2',
                         font=('helvetica', 30), bg='OliveDrab2', fg='black', bd=4, relief=RAISED).place(x=1150,
                                                                                                         y=604,
                                                                                                         width=140,
                                                                                                         height=45)
    Clear_Btn = Button(fd1, text='Clear', command=lambda: [clear()], cursor='hand2', font=('helvetica', 30),
                        bg='DodgerBlue', fg='black', bd=4, relief=RAISED).place(x=1150, y=684, width=140, height=45)


    # Add Savings Details
    Principal_Lbl = Label(fd1, text='P. Amt.', font=('goudy old style', 15), bg='lightyellow',
                      fg='black').place(x=-20, y=434, width=250, height=60)
    Ac_Entry = Entry(fd1, textvariable=var_Ac, font=('goudy old style', 15), bd=2, relief=SUNKEN,
                        bg='white', fg='black').place(x=230, y=449, width=150, height=50)

    custID_Lbl = Label(fd1, text='Cust ID', font=('goudy old style', 30), bg='lightyellow',
                     fg='black').place(
        x=380, y=444, width=250, height=60)
    custID_Entry = Entry(fd1, textvariable=var_custID, font=('goudy old style', 15), bd=2, relief=SUNKEN,
                       bg='white', fg='black').place(x=570, y=449, width=150, height=50)

    remark_Lbl = Label(fd1, text='Remarks', font=('goudy old style', 30), bg='lightyellow',
                       fg='black').place(
        x=-20, y=544, width=250, height=60)
    remark_Entry = Entry(fd1, textvariable=var_remark, font=('goudy old style', 15), bd=2,
                         relief=SUNKEN,
                         bg='white', fg='black').place(x=230, y=549, width=150, height=50)

    bank_Lbl = Label(fd1, text='Bank ', font=('goudy old style', 30), bg='lightyellow',
                       fg='black').place(
        x=380, y=544, width=250, height=60)
    bank_Combobox = ttk.Combobox(fd1, textvariable=var_bank,
                                   values=('Select', 'ICICI', 'SBI', 'BOB', 'HDFC', 'POST OFFICE'), state='readonly',
                                   justify=CENTER,
                                   font=('verdana', 15))
    bank_Combobox.place(x=570, y=560, width=150)
    bank_Combobox.current(0)

    Name_Lbl = Label(fd1, text='Name', font=('goudy old style', 30), bg='lightyellow',
                            fg='black').place(x=-20, y=644, width=250, height=60)
    Name_Combobox = ttk.Combobox(fd1, textvariable=var_Name,
                                        values=('Select', 'Shalini', 'SL+VK', 'Vinay', 'SL+VK+SS', 'VK+SS'), state='readonly', justify=CENTER,
                                        font=('verdana', 15))
    Name_Combobox.place(x=230, y=660, width=150)
    Name_Combobox.current(0)

    card_Lbl = Label(fd1, text='Card No.', font=('goudy old style', 30), bg='lightyellow',
                       fg='black').place(
        x=380, y=644, width=250, height=60)
    card_Entry = Entry(fd1, textvariable=var_card, font=('goudy old style', 15), bd=2, relief=SUNKEN,
                       bg='white', fg='black').place(x=590, y=660, width=400)

    branch_Lbl = Label(fd1, text='Branch', font=('goudy old style', 30), bg='lightyellow',
                      fg='black').place(
        x=720, y=444, width=250, height=60)
    branch_Entry = Entry(fd1, textvariable=var_branch, font=('goudy old style', 15), bd=2, relief=SUNKEN,
                        bg='white', fg='black').place(x=940, y=449, width=150, height=50)

    opendate_Lbl = Label(fd1, text='Open Date', font=('goudy old style', 30), bg='lightyellow',
                         fg='black').place(x=720, y=544, width=250, height=60)
    opendate_Entry = Entry(fd1, textvariable=var_opendate, font=('goudy old style', 15), bd=2,
                        relief=SUNKEN, bg='white', fg='black').place(x=940, y=549, width=150, height=50)