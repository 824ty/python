# coding:utf-8
for a in range(5):
    print(a +1)
    print("こんにちは")

for a in "Hallo":        #for文
    print(a)
    

total = 0                #while文
a = 1
while total <= 50:
    total = total + a
    a = a + 1
print(total)

for a in range(1, 10+1):
    if a <= 5:
        print("小さいです")
    else:
        print("大きいです")


#2の倍数は「〇」
#3の倍数は「×」
#2の倍数且つ3の倍数の時は「△」

for a in range(1, 10 + 1):
    print(a)
    if a % 2 == 0 :
        print("〇")
    if a % 3 == 0 :
        print("×")
    if (a % 2 == 0) and (a % 3 == 0):
        print("△")

def tashizan(a,b):
    total = 0
    for i in range(a, b + 1):
        total = total + i
    return total

c = tashizan(1, 5)
print(c)
