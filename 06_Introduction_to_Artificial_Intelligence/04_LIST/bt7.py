lst = []
lasta = None

while True:
    a = int(input("Enter a number (0 to stop): "))
    if a == 0:
        break
    if lasta is not None and a == lasta:
        print("Duplicate number, please enter a different number.")
        continue
    elif lasta is not None and a < lasta:
        print("Number must be greater than the last entered number.")
        continue
    lst.append(a)

print("List of numbers entered:", lst)