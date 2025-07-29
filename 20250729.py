'''
#문제 3)
number1 = input('첫번째 숫자를 입력하세요 : ')
number2 = input('두번째 숫자를 입력하세요 : ')
number3 = input('세번째 숫자를 입력하세요 : ')
number1 = int(number1)
number2 = int(number2)
number3 = int(number3)
number4 = number1+number2+number3
print("총합은 ", number4)
'''
'''
#문제 4)

radius = input('반지름을 입력하세요 : ')
radius = int(radius)

area = radius * radius * 3.14
girth = radius * 2 * 3.14

print('원의 넓이는 : ', area)
print('원의 둘레길이는 : {0:.1f}'.format(girth))
'''
'''
#문제 5)
upper = input('윗변을 입력하세요 : ')
lower = input('윗변을 입력하세요 : ')
high = input('높이를 입력하세요 : ')

upper = int(upper)
lower = int(lower)
high = int(high)

area = (upper+lower)*high/2
print('사다리꼴의 넓이는 ',area)
'''
'''
nut1 = '밤양갱'
nut2 = "달디단 밤양갱"
nut3 ="""달디달고 달디달고,
달디단 밤양갱 밤양갱
내가 먹고 싶었던 건,
달디단, 밤양갱, 밤양갱이야"""
'''
'''
sweat = '달디'
sweat2 = sweat*10
number = 255
message = sweat2+' '+'단 밤양갱'+str(number)+'개'
print(message)
'''
'''
line = "="*20
header = "밤양갱 대박 세일"
footer = "놓치지 마세요!"
message = line + "\n" + header + "\n" +line + "\n" + footer + "\n" + line
print(message)
'''
'''
#문제 1)
yourid = input('아이디 : ')
password = input('비밀번호 : ')

message = '당신의 아이디는 ' + '\"' + yourid + '\"' + '이며, 비밀번호는 ' + '\"' + password + '\"' + '입니다.'

print(message)
'''


'''
word = "문자열과 인덱스"

print(word[0])
print(word[3])
print(word[5])
print(word[-1])
'''
'''
snack = "떡볶이 순대 튀김"

setmenu = snack[0] + snack[4] + snack[7]

print(setmenu)
'''
'''
word = "부분만 바꾸려고 하면 에러가 나요"
print(word)

#word[0] = "수"
word = "새로 만들어 덮어쓰기는 가능"
print(word)
'''
'''
word = "슬라이싱으로 다양하게 문자를 잘라봅시다"

print(word[0:4])
print(word[7:9])
print(word[5:])
print(word[:12])
print(word[::3])
print(word[::-3])
'''
'''
song = "록도닳 고르마 이산두백 과물해동"

reverse = song[::-1]

print(reverse)
'''
'''
song = "동해물과 백두산이 마르고 닳도록"
part_song = song[:4]
print(part_song)
part_song = song[5:13]
print(part_song)
part_song = song[14:]
print(part_song)
'''
'''
#문제 1)
word = input('문자열을 입력하세요 : ')
print(word[1::2])
'''
'''
#문제 2)
word = input('주민번호를 입력하세요(-포함): ')
print(word[2:6])
'''
'''
#문제 3)
word = "타파에벅서이썬스나짱만스"
print(word[11]+word[0]+word[3]+word[7]+word[2]+word[4]+' '+word[10]+word[8])
'''
'''
#문제 4-1)
song = '동해물과 백두산이 마르고 닳도록 하느님이 보우하사 우리나라 만세. 무궁화 삼천리 화려 강산 대한 사람, 대한으로 길이 보전하세.'
print(song[33]+song[34])
print(song[68]+song[69])
'''

#문제 4-2)
song = '동해물과 백두산이 마르고 닳도록 하느님이 보우하사 우리나라 만세. 무궁화 삼천리 화려 강산 대한 사람, 대한으로 길이 보전하세.'









