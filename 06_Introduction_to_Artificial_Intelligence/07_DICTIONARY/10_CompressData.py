sparse_vector = [0,0,0,1,0,7,0,0,4,0,0,0,8,0,0,0,6,0,0,0,0,0,0,0,9,0,0]
print(sparse_vector)

# remove '0'
sparse_dict = {}
for i in range(len(sparse_vector)):
    if sparse_vector[i] != 0:
        sparse_dict[i] = sparse_vector[i]
        
print(sparse_dict)

# add length key to the sparse_dict
sparse_dict['length'] = len(sparse_vector)

for k, v in sparse_dict.items():
    print(k,v)
    
# Recover the dict back to the vector with the zeros
recovered = [0]*sparse_dict["length"] # make a temp vector with all zeros

for k,v in sparse_dict.items(): # insert the right value to the right place
    if k != "length":
        recovered[k] = v

print(recovered)