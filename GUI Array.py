from tkinter import *
import tkinter.messagebox

aroot = Tk()
aroot.title("GUI Array")
aroot.geometry("450x500+50+30")
aroot.maxsize(450,500)

def retrievedata(): #โหลดข้อมูลตอนเปิด
    global array_data
    array_data = []
    try:
        with open("save.txt", "r", encoding="utf-8") as file:
            for f in file:
                array_box.insert(END, f.strip())
                array_data.append(f.strip())
                print(array_data)
    except:pass

def addArray(): #ฟังก์ชั่น เพิ่ม Array
    global array_data
    if a_entry.get() == '' or a_entry.get() == '':
        tkinter.messagebox.showerror( 'Error', 'ท่านยังไม่ได้ใส่ ข้อมูลที่ต้องการเพิ่ม' )
    else:
        array_box.insert(END, array.get())
        array_data.append(array.get())
        a_entry.delete(0,END)

def modifylist(): #ฟังก์ชั่น แก้ไข ข้อมูล
    xam = a_entry.get()
    if a_entry.get() == '' or a_entry.get() == '':
        tkinter.messagebox.showerror( 'Error', 'ท่านยังไม่ได้ใส่ข้อมูล ที่ต้องการแก้ไข' )
    else:
        for i in array_box.curselection():
            array_box.delete(i)
            array_box.insert(i,xam)
        a_entry.delete(0,END)

def delete_All(): #ฟังก์ชั่นลบ ข้อมูล ทั้งหมด
        global array_data
        array_box.delete(0,END)
        array_data = []

def delete_selected(): #ฟังก์ชั่นลบ ข้อมูล ที่เลือก
    global array_data
    selected = array_box.get(array_box.curselection())
    array_box.delete(ANCHOR)
    array_data.pop(array_data.index(selected))

def showsearch(): #สร้างฟังก์ชั่น ค้นหา ตำแหน่งของ array นั้นๆใน data
    show_search1.config(text=array_box.get(ANCHOR))
    show_search2.config(text=array_box.curselection())

def quit_save(): #ดำเนินการเมื่อคุณคลิกปุ่มออกและบันทึก
    global aroot
    comfirm = tkinter.messagebox.askquestion("ยืนยัน","คุณต้องการปิดโปรแกรม หรือไม่ ? (ข้อมูลจะถูกเซฟ)")
    with open("save.txt", "w", encoding="utf-8") as file:
        for d in array_data:
            file.write( d + "\n")
    if comfirm == "yes" : aroot.destroy()

#สร้าง หน้าต่าง GUI
#สร้างช่องรับข้อมูล
array = StringVar()
a_entry = Entry(aroot ,font=1 , textvariable=array)
a_entry.pack(pady=20)

#The listbox
array_box = Listbox(aroot ,font=1)
array_box.pack()

#ปุ่ม เพิ่มข้อมูล
button_add = Button(aroot, text=" เพิ่มข้อมูล ",fg="green",font=1, command=addArray).place(x=340,y=30)

#ปุ่ม แก้ไข
button_modi = Button(aroot,text='แก้ไขข้อมูล',fg ="red",font=1,command=modifylist).place(x=340,y=80)

#ปุ่ม ลบข้อมูล ที่เลือก
button_delete_selected = Button(aroot,text="ลบข้อมูลที่เลือก",background="grey",font=1, command=delete_selected).place(x=80,y=320)

#ปุ่ม ลบข้อมูล ทั้งหมด
button_delete = Button(aroot,text="ลบข้อมูลทั้งหมด",background="grey",font=1, command=delete_All).place(x=220,y=320)

#ปุ่ม ค้นหา
button_search = Button(aroot,text="ค้นหา",fg="blue",font=1,command=showsearch).place(x=20,y=375)
Label(aroot,font=2,text="เลือก :").place(x=100,y=380)
show_search1 = Label(aroot,font=2)
show_search1.place(x=155,y=380)
Label(aroot,font=2,text="ตำแหน่งที่ :").place(x=280,y=380)
show_search2 = Label(aroot,font=2)
show_search2.place(x=370,y=380)

#ปุ่ม เพื่อออกและบันทึกข้อมูลในกล่องรายการ
bquit = Button(aroot, text="ออก และ บันทึก",font=1, command=quit_save).place(x=165,y=450)

# โหลดข้อมูลที่บันทึกไว้ก่อนหน้านี้
retrievedata()

#เริ่มการวนซ้ำของ GUI
aroot.mainloop()
