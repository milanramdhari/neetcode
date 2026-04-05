# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists:
            return None
        
        def merge_two_sorted_list(list1, list2):
            res = ListNode(0)
            head = res
            
            while (list1 is not None and list2 is not None):
                if (list1.val < list2.val):
                    head.next = list1
                    list1 = list1.next
                else:
                    head.next = list2
                    list2 = list2.next
                head = head.next
            
            if (list1):
                head.next = list1
            else:
                head.next = list2
            
            return res.next

        while(len(lists) > 1):
            list1 = lists.pop()
            list2 = lists.pop()
            lists.append(merge_two_sorted_list(list1, list2))
        
        return lists[0]
        