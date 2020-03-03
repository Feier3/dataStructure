"""对比生成列表的四种方法的效率"""


def test1():
    l = []
    for i in range(1000):
        l = l + [i]


def test2():
    l = []
    for i in range(1000):
        l.append(i)


def test3():
    l = [i for i in range(1000)]


def test4():
    l = list(range(1000))


from timeit import Timer

"""
timeit 模块是被设计成在一个持续稳定的环境中，竟可能使用与计算机操作系统相似的计时
机制，让python的开发者实现跨平台运行时间的测量
"""

# t1 = Timer("test1()", "from __main__ import test1")
# print("concat", t1.timeit(number=10000), "milliseconds")
#
# t2 = Timer("test2()", "from __main__ import test2")
# print("concat", t2.timeit(number=10000), "milliseconds")
#
# t3 = Timer("test3()", "from __main__ import test3")
# print("concat", t3.timeit(number=10000), "milliseconds")
#
# t4 = Timer("test4()", "from __main__ import test4")
# print("concat", t4.timeit(number=10000), "milliseconds")


pop_zero = Timer("x.pop(0)", "from __main__ import x")
pop_end = Timer("x.pop()", "from __main__ import x")
# x=list(range(2000000))
# print(pop_zero.timeit(number=1000))
#
# x=list(range(2000000))
# print(pop_end.timeit(number=1000))

# for i in range(1000000, 100000001, 1000000):
#     x = list(range(i))
#     pt = pop_end.timeit(number=1000)
#     x = list(range(i))
#     pz = pop_zero.timeit(number=1000)
#     print("%15.5f,%15.5f" % (pz, pt))


"""
对比列表和字典的包含操作的效率。
"""

import timeit
import random

for i in range(10000, 1000001, 20000):
    t = timeit.Timer("random.randrange(%d) in x" % i,
                     "from __main__ import random,x")

    x = list(range(i))
    lst_time = t.timeit(number=1000)

    x = {j: None for j in range(i)}
    d_time = t.timeit(number=1000)

    print("%d,%10.3f,%10.3f" % (i, lst_time, d_time))


