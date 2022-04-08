class ListNode():
    def __init__(self, data = 0, next = None):
        self.data = data
        self.next = next

def delete_nodes(list):
    print("Before deletion")
    for i in range(len(list)):
        print(list[i].data)
        if list[i].next is not None:
            print(list[i].next.data)
        else:
            print(list[i].next)
        print("")

    for i in range(len(list)):
        if list[i].next == None:
            if list[i].data == list[i-1].data:
                list.pop(i-1)
                break
        elif list[i].data == list[i].next.data:
            list[i].next = list[i].next.next
            list.pop(i+1)
            
    
    
    print("After deletion")
    for i in range(len(list)):
        print(list[i].data)
        if list[i].next is not None:
            print(list[i].next.data)
        else:
            print(list[i].next)
        print("")


node_list = []
# for i in range(8):
#     node_list.append(ListNode(i, None))
#     if i > 0:
#         node_list[i-1].next = node_list[i]

node_list.append(ListNode(3, None))
node_list.append(ListNode(3, None))
node_list[0].next = node_list[1]
node_list.append(ListNode(4, None))
node_list[1].next = node_list[2]
node_list.append(ListNode(5, None))
node_list[2].next = node_list[3]
node_list.append(ListNode(5, None))
node_list[3].next = node_list[4]
node_list.append(ListNode(5, None))
node_list[4].next = node_list[5]


delete_nodes(node_list)
