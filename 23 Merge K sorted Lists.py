# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        head = curr = ListNode(0)
        pq = []

        # push the head of each list
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(pq, (node.val, i, node))

        while pq:
            _, i, node = heapq.heappop(pq)

            curr.next = node
            curr = curr.next

            if node.next:
                heapq.heappush(pq, (node.next.val, i, node.next))

        return head.next