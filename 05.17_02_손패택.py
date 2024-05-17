'''
2024년05월17일
202195057 손패택
频繁的个数将单独的保存在列表中。已经找到的数字不用再找到个数了。
'''
num = (4,1,3,4,6,5,7,9,5,1,4,6,0,1,2,7,8,9)
print("생성된 튜플 : ",num)

for i in range(len(num)):
    print(num[i],"의 개수 : ",num.count(num[i]))

print()
print("중복 제거하고 개수 찾기")

num_list = []

#反复长度
#判断列表中是否有数字
#如果列表中有数字的话
#1.合格
#2.没有的话
#打印个数后添加到列表中
for i in range(len(num)):
    if num[i] in num_list :
        continue
    else :
        print(num[i], "의 개수 : ",num.count(num[i]))
        num_list.append(num[i])

        print()

        print("없으면...")

        for i in range(len(num)):
            if num[i] not in num_list:
                print(num[i],"의 개수 :",num.count(num[i]))
                num_list.append(num[i])