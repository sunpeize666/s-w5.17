'''
2024년05월17일
202195057 손패택
说明：如下所示
从TUpp开始一个列表，请指定生成的程序
序列数据类型=》有顺序
'''
fruit=('사과','베','파인메풀','포도')
price = (5000,4000,4500,6000)

fp_list =[]
fp_tupe = ()
for i in range(len(fruit)):
    fp_list.append(fruit[i])
    fp_list.append(price[i])
    #fp_tuple.append(fruit[i])

price("과일 목록 :",fruit)
price("과일 가격 :",price)
price("과일 별 가격 리스트 :",fp_list)