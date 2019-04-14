#### 原题目(简单——1)

Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

Given linked list -- head = [4,5,1,9], which looks like following:

![img](https://assets.leetcode.com/uploads/2018/12/28/237_example.png)

**Example 1:**

```
Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.
```

**Example 2:**

```
Input: head = [4,5,1,9], node = 1
Output: [4,5,9]
Explanation: You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 after calling your function.
```

**Note:**

- The linked list will have at least two elements.
- All of the nodes' values will be unique.
- The given node will not be the tail and it will always be a valid node of the linked list.
- Do not return anything from your function.

#### 思路

若删除结点为头结点，头结点变为下一个结点。否则遍历链表，遍历到指定结点时将该结点的值改为下一个结点的值，该节点的下一个结点改为下一个结点的下一个结点。

#### 第一遍解法
```python
class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # 是头结点
        if node.val == head.val:
            head = head.next
        else:
            curr = head
            while curr.val != node.val:
                curr = curr.next
            curr.val = curr.next.val
            curr.next = curr.next.next
        return  
```
#### 网上好的解法
```python
class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
        return 
```
#### 自己可以改进的地方
```python

```
#### 最简代码
```python
class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
        return 
```
#### 获得的思考

这个题真的醉了

我一直在想为什么不给头结点，不给头结点怎么遍历链表？没想到直接用给定结点用我的思路的方法就可以做出来。确实按照题目给定的条件，只要待删除结点不是尾结点，直接交换两个结点的值并且删除后一个结点即可。

> 删除结点不是尾结点，可以采用删除后一个结点的方法