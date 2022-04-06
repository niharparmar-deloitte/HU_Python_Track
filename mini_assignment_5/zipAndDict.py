list  = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = input()
    list.append(ele)
values = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = input()
    values.append(ele)
output_dictionary = dict(zip(list, values))
print(output_dictionary)