'''
from tkinter import *

window = Tk()

window.title('윈도창 연습')
window.geometry('400x100')
window.resizable(width = FALSE, height = FALSE)

window.mainloop()
'''
'''
from tkinter import *

window =Tk()

lable1 = Label(window, text = 'COOKBOOK~~ PYTHON을')
lable2 = Label(window, text = '열심히', font = ('궁서체', 30), fg = 'blue')
lable3 = Label(window, text = '공부 중입니다.', bg = 'magenta', width = 20, height = 5, anchor = SE)

lable1.pack()
lable2.pack()
lable3.pack()
               


window.mainloop()
'''
'''
from tkinter import *

window = Tk()
window.title('댕댕이')
window.geometry('300x300')
window.resizable(width = FALSE, height = FALSE)

photo = PhotoImage(file = '실습/dog.gif')
label2 = Label(window, text = '변댕댕', font = ('궁서체', 30), fg = 'pink')
label1 = Label(window, image = photo)

label2.pack()
label1.pack()


window.mainloop()
'''
'''
from tkinter import *

window = Tk()
window.title('냥이들')

photo1 = PhotoImage(file = '실습/cat.gif')
photo2 = PhotoImage(file = '실습/cat2.gif')
photo3 = PhotoImage(file = '실습/cat3.gif')

label1 = Label(window, image = photo1)
label2 = Label(window, image = photo2)
label3 = Label(window, image = photo3)
label4 = Label(window, text = '****김수현****', font = ('맑은고딕',30),fg = 'green')

label4.pack()
label1.pack(side = RIGHT)
label2.pack()
label3.pack()

window.mainloop()
'''
'''
from tkinter import *

window= Tk()

button1 = Button(window, text = '파이썬 종료', fg = 'red', bg = 'black', command = quit)

button1.pack()

window.mainloop()
'''
'''
from tkinter import *

window= Tk()

photo = PhotoImage(file = '실습/dog.gif')
button1 = Button(window, image = photo, command = quit)

button1.pack()

window.mainloop()
'''
'''
from tkinter import *
from tkinter import messagebox

def myfunc():
    messagebox.showinfo('강아지버튼',"강아지가 귀엽죠?")
    
window= Tk()

photo = PhotoImage(file = '실습/dog.gif')
button1 = Button(window, image = photo, command = myfunc)

button1.pack()

window.mainloop()
'''
'''
from tkinter import *
from tkinter import messagebox

window = Tk()

def myFunc() :
    if chk.get() == 0:
        messagebox.showinfo('','체크버튼이 꺼졌어요.')
    else :
        messagebox.showinfo('','체크버튼이 켜졌어요.')

chk = IntVar()
cb1 = Checkbutton(window, text = '클릭하세요.', variable = chk, command = myFunc)

cb1.pack()

window.mainloop()
'''
'''
from tkinter import *

window = Tk()

def myFunc() :
    if var.get() == 1:
        label.configure(text = '파이썬')
    elif var.get() == 2:
        label.configure(text = 'C++')
    else :
        label.configure(text = 'Java')        

var = IntVar()
rb1 = Radiobutton(window, text = '파이썬', variable = var, value = 1, command = myFunc)
rb2 = Radiobutton(window, text = 'C++', variable = var, value = 2, command = myFunc)
rb3 = Radiobutton(window, text = 'Java', variable = var, value = 3, command = myFunc)
label = Label(window, text = '선택한 언어: ', fg = 'red')

rb1.pack()
rb2.pack()
rb3.pack()
label.pack()


window.mainloop()
'''
'''
from tkinter import *

window = Tk()

photo1 = PhotoImage(file = '실습/dog.gif')
photo2 = PhotoImage(file = '실습/dog2.gif')
photo3 = PhotoImage(file = '실습/dog3.gif')


def myFunc():
    if var.get() == 1:
        label.configure(image = photo1)
    elif var.get() == 2:
        label.configure(image = photo2)
    else :
        label.configure(image = photo3)

var = IntVar()
rb1 = Radiobutton(window, image = photo1, variable = var, value = 1, command = myFunc)
rb2 = Radiobutton(window, image = photo2, variable = var, value = 2, command = myFunc)
rb3 = Radiobutton(window, image = photo3, variable = var, value = 3, command = myFunc)
label2 = Label(window, text = '선택한 갱얼쥐: ', font = ('맑은고딕',30))
label = Label(window, text = '', fg = 'red')

rb1.pack()
rb2.pack()
rb3.pack()
label2.pack()
label.pack()    

window.mainloop()
'''
'''
from tkinter import *

frameList = ['jeju1.gif','jeju2.gif','jeju3.gif','jeju4.gif','jeju5.gif','jeju6.gif','jeju7.gif','jeju8.gif','jeju9.gif']
photoList = [None] * 9
num = 0

def myFunc1():
    global num
    num += 1
    if num > 8 :
        num = 0
    photo = PhotoImage(file = '실습/' + frameList[num])
    pLabel.configure(image = photo)
    pLabel.image = photo
    
def myFunc2():
    global num
    num -= 1
    if num  < 0 :
        num = 8
    photo = PhotoImage(file = '실습/' + frameList[num])
    pLabel.configure(image = photo)
    pLabel.image = photo

window = Tk()
window.geometry('700x500')
window.title('사진 앨범 보기')

button1 = Button(window, text = '<< 이전', command = myFunc1)
button2 = Button(window, text = '다음 >>', command = myFunc2)

photo = PhotoImage(file = '실습/' + frameList[0])
pLabel = Label(window, image =photo)

button1.place(x = 250, y = 10)
button2.place(x = 400, y = 10)
pLabel.place(x = 15, y = 50)


window.mainloop()
'''
'''
from tkinter import *
from tkinter import messagebox

window = Tk()

def getposition(event):
    txt = '<Position> X : '+ str(event.x) + ' Y: ' + str(event.y)
    label1.configure(text = txt)
label1 = Label(window, text = 'Hello', font = ('',30), fg = 'magenta')
label1.bind('<B1-Motion>', getposition)


label2 = Label(window, text= '', width = 100, height = 100, bg ='black')
       
label1.pack()
label2.pack()

window.mainloop()
'''
'''
from tkinter import *
from tkinter import messagebox

window = Tk()

def getposition(event):
    txt = event.keycode
    label1.configure(text = txt)

label1 = Label(window, text = 'Hello', font = ('',30), fg = 'magenta')

label1.bind('<B1-Motion>', getposition)


label2 = Label(window, text= '', width = 100, height = 100, bg ='black')

window.bind('<Key>', getposition)
       
label1.pack()
label2.pack()

window.mainloop()
'''
'''
from tkinter import *
from tkinter import messagebox

window = Tk()

menu1= Menu(window)
window.config(menu = menu1)

menu2 = Menu(menu1)
menu3 = Menu(menu2)

menu1.add_cascade(label= 'File', menu = menu2)
menu2.add_command(label= 'New File', command=window.quit)
menu2.add_cascade(label = 'Recent files', menu = menu3)
menu3.add_command(label = 'A.py')
window.mainloop()
'''
'''
from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import *

window = Tk()

label1 = Label(window, text = '입력된 값: ', font = ('', 30), fg = 'magenta')
label1.pack()

var = askinteger('확대배수', '주사위 숫자 입력 (1~6)',minvalue = 1, maxvalue =6)

label1.configure(text = str(var))
window.mainloop()
'''
'''
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import *

window = Tk()

label1 = Label(window, text = '입력된 값: ', font = ('', 30), fg = 'black')
label1.pack()

var = askopenfilename(parent = window,filetypes = (('GIF파일','*.gif'),('모든 파일', '*.*')))

label1.configure(text = str(var))
window.mainloop()
'''
from tkinter import *
from tkinter.filedialog import *

window = Tk()
window.geometry('400x400')


def selectFile():
    filename = askopenfilename(parent = window,filetypes = (('GIF파일','*.gif'),('모든 파일', '*.*')))
    photo = PhotoImage(file = filename)
    pLabel.configure(image = photo)
    pLabel.image = photo

def func_exit() :
    window.quit()
    window.destroy()

photo =PhotoImage()
pLabel= Label(window, image=photo)
pLabel.pack(expand = 1, anchor = CENTER)

window = Tk()
window.geometry('400x400')

window.title('명화 감상하기')
menu1= Menu(window)
window.config(menu = menu1)
menu2 = Menu(menu1)

menu1.add_cascade(label= '파일', menu = menu2)
menu2.add_command(label = '파일 열기',command= selectFile)
menu2.add_separator()
menu2.add_command(label= '프로그램 종료', command= func_exit)

window.mainloop()


