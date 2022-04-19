class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not (head and head.next):
            return False
        slow = head
        fast = head.next
        while fast.next and fast.next.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        return False