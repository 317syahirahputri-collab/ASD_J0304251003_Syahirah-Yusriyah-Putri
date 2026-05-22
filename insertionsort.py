def insertionsort(data):
     for i in range(1, len(data)):
          
        key = data[i]
        j = i - 1

        while j >= 0 and data[j] > key:
               data[j+1] = data[j]
               j -= 1
        data[j + 1] = key

#data
data = [8, 3, 9, 7, 12]
print("Data sebelum sorting: ", data)

insertionsort(data)
print("Data sesudah sorting: ", data)