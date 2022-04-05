row2 = int(input('Enter number of rows required: '))
for i in range (0,row2):
    for j in range (0,row2):
        if i==0 or j==(row2-1) or i==j:
            print('*', end='')
        else:
            print(end=" ")
    print()