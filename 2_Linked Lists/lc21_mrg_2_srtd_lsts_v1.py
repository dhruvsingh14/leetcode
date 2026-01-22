# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        if list1:
            curr.next = list1
        else:
            curr.next = list2 

        return dummy.next



if __name__ == "__main__":
    solver = Solution()
    list11 = [1,2,4]
    list12 = [1,3,4]
    output1 = solver.mergeTwoLists(list1=list11, list2=list12)
    print(output1)  
    
    solver = Solution()
    list21 = []
    list22 = []
    output1 = solver.mergeTwoLists(list1=list21, list2=list22)
    print(output1)  

    solver = Solution()
    list31 = []
    list32 = [0]
    output1 = solver.mergeTwoLists(list1=list31, list2=list32)
    print(output1)  