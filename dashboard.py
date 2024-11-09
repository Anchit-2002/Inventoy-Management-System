from cProfile import label
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
class IMS:
    def __init__(self,root):
        self.root = root 
        self.root.geometry("1350x700")
        self.root.title("Inventory Management System")

        
        # resize image
        image = Image.open("logo.png")
        resized_image = image.resize((50, 50)) 
        self.icon_title = ImageTk.PhotoImage(resized_image)


        # Title
        title = Label(self.root, text="Inventory Management System", font=("Helvetica", 24, "bold"), image = self.icon_title , compound = LEFT, anchor = "w", padx =20,fg="white", bg="Dark Green")
        title.place(x=0, y=0, relwidth=1, height=90)

        #button
        logout = Button(self.root  ,text ="Logout" ,font = ("Helvetica",15 ,"bold") ,bg="Red" ,fg= "white",cursor="hand2").place(x =1150,y=25)

        
         # Clock
        self.clock_label = Label(self.root, font=("Helvetica", 15, "bold"), fg="white", bg="Dark blue")
        self.clock_label.place(x=880, y=29)
        self.update_clock()

    
        #left menu
        self.menulogo =Image.open("Menu.png")
        self.menulogo = self.menulogo.resize((200,200))
        self.menulogo = ImageTk.PhotoImage(self.menulogo)

        LeftMenu = Frame(self.root,bd =2,relief =RIDGE)
        LeftMenu.place(x=0,y=102,width=200,height=550)

        # menulogo 
        label_menulogo =Label(LeftMenu,image =self.menulogo)
        label_menulogo.pack(side =TOP ,fill =X)

        
        #Buttons
        btn_employee= Button(LeftMenu, text="Employee",image =self.icon_title,command =self.employee,compound =LEFT).pack(side =TOP,fill= X)
        btn_supplier= Button(LeftMenu, text="Supplier",image =self.icon_title,compound =LEFT).pack(side =TOP,fill= X)
        btn_category= Button(LeftMenu, text="Category",image =self.icon_title,compound =LEFT).pack(side =TOP,fill= X)
        btn_products= Button(LeftMenu, text="Products",image =self.icon_title,compound =LEFT).pack(side =TOP,fill= X)
        btn_sales= Button(LeftMenu, text="Sales",image =self.icon_title,compound =LEFT).pack(side =TOP,fill= X)
        btn_exit= Button(LeftMenu, text="Exit",image =self.icon_title,compound =LEFT).pack(side =TOP,fill=X)

        # content
        self.lbl_employee = Label(self.root,text ="Total Employee\n[0]",bd =5,relief=RIDGE,bg ="pink",fg="black")
        self.lbl_employee.place(x=300,y=120,height= 150,width=200)
        # content
        self.lbl_supplier = Label(self.root,text ="Total Supplier\n[0]",bd =5,relief=RIDGE,bg ="pink",fg="black")
        self.lbl_supplier.place(x=650,y=120,height= 150,width=200)
        # content
        self.lbl_category= Label(self.root,text ="Total Category\n[0]",bd =5,relief=RIDGE,bg ="pink",fg="black")
        self.lbl_category.place(x=1000,y=120,height= 150,width=200)
        # content
        self.lbl_products = Label(self.root,text ="Total Products\n[0]",bd =5,relief=RIDGE,bg ="pink",fg="black")
        self.lbl_products.place(x=300,y=300,height= 150,width=200)
        # content
        self.lbl_sales= Label(self.root,text ="Total Sales\n[0]",bd =5,relief=RIDGE,bg ="pink",fg="black")
        self.lbl_sales.place(x=650,y=300,height= 150,width=200)
        # content
        self.lbl_exit = Label(self.root,text ="Total Exit\n[0]",bd =5,relief=RIDGE,bg ="pink",fg="black")
        self.lbl_exit.place(x=650,y=120,height= 150,width=200)

        #Footer
        lbl_footer = Label(self.root ,text ="Inventory Mangement System | Developed By WebCode \n For any Technical Issue Contact",bg="Purple",fg ="Black").pack(side = BOTTOM,fill =X)

        # Clock
        self.clock_label = Label(self.root,font=("Helvetica", 15, "bold"), fg="white", bg="Dark blue")
        self.clock_label.place(x=880, y=29)
        self.update_clock()


    def update_clock(self):
            current_time = time.strftime("%H:%M:%S %p")
            self.clock_label.config(text=current_time)
            self.root.after(1000, self.update_clock)  # Update the clock every second

    def employee(self):
        self.new_win  =  Toplevel(self.root) # for child window
        self.new_obj = employeeClass(self.new_win)

        

if __name__=="__main__":
    root = Tk()
    obj = IMS(root)
    root.mainloop() 