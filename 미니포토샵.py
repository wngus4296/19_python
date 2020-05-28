from tkinter import *
from tkinter.filedialog import *
from tkinter.simpledialog import *
from wand.image import *


def displayimage(img, width, height):
    global window, canvas, paper, photo, photo2, oriX, oriY

    window.geometry(str(width) + 'x' + str(height))
    
    if canvas != None :
        canvas.destroy()
      
    canvas = Canvas(window, width = width, height = height)
    paper = PhotoImage(width = width, height = height)
    canvas.create_image((width/2, height/2), image = paper, state = 'normal')

    blob = img.make_blob(format = 'RGB')

    for i in range(0,height) :
        for k in range(0,width): 
            r = blob[(i * 3 * width) + (k * 3) + 0]
            g = blob[(i * 3 * width) + (k * 3) + 1]
            b = blob[(i * 3 * width) + (k * 3) + 2]
            paper.put('#%02x%02x%02x' % (r,g,b),(k,i))

        canvas.pack()
    
def fileopen():
    global window, canvas, paper, photo, photo2, oriX, oriY
    readFp = askopenfilename(parent = window,filetypes= (('모든 그림 파일', '*.jpg;*.jpeg;*.bmp;*.gif;*.png'),('모든파일','*.*')))
    photo = Image(filename = readFp)
    oriX = photo.width
    oriY = photo.height
                             
    photo2=photo.clone()
    newX = photo2.width
    newY = photo2.height
    
    displayimage(photo2,newX,newY)


def filesave():
    global window, canvas, paper, photo, photo2, oriX, oriY

    if photo2== None:
        return
    saveFp = asksaveasfile(parent = window,mode = 'w', defaultextension = '.jpg', filetypes = (('JPG파일', '*.jpg;*.jpeg'),('모든파일', '*.*')))
    savePhoto = photo2.convert('jpg')
    savePhoto.save(filename = saveFp.name)
    
    
def fileexit():
    pass

def zoomin():
    global window, canvas, paper, photo, photo2, oriX, oriY
    scale = askinteger('확대','확대할 배율을 입력하세요', minvalue = 2, maxvalue =4)
    photo2 =photo.clone()
    photo2.resize(int(oriX * scale), int(oriY * scale))
    newX = photo2.width
    newY = photo2.height
    displayimage(photo2,newX,newY)
    
def zoomout():
    global window, canvas, paper, photo, photo2, oriX, oriY
    scale = askinteger('축소','축소할 배율을 입력하세요', minvalue = 2, maxvalue =4)
    photo2 =photo.clone()
    photo2.resize(int(oriX / scale), int(oriY / scale))
    newX = photo2.width
    newY = photo2.height
    displayimage(photo2,newX,newY)

def switchupdown():
    global window, canvas, paper, photo, photo2, oriX, oriY
    photo2 =photo.clone()
    photo2.flip()
    newX = photo2.width
    newY = photo2.height
    displayimage(photo2,newX,newY)
    
def switchside():
    global window, canvas, paper, photo, photo2, oriX, oriY
    photo2 =photo.clone()
    photo2.flop()
    newX = photo2.width
    newY = photo2.height
    displayimage(photo2,newX,newY)

def rotate():
    global window, canvas, paper, photo, photo2, oriX, oriY
    degree = askinteger('회전','회전할 각도를 입력하세요', minvalue = 0, maxvalue = 360)
    photo2 =photo.clone()
    photo2.rotate(degree)
    newX = photo2.width
    newY = photo2.height
    displayimage(photo2,newX,newY)

def bright():
    global window, canvas, paper, photo, photo2, oriX, oriY
    value = askinteger('밝게','값을 입력하세요(100~200)', minvalue = 100, maxvalue = 200)
    photo2 =photo.clone()
    photo2.modulate(value,100,100)
    newX = photo2.width
    newY = photo2.height
    displayimage(photo2,newX,newY)

def dark():
    global window, canvas, paper, photo, photo2, oriX, oriY
    value = askinteger('어둡게','값을 입력하세요(0~100)', minvalue = 0, maxvalue = 100)
    photo2 =photo.clone()
    photo2.modulate(value,100,100)
    newX = photo2.width
    newY = photo2.height
    displayimage(photo2,newX,newY)

def clear():
    global window, canvas, paper, photo, photo2, oriX, oriY
    value = askinteger('선명하게','값을 입력하세요(100~200)', minvalue = 100, maxvalue = 200)
    photo2 =photo.clone()
    photo2.modulate(100,value,100)
    newX = photo2.width
    newY = photo2.height
    displayimage(photo2,newX,newY)

def unclear():
    global window, canvas, paper, photo, photo2, oriX, oriY
    value = askinteger('탁하게','값을 입력하세요(0~100)', minvalue = 0, maxvalue = 100)
    photo2 =photo.clone()
    photo2.modulate(100,value,100)
    newX = photo2.width
    newY = photo2.height
    displayimage(photo2,newX,newY)

def black():
    global window, canvas, paper, photo, photo2, oriX, oriY
    photo2 =photo.clone()
    photo2.type = 'grayscale'
    newX = photo2.width
    newY = photo2.height
    displayimage(photo2,newX,newY)

window, canvas, paper = None,None,None
photo,photo2=None,None
oriX,oriY=0,0

window = Tk()
window.geometry('250x250')
window.title('미니 포토샵')

mainmenu=Menu(window)
window.config(menu = mainmenu)
photo = PhotoImage()
pLabel = Label(window, image = photo)
pLabel.pack(expand= 1, anchor = CENTER)

#윈도우에 붙는 메뉴
filemenu = Menu(mainmenu)
imagemodify1=Menu(mainmenu)
imagemodify2=Menu(mainmenu)

#메인메뉴
mainmenu.add_cascade(label='파일', menu = filemenu)
mainmenu.add_cascade(label='이미지 처리(1)', menu = imagemodify1)
mainmenu.add_cascade(label='이미지 처리(2)', menu = imagemodify2)

#파일메뉴
filemenu.add_command(label='파일 열기', command = fileopen)
filemenu.add_command(label='파일 저장', command = filesave)
filemenu.add_separator()
filemenu.add_command(label='프로그램 종료', command = fileexit)

#이미지 처리(1)
imagemodify1.add_command(label='확대', command = zoomin)
imagemodify1.add_command(label='축소', command = zoomout)
imagemodify1.add_separator()
imagemodify1.add_command(label='상하 반전', command = switchupdown)
imagemodify1.add_command(label='좌우 반전', command = switchside)
imagemodify1.add_command(label='회전', command = rotate)

#이미지 처리(2)
imagemodify2.add_command(label='밝게', command = bright)
imagemodify2.add_command(label='어둡게', command = dark)
imagemodify2.add_separator()
imagemodify2.add_command(label='선명하게', command = clear)
imagemodify2.add_command(label='탁하게', command = unclear)
imagemodify2.add_command(label='흑백이미지', command = black)

window.mainloop()
