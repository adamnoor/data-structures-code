import random

class ListNode():
    def __init__(self, data = 0, next = None):
        self.data = data
        self.next = next

def search_list(list, key):
    while list and list.data != key:
        list = list.next
    return list

def insert_after(node, new_node):
    new_node.next = node.next
    node.next = new_node

def delete_after(node):
    node.next = node.next.next

def sort_linked_lists(list1, list2):
    
    l1 = []
    l2 = []
    n1 = list1
    n2 = list2

    n1.sort()
    n2.sort()

    for i in range(0, len(n1)):
        l1.append(ListNode(n1[i], next=None))
        if len(l1) != 1:
            l1[i-1].next = l1[i]

    for i in range(0, len(n2)):
        l2.append(ListNode(n2[i], next=None))
        if len(l2) != 1:
            l2[i-1].next = l2[i]

    print("This is L1")
    for element in l1:
        print("data is: " + str(element.data))
        print("the address is: " + str(element))
        if element.next is not None:
            print("next nodes data is: " + str(element.next.data))
            print("next nodes address is " + str(element.next))
        else:
            print("next node is None")

    print("This is L2")

    for element in l2:
        print("data is: " + str(element.data))
        if element.next is not None:
            print("next nodes data is: " + str(element.next.data))
            print("next nodes address is " + str(element.next))
        else:
            print("next node is None")

    i = 0
    j = 0

    while i < len(l1) and j < len(l2):

        if l1[i].data < l2[j].data: 
            if l1[i].next is None:
                l1[i].next = l2[j]
            elif l1[i].next.data > l2[j].data:
                l1[i].next = l2[j]
            i += 1
        elif l1[i].data >= l2[j].data:
            if l2[j].next is None:
                l2[j].next = l1[i] 
            elif l2[j].next.data > l1[i].data:
                l2[j].next = l1[i]
            j += 1 
        else:
            print ("If you are seeing this something went wrong")

    print("This is L1 after sorting")
    for element in l1:
        print("data is: " + str(element.data))
        if element.next is not None:
            print("next nodes data is: " + str(element.next.data))
            print("next nodes address is " + str(element.next))
        else:
            print("next node is None")

    print("This is L2 after sorting")

    for element in l2:
        print("data is: " + str(element.data))
        if element.next is not None:
            print("next nodes data is: " + str(element.next.data))
            print("next nodes address is " + str(element.next))
        else:
            print("next node is None")



#sort_linked_lists([2, 4, 6], [1, 3, 5])
# sort_linked_lists([2], [3, 1, 5])
sort_linked_lists([], [1, 2, 3])


