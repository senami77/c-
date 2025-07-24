'''
num2= 98
print("{0} {1:c}" .format(num2,num2))
'''
'''
float1=1234.567
print(float1)
print("기본 출력 {0:f}" .format(float1))
print("지수표기법 {0:e}" .format(float1))
print("소수 둘째자리까지 {0:.2f}" .format(float1))
'''
'''
txt1="Hello"
txt2="World!"
print("기본 출력\n{0:s} {1:s}" .format(txt1, txt2))
print("7칸 출력\n{0:7s} {1:7s}?" .format(txt1, txt2))
'''
'''
num1=17
print(num1)
print(f'10진수 17 = {num1}')
print(f'10진수 17의 8진수 = {num1:o}')
print(f'10진수 17의 16진 = {num1:x}')
'''
'''
num2 = 100
print(f"{num2} {num2:c}")
'''
'''
float1=1234.567
print(float1)
print(f"기본 출력 {float1:f}")
print(f"지수표기법 {float1:e}")
print(f"소수 둘째자리까지 {float1:.2f}")
'''
'''
txt1="Hello"
txt2="World!"
print(f'기본 출력\n{txt1:s} {txt2:s}')
print(f'7칸 출력\n{txt1:7s} {txt2:7s}?')
'''
'''
#문제 1)
r = 5
pi = 3.14
print('넓이는 %d * %d * %.2f = %.1f' %(r,r,pi,r*r*pi))
'''
'''
#문제 2)
r = 5
pi = 3.14
print('넓이는 {0:d} * {1:d} * {2:.2f} = {3:.1f}' .format(r,r,pi,r*r*pi))
'''
'''
#문제 3)
r = 5
pi = 3.14
print(f'넓이는 {r:d} * {r:d} * {pi:.2f} = {r*r*pi:.1f}')
'''
'''
#문제 4)
golden_ratio = 1.61804
print(f'소수 첫째 자리까지 출력 : {golden_ratio:.1f}')
print(f'소수 둘째 자리까지 출력 : {golden_ratio:.2f}')
print(f'소수 셋째 자리까지 출력 : {golden_ratio:.3f}')
print(f'소수 넷째 자리까지 출력 : {golden_ratio:.4f}')
'''
'''
#문제 1)
nickname = input("닉네임을 입력하세요 : ")
print("환영합니다 ABC님!")
'''
'''
#문제 2)
number = input('실수를 입력하세요 : ')
number = float(number)
print(number*10)
'''

number1 = input('첫번째 숫자를 입력하세요 : ')
number2 = input('두번째 숫자를 입력하세요 : ')
number3 = input('세번째 숫자를 입력하세요 : ')
number1 = int(number1)
number2 = int(number2)
number3 = int(number3)
number4 = number1+number2+number3
print("총합은", number4)















 
