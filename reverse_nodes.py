class ListNode():
    def __init__(self, data = 0, next = None):
        self.data = data
        self.next = next

def reverse_nodes(list):
    print("Before reverse")
    for i in range(len(list)):
        print(list[i].data)
        if list[i].next is not None:
            print(list[i].next.data)
        else:
            print(list[i].next)
        print("")

    count = len(list)-1

    while count > -1:
        if count == 0:
            list[count].next = None
        else:
            list[count].next = list[count-1]
        

        
        count -= 1
    
    print("After reverse")
    for i in range(len(list)):
        print(list[i].data)
        if list[i].next is not None:
            print(list[i].next.data)
        else:
            print(list[i].next)
        print("")


node_list = []
for i in range(8):
    node_list.append(ListNode(i, None))
    if i > 0:
        node_list[i-1].next = node_list[i]

reverse_nodes(node_list)
