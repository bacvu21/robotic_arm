from tkinter import *
from PIL import Image,ImageTk
import tkinter as tk 


import os 


def buon_ngu():
    filename = 'robotic_vison.py'
    os.system(filename)

    
 
    
    
    
root = Tk()

root.geometry("900x500+200+50")

root.resizable(FALSE,FALSE)

title =Label(root,text ="TRƯỜNG ĐẠI HỌC SƯ PHẠM KỸ THUẬT HƯNG YÊN",font =("times new roman ",20),bg ="#0a064f",fg = "White")
title.place (x =30,y = 0, relwidth=1)

title =Label(root,text ="CHƯƠNG TRÌNH KHỞI ĐỘNG ROBOT",font =("times new roman ",15),bg ="#0a064f",fg = "yellow")
title.place (x =30,y =37, relwidth=1)

frm = Frame(root,bd = 2 ,relief=RIDGE,bg ="white")

frm.place(x = 60 ,y = 70, width =790,height=300)


load = Image.open("My project (1).jpg")
render = ImageTk.PhotoImage(load)
img = Label(frm,image = render)
img.place(x = 0,y =0)


pilImage = Image.open("logo.jfif")   
pilImage = pilImage.resize((70, 65), Image.ANTIALIAS)
logo= ImageTk.PhotoImage(pilImage) 
label1 = tk.Label(image = logo)
label1.image = logo
label1.place(x=0, y=0) 



btn = Button(root,text = "START",font =("times new roman",20),bg ="#326fa8",bd =10 ,fg ="white",command =buon_ngu)
btn.place (x = 450,y = 400)
btn = Button(root,text = "STOP",font =("times new roman",20),bg ="RED",bd =10 ,fg ="white",command =exit)
btn.place (x = 300,y = 400)
# ten0 =Label(root ,text ="SVTH:",font=("time new roman",15),fg = "#0a064f")  
# ten0.place(x =630,y =390)
# ten = Label(root ,text ="Vũ Hữu Bắc",font=("time new roman",15),fg = "#0a064f")
# ten.place(x =700,y =390)
# ten1 = Label(root ,text ="Vũ Hữu Huy",font=("time new roman",15),fg = "#0a064f") 
# ten1.place(x =700,y =420)
# ten2 = Label(root ,text ="Vũ Thạch Quang Anh",font=("time new roman",15),fg = "#0a064f")  
# ten2.place(x =700,y =450)
# ten3 = Label(root ,text ="GVHD:",font=("time new roman",15),fg = "#0a064f")  
# ten3.place(x =0,y =400)
# ten4 = Label(root ,text ="TH.S TRỊNH THANH NGA",font=("time new roman",15),bg = "Yellow",fg = "#0a064f")  
# ten4.place(x =0,y =430)

root.mainloop()
    
