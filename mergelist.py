class ListNode:

    def __init__(self, val=0, next=None):

        self.val = val
        self.next = next

class Solution:

    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:

        # Create a node to act as the start of the merged list
        dummy = ListNode()
        current = dummy

        # splice together the nodes in sorted order
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # If any nodes remain in either list, append them to the merged list
        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        return dummy.next

# Helper function to convert a list to a linked list
def list_to_linked_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print a linked list
def print_linked_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

# Create two sorted linked lists
list1 = list_to_linked_list([1, 2, 4])
list2 = list_to_linked_list([1, 3, 4])

# Merge the lists
solution = Solution()
merged_list = solution.mergeTwoLists(list1, list2)

# Print the merged list
print_linked_list(merged_list)
