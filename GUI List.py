from tkinter import *
import tkinter.messagebox

lroot = Tk()
lroot.title("GUI List")
lroot.geometry("1000x500+100+70")

def retrievedata_X(): #ฟังก์ชั่น โหลดข้อมูล list X ตอนเปิด
    global list_data1
    list_data1 = []
    try:
        with open("list_X.txt", "r", encoding="utf-8") as file:
            for f in file:
                list_box_1.insert(END, f.strip())
                list_data1.append(f.strip())
                print(list_data1)
    except:pass

def retrievedata_Y(): #ฟังก์ชั่น โหลดข้อมูล list Y ตอนเปิด
    global list_data2
    list_data2 = []
    try:
        with open("list_Y.txt", "r", encoding="utf-8") as file:
            for f in file:
                list_box_2.insert(END, f.strip())
                list_data2.append(f.strip())
                print(list_data2)
    except:pass

def add_showChoice(): #เลือกฟังก์ชั่น เพิ่มข้อมูล
    add_choice = add_language.get()
    if add_choice == 1 :
        tkinter.messagebox.showinfo("แจ้งเตือน","คุณเลือก เพิ่มข้อมูล list X")
        global list_data1
        if l_entry.get() == '' or l_entry.get() == '':
            tkinter.messagebox.showerror( 'Error', 'ท่านยังไม่ได้ใส่ ข้อมูลที่ต้องการเพิ่ม' )
        else:
            list_box_1.insert(END, newlist.get())
            list_data1.append(newlist.get())

    elif add_choice == 2 :
        tkinter.messagebox.showinfo("แจ้งเตือน","คุณเลือก เพิ่มเพิ่มข้อมูล list Y")
        global list_data2
        if l_entry.get() == '' or l_entry.get() == '':
            tkinter.messagebox.showerror( 'Error', 'ท่านยังไม่ได้ใส่ ข้อมูลที่ต้องการเพิ่ม' )
        else:
            list_box_2.insert(END, newlist.get())
            list_data2.append(newlist.get())
    l_entry.delete(0,END)

def modifylist_showChoice(): #เลือกฟังก์ชั่น แก้ไขข้อมูล
    modifylist_choice = modifylist_language.get()
    if modifylist_choice == 1 :
        tkinter.messagebox.showinfo("แจ้งเตือน","คุณเลือก แก้ไข list X")
        xlistm = l_entry.get()
        if l_entry.get() == '' or l_entry.get() == '':
            tkinter.messagebox.showerror( 'Error', 'ยังท่านยังไม่ได้ใส่ ข้อมูลที่ต้องการแก้ไข' )
        else:
            for i in list_box_1.curselection():
                list_box_1.delete(i)
                list_box_1.insert(i,xlistm)
                l_entry.delete(0,END)

    elif modifylist_choice == 2 :
        tkinter.messagebox.showinfo("แจ้งเตือน","คุณเลือก แก้ไข list Y")
        xlistm = l_entry.get()
        if l_entry.get() == '' or l_entry.get() == '':
            tkinter.messagebox.showerror( 'Error', 'ยังท่านยังไม่ได้ใส่ ข้อมูลที่ต้องการแก้ไข' )
        else:
            for i in list_box_2.curselection():
                list_box_2.delete(i)
                list_box_2.insert(i,xlistm)
                l_entry.delete(0,END)

def delete_showChoice(): #เลือกฟังก์ชั่น ลบข้อมูล ทั้งหมด
    global list_data1,list_data2
    delete_showChoice = delete_language.get()
    if delete_showChoice == 1 :
        tkinter.messagebox.showinfo("แจ้งเตือน","คุณเลือก ลบข้อมูลทั้งหมดใน list X")
        list_box_1.delete(0,END)
        list_data1 = []

    elif delete_showChoice == 2 :
        tkinter.messagebox.showinfo("แจ้งเตือน","คุณเลือก ลบข้อมูลทั้งหมดใน list Y")
        list_box_2.delete(0,END)
        list_data2 = []

def delete_s_showChoice(): #ฟังก์ชั่น ลบ ข้อมูลที่เลือก
    global list_data1,list_data2
    delete_S_choice = delete_s_language.get()
    if delete_S_choice == 1 :
        tkinter.messagebox.showinfo("แจ้งเตือน","คุณลบข้อมูล ที่เลือกใน list X")
        list_box_1.delete(ANCHOR)

    elif delete_S_choice == 2 :
        tkinter.messagebox.showinfo("แจ้งเตือน","คุณลบข้อมูล ที่เลือกใน list Y")
        list_box_2.delete(ANCHOR)

def search_showChoice(): #เลือกฟังก์ชั่น ค้นหาข้อมูล
    search_showChoice = search_language.get()
    if search_showChoice == 1 :
        tkinter.messagebox.showinfo("แจ้งเตือน","คุณเลือก ค้นหาข้อมูลใน list X")
        show_search1.config(text=list_box_1.get(ANCHOR))
        show_search2.config(text=list_box_1.curselection())

    elif search_showChoice == 2 :
        tkinter.messagebox.showinfo("แจ้งเตือน","คุณเลือก ค้นหาข้อมูล list Y")
        show_search1.config(text=list_box_2.get(ANCHOR))
        show_search2.config(text=list_box_2.curselection())

def showsort_M_1(): #ฟังก์ชั่น สำหรับการเรียง List X
    global list_data1
    window_1 = Tk()
    window_1.title("จัดเรียง List X")
    window_1.geometry("600x150")
    
    showsort_mix_text = Label(window_1,font=1,text="มาก -> น้อย :").place(x=15,y=35)
    showsort_mix = Label(window_1,font=1)
    showsort_mix.place(x=135,y=35)

    showsort_min_text = Label(window_1,font=1,text="น้อย -> มาก :").place(x=15,y=70)
    showsort_min = Label(window_1,font=1)
    showsort_min.place(x=135,y=70)

    mix_sort = sorted(list_data1)
    showsort_mix.config(text=mix_sort)
    min_sort = sorted(list_data1,reverse=True)
    showsort_min.config(text=min_sort)

    window_1.mainloop

def showsort_M_2(): #ฟังก์ชั่น สำหรับการเรียง List Y
    global list_data2
    window_2 = Tk()
    window_2.title("จัดเรียง List Y")
    window_2.geometry("600x150")
    
    showsort_mix_text = Label(window_2,font=1,text="มาก -> น้อย :").place(x=15,y=35)
    showsort_mix = Label(window_2,font=1)
    showsort_mix.place(x=135,y=35)

    showsort_min_text = Label(window_2,font=1,text="น้อย -> มาก :").place(x=15,y=70)
    showsort_min = Label(window_2,font=1)
    showsort_min.place(x=135,y=70)

    mix_sort = sorted(list_data2)
    showsort_mix.config(text=mix_sort)
    min_sort = sorted(list_data2,reverse=True)
    showsort_min.config(text=min_sort)

    window_2.mainloop

def sun_list(): #ฟังกัชั่น สำหรับการ รวม List
    global list_data2
    window_sum = Tk()
    window_sum.title("จัดเรียง List Y")
    window_sum.geometry("600x100")
    
    showsort_mix_text = Label(window_sum,font=1,text="List X + List Y : ").place(x=10,y=35)
    showsort_mix = Label(window_sum,font=1)
    showsort_mix.place(x=155,y=35)

    sum_sort = list_data1 + list_data2
    showsort_mix.config(text=sum_sort)

    window_sum.mainloop
    
def save_X(): #ฟังก์ชั่น บันทึก List X
    tkinter.messagebox.askquestion("ยืนยัน"," คุณต้องการ บันทึกข้อมูล List X หรือไม่ ? ")
    with open("list_X.txt", "w", encoding="utf-8") as file:
        for X in list_data1:
            file.write( X + "\n")

def save_Y(): #ฟังก์ชั่น บันทึก List Y
    tkinter.messagebox.askquestion("ยืนยัน"," คุณต้องการ บันทึกข้อมูล List Y หรือไม่ ? ")
    with open("list_Y.txt", "w", encoding="utf-8") as file:
        for Y in list_data2:
            file.write( Y + "\n")

def quit_sum(): #ฟังก์ชั่น ออกจากโปรแกรม
    comfirm = tkinter.messagebox.askquestion("ยืนยัน","คุณต้องการปิดโปรแกรม หรือไม่?")
    if comfirm == "yes" : lroot.destroy()

#สร้างหน้าต่างโปรแกรม GUI
#สร้างช่องรับข้อมูล
newlist = StringVar()
l_entry = Entry(lroot ,font=2 , textvariable=newlist)
l_entry.place(x=80,y=70)

#สร้าง The listbox เพื่อแสดงผลข้อมูล
list_box_1 = Listbox(lroot ,font=1)
list_box_1.place(x=400,y=90)
Label(lroot,font=2,text=" List X ",fg="blue").place(x=475,y=50)

list_box_2 = Listbox(lroot ,font=1)
list_box_2.place(x=690,y=90)
Label(lroot,font=2,text=" List Y ",fg="blue").place(x=760,y=50)

#ตัวเลือกโปรแกรม เพิ่มข้อมูล 
add_language = IntVar()
add_language.set(2)
Radiobutton(text="List X",font=2,variable=add_language,value=1,command=add_showChoice,background="green").place(x=130,y=110)
Radiobutton(text="List Y",font=2,variable=add_language,value=2,command=add_showChoice,background="green").place(x=220,y=110)
Label(lroot,font=4,text="   เพิ่มข้อมูลใน  :",background="green").place(x=0,y=113)

#ตัวเลือกโปรแกรม แก้ไขข้อมูล 
modifylist_language = IntVar()
modifylist_language.set(2)
Radiobutton(text="List X",font=2,variable=modifylist_language,value=1,command=modifylist_showChoice,background="red").place(x=130,y=155)
Radiobutton(text="List Y",font=2,variable=modifylist_language,value=2,command=modifylist_showChoice,background="red").place(x=220,y=155)
Label(lroot,font=4,text="  แก้ไขข้อมูลใน :",background="red").place(x=0,y=158)

#ตัวเลือกโปรแกรม ลบข้อมูล ที่เลือก
delete_s_language = IntVar()
delete_s_language.set(2)
Radiobutton(text="List X",font=2,variable=delete_s_language,value=1,command=delete_s_showChoice,background="MAGENTA").place(x=150,y=200)
Radiobutton(text="List Y",font=2,variable=delete_s_language,value=2,command=delete_s_showChoice,background="MAGENTA").place(x=240,y=200)
Label(lroot,font=4,text="ลบข้อมูลที่เลือกใน :",background="MAGENTA").place(x=0,y=203)

#ตัวเลือกโปรแกรม ลบข้อมูล ทั้งหมด
delete_language = IntVar()
delete_language.set(2)
Radiobutton(text="List X",font=2,variable=delete_language,value=1,command=delete_showChoice,background="grey").place(x=150,y=240)
Radiobutton(text="List Y",font=2,variable=delete_language,value=2,command=delete_showChoice,background="grey").place(x=240,y=240)
Label(lroot,font=4,text=" ลบข้อมูลทั้งหมด  :",background="grey").place(x=0,y=243)

#ตัวเลือกโปรแกรม ค้นหา
search_language = IntVar()
search_language.set(2)
Radiobutton(text="List X",font=2,variable=search_language,value=1,command=search_showChoice,background="blue").place(x=150,y=310)
Radiobutton(text="List Y",font=2,variable=search_language,value=2,command=search_showChoice,background="blue").place(x=240,y=310)
Label(lroot,font=4,text="ค้นหาข้อมูลใน list :",background="blue").place(x=0,y=313)

Label(lroot,font=5,text="เลือก :").place(x=90,y=360)
show_search1 = Label(lroot,font=5)
show_search1.place(x=165,y=360)
Label(lroot,font=5,text="ตำแหน่งที่ :").place(x=270,y=360)
show_search2 = Label(lroot,font=5)
show_search2.place(x=365,y=360)

#ปุ่ม จัดเรียง
Button(lroot,text="จัดเรียง List X",fg="blue",font=1,command=showsort_M_1).place(x=450,y=340)
Button(lroot,text="จัดเรียง List Y",fg="blue",font=1,command=showsort_M_2).place(x=735,y=340)

#ปุ่ม รวม list
Button(lroot, text=" รวม List ",font=1, command=sun_list,fg="blue").place(x=610,y=420)

#ปุ่ม ออกและบันทึกข้อมูล
Button(lroot, text="บันทึก List X",font=1, command=save_X).place(x=452,y=385)
Button(lroot, text="บันทึก List Y",font=1, command=save_Y).place(x=738,y=383)
Button(lroot, text="ออกจากโปรแกรม",font=1, command=quit_sum,fg="blue").place(x=125,y=420)

# โหลดข้อมูลที่บันทึกไว้ก่อนหน้านี้
retrievedata_X()
retrievedata_Y()

# ฟังก์ชันในตัวเพื่อเริ่มการวนซ้ำของ GUI
lroot.mainloop()
