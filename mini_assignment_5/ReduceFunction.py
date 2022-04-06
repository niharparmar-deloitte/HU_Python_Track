import functools

print("Implementing reduce function: ")
lst1 = [-10, 5, -6, 7, 50, -90, -1]
output_reduce = functools.reduce(lambda x, y: x * y, lst1)
print(output_reduce)
print()