#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

if __name__ == "__main__":
    solver = Solution()
    head1 = [1,2,3,4,5]
    output1 = solver.reverseList(head=head1)
    print(output1)  
    
    solver = Solution()
    head2 = [1,2]
    output2 = solver.reverseList(head=head2)
    print(output2)  

    solver = Solution()
    head3 = []
    output3 = solver.reverseList(head=head3)
    print(output3)  
