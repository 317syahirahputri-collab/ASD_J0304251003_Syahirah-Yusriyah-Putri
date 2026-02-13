#=====================================================
#praktikum 3:  Linked List 
#Latihan 1: Implementasi fungsi pencarian pada node tertentu
#=====================================================

class node:
    def __init__(self, data):
        self.data =	data
        self.next =	None
        self.prev = None  # Untuk Doubly Linked List 

class Doublylinkedlist:
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
            new_node.prev = self.tail
            self.tail = new_node  

    def display(self): 
        temp = self.head 
        while temp: 
            print(temp.data, end=" -> ") 
            temp = temp.next 
        print("null")

    def search(self, key):
        if not self.head:
            print("Doubly linked list kosong. Tidak dapat mencari elemen.")
            return

        temp = self.head
        position = 0
        while temp:
            if temp.data == key:
                print(f"Elemen {key} ditemukan dalam doubly linked list.")
                return
            temp = temp.next
            position += 1
            print(f"Elemen {key} tidak ditemukan dalam doubly linked list.")

#penggunaan
dll = Doublylinkedlist()

inputuser = input("masukan elemen ke doubly linked list: ").split(",")
for num in inputuser:
   dll.insert_at_end(int(num.strip()))

key = input("Masukan elemen yang ingin dicari dalam list: ").strip()
dll.search(int(key))