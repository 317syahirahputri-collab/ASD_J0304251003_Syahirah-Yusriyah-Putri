#==================================================
#Nama : Syahirah Yusriyah Putri
#NIM : J0403251003 
#Kelas : TPL A1
#==================================================

#==================================================
#Implementasi Dasar : Queue
#==================================================

class Node:
    #Konstruktor adalah fungsi yang dijalankan secara otomatis ketika kelas node dipanggil/diinstantiasi
    def __init__(self,data):
        self.data = data  #menyimpan nilai atau data pada list
        self.next = None #pointer ini menunjuk ke note berikutnya (awal=none)
        
class queue:
    #buat konstruktor untuk inisialisasi variabel front dan rear
    def __init__(self):
        self.front = None #node paling depan
        self.rear = None #node paling belakang
        
    def is_empty(self):
        return self.front is None
        
    #membuat fungsi untuk menambahkan data baru
    def enqueue(self,data):
        nodeBaru = Node(data) #menambah data baru
        
        #jika queue kosong, front dan rear menunjuk node yang sama
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
            return
        
        self.rear.next = nodeBaru #letakan data baru pada setelahnya rear
        self.rear = nodeBaru #jadikan data baru sebagai rear
        
    def dequeue(self):
        #menghapus data dari depan / front
        data_terhapus = self.front.data #lihat data paling depan
        
        #geser front ke node berikutnya
        self.front = self.front.next
        
        #jika setelah geser front menjadi none, maka queue kosong
        #rear juga harus jadi none
        if self.front is None:
            self.rear = None
        
        
    def tampilkan(self):
        current = self.front
        print("Front ->", end="")
        while current is not None:
            print(current.data, end="")
            current = current.next
        print("Rear")
        
#instantiasi class queue
q = queue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.tampilkan()