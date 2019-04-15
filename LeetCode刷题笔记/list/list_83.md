#### 原题目

Given a sorted linked list, delete all duplicates such that each element appear only *once*.

**Example 1:**

```
Input: 1->1->2
Output: 1->2
```

**Example 2:**

```
Input: 1->1->2->3->3
Output: 1->2->3
```

#### 思路

遍历链表，只要前一个结点的值和后一个结点的值相同，就删除前一个结点。头结点指针需要单独判断，指向第一个和后面结点值不同（或者 None）的结点

#### 第一遍解法
```python
# Runtime: 48 ms, faster than 84.01% of Python3
# Memory Usage: 13.1 MB, less than 5.26% of Python3
class Solution:
    def deleteDuplicates(self, head):
        if not head or not head.next: # 空链表或只有一个结点
            return head
        else:
            node = head
            while node.next:
                if node.val == node.next.val:
                    node.next = node.next.next
                else:
                    node = node.next
            return head
```
#### 网上好的解法
```java
public ListNode deleteDuplicates(ListNode head) {
        if(head == null || head.next == null)return head;
        head.next = deleteDuplicates(head.next);
        return head.val == head.next.val ? head.next : head;
}
```
#### 自己可以改进的地方
if else 可以用 while 语句代替

#### 最简代码
```python
class Solution:
    def deleteDuplicates(self, head):
        while head and head.next: # 不是空链表或者只有一个结点的链表
            node = head
            while node.next:
                if node.val == node.next.val:
                    node.next = node.next.next
                else:
                    node = node.next
            return head
        return head
```
#### 获得的思考

递归的思想，如果一个不重复链表在表头添加一个结点，结点值和头结点值相同时不添加，不同时添加为表头结点。反过来写，如果表头结点和下一个结点值相同，表头指针指向下一个结点，值不同的时候表头指针不变。

`head.next = deleteDuplicates(head.next)` 确保从 `head.next` 结点到 `NULL` 结点的链表是不重复的链表，因此只需要判断头结点是指向`head` 还是 `head.next`。