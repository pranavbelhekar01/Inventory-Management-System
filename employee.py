import mysql.connector
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
class employeeclass:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1070x500+200+130')
        self.root.title('Inventory Management System | Developed By Rangesh')
        self.root.config(bg='sandy brown')
        self.root.focus_force()


        #==================================
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()

        self.var_emp_id = StringVar()
        self.var_gender= StringVar()
        self.var_contact = StringVar()
        self.var_name = StringVar()
        self.var_dob = StringVar()
        self.var_doj = StringVar()
        self.var_email = StringVar()
        self.var_pass = StringVar()
        self.var_utype = StringVar()
        self.var_salary = StringVar()
        self.var_address = StringVar()



        # ==========Search Frame============
        SearchFrame = LabelFrame(self.root, text='Search Employee', bg='#FFF6BD', font=('goudy old style',12,'bold'), bd=2, relief=RIDGE)
        SearchFrame.place(x = 230, y = 20, width = 600, height=70)

        # ==========Options==================
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby, values=('Select', 'Email','Name','Contact'), state='readonly',justify=CENTER, font=('goudy old style', 12))
        cmb_search.place(x=10, y=10, width=180)
        cmb_search.current(0) # to display select word by default as selected value
        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt, font=('goudy old style', 12), bg='#CEEDC7').place(x=200, y=10, width=200)
        btn_search=Button(SearchFrame, text='Search', command= self.search, font=('goudy old style', 12), bg='#3A4F7A', fg= 'white', cursor='hand2').place(x=410, y=6, width=150, height=30)
        

        #============= title =============
        title = Label(self.root, text='Details', font=('groudy old style', 12), bg='#82AAE3', fg= 'black').place(x=50, y=100, width=1000)

        #=============content=============

        #======row1==========
        lbl_empid = Label(self.root, text='Emp ID', font=('groudy old style', 12), bg='sandy brown', fg= 'black').place(x=50, y=150)
        lbl_gender = Label(self.root, text='Gender', font=('groudy old style', 12), bg='sandy brown', fg= 'black').place(x=400, y=150)
        lbl_contact = Label(self.root, text='Contact', font=('groudy old style', 12), bg='sandy brown', fg= 'black').place(x=750, y=150)

        txt_empid = Entry(self.root, textvariable=self.var_emp_id, font=('groudy old style', 12), bg='#CEEDC7', fg= 'black').place(x=150, y=150, width=180)
        #txt_gender = Entry(self.root, textvariable=self.var_gender, font=('groudy old style', 12), bg='sandy brown', fg= 'white').place(x=400, y=150, width=180)
        cmb_gender=ttk.Combobox(self.root,textvariable=self.var_gender, values=('Select', 'Male','Female','other'), state='readonly',justify=CENTER, font=('goudy old style', 12), background='#CEEDC7')
        cmb_gender.place(x=500, y=150, width=180)
        cmb_gender.current(0) # to display select word by default as selected value
        txt_contact = Entry(self.root, textvariable=self.var_contact, font=('groudy old style', 12), bg='#CEEDC7', fg= 'black').place(x=850, y=150, width=180)


        #========row2=========
        lbl_name = Label(self.root, text='Name', font=('groudy old style', 12), bg='sandy brown', fg= 'black').place(x=50, y=190)
        lbl_dob = Label(self.root, text='D.O.B', font=('groudy old style', 12), bg='sandy brown', fg= 'black').place(x=400, y=190)
        lbl_doj = Label(self.root, text='D.O.J', font=('groudy old style', 12), bg='sandy brown', fg= 'black').place(x=750, y=190)

        txt_name = Entry(self.root, textvariable=self.var_name, font=('groudy old style', 12), bg='#CEEDC7', fg= 'black').place(x=150, y=190, width=180)
        txt_dob = Entry(self.root, textvariable=self.var_dob, font=('groudy old style', 12), bg='#CEEDC7', fg= 'black').place(x=500, y=190, width=180)
        txt_doj = Entry(self.root, textvariable=self.var_doj, font=('groudy old style', 12), bg='#CEEDC7', fg= 'black').place(x=850, y=190, width=180)

        #=========row3========
        lbl_email = Label(self.root, text='Email', font=('groudy old style', 12), bg='sandy brown', fg= 'black').place(x=50, y=230)
        lbl_pass = Label(self.root, text='Password', font=('groudy old style', 12), bg='sandy brown', fg= 'black').place(x=400, y=230)
        lbl_utype = Label(self.root, text='User type', font=('groudy old style', 12), bg='sandy brown', fg= 'black').place(x=750, y=230)

        txt_email = Entry(self.root, textvariable=self.var_email, font=('groudy old style', 12), bg='#CEEDC7', fg= 'black').place(x=150, y=230, width=180)
        txt_pass = Entry(self.root, textvariable=self.var_pass, font=('groudy old style', 12), bg='#CEEDC7', fg= 'black').place(x=500, y=230, width=180)
        #txt_utype = Entry(self.root, textvariable=self.var_utype, font=('groudy old style', 12), bg='#CEEDC7', fg= 'black').place(x=850, y=230, width=180)
        cmb_utype=ttk.Combobox(self.root,textvariable=self.var_utype, values=('Admin','Employee'), state='readonly',justify=CENTER, font=('goudy old style', 12), background='#CEEDC7')
        cmb_utype.place(x=850, y=230, width=180)
        cmb_utype.current(0)

        #==========row4============
        lbl_address = Label(self.root, text='Address', font=('groudy old style', 12), bg='sandy brown', fg= 'black').place(x=50, y=270)
        lbl_salary = Label(self.root, text='Salary', font=('groudy old style', 12), bg='sandy brown', fg= 'black').place(x=600, y=270)

        self.txt_address = Entry(self.root, textvariable=self.var_address, font=('groudy old style', 12), bg='#CEEDC7', fg= 'black')
        self.txt_address.place(x=150, y=270, width=300, height=60)
        txt_salary = Entry(self.root, textvariable=self.var_salary, font=('groudy old style', 12), bg='#CEEDC7', fg= 'black').place(x=700, y=270, width=180)


        #=======buttons=======
        btn_add=Button(self.root, text='Save', command=self.add, font=('goudy old style', 12), bg='#227C70', fg= 'white', cursor='hand2').place(x=500, y=300, width=100, height=30)
        btn_update=Button(self.root, text='Update', command=self.update, font=('goudy old style', 12), bg='#82C3EC', fg= 'white', cursor='hand2').place(x=610, y=300, width=100, height=30)
        btn_delete=Button(self.root, text='Delete',command=self.delete, font=('goudy old style', 12), bg='#DC0000', fg= 'white', cursor='hand2').place(x=720, y=300, width=100, height=30)
        btn_clear=Button(self.root, text='Clear', command=self.clear, font=('goudy old style', 12), bg='#1A120B', fg= 'white', cursor='hand2').place(x=830, y=300, width=100, height=30)
       
        #====================Employee Details==============
        emp_frame=Frame(self.root, bd=3, relief=RIDGE)
        emp_frame.place(x=0,y=350,relwidth=1, height=150)
        
        scrolly = Scrollbar(emp_frame,orient=VERTICAL)
        scrollx = Scrollbar(emp_frame,orient=HORIZONTAL)

        self.EmployeeTable=ttk.Treeview(emp_frame, columns= ('eid','name','email','gender', 'contact','dob', 'doj', 'pass','utype','address', 'salary'), yscrollcommand=scrolly.set, xscrollcommand=scrolly.set) ## Import for database
        scrollx.pack(side=BOTTOM, fill= X)
        scrolly.pack(side=LEFT, fill=Y)
        scrollx.config(command=self.EmployeeTable.xview)
        scrolly.config(command=self.EmployeeTable.yview)
        self.EmployeeTable.heading('eid', text='Employe ID')
        self.EmployeeTable.heading('name', text='Name')
        self.EmployeeTable.heading('email', text='Email')
        self.EmployeeTable.heading('gender', text='Gender')
        self.EmployeeTable.heading('contact', text='Contact')
        self.EmployeeTable.heading('dob', text='Date of Birth')
        self.EmployeeTable.heading('doj', text='Date of Joining')
        self.EmployeeTable.heading('pass', text='Password')
        self.EmployeeTable.heading('utype', text='User Type')
        self.EmployeeTable.heading('address', text='Adress')
        self.EmployeeTable.heading('salary', text='Salary')
        self.EmployeeTable['show'] = 'headings'

        self.EmployeeTable.column('eid', width=90)
        self.EmployeeTable.column('name', width=100)
        self.EmployeeTable.column('email', width=100)
        self.EmployeeTable.column('gender', width=100)
        self.EmployeeTable.column('contact', width=100)
        self.EmployeeTable.column('dob', width=100)
        self.EmployeeTable.column('doj', width=100)
        self.EmployeeTable.column('pass', width=100)
        self.EmployeeTable.column('utype', width=100)
        self.EmployeeTable.column('address', width=100)
        self.EmployeeTable.column('salary', width=100)
        self.EmployeeTable.pack(fill=BOTH,expand=1)
        self.EmployeeTable.bind('<ButtonRelease-1>', self.get_data)

        self.show()

#======================================================================================================
    def add(self):
        con=mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '1234',
        database = 'IMS'
        )
        cur = con.cursor()

        try:
            if self.var_emp_id.get()=='':
                messagebox.showerror('Error', 'Employee ID must be required', parent=self.root)
            else:
                cur.execute('select * from employee where eid =%s ', (self.var_emp_id.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror('Error', 'This Employee ID already assigned, try Different ID')
                
                else:
                    cur.execute('insert into employee(eid,name,email,gender, contact,dob, doj, pass,utype,address, salary) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', \
                        (self.var_emp_id.get(),
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_contact.get(),
                        self.var_dob.get(),
                        self.var_doj.get(),
                        self.var_pass.get(),
                        self.var_utype.get(),
                        self.txt_address.get(),
                        self.var_salary.get()
                    ))
                    con.commit()
                    messagebox.showinfo('Success', 'Employee added Successfully', parent=self.root)
                    self.show()
    
        except Exception as ex: 
            messagebox.showerror('Error', f'Error due to : {str(ex)}')


    def show(self):
        con=mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '1234',
        database = 'IMS'
        )
        cur = con.cursor()

        try:
            cur.execute('select * from employee')
            rows = cur.fetchall()
            self.EmployeeTable.delete(*self.EmployeeTable.get_children())
            for row in rows:
                self.EmployeeTable.insert('',END, values=row)

        except Exception as ex: 
            messagebox.showerror('Error', f'Error due to : {str(ex)}')


    def get_data(self,ev):
        f=self.EmployeeTable.focus()
        content= (self.EmployeeTable.item(f))
        row = content['values']
        self.var_emp_id.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_contact.set(row[4])
        self.var_dob.set(row[5])
        self.var_doj.set(row[6])
        self.var_pass.set(row[7])
        self.var_utype.set(row[8])
        self.txt_address.delete(END)
        self.txt_address.insert(END,row[9])
        self.var_salary.set(row[10])

    def update(self):
        con=mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '1234',
        database = 'IMS'
        )
        cur = con.cursor()

        try:
            if self.var_emp_id.get()=='':
                messagebox.showerror('Error', 'Employee ID must be required', parent=self.root)
            else:
                cur.execute('select * from employee where eid =%s ', (self.var_emp_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror('Error', 'Invalid Employee ID')
                
                else:
                    cur.execute('update employee set name=%s,email=%s,gender=%s, contact=%s,dob=%s, doj=%s, pass=%s,utype=%s,address=%s, salary=%s where eid=%s', (
                        
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_contact.get(),
                        self.var_dob.get(),
                        self.var_doj.get(),
                        self.var_pass.get(),
                        self.var_utype.get(),
                        self.txt_address.get(),
                        self.var_salary.get(),
                        self.var_emp_id.get()
                    ))
                    con.commit()
                    messagebox.showinfo('Success', 'Employee Updated Successfully', parent=self.root)
                    self.show()
    
        except Exception as ex: 
            messagebox.showerror('Error', f'Error due to : {str(ex)}')
    

    def delete(self):
        con=mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '1234',
        database = 'IMS'
        )
        cur = con.cursor()

        try:
            if self.var_emp_id.get()=='':
                messagebox.showerror('Error', 'Employee ID must be required', parent=self.root)
            else:
                cur.execute('select * from employee where eid =%s ', (self.var_emp_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror('Error', 'Invalid Employee ID')
                else:
                    op = messagebox.askyesno('Confirm', 'Do you really want to delete?', parent=self.root)
                    if op==True:
                        cur.execute('delete from employee where eid=%s', (self.var_emp_id.get(),))
                        con.commit()
                        messagebox.showinfo('Delete', 'Employee Details Deleted Successfully', parent=self.root)
                        self.clear()

        except Exception as ex: 
            messagebox.showerror('Error', f'Error due to : {str(ex)}')



    def clear(self):
        
        self.var_emp_id.set('')
        self.var_name.set('')
        self.var_email.set('')
        self.var_gender.set('Select')
        self.var_contact.set('')
        self.var_dob.set('')
        self.var_doj.set('')
        self.var_pass.set('')
        self.var_utype.set('Admin')
        self.txt_address.delete(END)
        self.txt_address.insert(END,'')
        self.var_salary.set('')
        self.var_searchtxt.set('')
        self.var_searchby.set('Select')
        self.show()

    def search(self):
        con=mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '1234',
        database = 'IMS'
        )
        cur = con.cursor()

        try:
            if self.var_searchby.get() == 'Select':
                messagebox.showerror('Error', 'Select By option', parent=self.root)
            elif self.var_searchtxt.get() =='':
                messagebox.showerror('Error', 'Search input is required', parent=self.root)
            else:
                cur.execute('select * from employee where ' + self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows = cur.fetchall()
                if len(rows)!=0:
                    self.EmployeeTable.delete(*self.EmployeeTable.get_children())
                    for row in rows:
                        self.EmployeeTable.insert('',END, values=row)
                else:
                    messagebox.showerror('Error', 'No Record Found', parent=self.root)

        except Exception as ex: 
            messagebox.showerror('Error', f'Error due to : {str(ex)}')





if __name__ == '__main__':
    root = Tk()
    obj=employeeclass(root)
    root.mainloop()