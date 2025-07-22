#print("Hello World")
#이렇게 하면 한문장 주석처리

'''
이렇게 하면
전체 주석처리
'''

'''
print("이샘","학원",sep="코딩전문") #쉼표때문에 띄어쓰기 되는 것을 막음
print("이샘코딩학원",end="") #줄바꿈을 막음
print("이샘","코딩","전문","학원")
print("코딩세계에","오신걸","환영합니다")
'''

'''
print("안녕하세요")
print("안녕하세요")

print("안녕하세요\n")
print("안녕하세요\n")

print('안녕하세요',end="")
print('안녕하세요',end='')

print("\",\'는 따옴표의 대체 기호입니다.") #\는 출력되지 않음
print("\\n은 줄바꿈의 대체 기호입니다.") #\\가 두 개씩 있으면 \하나 출력

print("따옴표는 '역할'이 같아요")
print('따옴표는 "역할"이 같아요')
'''

'''
#실행불가
print('따옴표는 "역할'이 같아요")
print('따옴표는 "역할"이 같아요")
'''

'''
apple = "사과"
print(apple,1,"상자")

apple = "사과"
print(apple,1,"상자",sep="++")

print("이샘")
print("코딩")
print("학원")

print("이샘",end="")
print("코딩",end="")
print("학원",end="!")
'''

'''
num1 = 10
print(num1, type(num1))

num2 = 3.14
print(num2, type(num2))

m_str = "안녕하세요"
print(m_str, type(m_str))

print(1+1, type(1+1))

print(0.3+2.04, type(0.3+2.04))

print(1+2.3, type(1+2.3))
'''

'''
#문제1)
print("\"이샘",end="")
print("코딩",end="")
print("학원",end="\"")

#문제2)
print(1,2,3,sep="+",end="=6")
'''

'''
num1=17
print(num1)
print("10진수 17 = %d"%(num1))
print("10진수 17의 8진수 = %o"%(num1))
print("10진수 17의 16진수 = %x"%(num1))

num2 = 97
print("%d %c" % (num2,num2)) #문자 <-유니코드 표에 적힌 숫자 번호로 출력

float1=1234.567
print(float1)
print("기본 출력 %f"%(float1))
print("지수표기법 %e"%(float1))
print("소수 둘째자리까지%.2f"%(float1))

txt1="Hello"
txt2="World!"

print("기본 출력\n%s %s"%(txt1,txt2))
print("7칸 출력\n%7s %7s"%(txt1,txt2))
'''

num1=17
print(num1)
print("10진수 17 = {0}".format(num1))
print("10진수 17의 8진수 = {0:o}".format(num1))
print("10진수 17의 16진수 = {0:x}".format(num1))

num2=98
print("{0} {1:c}".format(num2,num2))







