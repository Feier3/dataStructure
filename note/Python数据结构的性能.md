### 列表操作时间复杂度

|       操作       | 时间效率(大O表示法) |
| :--------------: | :-----------------: |
|     idnex []     |        O(1)         |
| index assignment |        O(1)         |
|      append      |        O(1)         |
|      pop()       |        O(1)         |
|      pop(i)      |        O(n)         |
|  insert(i,item)  |        O(n)         |
|   del operator   |        O(n)         |
|    iteration     |        O(n)         |
|   contains(in)   |        O(n)         |
| get slice [x:y]  |        O(k)         |
|    del slice     |        O(n)         |
|    set slice     |       O(n+k)        |
|     reverse      |        O(n)         |
|   concatenate    |        O(k)         |
|       sort       |     O(n log n)      |
|     multiply     |        O(nk)        |

### 字典操作时间复杂度

|          操作           | 时间效率(大O表示法) |
| :---------------------: | :-----------------: |
|       copy(复制)        |        O(n)         |
|     get item(访问)      |        O(1)         |
|     set item(赋值)      |        O(1)         |
|    delete item(删除)    |        O(1)         |
| contains(in)  (包含 in) |        O(1)         |
|     iteration(迭代)     |        O(n)         |

Python数据结构性能速查：https://wiki.python.org/moin/TimeComplexity

