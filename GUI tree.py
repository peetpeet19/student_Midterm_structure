from tkinter import *
import tkinter.messagebox
from binarytree import build, tree

treeroot = Tk()
treeroot.title("GUI Tree")
treeroot.geometry("450x550+50+30")

tree_data=[]
def addArray(): #ฟังก์ชั่น เพิ่ม Array
    global tree_data
    if t_entry.get() == '' or t_entry.get() == '':
        tkinter.messagebox.showerror( 'Error', 'ท่านยังไม่ได้ใส่ ข้อมูลที่ต้องการเพิ่ม' )
    else:
        tree_box.insert(END, tree_1.get())
        tree_data.append(tree_1.get())
        t_entry.delete(0,END)

def delete_All(): #ฟังก์ชั่นลบ ข้อมูล ทั้งหมด
        global tree_data
        tree_box.delete(0,END)
        array_data = []

def delete_selected(): #ฟังก์ชั่นลบ ข้อมูล ที่เลือก
    global tree_data
    selected = tree_box.get(tree_box.curselection())
    tree_box.delete(ANCHOR)
    tree_data.pop(tree_data.index(selected))

def showsearch(): #สร้างฟังก์ชั่น ค้นหา ตำแหน่งนั้นๆใน data
    show_search1.config(text=tree_box.get(ANCHOR))
    show_search2.config(text=tree_box.curselection())

def quit_save(): #ฟังก์ชั่นออกจากโปรแกรม
    global treeroot
    comfirm = tkinter.messagebox.askquestion("ยืนยัน","คุณต้องการปิดโปรแกรม หรือไม่ ? (ข้อมูลจะถูกเซฟ)")
    if comfirm == "yes" : treeroot.destroy()

def def_binarytree():
    global tree_data
    binary_tree_sum = build(tree_data)
    print('Binary tree from list :\n',binary_tree_sum)
    print("")
    print('\nList from binary tree :',binary_tree_sum.values)
    print("")
    # รับรายการโหนด
    print('List of nodes :', list(binary_tree_sum))
    print("")
    # เรียงลำดับโหนด ทั้ง 3 แบบ
    print('Inorder of nodes :', binary_tree_sum.inorder)
    print("")
    print('Preorder of nodes :', binary_tree_sum.preorder)
    print("")
    print('Postorder of nodes :', binary_tree_sum.postorder)
    print("")
    # ตรวจสอบ คุณสมบัติของต้นไม้
    print('Size of tree :', binary_tree_sum.size)
    print('Height of tree :', binary_tree_sum.height)
    print("")
    # ตรวจสอบ คุณสมบัติทั้งหมดพร้อมกัน
    print('Properties of tree : \n', binary_tree_sum.properties)

#สร้าง หน้าต่าง GUI
#สร้างช่องรับข้อมูล
tree_1 = IntVar()
t_entry = Entry(treeroot ,font=1 , textvariable=tree_1)
t_entry.pack(pady=20)

#The listbox
tree_box = Listbox(treeroot ,font=1)
tree_box.pack()

#ปุ่ม เพิ่มข้อมูล
Button(treeroot, text=" เพิ่มข้อมูล ",fg="green",font=1, command=addArray).place(x=340,y=30)

#ปุ่ม ลบข้อมูล ที่เลือก
Button(treeroot,text="ลบข้อมูลที่เลือก",background="grey",font=1, command=delete_selected).place(x=80,y=320)

#ปุ่ม ลบข้อมูล ทั้งหมด
Button(treeroot,text="ลบข้อมูลทั้งหมด",background="grey",font=1, command=delete_All).place(x=220,y=320)

#ปุ่ม ค้นหา
Button(treeroot,text="ค้นหา",fg="blue",font=1,command=showsearch).place(x=20,y=365)
Label(treeroot,font=2,text="เลือก :").place(x=100,y=370)
show_search1 = Label(treeroot,font=2)
show_search1.place(x=155,y=370)
Label(treeroot,font=2,text="ตำแหน่งที่ :").place(x=280,y=370)
show_search2 = Label(treeroot,font=2)
show_search2.place(x=370,y=370)

#ปุ่ม คำนวณ binarytree
Button(treeroot, text="สร้าง binarytree และ รายล่ะเอียดต่างๆ",font=1, command=def_binarytree,fg="red").place(x=70,y=420)

#ปุ่ม เพื่อออกและบันทึกข้อมูลในกล่องรายการ
Button(treeroot, text="  ออก   ",font=1, command=quit_save).place(x=160,y=480)

#เริ่มการวนซ้ำของ GUI
treeroot.mainloop()
