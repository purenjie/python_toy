#### 原题目（简单——1）

Given a non-empty, singly linked list with head node `head`, return a middle node of linked list.

If there are two middle nodes, return the second middle node.

**Example 1:**

```
Input: [1,2,3,4,5]
Output: Node 3 from this list (Serialization: [3,4,5])
The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
Note that we returned a ListNode object ans, such that:
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.
```

**Example 2:**

```
Input: [1,2,3,4,5,6]
Output: Node 4 from this list (Serialization: [4,5,6])
Since the list has two middle nodes with values 3 and 4, we return the second one.
```

**Note:**

- The number of nodes in the given list will be between `1` and `100`.

#### 思路

用两个指针 p 和 q ，开始时 p 、q 都指向头结点，用 p 指针遍历链表，len 记录链表长度，q 指针指向 p 指针的二分之一处，index 记录 q 指针的位置。p 指针遍历到最后一个结点时 q 指针指向中间结点。

#### 第一遍解法
```python
# Runtime: 36 ms, faster than 72.12% of Python3
# Memory Usage: 13.1 MB, less than 5.04% of Python3
class Solution:
    def middleNode(self, head):
        p = head
        q = head
        len = index = 1

        while p.next != None:
            p = p.next
            len = len + 1
            while index <= len // 2:
                q = q.next
                index = index + 1
        return q  
```
#### 网上好的解法
```python
# Runtime: 36 ms, faster than 72.12% of Python3
# Memory Usage: 13.1 MB, less than 5.04% of Python3
class Solution(object):
    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
```
#### 自己可以改进的地方
```python

```
#### 最简代码
```python

```
#### 获得的思考

两个代码时间复杂度都是O(N)，空间复杂度都是O(1)

和下面的代码比起来，我的代码看起来比较笨拙，下面的代码思想就卓越在最后寻找的是链表的中间结点，也就是一半的结点位置，每次 slow 结点走 1 个位置 fast 结点走 2 个位置，这样 slow 就是 fast 的一半了。关于奇偶的判断，通过`fast and fast.next != None` 判断。分别用奇偶测试集测试一下，对比验证结果。

没有什么结果是一蹴而就的，找好方法，然后慢慢修改，最后甄于完美。