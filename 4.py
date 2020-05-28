'''
class Car:
    color = ''
    speed = 0

    def getColor(self):
        return self.color

    def upSpeed(self,value):
        self.speed += value

    def downSpeed(self,value):
        self.speed -= value

myCar1 = Car()
myCar2 = Car()
myCar3 = Car()

myCar1.color = '빨강'
myCar1.speed = 0

myCar2.color = '파랑'
myCar2.speed = 0

myCar3.color = '노랑'
myCar3.speed = 0

myCar1.upSpeed(30)
print('자동차1의 색상은 %s이며, 현재 속도는 %dkm입니다.' % (myCar1.color, myCar1.speed))

myCar2.upSpeed(60)
print('자동차2의 색상은 %s이며, 현재 속도는 %dkm입니다.' % (myCar2.color, myCar2.speed))

myCar3.upSpeed(0)
print('자동차3의 색상은 %s이며, 현재 속도는 %dkm입니다.' % (myCar3.color, myCar3.speed))
'''
'''
class Car:
    color = ''
    speed = 0

    def __init__(self, value1, value2):
        self.color = value1
        self.speed = value2
        
    def getColor(self):
        return self.color

    def upSpeed(self,value):
        self.speed += value

    def downSpeed(self,value):
        self.speed -= value

myCar1 = Car('빨강',100)
myCar2 = Car('파랑',200)
myCar3 = Car('검정',300)


print('자동차1의 색상은 %s이며, 현재 속도는 %dkm입니다.' % (myCar1.color, myCar1.speed))
print('자동차2의 색상은 %s이며, 현재 속도는 %dkm입니다.' % (myCar2.color, myCar2.speed))
print('자동차3의 색상은 %s이며, 현재 속도는 %dkm입니다.' % (myCar3.color, myCar3.speed))

myCar1.upSpeed(30)

print('자동차1의 색상은 %s이며, 현재 속도는 %dkm입니다.' % (myCar1.color, myCar1.speed))
print(myCar1.getColor())
'''
'''
class SM:
    그룹 이름
    소속 인원
    각 멤버 이름
    대표곡

    멤버 추가() : 소속 인원 + 1, 멤버 이름에 추가되는 멤버 append
    필드별로 값 리턴 ()
    
GG = SM(그룹 이름, 소속 인원, 각 멤버 이름, 대표곡)
'''
'''
class SM:
    gname = ''
    num = 0
    name =[]
    song = ''

    def __init__(self, value1, value2, value3, value4) :
        self.gname = value1
        self.name= value2
        self.song = value3
        self.num = value4
        
    def add(self, addname):
        orinum = len(GG.name)
        GG.name.append(new)
        for i in range(orinum, len(GG.name)):
            GG.num += 1
        
GG = None

GG = SM('소녀시대', ['태연','써니','티파니','효연','유리','수영','윤아','서현'], 'GEE', 8)
print('그룹이름: %s' % GG.gname)
print('인원: %d' % GG.num)
print('멤버: %s'% GG.name)
print('대표곡: %s' % GG.song)

new = ''
new = input('추가할 멤버: ')

GG.add(new)

print('')
print('====%s 추가====' % new)
print('그룹이름: %s' % GG.gname)
print('인원: %d' % GG.num)
print('멤버: %s'% GG.name)
print('대표곡: %s' % GG.song)
'''
