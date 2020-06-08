class Node():
    def __init__(self, data):
        self.data_val = data
        self.next_val = None

class SingleLinkedList():
    def __init__(self):
        self.head_val = None
        self.length = 0
        
    def print_data_vals(self):
        val = self.head_val
        while val!=None:
            print(val.data_val)
            val = val.next_val
            
    def add_data(self, data):
        if self.head_val == None:
            self.head_val = Node(data)
            self.length = self.length + 1
            return 
        else:
            val = self.head_val
            while val.next_val != None:
                val = val.next_val
            val.next_val = Node(data)
            self.length = self.length + 1
            return

    def delete_middle_node(self):
        mid_index = self.length // 2
        val = self.head_val
        i = 0
        while i != mid_index-1:
            val = val.next_val
            i = i+1
        val.next_val = val.next_val.next_val
        return 
