num = int(input('Number: '))

def square_root(x):
    if x < 2:
        return x
    result = 0
    left = 0
    right = x
    while left <= right:
        # find the middle element
        midd = (left + right) // 2
        if midd*midd == x:
            return midd
        elif midd*midd < x:
            # discard left search space
            left = midd + 1
            # update result
            result = midd
        else:
            # discard the right search space
            right = midd - 1
    return result

print('Square root: ', square_root(num))
