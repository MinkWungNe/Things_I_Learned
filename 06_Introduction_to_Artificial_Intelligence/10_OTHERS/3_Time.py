import time

#Lists Length
n_of_elements=[10,100,1000]

# for each Length
for n in n_of_elements:
    numbers = []
    print("N. of zeros:", len(numbers))

    # create the List using the for Loop
    start = time.time()
    
    for _ in range(n):
        numbers.append(0)
    end = time.time()
    print("For loop: {:.6f} sec".format(end-start))

    # create the List using list replication

    start = time.time()
    numbers = [0]*n

    end = time.time()
    print("List repl: {:.6f} sec \n".format(end-start))