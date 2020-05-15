class Node():
    def __init__(self, data):
        self.data_val = data
        self.next_val = None

class SingleLinkedList():
    def __init__(self):
        self.head_val = None

    def print_data_vals(self):
        val = self.head_val
        while val!=None:
            print(val.data_val)
            val = val.next_val
            
    def add_data(self, data):
        if self.head_val == None:
            self.head_val = Node(data)
            return 
        else:
            val = self.head_val
            while val.next_val != None:
                val = val.next_val
            val.next_val = Node(data)
            return
            
    def remove_duplicates_(self):
        unique = []
        val = self.head_val
        unique.append(self.head_val.data_val)
        while val.next_val:
            if val.next_val.data_val not in unique:
                unique.append(val.next_val.data_val)
                val = val.next_val
                
            elif val.next_val.next_val:
                val.next_val = val.next_val.next_val
            else: 
                val.next_val = None



if __name__ == '__main__':
	linked_list = SingleLinkedList()
	elements = [1, 2, 3, 2, 4, 55, 2, 1, 5, 8]
	for i in elements:
	    linked_list.add_data(i)
	linked_list.remove_duplicates()
	linked_list.print_data_vals()
