score=60

if 80< score <=100:
    print('A학점입니다')
elif 60< score <= 80:
    print('B학점입니다')
elif 40< score <= 60:
    print('C학점입니다')
else:
    print('F학점입니다')





ages=[22,23,17,21,38,9,10,5]

for age in ages:
    if age>=20:
        print('티켓값은 8000원입니다')
    elif 10<= age <20:
        print('티켓값은 5000원입니다')
    else:
        print('티켓값은 2500원입니다')
        
total_price=0
ages=[22,23,17,21,38,9,10,5]

for age in ages:
    if age>=20:
        total_price=total_price +8000
    elif 10<= age <20:
        total_price=total_price +5000
    else:
        total_price=total_price +2500

print('총 금액은', total_price, '원입니다.')


games=12
points=22

if games>=10 and points >=20:
    print('MVP가 되셨습니다')


print(True and False)
print(True and True)
print(True or False)
print(False or False)
print(not True)
print(not False)


ps4_titles=[['데이즈곤','아포칼립스','fps'],['갓오브워','오픈월드','고티'],['용과같이','오픈월드','야쿠자']]
for ps4 in ps4_titles:
    if ps4[1]== '오픈월드'or ps4[2]== '야쿠자':
        print(ps4[0], '은 고객님 취향의 게임입니다')
       

    
