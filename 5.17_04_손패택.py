'''
2024년05월17일
202195057 손패택
说明：制作彩票号码
生成彩票号码，按升序排列。
6个1到45之间的号码
'''
import random

print("로또 번호 생성 - 리스트")

lotto=list()

i = 0
while True :
    lotto.append(random.randint(1,45))
    i = i + 1
    if len(lotto)==6 :
        break
    print("이번주 로뜨 번호 : ",sorted(lotto))

    print()

    print("로뜨 번호 생성 - 세트")

    lotto = set()

    i = 0
    while True :
        lotto.add(random.randint(1,45))
        i = i + 1
        if len(lotto) == 6:
            break
        print ("이번주 로뜨 번호 : ",sorted(lotto))

