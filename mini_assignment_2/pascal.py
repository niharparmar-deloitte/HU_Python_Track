def printPascal(n: int):
    arr = [[0 for x in range(n)]
           for y in range(n)]

    for line in range(0, n):

        for i in range(0, n):

            if i is 0 or i is line:
                arr[line][i] = 1
                print(arr[line][i], end=" ")


            else:
                arr[line][i] = (arr[line - 1][i - 1] +
                                arr[line - 1][i])
                print(arr[line][i], end=" ")
        print("\n", end="")
n=int(input("Enter no of rows: "))
printPascal(n)