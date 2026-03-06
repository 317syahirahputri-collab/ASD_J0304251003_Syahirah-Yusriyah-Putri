def quickSort(data):

    if len(data) <= 1:
        return data

    pivot = data[0]

    less = []
    greater = []

    for x in data[1:]:
        if x <= pivot:
            less.append(x)
        else:
            greater.append(x)

    return quickSort(less) + [pivot] + quickSort(greater)


data = [54,26,93,17,77,31,44,55,20]

hasil = quickSort(data)

print("Hasil Ascending:", hasil)