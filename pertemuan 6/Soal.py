data = [43,76,12,89,33,57,98,22,68,9]

data.sort(reverse=True)

print("Nilai setelah diurutkan (Descending):")
print(data)

print("\n5 kandidat dengan nilai tertinggi:")

for i in range(5):
    print(data[i])