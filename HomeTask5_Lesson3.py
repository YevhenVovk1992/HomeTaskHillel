N = 1
AMOUNT = 0
N_MAX = None
N_MIN = None
while True:
    number = input("Enter number: ")
    if number == '':
        break
    N += 1
    AMOUNT += int(number)
    if N_MAX == None or N_MAX < int(number):
        N_MAX = int(number)
    if N_MIN == None or N_MIN > int(number):
        N_MIN = int(number)
MEAN = AMOUNT / N
print()
print("N =", N)
print("AMOUNT =", AMOUNT)
print("MAX = ", N_MAX, "MIN = ", N_MIN)
print("MEAN = ", MEAN)