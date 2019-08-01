num=0

while num<3:
    print('안녕 거북이',num)
    num=num+1

counts=[1,2,3,4,5]
for count in counts:
    if count<=5:
       print(count,'번째 경기입니다.')
    
print('경기 끝!')


count=1
while count<6:
    print(count, '번째 경기입니다.')
    count=count+1

print('경기 끝!')


name=input('이름이 뭔가요?')
print(name,'안녕!')


name=input('성함이 어떻게 되시나요?')
print('어서오십쇼',name, '님')


password='1234'
while password != '1234':
    print('비밀번호를 다시 입력해주세요')
    input('비밀번호: ')
print('로그인 되었습니다.')

password=''
account=''
while password != '1234' and account != '노현우':
    account=input('아이디: ')
    password=input('비밀번호: ')
    print('아이디 혹은 비밀번호를 다시 입력해주세요')
print('로그인 되었습니다.')

password='1234'
account='노현우'

account=input('아이디:')
#if account == '노현우':
    print('아이디가 확인되었습니다.')
#else:
    while account != '노현우':
        print('아이디를 다시 입력해주세요')
        account=input('아이디:')

password=input('비밀번호:')
#if password == '1234':
    print('로그인 되었습니다')
#else:
    while password != '1234':
        print('비밀번호를 다시 입력해주세요')
        password=input('비밀번호:')

x=1
for count in range(1,21):
    if count != 2*x:
        print(count)
    else:
        count == 2*x
        x=x+1
        continue

while True:
    answer=input('런던,파리,서울 중 영국의 수도는 어디일까요?')
    if answer == '런던':
        print('정답입니다.')
        break
    elif answer == '파리':
        print('파리는 프랑스의 수도입니다.')
    elif answer == '서울':
        print('서울은 대한민국의 수도입니다.')
    else:
        print('보기에서 골라주세요')
        
