def finoNacci(n):
    if n == 1 or n == 0:
        return n

    return finoNacci(n - 1) + finoNacci(n - 2)


def check_two_array_is_same(a, b):
    # a.sort()
    # b.sort()
    if a.sort() == b.sort():
        return True
    else:
        return False


for i in range(6):
    a = finoNacci(i)
    print(a)


# a=check_two_array_is_same([3,1,2],[1,2,3])
# print(a)