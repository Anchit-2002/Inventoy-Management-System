from tkinter import *
from typing_extensions import Self
from PIL import Image, ImageTk
from tkinter import ttk

class employeeClass:
    def __init__(self,root):
        self.root = root 
        self.root.geometry("1150x500+220+130")
        self.root.title("Inventory Management System")
        self.root.config(bg ="white")
        self.root.focus_force()

        # All Variables====
        self.var_Searchby=StringVar()
        self.var_searchtxt=StringVar()

        self.var_emp_id =  StringVar()
        self.var_name = StringVar()
        self.var_email =  StringVar()
        self.var_gender =  StringVar()
        self.var_dob=  StringVar()
        self.var_email =  StringVar()
        self.var_pass =  StringVar()
        self.var_utype=  StringVar()
        self.var_contact = StringVar()

    

        #===SearchFrame====
        SearchFrame= LabelFrame(self.root,text="Search Employee", font=("Helvetica", 12, "bold"),bg="white" ,bd =2)
        SearchFrame.place(x=250,y=20,width=600,height=70)

        # Drop DownList
        cmb_search = ttk.Combobox(SearchFrame,values=("Select","Email","Name","Contact") , textvariable = self.var_Searchby,font=("bold") , justify=CENTER)
        cmb_search.place(x=10,y=10,width=180,height=30)

    
         # Text Search
        text_search = Entry(SearchFrame, font=(15), bg="lightyellow", textvariable=self.var_searchtxt)
        text_search.place(x=200, y=10, width=200, height=30)

        # Search Button
        search_button = Button(SearchFrame, text="Search", font=(15), bg="lightgreen", cursor="hand2")
        search_button.place(x=440, y=9, width=150, height=30)

        # Title
        title = Label(self.root, text="Employee Details", font=("goudy old style", 15), bg="Purple", fg="White")
        title.place(x=50, y=100, width=1000)

        # Labels and Entry Fields
        lbl_empid = Label(self.root, text="Emp ID", font=("goudy old style", 15), bg="white")
        lbl_empid.place(x=50, y=150)

        lbl_gender = Label(self.root, text="Gender", font=("goudy old style", 15), bg="white")
        lbl_gender.place(x=350, y=150)


        lbl_contact = Label(self.root, text="Contact", font=("goudy old style", 15), bg="white")
        lbl_contact.place(x=750, y=150)

        # Entry Fields for Employee Details
        txt_empid = Entry(self.root, textvariable=self.var_emp_id, font=("goudy old style", 15), bg="white")
        txt_empid .place(x=150, y=150, width=180, height=30)

        txt_gender = Entry(self.root, textvariable=self.var_gender, font=("goudy old style", 15), bg="white")
        txt_gender.place(x=500, y=150, width=180, height=30)

        txt_contact= Entry(self.root, textvariable=self.var_contact, font=("goudy old style", 15), bg="white")
        txt_contact.place(x=850, y=150, width=180, height=30)

        



if __name__=="__main__":
    root = Tk()
    obj = employeeClass(root)
    root.mainloop() 