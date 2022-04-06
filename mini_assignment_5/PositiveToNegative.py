# lst1 = [-1000, 500, -600, 700, 5000, -90000, -17500]
# output_filter = list(filter(lambda x: True if x>0 else False, map(lambda x: x*-1, lst1)))
# print(output_filter)
# print()

input_list = []

# number of elements as input
n = int(input("Enter number of elements : "))

# iterating till the range
for i in range(0, n):
    ele = int(input())

    input_list.append(ele)  # adding the element
print(input_list)

output_filter = list(filter(lambda x: True if x>0 else False, map(lambda x: x*-1, input_list)))
print(output_filter)
print()