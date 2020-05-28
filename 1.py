'''
def calc(rPtks, num1, num2):
    result = 0
    if rPtks == '+':
        result = num1 + num2
    elif rPtks == '-':
        result = num1 - num2
    elif rPtks == '*':
        result = num1 * num2
    elif rPtks == '/':
        result = num1 / num2
    return result


ekq = 0
op,n1,n2 = '',0,0
op = input('계산을 입력하세요(+, -, *, /): ')
n1 = int(input('첫 번째 수를 입력하세요.: '))
n2 = int(input('두 번째 수를 입력하세요.: '))

ekq = calc(op, n1, n2)
print('## 계산기: %d %s %d = %d' % (n1, op, n2, ekq))            
'''
'''
import random

def getNumber() :
    return random.randrange(1, 46)

lotto = []
num = 0

print('** 로또 추첨을 시작합니다. **')
print()

while True:
    num = getNumber()

    if lotto.count(num) == 0:
        lotto.append(num)

    if len(lotto) >= 6:
        break

lotto.sort()

for i in range(0, 6):
    print('%d ' % lotto[i], end = '')
'''
'''
def myRange(start,end, hop = 1):
    retVal = start
    while retVal <= end :
        yield retVal
        retVal += hop

hap = 0
for i in myRange(1,5,2):
    hap += i
print(hap)
'''
