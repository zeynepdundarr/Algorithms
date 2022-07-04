
class Node: 

    def __init__(self, data):
        self.data =  data
        self.next = None

def array_to_node_list(arr, m):
    node_arr = []
    for i in arr:
        node_arr.append(Node(i))

    for i in range(len(node_arr)):
        if i < (len(node_arr) - 1): 
            node_arr[i].next = node_arr[i+1]
        else:
            node_arr[i].next = None

    
    return find_m_to_end(node_arr[0], m)

def print_nodes(node_arr, m):
    node = node_arr[0]

    for _ in range(m-1):
        print("Node:", node.data)
        print("Node.next :", node_arr[0].next)
        node = node_arr[0].next

def find_m_to_end(head_ptr, m):

   
    # init mBehind and curr pointer
    m_ptr = None
    curr_ptr = head_ptr

    # check if m>n 
    # move curr pointer forward
    # if m is bigger than n, curr_ptr.next should be empty, so return m_ptr ads null
    for _ in range(m-1):
        if (curr_ptr.next):
            curr_ptr = curr_ptr.next
        else:
            return m_ptr
            
    m_ptr = head_ptr

    while(curr_ptr.next):
        m_ptr = m_ptr.next
        curr_ptr = curr_ptr.next
    return m_ptr.data


    # iterate until you find the curr->next = NULL
     

if __name__ == "__main__":

    a = int(input())
    b = input()
    b_arr = list(map(int, b.split()))

    res = array_to_node_list(b_arr,a) 

    if res:
        print(res)
    else:
        print("NIL")

