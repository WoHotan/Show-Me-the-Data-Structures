class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_list = []
        while cur_head:
            out_list.append(str(cur_head.value))
            cur_head = cur_head.next
        return "->".join(out_list)


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    # Your Solution Here
    s_llist = set()
    union_llist = LinkedList()
    node1 = llist_1.head
    while node1:
        s_llist.add(node1.value)
        node1 = node1.next
    node2 = llist_2.head
    while node2:
        s_llist.add(node2.value)
        node2 = node2.next
    for value in s_llist:
        union_llist.append(value)
    return union_llist

def intersection(llist_1, llist_2):
    # Your Solution Here
    intersection_llist = LinkedList()
    s_llist1 = set()
    s_llist2 = set()
    node1 = llist_1.head
    while node1:
        s_llist1.add(node1.value)
        node1 = node1.next
    
    node2 = llist_2.head
    while node2:
        s_llist2.add(node2.value)
        node2 = node2.next
    intersection = s_llist1 & s_llist2
    for value in intersection:
        intersection_llist.append(value)
    return intersection_llist

print('# Test case 1')

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))        # return a linked list, elements are linked_list_1 ∪ linked_list_2.
print (intersection(linked_list_1,linked_list_2)) # return a linked list, elements are linkded_list_1 ∩ linked_linst_2.

print('\n# Test case 2')

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [9,15, 5, 23, 8]
element_2 = [8, 2, 5, 11, 8]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))        # return a linked list, elements are linked_list_3 ∪ linked_list_4.
print (intersection(linked_list_3,linked_list_4)) # return a linked list, elements are linkded_list_3 ∩ linked_linst_4

print('\n# Test case 3')

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = []
element_2 = [1]

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print (union(linked_list_5,linked_list_6))        # return a linked list, elements are linked_list_5 ∪ linked_list_6.
print (intersection(linked_list_5,linked_list_6)) # return a linked list, elements are linkded_list_5 ∩ linked_linst_6.
