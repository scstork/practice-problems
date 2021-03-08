# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # to save time (and add space), save each node in a dict
        # this enables us to do this problem with only one pass through the list
        nodes = {}
        index = 0
        while head != None:
            nodes[index] = head
            head = head.next
            index += 1
        if n > index:
            raise ValueError(f"Index {n} greater than list length, {index + 1}")
        # "remove" the nth node from the end
        nth_from_end = index- n
        head = nodes.get(0)
        if nth_from_end == 0:
            head = nodes.get(1)
        elif nth_from_end == index - 1:
            nodes.get(nth_from_end - 1).next = None
        else:
            nodes.get(nth_from_end - 1).next = nodes.get(nth_from_end + 1)
        return head