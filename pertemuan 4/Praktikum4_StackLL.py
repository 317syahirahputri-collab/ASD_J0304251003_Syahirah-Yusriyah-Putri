
#==================================================
#Nama : Syahirah Yusriyah Putri
#NIM : J0403251003 
#Kelas : TPL A1
#==================================================

#==================================================
#Implementasi Dasar : Stock
#==================================================

class Node:
    #Konstruktor adalah fungsi yang dijalankan secara otomatis ketika kelas node dipanggil/diinstantiasi
    def __init__(self,data):
        self.data = data  #menyimpan nilai atau data pada list
        self.next = None #pointer ini menunjuk ke note berikutnya (awal=none)


#stock ada operasi push(memasukan head baru) dan pop (menghapus head)

class stack:
    def __init__(self):
         self.top = None #top menunjuk ke node paling atas (awalnya kososng)
         
    def push(self, data):  #memasukan data baru pada stack
        #1 membuat node baru
        nodeBaru = Node(data) #instantiasi/memanggil konstruktor pada class node
        
        #2 node baru menunjuk ke top yang lama (head lama)
        nodeBaru.next = self.top
        
        #geser top pindah ke node baru
        self.top = nodeBaru
        
    def is_empty(self):
        return self.top is None
        
    def pop(self): #mengambil / menghapus node paling atas (top/head) 
        if self.is_empty():
            print("stack kosong, tidak ada pop")
            return None
        data_terhapus = self.top.data #soroti bagian top dan simpan di variabel (peek)
        # B -> A -> None
        self.top = self.top.next #geser top ke node berikutnya
        return data_terhapus
    
    def peek(self):
        #melihat data yang paling atas tanpa menghapus
        if self.is_empty():
            return None
        return self.top.data   
        
    def tampilkan(self):
        #top -> A -> B
        current = self.top
        print ("Top ->" , end=" ")
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print("None")

#instantiasi class stack
s = stack()
s.push("A")
s.push("B")
s.push("C")
s.tampilkan()
print("Peek (lihat top): ", s.peek())
s.pop()
s.tampilkan()
print("Peek (lihat top): ", s.peek())