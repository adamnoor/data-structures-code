class ListNode():
    def __init__(self, data = 0, next = None):
        self.data = data
        self.next = next

def even_odd_nodes(list):
    for i in range(len(list)):
        if list[i].next is not None:
            if list[i].next.next is not None:
                list[i].next = list[i].next.next
            else:
                if i%2 == 0:
                    list[i].next = list[~i]
                else:
                    list[i].next = None
    
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

even_odd_nodes(node_list)
