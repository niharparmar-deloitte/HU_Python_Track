import functools
list = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())
    list.append(ele)
output_reduce = functools.reduce(lambda x, y: x * y, list)
print(output_reduce)
print()