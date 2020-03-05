"""
乱序字符串是指一个字符串知识另一字符串的重新排序
前提：字符串由26个小字母集合组成，长度相同
比如：python typhon
定义一个函数，用来判断两个字符串是否为乱序字符串，返回结果为布尔值
"""


# 计数和比较法
def solutions1(str1, str2):
    if len(str1) != len(str2):
        return False
    s1_list = list(map(lambda x: {x: str1.count(x)}, str1))
    s2_list = list(map(lambda y: {y: str2.count(y)}, str2))
    for i in s1_list:
        if i not in s2_list:
            return False
    return True


# 检查s1中的每一个字符是否出现在s2中，如果均可检测到，则为乱序。
# 可在检测过程中将出现在s2中的对应字符删除
def solutions2(s1, s2):
    alist = list(s2)
    pos1 = 0
    flag = True

    while flag and pos1 < len(s1):
        pos2 = 0
        found = False
        while pos2 < len(s2) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 + 1
        if found:
            alist[pos2] = None
            pos1 = pos1 + 1
        else:
            flag = False
    return flag


# 排序和比较
# 可以按照从a-z排列每一个字符串，如果两个字符串相同，则两个字符串为乱序字符串
def solutions3(str1, str2):
    if sorted(str1) == sorted(str2):
        return True
    else:
        return False


print(solutions3('aaad', 'ddda'))
