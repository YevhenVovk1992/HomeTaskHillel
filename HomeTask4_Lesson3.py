number = input("Enter number: ")
if number == '':
    N = 0
    AMOUNT = 0
    N_MAX = 0
    N_MIN = 0
    MEAN = 0
else:
    N = 1
    AMOUNT = int(number)
    N_MAX = int(number)
    N_MIN = int(number)
    while True:
        number = input("Enter number: ")
        if number == '':
            break
        N += 1
        AMOUNT += int(number)
        if N_MAX < int(number):
            N_MAX = int(number)
        if N_MIN > int(number):
            N_MIN = int(number)
    MEAN = AMOUNT/N
print()
print("N =", N)
print("AMOUNT =", AMOUNT)
print("MAX = ", N_MAX, "MIN = ", N_MIN)
print("MEAN = ", MEAN)

