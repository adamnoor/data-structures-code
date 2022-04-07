class ListNode():
    def __init__(self, data = 0, next = None):
        self.data = data
        self.next = next

def delete_node(node, node_list):
    print(node.data)
    node.data = node.next.data
    node.next = node.next.next
    print (node.data)

node_list = []
for i in range(8):
    node_list.append(ListNode(i, None))
    if i > 0:
        node_list[i-1].next = node_list[i]

node = node_list[5]
delete_node(node, node_list)
