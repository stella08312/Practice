#구구단 프로그램 > 같은 결과를 내는 프로그램(다른 형식)
def GuGu(n):
    result = []
    result.append(n*1)
    result.append(n*2)
    result.append(n*3)
    result.append(n*4)
    result.append(n*5)
    result.append(n*6)
    result.append(n*7)
    result.append(n*8)
    result.append(n*9)
    return result
print(GuGu(2))

def GuGu(n):
    result = []
    i = 1
    while i<10:
        result.append(n*i)
        i = i+1
    return result
print(GuGu(2))

#3과 5의 배수 합하기
result = 0
for n in range(1, 1000):
    if n % 3 == 0 or n % 5 ==0:
        result +=n
print(result)