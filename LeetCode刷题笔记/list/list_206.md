#### 原题目(简单——1)

Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?

#### 思路

用两个指针 head 和 rear 分别指向第一个和最后一个元素，然后交换两个指针的值，head 指针向后移动，rear 指针向前移动，当 head 指针和 rear 指针相同时停止。

#### 第一遍解法

```

```

#### 网上好的解法

```python
# 三个指针顺时转动 C（current）、N（next）、P（previous）
# N=C.next C->P P=C C=N 
# C=None 时所有元素遍历完，prev 指向原序列最后一个元素 也是 新序列第一个元素

# 迭代
class Solution:
def reverseList(self, head):
prev = None
while head:
curr = head
head = head.next
curr.next = prev
prev = curr
return prev

# 递归
def reverseList(self, head, pre = None):
if not head: 
return pre
cur, head.next = head.next, pre
return self.reverseList(cur, head)
```

#### 自己可以改进的地方

```

```

#### 最简代码

```python
# 迭代
# Runtime: 40 ms, faster than 91.21% of Python3
# Memory Usage: 14.5 MB, less than 31.44% of Python3
class Solution:
def reverseList(self, head):
pre = None
while head:
head.next, pre, head = pre, head, head.next
return pre

# 递归
# Runtime: 44 ms, faster than 66.99% of Python3
# Memory Usage: 20.4 MB, less than 5.22% of Python3
class Solution:
def reverseList(self, head, pre=None):
if not head:
return pre
n = head.next
head.next = pre
return self.reverseList(n, head)
```

#### 获得的思考

![](https://i.loli.net/2019/04/11/5caf3ec9d9140.png)

通用解法：用三个变量指示三个地方，依次轮转

python 特解：元组拆包，两个变量可以指示三个地方

递归空间复杂度较高，可以不使用递归就不适用