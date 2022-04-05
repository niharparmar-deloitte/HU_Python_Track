rows=int(input("Enter no of rows: "))
for i in range(rows):
    print(" "*(rows-i-1)+"*"*(2*(i+1)-1))
for i in range(rows-1):
    print(" "*(i+1)+"*"*(2*(rows-i-1)-1))