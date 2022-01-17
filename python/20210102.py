#클래스
class FourCal: #사칙연산 클래스
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

a = FourCal(4,2) #생성자 실행
print(a.first)
print(a.second)
print(a.div())

class MoreFourCal(FourCal): #클래스의 상속
    def pow(self):
        result = self.first ** self.second
        return result

a = MoreFourCal(4,2)
print(a.pow())

class SafeFourCal(FourCal):
    def div(self):
        if self.second ==0:
            return 0
        else:
            return self.first/self.second

a = SafeFourCal(4,0)
print(a.div())
print('\n')

#클래스 변수
class Family:
    lastname = "김"

print(Family.lastname)
a = Family()
b = Family() #클래스로 만든 객체 동해서도 클래스 변수 사용 가능
print(a.lastname)
print(b.lastname)
print('\n')

#모듈
from mod1 import add #from 모듈이름 import 모듈함수
print(add(3,4))
from mod1 import * #모듈 안에 모든 함수 다 불러오겠다는 뜻 *
print(sub(4,3))

import mod2
a = mod2.Math()
print(a.solv(2)) 
print('\n')