# Merged two sorted lists

# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: ListNode | None, list2: ListNode | None
    ) -> ListNode | None:

        # Auxiliary node
        dummy = ListNode()
        actual = dummy

        # Compare the nodes while both lists have elements.
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                actual.next = list1
                list1 = list1.next
            else:
                actual.next = list2
                list2 = list2.next

            actual = actual.next

        # Connect the remaining nodes.
        if list1 is not None:
            actual.next = list1
        else:
            actual.next = list2

        return dummy.next


# This function prints the sorted list in the console.
def print_list(head: ListNode | None):
    actual = head

    while actual is not None:
        print(actual.val, end=" → ")
        actual = actual.next

    print("None")


solution = Solution()

list_1 = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=4)))

list_2 = ListNode(val=1, next=ListNode(val=3, next=ListNode(val=4)))

result = solution.mergeTwoLists(list1=list_1, list2=list_2)

print_list(result)
