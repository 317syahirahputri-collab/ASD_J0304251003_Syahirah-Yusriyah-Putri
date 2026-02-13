#=====================================================
#praktikum 3:  Linked List 
#Latihan 1: delete node
#=====================================================

class node:
    def __init__(self, data):
        self.data =	data
        self.next =	None

class linked_list:
    def __init__(self):
        self.head = None
        self.tail = None #tambahkan pointer tail

    def insert_at_end(self, data): 
        new_node = node(data) 
        if not self.head: 
            self.head = new_node 
            self.tail = new_node  
        else:
            self.tail.next = new_node  
            self.tail = new_node  

    def display(self): 
        temp = self.head 
        while temp: 
            print(temp.data, end=" -> ") 
            temp = temp.next 
        print("null")

#menghapus node dengan nilai tertentu
    def	delete_node(self,	key):	
        temp = self.head	

         # Jika head node sendiri yang akan dihapus
        if	temp and temp.data	==	key:	
            self.head =	temp.next	
            temp = None	
            return	
        # Cari node yang akan dihapus, simpan prev node
        prev = None	
        while temp and	temp.data!=	key:	
            prev = temp	
            temp =	temp.next
        # Jika key tidak ditemukan dalam linked list        	
        if	temp is	None:	
            return	
        prev.next =	temp.next	
        temp = None

ll = linked_list()
print("Menambahkan beberapa node ke linked list:")
ll.insert_at_end(3)
ll.insert_at_end(5)
ll.insert_at_end(13)
ll.insert_at_end(2)
ll.display()
#menghapus node dengan nilai 13 dan 3
ll.delete_node(13)
ll.delete_node(3)
ll.insert_at_end(8)
ll.insert_at_end(21)
print("Linked list setelah menghapus beberapa node:")
ll.display()