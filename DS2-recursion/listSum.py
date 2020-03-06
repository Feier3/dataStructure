def listSum(numList):
    sum = 0
    for i in numList:
        sum = sum + i

    return sum


print(listSum([1, 2, 3, 4, 5]))


#  不能使用while或者for
# 使用小学的内容：连加
# （1+（3+（5+（7+9））））第四个数 + 后面所有数的和
#     （1+（3+（5+16））） 第三个数 + 后面所有数的和
#          （1+（3+21）） 第二个数 + 后面所有数的和
#               （1+24） 第一个数 + 后面所有数的和
#                   25
def listSum2(numList):
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + listSum2(numList[1:])


print(listSum2([1, 2, 3, 4, 5]))

"""
toStr(10,10)+'0'
toStr(1,10)+'0'
'1'
"""


def toStr(n, base):
    str1 = '0123456789ABCDEF'
    if n < base:
        return str1[n]
    else:
        return toStr(n // base, base) + str1[n % base]


print(toStr(100, 10))
print(toStr(1453, 16))


#栈 实现递归

from pythonds.basic.stack import Stack

rStack=Stack()
def toStr():

