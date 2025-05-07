# -*- coding: utf-8 -*-
"""
Created on Wed May  7 22:17:51 2025
@author: bahob
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        # Bağlı listeyi yazdırmak için
        result = []
        current = self
        while current:
            result.append(str(current.val))
            current = current.next
        return " -> ".join(result)

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        current.next = list1 if list1 else list2
        return dummy.next

# Test için yardımcı fonksiyon
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# === Test örneği ===
if __name__ == "__main__":
    list1 = create_linked_list([1, 3, 5])
    list2 = create_linked_list([2, 4, 6])

    sol = Solution()
    merged = sol.mergeTwoLists(list1, list2)
    print("Birleştirilmiş Liste:")
    print(merged)  # Beklenen çıktı: 1 -> 2 -> 3 -> 4 -> 5 -> 6
