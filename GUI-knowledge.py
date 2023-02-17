from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox


GUI = Tk() # หน้าจอหลักโปรแกรม
GUI.title('โปรแกรมบันทึกข้อมูล') # ชื่้อโปรแกรม
GUI.geometry('500x400') #ขนาดโปรแกรม

L1 = Label(GUI,text='โปรแกรมบันทึกความรู้ ',font=('Angsana New',30),fg='green')
L1.place(x=30,y=20)
###################
def Button2():
    text = 'ตอนนี้มีเงินในบชอยู่ 300 บาท'
    messagebox.showinfo('เงินในบช',text)

    

FB1 = Frame(GUI) #คล้ายกระดาน
FB1.place(x=100,y=80)
B2 = ttk.Button(FB1,text='เงินมีอยู่กี่บาท',command=Button2)
B2.pack(ipadx=20,ipady=20)
###############

def Button3():
    text = 'วิชา phyton'
    messagebox.showinfo('สัปดาห์ทที่ 12-15 ก.พ. ',text)

    

FB2 = Frame(GUI) #คล้ายกระดาน
FB2.place(x=100,y=180)
B3 = ttk.Button(FB1,text='เรียนอะไร',command=Button3)
B3.pack(ipadx=20,ipady=20)


GUI.mainloop()
