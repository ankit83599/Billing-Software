from tkinter import * 
from tkinter import ttk
from PIL import Image, ImageTk  #pip install pillow
import random,os
from tkinter import messagebox
import tempfile     # print
from time import strftime


class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Billing Software")

        # ========Variables========
        self.c_name=StringVar()
        self.c_phon=StringVar()
        self.bill_no=StringVar()
        z=random.randint(1000,9999)
        self.bill_no.set(z)
        self.c_email=StringVar()
        self.search_bill=StringVar()
        self.product=StringVar()
        self.prices=IntVar()
        self.qty=IntVar()
        self.sub_total=StringVar()
        self.tax_input=StringVar()
        self.total=StringVar()
    
        
        # Product categories list
        self.Category=['Select Option','Clothing','LifeStyle','Mobiles']

        # SubCategoryClothing
        self.SubCatClothing=["Pant","T_Shirt","Shirt"]
        self.Pant=["Levis","Mufti","Spykar"]
        self.Price_levis=5000
        self.Price_mufti=6000
        self.Price_spykar=7000

        self.T_Shirt=["Polo","Roadster","Jack&Jones"]
        self.Price_polo=1500
        self.Price_Roadster=1800
        self.Price_jackjones=1700

        self.Shirt=["Peter England","Louis Phillipe","ParkAvenue"]
        self.Price_peter=2000
        self.Price_Louis=2600
        self.Price_Park=1700

        # SubCategoryLifeStyle
        self.SubCatLifeStyle=["Bath_Soap","Face_Creame","Hair_Oil"]
        self.Bath_Soap=["LifeBuy","Lux","Santoor","Pearl"]
        self.Price_life=20
        self.Price_lux=25
        self.Price_santoor=27
        self.Price_pearl=30
        
        self.Face_Creame=["Fair&Lovely","Ponds","Olay","Garnier"]
        self.Price_fair=25
        self.Price_ponds=20
        self.Price_olay=25
        self.Price_gernier=30

        self.Hair_Oil=["Parachute","Jashmin","Bajaj"]
        self.Price_parachute=25
        self.Price_jasmin=24
        self.Price_bajaj=30
        
        
        # SubCategoryMobiles
        self.SubCatMobiles=["IPhone","Sumsung","Realme","One+"]
        self.IPhone=["IPhone_X","IPhone_11","IPhone_12"]
        self.Price_IX=40000
        self.Price_I11=60000
        self.Price_I12=85000
        
        self.Sumsung=["Sumsung M16","Sumsung M12","Sumsung M21"]
        self.Price_s16=16000
        self.Price_s12=12000
        self.Price_s21=18000

        self.Realme=["Realme 12","Realme 13","RealmePro"]
        self.Price_r12=25000
        self.Price_r13=22000
        self.Price_rpro=30000

        self.OnePlus=["OnePlus1","OnePlus2","OnePlus3"]
        self.Price_one1=45000
        self.Price_one2=60000
        self.Price_one3=47000

        # # image 1
        img = Image.open("image/b1.jpg")
        img = img.resize((455, 130), Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        lbl_img=Label(self.root,image=self.photoimg)
        lbl_img.place(x=0,y=0,width=455,height=110)

        # image 2
        img_1 = Image.open("image/b2.jpg") 
        img_1 = img_1.resize((455, 110), Image.Resampling.LANCZOS)
        self.photoimg_1=ImageTk.PhotoImage(img_1)
        lbl_img_1=Label(self.root,image=self.photoimg_1)
        lbl_img_1.place(x=455 ,y=0,width=455,height=110)

        # image 3 
        img_2 = Image.open("image/b3.jpg")
        img_2 = img_2.resize((475, 110), Image.Resampling.LANCZOS)
        self.photoimg_2=ImageTk.PhotoImage(img_2) 
        lbl_img_2=Label(self.root,image=self.photoimg_2)
        lbl_img_2.place(x=910 ,y=0,width=455,height=110)
         
        lbl_title=Label(self.root,text="BILLING SOFTWARE " ,font=("times new roman",30,"bold"),bg="white",fg="red")    
        lbl_title.place(x=0,y=110,width=1366 ,height=30)

        def time():
           string = strftime("%H:%M:%S %p")
           lbl.config(text = string)
           lbl.after(1000, time)

        lbl = Label(lbl_title,font = ("times new roman",16,'bold'),background = 'white',foreground ='green')
        lbl.place(x=0,y=0,width=120,height=38)
        time()

        Main_Frame=Frame(self.root,bd=5,relief=GROOVE,bg="white")
        Main_Frame.place(x=0,y= 141,width=1366,height=620)
 
        # Customer LabelFrame
        Cust_Frame=LabelFrame(Main_Frame,text="Customer",font=("times new roman",12,"bold"),bg="white",fg="red")     
        Cust_Frame.place(x=10,y=5,width=340,height=135) 

        self.lbl_mob=Label(Cust_Frame,text="Mobile No.",font=("times new roman",10,"bold"),bg="white")
        self.lbl_mob.grid(row=0,column=0,stick=W,padx=5,pady=2)

        self.entry_mob=ttk.Entry(Cust_Frame,textvariable=self.c_phon,font=("times new roman",10,"bold"),width=24)  
        self.entry_mob.grid(row=0,column=1)

        self.lblCustName=Label(Cust_Frame,font=('arial',10,'bold'),bg="white",text="Customer Name",bd=4)
        self.lblCustName.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.txtCustName=ttk.Entry(Cust_Frame,textvariable=self.c_name,font=('arial',9,'bold'),width=24)
        self.txtCustName.grid(row=1,column=1,sticky=W,padx=5,pady=2)

        self.lblEmail=Label(Cust_Frame,font=('arial',10,'bold'),bg="white",text="Email",bd=4)
        self.lblEmail.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.txtEmail=ttk.Entry(Cust_Frame,textvariable=self.c_email,font=('arial',9,'bold'),width=24)
        self.txtEmail.grid(row=2,column=1,sticky=W,padx=5,pady=2)

        # Product LabelFrame
        Product_Frame=LabelFrame(Main_Frame,text="Product",font=("times new roman",12,"bold"),bg="white",fg="red")     
        Product_Frame.place(x=370,y=5,width=550,height=135) 
 
        # Category
        self.lblCategory=Label(Product_Frame,font=('arial',10,'bold'),bg="white",text="Select Category",bd=4)
        self.lblCategory.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.Combo_Category=ttk.Combobox(Product_Frame,value=self.Category,font=('arial',9,'bold'),width=20,state="readonly") 
        self.Combo_Category.current(0)
        self.Combo_Category.grid(row=0,column=1,sticky=W,padx=5,pady=2)
        self.Combo_Category.bind("<<ComboboxSelected>>",self.Categories)

        # SubCategory 
        self.lblSubCategory=Label(Product_Frame,font=('arial',10,'bold'),bg="white",text="Subcategory",bd=4)
        self.lblSubCategory.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.ComboSubCategory=ttk.Combobox(Product_Frame,value=[""],state="readonly",font=('arial',9,'bold'),width=20) 
        self.ComboSubCategory.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        self.ComboSubCategory.bind("<<ComboboxSelected>>",self.Product_add)

        # Product Name
        self.lblproduct=Label(Product_Frame,font=('arial',10,'bold'),bg="white",text="Product Name",bd=4)
        self.lblproduct.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.ComboProduct=ttk.Combobox(Product_Frame,textvariable=self.product,state="readonly",font=('arial',9,'bold'),width=20)
        self.ComboProduct.grid(row=2,column=1,sticky=W,padx=5,pady=2)
        self.ComboProduct.bind("<<ComboboxSelected>>",self.price)
 
        # Price
        self.lblPrice=Label(Product_Frame,font=('arial',10,'bold'),bg="white",text="Price",bd=4)
        self.lblPrice.grid(row=0,column=2,sticky=W,padx=5,pady=2)

        self.ComboPrice=ttk.Combobox(Product_Frame,textvariable=self.prices,state="readonly",font=('arial',9,'bold'),width=20)
        self.ComboPrice.grid(row=0,column=3,sticky=W,padx=5,pady=2)

        # Qty
        self.lblQty=Label(Product_Frame,font=('arial',10,'bold'),bg="white",text="Qty",bd=4)
        self.lblQty.grid(row=1,column=2,sticky=W,padx=5,pady=2)

        self.ComboQty=ttk.Entry(Product_Frame,textvariable=self.qty,font=('arial',9,'bold'),width=22 )
        self.ComboQty.grid(row=1,column=3,sticky=W,padx=5,pady=2)

        # Middle Frame
        MiddleFrame=Frame(Main_Frame,bd=10)
        MiddleFrame.place(x=10,y=145,width=910,height=340)

        # image 1
        img_11 = Image.open("image/b4.jpg")
        img_11 = img_11.resize((455, 340), Image.Resampling.LANCZOS)
        self.photoimg_11=ImageTk.PhotoImage(img_11)

        lbl_img_11=Label(MiddleFrame,image=self.photoimg_11)
        lbl_img_11.place(x=0,y=0,width=455,height=340)

        # image 2 
        img_12 = Image.open("image/b5.jpg") 
        img_12 = img_12.resize((455, 340), Image.Resampling.LANCZOS)
        self.photoimg_12=ImageTk.PhotoImage(img_12)

        lbl_img_12=Label(MiddleFrame,image=self.photoimg_12)
        lbl_img_12.place(x=457 ,y=0,width=455,height=340)

        # Search
        Search_Frame=Frame(Main_Frame,bd=2,bg="white")
        Search_Frame.place(x=940 ,y=15,width=500,height=40)

        self.lblBill=Label(Search_Frame,font=('arial',10,'bold'),fg="white",bg="red",text="Bill Number")
        self.lblBill.grid(row=0,column=0,sticky=W,padx=1)

        self.txt_Entry_Search=ttk.Entry(Search_Frame,textvariable=self.search_bill,font=('arial',10,'bold'),width=22 )
        self.txt_Entry_Search.grid(row=0,column=1,sticky=W,padx=2)

        self.BtnSearch=Button(Search_Frame,command=self.find_bill,text="Search",font=('arial',9,'bold'),bg="orangered",fg="white",width=13, cursor='hand2')
        self.BtnSearch.grid(row=0,column=2)
          
        # RightFrame Bill Aria
        RightLabelFrame=LabelFrame(Main_Frame,text="Bill Aria",font=("times new roman",12,"bold"),bg="white",fg="red")
        RightLabelFrame.place(x=930,y=45,width=400,height=385)

        scroll_y=Scrollbar(RightLabelFrame,orient=VERTICAL)
        self.textarea=Text(RightLabelFrame,yscrollcommand=scroll_y.set,bg="white",fg="blue",font=("times new roman",12,"bold"))
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1) 

        #Bill Counter Product LabelFrame
        Bottom_Frame=LabelFrame(Main_Frame,text="Bill Counter",font=("times new roman",12,"bold"),bg="white",fg="red")     
        Bottom_Frame.place(x=0,y=430,width=1350,height=118)

        self.lblSubTotal=Label(Bottom_Frame,font=('arial',10,'bold'),bg="white",text="Sub Total",bd=4)
        self.lblSubTotal.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.EntrySubTotal=ttk.Entry(Bottom_Frame,font=('arial',10,'bold'),width=22 )
        self.EntrySubTotal.grid(row=0,column=1,sticky=W,padx=5,pady=2)

        
        self.lbl_txt=Label(Bottom_Frame,font=('arial',10,'bold'),bg="white",text="Gov Tax",bd=4)
        self.lbl_txt.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.txt_tax=ttk.Entry(Bottom_Frame,font=('arial',10,'bold'),width=22 )
        self.txt_tax.grid(row=1,column=1,sticky=W,padx=5,pady=2)

        
        self.lblAmountTotal=Label(Bottom_Frame,font=('arial',10,'bold'),bg="white",text="Total",bd=4)
        self.lblAmountTotal.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.txtAmountTotal=ttk.Entry(Bottom_Frame,font=('arial',10,'bold'),width=22 )
        self.txtAmountTotal.grid(row=2,column=1,sticky=W,padx=5,pady=2)

        # Button Frame
        Btn_Frame=Frame(Bottom_Frame,bd=2,bg="white")
        Btn_Frame.place(x=320,y=0)

        self.BtnAddToCart=Button(Btn_Frame,command=self.AddItem,height=2,text="Add to Cart",font=('arial',15,'bold'),bg="orangered",fg="white",width=13, cursor='hand2')
        self.BtnAddToCart.grid(row=0,column=0)

        self.Btngenerate=Button(Btn_Frame,command=self.gen_bill,height=2,text="Generate Bill",font=('arial',15,'bold'),bg="orangered",fg="white",width=13, cursor='hand2')
        self.Btngenerate.grid(row=0,column=1) 

        self.BtnSave=Button(Btn_Frame,command=self.save_bill,height=2,text="Save Bill",font=('arial',15,'bold'),bg="orangered",fg="white",width=13, cursor='hand2')
        self.BtnSave.grid(row=0,column=2) 

        self.BtnPrint=Button(Btn_Frame,command=self.iprint,height=2,text="Print",font=('arial',15,'bold'),bg="orangered",fg="white",width=13, cursor='hand2')
        self.BtnPrint.grid(row=0,column=3)

        self.BtnClear=Button(Btn_Frame,command=self.clear,height=2,text="Clear",font=('arial',15,'bold'),bg="orangered",fg="white",width=13, cursor='hand2')
        self.BtnClear.grid(row=0,column=4)

        self.BtnExit=Button(Btn_Frame,command=self.root.destroy,height=2,text="Exit",font=('arial',15,'bold'),bg="orangered",fg="white",width=13, cursor='hand2')
        self.BtnExit.grid(row=0,column=5)
        self.welcome()

        self.l=[] 

    # Funtion declaration=====

    def welcome(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END,"\t Welcome Shopping Mall")
        self.textarea.insert(END,f"\n Bill Number:{self.bill_no.get()}")
        self.textarea.insert(END,f"\n Customer Name:{self.c_name.get()}")
        self.textarea.insert(END,f"\n Phone Number:{self.c_phon.get()}")
        self.textarea.insert(END,f"\n Customer Email:{self.c_email.get()}")

        self.textarea.insert(END,"\n=========================================")
        self.textarea.insert(END,f"\n Product\t\tQTY\t\tPrice")
        self.textarea.insert(END,"\n=========================================\n")

    def AddItem(self):
        Tax=1
        self.n=self.prices.get()
        self.m=self.qty.get()*self.n
        self.l.append(self.m)
        if self.product.get()=="":
            messagebox.showerror("Error","Please Select The Product Name")
        else:
            self.textarea.insert(END,f"\n {self.product.get()}\t\t{self.qty.get()}\t\t{self.m}")
            self.sub_total.set(str('Rs.%.2f'%(sum(self.l))))
            self.tax_input.set(str('Rs.%.2f'%((((sum(self.l))-(self.prices.get()))*Tax)/100)))
            self.total.set(str('Rs.%.2f'%(((sum(self.l))+((((sum(self.l))-(self.prices.get()))*Tax)/100)))))

    def gen_bill(self):
        if self.product.get()=="":
            messagebox.showerror("Error","Please Add To Cart Product")
        else:
            text=self.textarea.get(10.0,(10.0+float(len(self.l))))
            self.welcome()
            self.textarea.insert(END,text)
            self.textarea.insert(END,"\n========================================")
            self.textarea.insert(END,f"\n Sub Amount:\t\t\t{self.sub_total.get()}")
            self.textarea.insert(END,f"\n Tax Amount:\t\t\t{self.tax_input.get()}")
            self.textarea.insert(END,f"\n Total Amount:\t\t\t{self.total.get()}")
            self.textarea.insert(END,"\n========================================")

    def save_bill(self): 
        op=messagebox.askyesno("Save Bill","Do You Want To Save The Bill")
        if op>0:
            self.bill_data=self.textarea.get(1.0,END)
            f1=open('bills/'+str(self.bill_no.get())+".txt",'w')
            f1.write(self.bill_data)
            op=messagebox.showinfo("Saved",f"Bill No:{self.bill_no.get()}saved successfully")
            f1.close()

    def iprint(self):
        q=self.textarea.get(1.0,"end-1c")
        filename=tempfile.mktemp('.txt')
        open(filename,'w').write(q)
        os.startfile(filename,"print")

    def find_bill(self):
        found="no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f'bills/{i}','r')
                self.textarea.delete(1.0,END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                found="yes"
        if found=="no":
             messagebox.showerror("Error","Invalid Bill No.")

    def clear(self):
        self.textarea.delete(1.0,END)
        self.c_name.set("")
        self.c_phon.set("")
        self.c_email.set("")
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill.set("")
        self.product.set("")
        self.prices.set("")
        self.qty.set(0)
        self.l=[0]
        self.total.set("")
        self.sub_total.set("")
        self.tax_input.set('')
        self.welacome()

    def Categories(self,event=""):
        if self.Combo_Category.get()=="Clothing":
            self.ComboSubCategory.config(value=self.SubCatClothing)
            self.ComboSubCategory.current(0)

        if self.Combo_Category.get()=="LifeStyle":
            self.ComboSubCategory.config(value=self.SubCatLifeStyle)
            self.ComboSubCategory.current(0)

        if self.Combo_Category.get()=="Mobiles":
            self.ComboSubCategory.config(value=self.SubCatMobiles)
            self.ComboSubCategory.current(0)

    def Product_add(self,event=""):
        if self.ComboSubCategory.get()=="Pant":
            self.ComboProduct.config(value=self.Pant)
            self.ComboProduct.current(0)


        if self.ComboSubCategory.get()=="T_Shirt": 
            self.ComboProduct.config(value=self.T_Shirt)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="Shirt":
            self.ComboProduct.config(value=self.Shirt)
            self.ComboProduct.current(0)

        # LifeStyle
        if self.ComboSubCategory.get()=="Bath_Soap":
            self.ComboProduct.config(value=self.Bath_Soap)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="Face_Creame":
            self.ComboProduct.config(value=self.Face_Creame)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="Hair_Oil":
            self.ComboProduct.config(value=self.Hair_Oil)
            self.ComboProduct.current(0)

        # Mobiles
        if self.ComboSubCategory.get()=="IPhone":
            self.ComboProduct.config(value=self.IPhone)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="Sumsung":
            self.ComboProduct.config(value=self.Sumsung)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="Realme":
            self.ComboProduct.config(value=self.Realme)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="One+":
            self.ComboProduct.config(value=self.OnePlus)
            self.ComboProduct.current(0)
    def price(self,event=""):       
        # pant
        if self.ComboProduct.get()=="Levis":
            self.ComboPrice.config(value=self.Price_levis)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Mufti":
            self.ComboPrice.config(value=self.Price_mufti)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Spykar":
            self.ComboPrice.config(value=self.Price_spykar)
            self.ComboPrice.current(0)
            self.qty.set(1)

        # T_shirt
        if self.ComboProduct.get()=="Polo":
            self.ComboPrice.config(value=self.Price_polo)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Roadster":
            self.ComboPrice.config(value=self.Price_Roadster)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Jack&Jones":
            self.ComboPrice.config(value=self.Price_jackjones)
            self.ComboPrice.current(0)
            self.qty.set(1)

        # Shirt
        if self.ComboProduct.get()=="Peter England":
            self.ComboPrice.config(value=self.Price_peter)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Louis Phillipe":
            self.ComboPrice.config(value=self.Price_Louis)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="ParkAvenue":
            self.ComboPrice.config(value=self.Price_Park)
            self.ComboPrice.current(0)
            self.qty.set(1)

        # Bath_soap
        if self.ComboProduct.get()=="LifeBuy":
            self.ComboPrice.config(value=self.Price_life)
            self.ComboPrice.current(0)
            self.qty.set(1)

        
        if self.ComboProduct.get()=="Lux":
            self.ComboPrice.config(value=self.Price_lux)
            self.ComboPrice.current(0)
            self.qty.set(1)

        
        if self.ComboProduct.get()=="Santoor":
            self.ComboPrice.config(value=self.Price_santoor)
            self.ComboPrice.current(0)
            self.qty.set(1)

        
        if self.ComboProduct.get()=="Pearl":
            self.ComboPrice.config(value=self.Price_pearl)
            self.ComboPrice.current(0)
            self.qty.set(1)

        # Face Creame
        if self.ComboProduct.get()=="Fair&Lovely":
            self.ComboPrice.config(value=self.Price_fair)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Ponds":
            self.ComboPrice.config(value=self.Price_ponds)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Olay":
            self.ComboPrice.config(value=self.Price_olay)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Garnier":
            self.ComboPrice.config(value=self.Price_gernier)
            self.ComboPrice.current(0)
            self.qty.set(1)

        # Hair oil
        if self.ComboProduct.get()=="Parachute":
            self.ComboPrice.config(value=self.Price_parachute)
            self.ComboPrice.current(0)
            self.qty.set(1)
        
        if self.ComboProduct.get()=="Jashmin":
            self.ComboPrice.config(value=self.Price_jasmin)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Bajaj":
            self.ComboPrice.config(value=self.Price_bajaj)
            self.ComboPrice.current(0)
            self.qty.set(1)

        # Iphone
        if self.ComboProduct.get()=="IPhone_X":
            self.ComboPrice.config(value=self.Price_IX)
            self.ComboPrice.current(0)
            self.qty.set(1)
        
        if self.ComboProduct.get()=="IPhone_11":
            self.ComboPrice.config(value=self.Price_I11)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="IPhone_12":
            self.ComboPrice.config(value=self.Price_I12)
            self.ComboPrice.current(0)
            self.qty.set(1)

        # Sumsung
        if self.ComboProduct.get()=="Sumsung M16":
            self.ComboPrice.config(value=self.Price_s16)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Sumsung M12":
            self.ComboPrice.config(value=self.Price_s12)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Sumsung M21":
            self.ComboPrice.config(value=self.Price_s21)
            self.ComboPrice.current(0)
            self.qty.set(1)

           

        # Realme
        if self.ComboProduct.get()=="Realme 12":
            self.ComboPrice.config(value=self.Price_r12)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Realme 13":
            self.ComboPrice.config(value=self.Price_r13)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="RealmePro":
            self.ComboPrice.config(value=self.Price_rpro)
            self.ComboPrice.current(0)
            self.qty.set(1)

        # One+
        if self.ComboProduct.get()=="OnePlus1":
            self.ComboPrice.config(value=self.Price_one1)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="OnePlus2":
            self.ComboPrice.config(value=self.Price_one2)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="OnePlus3":
            self.ComboPrice.config(value=self.Price_one3)
            self.ComboPrice.current(0)
            self.qty.set(1)
 
if __name__ =='__main__': 
    root=Tk()
    obj=Bill_App(root) 
    root.mainloop()