'''
2024년05월17일
202195057 손패택
'''
num = set()
num1 = (2,1,3)
print("num1 : ",num1)

num2 =set[1,2,3,1,2]
print("num2 : ",num2)


text1 = set("abcda")
print("text1 : ",text1)

num3 = (2,1,3)

if 1 in num3 :
    print("1이 세트에 있습니다.")

    num4=(9,1,2,5,4,1,3,7,6,5,4,6,7,8,1)
    print("num4 : ",num4)

    for num in num4 :
        print(num,end=' ')

print()

num4.add(100)
print("num4(100추가):",num4)

for num in sorted(num4):
 print(num,end='')

print()

num4.remove(100)
print("num4(num삭재) : ",num4)

print("num4의 길이:",len(num4))

print("num4에서 최대값 :",max(num4))
print("num4에서 최소값 :",max(num4))
print("num4의 합게 :",sum(num4))

A = (1,2,3)
B = (3,4,5)

print("A | B =",A | B)

print("A | B =",A.union(B))

print("A & B =",A&B)

print("A & B =",A.intersection(B))

print("A - B =",A.defrense(B))

print("A ^ B =",A ^ B)