i = [3,3,5,5,7,7]
j = [5,7,3,7,3,5]
k = [7,5,7,3,5,3]

for index in range(len(i)):
    if i[index] < j[index]:
        if j[index] < k[index]:
            i[index] = j[index]
        else:
            j[index] = k[index]
    else:
        if j[index] > k[index]:
            j[index] = i[index]
        else:
            i[index] = k[index]
    print(f"i = {i[index]}, j = {j[index]}, k = {k[index]}")

print()

i = int(input("Nhập i: "))
j = int(input("Nhập j: ")) 
k = int(input("Nhập k: "))
if i < j:
    if j < k:
        i = j
    else:
        j = k
else:
    if j > k:
        j = i
    else:
        i = k

print(f"i = {i}, j = {j}, k = {k}")

# Here is a sample output for the first part of the code: