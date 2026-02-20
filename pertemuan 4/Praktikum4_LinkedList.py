#==================================================
#Nama : Syahirah Yusriyah Putri
#NIM : J0403251003 
#Kelas : TPL A1
#==================================================

#==================================================
#Implementasi Dasar : Node pada linked List
#==================================================

class Node:
    #Konstruktor adalah fungsi yang dijalankan secara otomatis ketika kelas node dipanggil/diinstantiasi
    def __init__(self,data):
        self.data = data #menyimpan nilai atau data pada list
        self.next = None #pointer ini menunjuk ke note berikutnya (awal=none)
        
#membuat node dengan instantiasi class node
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")

#2) menghubungkan node : a -> b -> c -> none
head = nodeA 
nodeA.next = nodeB
nodeB.next = nodeC

#4) menelusuri kode dari head sampai ke none
current = head
while current is not None:
    print(current.data) #menampilkan data pada node saat ini
    current = current.next #pindah ke node berikutya
    