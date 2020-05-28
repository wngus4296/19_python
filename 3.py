'''
fp = open('guru.txt','w')

instr = fp
'''

'''
fp = open("guru.txt",'r')


instr = fp.readlines()

for i in instr:
    print(i,end='')
fp.close()
'''

'''
import os

file = 'guru.txt'

if os.path.exists(file):

    fp = open(file,'r')

    instr = fp.readlines()

    for i in instr:
        print(i,end='')
    fp.close()

else:
    print('%s 파일이 없습니다.'% file)
'''
'''
inFp,outFp=None,None
inStr = ''

inFp = open('juhyeon.txt','r')
outFp= open('byun.txt','w')

inList= inFp.readlines()
for inStr in inList :
    outFp.writelines(inStr)

inFp.close()
outFp.close()
print('--파일이 정상적으로 복사되었음--')
'''
'''
inFp,outFp=None,None
inStr, outStr = '',''
i=0
secu = 0

secuYN = input('1.암호화 2.암호해독 중 선택: ')
inFname = input('입력 파일명을 입력하세요: ')
outFname = input('출력 파일명을 입력하세요: ')

if secuYN == '1':
    secu = 100
elif secuYN == '2':
    secu = -100

inFp = open(inFname, 'r', encoding = 'utf-8')
outFp = open(outFname,'w',encoding = 'utf-8')

while True :
    inStr = inFp.readline()
    if not inStr :
        break

    outStr = ''
    for i in range(0,len(inStr)):
        ch = inStr[i]
        chNum = ord(ch)
        chNum = chNum + secu
        ch2 = chr(chNum)
        outStr = outStr + ch2

    outFp.write(outStr)
    
outFp.close()
inFp.close()
print('%s --> %s 변환 완료' % (inFname, outFname))
'''
'''
import csv

fp = open('student.csv','r')

data = csv.reader(fp)

print(list(data))
'''
'''
import csv

fp = open('student.csv','r')

data = csv.reader(fp)

for csvStr in data:
    print(csvStr)
'''
'''
inFp,outFp = None, None
inStr = ''

inFp= open('C:/windows/notepad.exe','rb')
outFp = open('C:/Temp/notepad.exe.txt','wb')

while True :
    inStr= inFp.read(1)
    if not inStr:
        break
    outFp.write(inStr)

inFp.close()
outFp.close()
print('==이진 파일이 정상적으로 복사되었음==')
'''
from tkinter import *

def loadImage(fname):
    global inImage,XSIZE, YSIZE
    fp= open(fname,'rb')

    for i in range(0,XSIZE):
        tmpList = []
        for k in range(0,YSIZE):
            data= int(ord(fp.read(1)))
            tmpList.append(data)
        inImage.append(tmpList)

    fp.close()

def displayImage(image):
    global XSIZE, YSIZE
    for i in range(0,XSIZE):
        for k in range(0,YSIZE):
            data = image[i][k]
            paper.put('#%02x%02x%02x' % (data,data,data), (k,i))
window = None
canvas = None
XSIZE, YSIZE = 256, 256
inImage = []

window = Tk()
window.title('흑백 사진 보기')
canvas =Canvas(window, height =XSIZE, width = YSIZE)
paper = PhotoImage(width = XSIZE, height = YSIZE)

canvas.create_image((XSIZE /2, YSIZE /2), image = paper, state = 'normal')

filename = 'window/tree.raw'
loadImage(filename)
displayImage(inImage)

canvas.pack()
window.mainloop()
