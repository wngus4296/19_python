'''
hap= 0

for i in range(1, 11, 1):
    hap = hap + i    

print('1에서10까지의 합계: %d' % hap)
'''

'''
hap= 0

for i in range(501, 1000, 2):
    hap= hap+i

print('500과 1000사이에 있는 홀수의 합계: %d' %hap)
'''

'''
a = int(input('단을 입력하세요: '))
hap = 0
for i in range(1, 10, 1):
    hap = a * i
    print('%d * %d = %2d' % (a, i, hap))
'''

'''
import random

n1=random.randrange(1,7)
n2=random.randrange(1,7)
print('A의 주사위 숫자는 %d입니다.' %n1)
print('B의 주사위 숫자는 %d입니다.' %n2)

if n1 > n2:
    print('A가 이겼습니다.')
elif n1 == n2:
    print('비겼습니다.')
else :
    print('B가 이겼습니다.')
'''

'''
gop = 0
for a in range(1,10,1):
    for k in range(2,10,1):
        gop = a * k
        print('%d * %d =%2d' % (k,a,gop),end='  ')
    print('')
'''

'''
i = 0
hap = 0
while i < 11 :
    hap += i
    i +=1

print('1에서 10까지의 합계는: %d' %hap)
'''

'''
k = 9
for i in range(9,0,-1):
    gop = k*i
    print ('%d * %d = %2d'%(k,i,gop))
'''

'''
hap = 0
for i in range (1,101,1):
    hap = hap + i
    if hap >= 1000 :
        break
print('1~100의 합계를 최초로 1000이 넘게 하는 숫자: %d' %i)
'''

'''
hap = 0
for i in range(1,101,1):
    if i % 3 == 0 :
        continue
    hap = hap + i

print('1~100의 합계(3의 배수 제외): %d' % hap)
'''


dk = 0
zk = 0
ak = 0
ehs = 0
a = 3
while a != 4 :
    print('')
    print('===== 슈먼 카페=====')
    print('1. 아메리카노: 2000원\n2. 카페라테: 2500원\n3. 마끼야또: 3000원\n4. 주문종료')
    print('')
    a = int(input('메뉴를 입력해주세요 => '))
    if a == 4:
        break
    elif a <= 0 or a >= 5:
        print('잘못 입력되었습니다. 다시 입력해주세요.')
    else:
        b = int(input('수량을 입력해주세요 => '))
        if a == 1:
            dk += b
            ehs += 2000 * b
        elif a == 2:
            zk += b
            ehs += 2500 * b
        elif a == 3:
            ak += b
            ehs += 3000 * b
    
    print('')    
    print('***** 총 주문 내역 *****')
    print('1. 아메리카노: %d잔\n2. 카페라테: %d잔\n3. 마끼야또: %d잔\n총금액: %d원' % (dk, zk, ak, ehs))
    
print('주문을 종료합니다.')



    

