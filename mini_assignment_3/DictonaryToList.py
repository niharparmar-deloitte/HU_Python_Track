d = {'HuEx': [1, 3, 4], 'is': [7, 6], 'best': [4, 5]}
print("The original dictionary is : " + str(d))

# Convert Key-Value list Dictionary to Lists of List
# Using loop + items()
res = []
for key, val in d.items():
    res.append([key] + val)

# printing result
print("The converted list is : " + str(res))