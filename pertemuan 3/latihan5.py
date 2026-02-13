# ================================
# Praktikum 3: Linked List dan Implementasinya
# Latihan 5: Tambahkan metode untuk membalik (reverse) sebuah single linked list tanpa membuat linked list baru.
# ================================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None # Tambahkan pointer tail

    # Metode untuk membalik linked list
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next  # Simpan node berikutnya
            current.next = prev       # Balikkan arah pointer
            prev = current            # Geser prev ke current
            current = next_node       # Geser current ke next_node
        self.head = prev              # Update head ke node terakhir yang diproses

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head: # Jika linked list kosong
            self.head = new_node
            self.tail = new_node # Tail juga menunjuk ke node pertama
        else:
            self.tail.next = new_node # Sambungkan tail ke node baru
            self.tail = new_node # Update tail ke node baru
    
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

# Contoh Penggunaan
ll = SingleLinkedList()
angkaUser = input("Masukkan elemen untuk Single Linked List: ").split(", ")
for num in angkaUser:
    ll.insert_at_end(int(num.strip()))

print("Linked list sebelum dibalik: ", end="")
ll.display()
ll.reverse()
print("Linked list setelah dibalik: ", end="")
ll.display()