from tkinter import *
from tkinter.simpledialog import *
from tkinter import messagebox 

#전역변수 추가
flag = True
name, birth, answer, site, idid, pw = [],[],[],[],[],[]
pname, pbirth, panswer, psite, pid, ppw, ppw1 = '',0,'','','','a','b'
fname, fbirth, fanswer, fsite, fpid, fppw = 0,0,0,0,0,0
check = 0

#취소를 누르거나 X를 누르면 방금 입력한 값 모두 사라짐
def on_closing():
    if messagebox.askokcancel('종료', '종료하시겠습니까?'):
        window.destroy()

def warningpw():
    messagebox.showinfo('경고','입력한 비밀번호와 일치하지 않습니다.')

def warninginput():
    messagebox.showinfo('경고','입력한 값과 일치하는 정보가 없습니다.')

def warningaw():
    messagebox.showinfo('경고', '답이 틀렸습니다.')

def warningzero():
    messagebox.showinfo('경고', '입력값은 1자 이상이어야 합니다.')

def complete():
    messagebox.showinfo('완료', '비밀번호 입력이 완료되었습니다.')


def answerpf1():
    while True:
        flag = True
        panswer = ''
        panswer = askstring('답변 입력', '1.당신의 어릴적 고향은?')
        if panswer != None:
            if panswer == '':
                warningzero()
            elif answer[fbirth][0] != panswer:
                warninginput()
            else:
                sitetopid()
        else:
            flag = True
            
        if flag == True:
            break
    
def answerpf2():
    while True:
        flag = True
        panswer = ''
        panswer = askstring('답변 입력', '2.당신의 보물 1호는?')
        if panswer != None:
            if panswer == '':
                warningzero()
            elif answer[fbirth][1] != panswer:
                warninginput()
            else:
                sitetopid()
        else :
            flag = True

        if flag == True:
            break
        
def answerpf3():
    while True:
        flag = True
        panswer = ''
        panswer = askstring('답변 입력', '3.당신에게 가장 특별한 사람은?')
        if panswer != None:
            if panswer == '':
                warningzero()
            elif answer[fbirth][2] != panswer:
                warninginput()
            else:
                sitetopid()
        else :
            flag = True

        if flag == True:
            break
        
def answerpf4():
    while True:
        flag = True
        panswer = ''
        panswer = askstring('답변 입력', '4.당신이 나온 초등학교 이름은?')
        if panswer != None:
            if panswer == '':
                warningzero()
            elif answer[fbirth][3] != panswer:
                warninginput()
            else:
                sitetopid()
        else :
            flag = True

        if flag == True:
            break
        
def answerpf5():
    while True:
        flag = True
        panswer = ''
        panswer = askstring('답변 입력', '5.당신의 어머니의 성함은?')
        if panswer != None:
            if panswer == '':
                warningzero()
            elif answer[fbirth][4] != panswer:
                warninginput()
            else:
                sitetopid()
        else :
            flag = True

        if flag == True:
            break

def ididpf():
    #값 맞는지 확인
    while True:
        flag = True
        pid = ''
        pid = askstring('아이디 입력', '아이디를 입력하세요')
        if pid != None:
            if pid == '':
                warningzero()
            elif idid[fbirth] != pid:
                warninginput()
            else:
                pass
        else :
            flag = True

        if flag == True:
            break
    
def sitetopid():
    while True:
        flag = True
        psite = ''
        psite = askstring('사이트  입력', '사이트를 입력하세요')
        if psite != None:
            if psite == '':
                warningzero()
            elif site[fbirth] != psite:
                warninginput()
            else:
                pid = ''
                pid = askstring('아이디 입력', '아이디를 입력하세요')
                if pid != None:
                    if pid == '':
                        warningzero()
                    elif idid[site.index(psite)] != pid:
                        warninginput()
                    else:
                        messagebox.showinfo('비밀번호', '사이트: %s\n아이디: %s\n비밀번호: %s' % (site[fbirth],idid[site.index(psite)],pw[site.index(psite)]))
                else:
                    flag = True
                
        else :
            flag = True

        if flag == True:
            break
            
            
def addpw():
    global name, birth, answer, site, idid, pw, flag
    
    while True:
        flag = True
        pname = ''
        pname = askstring('이름 입력', '이름을 입력하세요')
        if pname != None:
            if pname == '':
                warningzero()
            else:
                name.append(pname)

                pbirth = '' 
                while pbirth == '':
                    pbirth = askstring('생년월일 입력', '생년월일을 입력하세요')
                    if pbirth != None:
                        if pbirth == '':
                            warningzero()
                        else:
                            birth.append(pbirth)  
        
                            aw = []
                            panswer = ''
                            while panswer == '':
                                panswer = askstring('답변 입력', '1.당신의 어릴적 고향은?')
                                if panswer != None:
                                    if panswer == '':
                                        warningzero()
                                    else:
                                        aw.append(panswer)

                                        panswer = ''
                                        while panswer == '':
                                            panswer = askstring('답변 입력', '2.당신의 보물 1호는?')
                                            if panswer != None:
                                                if panswer == '':
                                                    warningzero()
                                                else:
                                                    aw.append(panswer)

                                                    panswer = ''
                                                    while panswer == '':
                                                        panswer = askstring('답변 입력', '3.당신에게 가장 특별한 사람은?')
                                                        if panswer != None:
                                                            if panswer == '':
                                                                warningzero()
                                                            else:
                                                                aw.append(panswer)

                                                                panswer = ''
                                                                while panswer == '':
                                                                    panswer = askstring('답변 입력', '4.당신이 나온 초등학교 이름은?')
                                                                    if panswer != None:
                                                                        if panswer == '':
                                                                            warningzero()
                                                                        else:
                                                                            aw.append(panswer)

                                                                            panswer = ''
                                                                            while panswer == '':
                                                                                panswer = askstring('답변 입력', '5.당신의 어머니의 성함은?')
                                                                                if panswer != None:
                                                                                    if panswer == '':
                                                                                        warningzero()
                                                                                    else:
                                                                                        aw.append(panswer)
                                                                                        answer.append(aw)

                                                                                        psite = ''
                                                                                        while psite == '':
                                                                                            psite = askstring('사이트 입력', '사이트를 입력하세요')
                                                                                            if psite != None:
                                                                                                if psite == '':
                                                                                                    warningzero()
                                                                                                else:
                                                                                                    site.append(psite)
                                                                                                
                                                                                                    pid = ''
                                                                                                    while pid == '':
                                                                                                        pid = askstring('아이디 입력', '아이디를 입력하세요')
                                                                                                        if pid != None:
                                                                                                            if pid == '':
                                                                                                                warningzero()
                                                                                                            else:
                                                                                                                idid.append(pid)

                                                                                                                ppw = 'a'
                                                                                                                ppw1 = 'b'
                                                                                                                while ppw != ppw1:
                                                                                                                    ppw = askstring('비밀번호 입력', '비밀번호를 입력하세요')
                                                                                                                    if ppw != None:
                                                                                                                #비밀번호 확인 if문 사용
                                                                                                                        ppw1 = askstring('비밀번호 확인', '비밀번호를 한 번 더 입력하세요')
                                                                                                                        if ppw1 != None:
                                                                                                                            if ppw1 != ppw:
                                                                                                                                warningpw()
                                                                                                                            else:
                                                                                                                                pw.append(ppw)
                                                                                                                                breakpoint
                                                                                                                                
                                                                                                                                complete()
                                                                                                                        else:
                                                                                                                            name.pop()
                                                                                                                            birth.pop()
                                                                                                                            aw.pop()
                                                                                                                            aw.pop()
                                                                                                                            aw.pop()
                                                                                                                            aw.pop()
                                                                                                                            aw.pop()
                                                                                                                            site.pop()
                                                                                                                            idid.pop()
                                                                                                                            flag = True
                                                                                                        else:
                                                                                                            name.pop()
                                                                                                            birth.pop()
                                                                                                            aw.pop()
                                                                                                            aw.pop()
                                                                                                            aw.pop()
                                                                                                            aw.pop()
                                                                                                            aw.pop()
                                                                                                            site.pop()
                                                                                                            flag = True
                                                                                            else:
                                                                                                name.pop()
                                                                                                birth.pop()
                                                                                                aw.pop()
                                                                                                aw.pop()
                                                                                                aw.pop()
                                                                                                aw.pop()
                                                                                                aw.pop()
                                                                                                flag = True
                                                                                else:
                                                                                    name.pop()
                                                                                    birth.pop()
                                                                                    aw.pop()
                                                                                    aw.pop()
                                                                                    aw.pop()
                                                                                    aw.pop()
                                                                                    flag = True
                                                                    else:
                                                                        name.pop()
                                                                        birth.pop()
                                                                        aw.pop()
                                                                        aw.pop()
                                                                        aw.pop()
                                                                        flag = True
                                                        else:
                                                            name.pop()
                                                            birth.pop()
                                                            aw.pop()
                                                            aw.pop()
                                                            flag = True
                                            else:
                                                name.pop()
                                                birth.pop()
                                                aw.pop()
                                                flag = True
                                else:
                                    name.pop()
                                    birth.pop()
                                    flag = True
                    else:
                        name.pop()
                        flag = True
        else :
            flag = True

        if flag == True:
            break
                            
def findpw():
    global fname, fbirth, fanswer, fsite, fpid, fppw, var,check
    while True:
        flag = True
        pname = ''
        pname = askstring('이름 입력', '이름을 입력하세요')
        if pname != None:
            if pname == '':
                warningzero()
            elif name.count(pname) == 0:
                warninginput()
            else:
                fname = name.index(pname)
                pbirth = ''
                pbirth = askstring('생년월일  입력', '생년월일을 입력하세요')
                if pbirth != None:
                    if pbirth == '':
                        warningzero()
                    elif birth[fname] != pbirth:
                            warninginput()
                    else:
                        fbirth = birth.index(pbirth)

                        ranswer1 = Button(window, text = '1.당신의 어릴적 고향은?',command = answerpf1)
                        ranswer2 = Button(window, text = '2.당신의 보물 1호는?',command = answerpf2)
                        ranswer3 = Button(window, text = '3.당신에게 가장 특별한 사람은?',command = answerpf3)
                        ranswer4 = Button(window, text = '4.당신이 나온 초등학교 이름은?',command = answerpf4)
                        ranswer5 = Button(window, text = '5.당신의 어머니의 성함은?',command = answerpf5)
                        label1 = Label(window, text = '질문을 선택하세요.')

                        if check == 0:
                            label1.pack()
                            ranswer1.pack()
                            ranswer2.pack()
                            ranswer3.pack()
                            ranswer4.pack()
                            ranswer5.pack()
                            check += 1


                        else:
                            label1.configure(text = '질문을 선택하세요.')
                            ranswer1.configure(text = '1.당신의 어릴적 고향은?')
                            ranswer2.configure(text = '2.당신의 보물 1호는?')
                            ranswer3.configure(text = '3.당신에게 가장 특별한 사람은?')
                            ranswer4.configure(text = '4.당신이 나온 초등학교 이름은?')
                            ranswer5.configure(text = '5.당신의 어머니의 성함은?')
                else:
                    flag = True
        else :
            flag = True

        if flag == True:
            break


    
#메인 코드   
window = Tk()
window.protocol('WM_DELETE_WINDOW', on_closing)

window.title('PW')
buttonaddpw = Button(window, text = '비밀번호 추가', command = addpw)
buttonfindpw = Button(window, text = '비밀번호 찾기', command = findpw)

buttonaddpw.pack(side=LEFT, fill = X, padx = 10, pady = 10)
buttonfindpw.pack(side=LEFT, fill = X, padx = 10, pady = 10)

window.mainloop()

