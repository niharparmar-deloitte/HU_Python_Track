lst = list(map(int, input().split()))
num1 = lst[0]
num2 = lst[1]


def multiply(func):
    def inner(num1, num2):
        func(num1, num2)
        return func(num1, num2)

    return inner


@multiply
def executableFunc(num1, num2):
    print(num1 * num2)


executableFunc(num1, num2)
