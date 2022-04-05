rows=int(input("Enter no of rows: "))
for i in range(rows):
    # printing spaces
    for j in range(rows - i - 1):
        print(' ', end='')

    # printing stars
    for k in range(2 * i + 1):
        # print star at start and end of the row
        if k == 0 or k == 2 * i:
            print('*', end='')
        else:
            if i == rows - 1:
                print('*', end='')
            else:
                print(' ', end='')
    print()