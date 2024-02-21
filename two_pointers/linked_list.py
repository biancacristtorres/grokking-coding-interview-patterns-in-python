from linked_list_node import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_node_at_head(self, node):
        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = node

    def insert_node_at_end(self,node):
        if not self.head:
            self.head = node
            return

        cursor = self.head

        while cursor.next:
            cursor = cursor.next
        
        cursor.next = node    


    def __str__(self):
        result = ""
        temp = self.head
        while temp:
            result += str(temp.data)
            temp = temp.next
            if temp:
                result += ", "
        result += ""
        return result
    
    def create_linked_list(self, lst):
        for x in lst:
            new_node = Node(x)
            self.insert_node_at_end(new_node)


