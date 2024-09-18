# start
#
# high: float = float(input("what the is high?"))
#
# while  high < 0.4 or high > 2.5:
#     print("input wrong")
#     high: float = float(input("what the is high?"))
from operator import truth

# stop

# start
#
# x: int = int (input(" number 1:"))
# y: int = int (input(" number 2:"))
#
# for i in range ( x , y ,):
#     print(i , end = " ")
# print()

# stop

# # start
# counter: int = 1
# length_pie: float = 3.14
# pie: float = float(input("how much is the pie ?"))
#
# while pie < length_pie and counter < 3:
#     print("correct are you")
#     pie: float = float(input("how much is the pie ?"))
# if pie > length_pie:
#     print("3.14 is pie")
# # stop

# start
while True:
    x: int = int(input("number 1:"))
    y: int = int(input("number 2 :"))
    z: int = int(input("number 3:"))
    aver: int = x + y + z
    c: int = aver // 3
    x1: bool = 0 <= x <= 10
    y2: bool = 10 <= y <= 60
    z3: bool = 60 <= z <= 100

    if x1 and y2 and z3 and c == y and not x == y== z:
        break
    else:
        print("finish")

#stop

#start
