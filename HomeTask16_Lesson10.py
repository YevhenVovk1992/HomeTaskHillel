N = int(input('Enter your number: '))

# calculate the power 2 using a recursion function
def degree_of_2(N: int) -> int:
    if N == 0:
        return 1
    else:
        return degree_of_2(N-1) * 2

# calculate the power 2 using a loop
def power_2(x: int) -> int:
    i = 0
    deg_2 = 1
    while i < x:
        deg_2 = deg_2 * 2
        i += 1
    return deg_2

# check input number is negative
if N >= 0:
    print('(loop)degree_of_2 =', power_2(N))
    print('(recursion)degree_of_2 =', degree_of_2(N))
else:
    print('(loop)degree_of_2 =', 1/power_2(abs(N)))
    print('(recursion)degree_of_2 =', 1/degree_of_2(abs(N)))