from linked_list_node import Node
from linked_list import LinkedList

def remove_nth_last_node(linked_list, n):
    left = linked_list.head
    right = linked_list.head


    for i in range(n):
      right = right.next

    if right is None:
       linked_list.head = left.next
       return

    while right and right.next:
        right = right.next
        left = left.next
    
    left.next = left.next.next
        
test = [69, 8, 49, 106, 116, 112]

linked_list = LinkedList()
linked_list.create_linked_list(test)
print("primeira")
print(linked_list)

print("secunda")
remove_nth_last_node(linked_list, 6)
print(linked_list)



