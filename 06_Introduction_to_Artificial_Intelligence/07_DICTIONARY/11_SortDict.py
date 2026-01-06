registry = {"Shaili": 4, "Chris": 90, "Maris": 70}
print(registry)

# SORT BY KEYS
sorteds = {}

sort_keys = list(registry.keys())
sort_keys.sort()

print(sort_keys)

# initialize key for sorted dict
for k in sort_keys:
    sorteds[k] = registry[k]

print(sorted)

# SORT BY VALUES
sorteds = {}
sort_keys = sorted(registry, key = registry.get)
print(sort_keys)

for k in sort_keys:
    sorteds[k] = registry[k]
print(sorteds)