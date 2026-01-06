a = 0
while a < 100:
    b = 0
    while b < 40:
        if (a+b) % 2 == 0:
            print('*', end='')
        b += 1
    print()
    a += 1

# In ra hình chữ nhật 100x40 với các ký tự '*' và ' ' xen kẽ nhau.