class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def append(self, data):
        
        if not self.head:
            self.head = Node(data)
            self.tail = self.head
        else:
            new_node = Node(data)
            self.tail.next = new_node
            self.tail = new_node
       
        
    def get_nth_last(self, n):
        if not self.head:
            return('NIL')
        
        node_arr = []
        
        curr = self.head
        node_arr.append(curr.data)
        
        while curr.next != None:
            curr = curr.next
            node_arr.append(curr.data)
        
    
        n *=-1
            
        return(node_arr[n])

        

if __name__ == '__main__':
    
    n = int(input())
    
    nodes = list(map(int, input().split()))
    if n > len(nodes):
        print("NIL")
    else:
        ll = LinkedList()
        for node in nodes:
            ll.append(node)

        print(ll.get_nth_last(n))