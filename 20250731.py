'''
#문제 4-1)
song = '동해물과 백두산이 마르고 닳도록 하느님이 보우하사 우리나라 만세. 무궁화 삼천리 화려 강산 대한 사람, 대한으로 길이 보전하세.'
print(song[33]+song[34])
print(song[68]+song[69])
'''

'''
#문제 4-2)
song = '동해물과 백두산이 마르고 닳도록 하느님이 보우하사 우리나라 만세. 무궁화 삼천리 화려 강산 대한 사람, 대한으로 길이 보전하세.'
print(song[0:47],end=" ")
print(song[48]+song[34],end=" ")
print(song[51:71])
'''

'''
bab = "국밥 컵밥 초밥 김밥 비빔밥"
print("가장 앞에 있는 밥은 "+str(bab.find("밥"))+"번째!")
print("가장 뒤에 있는 밥은 "+str(bab.rfind("밥"))+"번째!")
'''

'''
eng = "FunnyPython"
kor = "신나는파이썬"
blank = "B L A N K"
print(eng.isalpha())
print(kor.isalpha())
print(blank.isalpha())
'''

'''
num = "20240505"
date = "2024.05.05"
print(num.isnumeric())
print(date.isnumeric())
'''

'''
#문제 1)
sentence = "강낭콩 옆 빈 콩깍지는 완두콩 깐 빈 콩깍지고 완두콩 옆 빈 콩깍지는 강낭콩 깐 빈 콩깍지다."
print("첫번째 완두콩은 "+str(sentence.find("완두콩"))+"번째에 있습니다.")
print("두번째 완두콩은 "+str(sentence.rfind("완두콩"))+"번째에 있습니다.")
'''

'''
#문제 2)
sentence = "강낭콩 옆 빈 콩깍지는 완두콩 깐 빈 콩깍지고 완두콩 옆 빈 콩깍지는 강낭콩 깐 빈 콩깍지다."
print(str(sentence.find("완두콩"))+str(sentence.find("깐 빈"))+str(sentence.find("콩깍지")))
print(sentence[13:16]+" "+sentence[17:20]+" "+sentence[8:11])
print(str(sentence.find("강낭콩"))+str(sentence.find("깐 빈"))+str(sentence.find("콩깍지")))
print(sentence[0:3]+" "+sentence[17:20]+" "+sentence[8:11])
'''

'''
#문제 3)
email = input("이메일을 입력해주세요 : ")
#print(str(email.find('@')))
print("이 이메일의 아이디는 "+email[0:6]+"입니다.")
'''

'''
dessert = "초코케이크 녹차마카롱 모카라떼"
cake, macaron, coffee = dessert.split(" ")
print("[ 오늘 먹을 간식 목록 ]")
print("케이크 :", cake)
print("마카롱 :", macaron)
print("커피 :", coffee)
'''

'''
n1,n2 = input("int 둘 입력 : ").split()
print(n1)
print(n2)
print(n1+n2)
print(int(n1)+int(n2))
'''

'''
a,b,c = input("알파벳 셋 입력 : ").split()
print(c,b,a,sep=">")
'''

'''
r1,r2 = input("float 둘 입력 : ").split()
r1=float(r1)
r2=float(r2)
print(r1*r2)
'''

'''
message = """대공원에 봄 벚꽃 놀이는
낮 봄 벚꽃 놀이보다
밤 봄 벚꽃 놀이니라."""

print(message.replace("벚꽃","개나리"))
'''

'''
win = "WindowXP"
update = win.replace("XP","11")

print(update + "로 업데이트 됐습니다.")
'''

'''
japangi = """이 자판기 안에는
포도맛 사이다,
포도맛 쥬스,
포도맛 슬러쉬
가 있습니다."""
taste = input("무슨 맛 자판기로 바꿀까요 : ")
print(japangi.replace("포도",taste))
'''

'''
message = input("영어로 문장을 적어주세요 : ")
print(message.upper())
print(message.lower())
'''

'''
message = "abcD 1234 ..@@ !!!"
trans = message.upper()
print(trans)
'''

'''
#문제 1)
number = input("전화번호 입력 : ")
#split() <- ()안에 문자열을 넣어주면 그 부분마다 자름. ()를 비워두면 띄어쓰기.
a,b,c = number.split("-")
print(a)
print(b)
print(c)
'''

'''
#문제 2)
filename = input("파일명을 입력해주세요 : ")
change = filename.replace("jpg","png")
print(filename+" 파일을 "+change+" 파일로 변경하였습니다.")
'''

#문제 3)
sentence = "Hello, Python! Helo, String!"
print(sentence.upper())
print(sentence.lower())






























