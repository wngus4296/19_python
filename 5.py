'''
def __init__(self,v1,v2):
    self.id=v1
    self.balance=v2
'''
'''
class 계좌:
    계좌번호
    잔액

    입금():
        잔액 += 매개변수 값
    출금():
        잔액 -= 매개변수 값

계좌1(초기값 주어주기: 계좌번호, 잔액)
계좌2(초기값 주어주기: 계좌번호, 잔액)

print(현재 계좌1 계좌번호, 잔액)
계좌1.출금(원하는 값)
print(현재 계좌1 계좌번호, 잔액)

print(현재 계좌2 계좌번호, 잔액)
계좌1.입금(원하는 값)
print(현재 계좌2 계좌번호, 잔액)
'''
'''
class account:
    id = ''
    balance = 0

    def __init__(self, val1, val2):
        self.id = val1
        self.balance= val2

    def inmoney(self, val1):
        self.balance += val1

    def outmoney(self, val2):
        self.balance -= val2

ju = account('1002-159-508692', 3000000)
hyeon = account('352-0694-3524-43', 5000000)

print('ju의 계좌번호는 %s, 잔액은 %d원 입니다.' % (ju.id,ju.balance))

ju.inmoney(int(input('입금할 금액을 입력하세요: ')))

print('ju의 계좌번호는 %s, 입금 후 잔액은 %d원 입니다.' % (ju.id,ju.balance))

print('hyeon의 계좌번호는 %s, 잔액은 %d원 입니다.' % (hyeon.id,hyeon.balance))

hyeon.outmoney(int(input('출금할 금액을 입력하세요: ')))

print('hyeon의 계좌번호는 %s, 출금 후 잔액은 %d원 입니다.' % (hyeon.id,hyeon.balance))
'''


