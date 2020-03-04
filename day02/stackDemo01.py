# 栈抽象数据类型的底层实现采用什么？ list
# 确定列表的哪一端是顶部，然后使用append和pop来实现操作

# 假设列表的尾部是栈的顶部元素，

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def peek(self):
        return self.items[-1]

    def pop(self):
        self.pop()

    def size(self):
        return len(self.items)


from pythonds.basic.stack import Stack

# s=Stack()
# print(s.isEmpty())
# s.push(1)
# s.push("fdsa")
#
# print(s.peek())
# s.push(True)
#
# print(s.size())
# print(s.isEmpty())
#
# s.push(10.9)
# print(s.pop())
# print(s.pop())


# ()匹配
from pythonds.basic.stack import Stack


def parChecker(symbolString):
    s = Stack()
    flag = True
    index = 0

    while index < len(symbolString) and flag:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                flag = False
            else:
                s.pop()

        index = index + 1

    if flag and s.isEmpty():
        return True
    else:
        return False


print(parChecker("(())"))
print(parChecker("((())"))


# 有效的括号

def isValid(s):
    # 跟踪开括号的堆栈
    stack = []

    # 用于跟踪映射的散列映射，这使代码非常简洁
    # 也使添加更多类型的括号更容易
    mapping = {")": "(", "}": "{", "]": "["}

    for char in s:

        # 如果字符是右括号
        if char in mapping:

            # 如果栈不是空的，弹出最上面的一个元素
            top_element = stack.pop() if stack else "#"

            # 如果散列中映射的左括号和弹出的左括号不匹配，返回False
            if mapping[char] != top_element:
                return False
        # 如果字符是左括号，添加到栈
        else:
            stack.append(char)

    return not stack

print(isValid("{{}}[((()))]"))

 

# 解法二
from pythonds.basic.stack import Stack

def parChecker(symbolString):
    s = Stack()
    flag = True
    index = 0

    while index < len(symbolString) and flag:
        symbol = symbolString[index]

        if symbol in "([{":     # [{
            s.push(symbol)
        else:
            if s.isEmpty():
                flag = False
            else:
                top = s.pop()   # {
                start = '([{'  # 2
                end = ')]}'   # 1

                if not start.index(top) == end.index(symbol):
                    flag = False
        index = index + 1


    if flag and s.isEmpty():
        return True
    else:
        return False

print(parChecker('{[()]}'))
print(parChecker('{{([][])}()}'))
print(parChecker('[{()]'))