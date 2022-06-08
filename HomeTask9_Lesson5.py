import random

#generate an array of length N from elements from 0 to N
N = int(input("Please, input a number: "))
ARRAY = []
for i in range(N):
    ARRAY.append(random.randrange(0, N+1))

N2 = int(input("Please, input second number: "))
if N2 not in ARRAY:
    print("This number is not in the list!")
else:
    for i, el in enumerate(ARRAY):
        #if N is the first
        if i == 0 and el == N2:
            L_NEIGHBOR = None
            R_NEIGHBOR = ARRAY[i + 1]
            print(L_NEIGHBOR, R_NEIGHBOR)
        #if N is last
        elif i != 0 and i != len(ARRAY) - 1 and el == N2:
            L_NEIGHBOR = ARRAY[i - 1]
            R_NEIGHBOR = ARRAY[i + 1]
            print(L_NEIGHBOR, R_NEIGHBOR)
        #if N is inside an array
        elif i == len(ARRAY) - 1 and el == N2:
            L_NEIGHBOR = ARRAY[i - 1]
            R_NEIGHBOR = None
            print(L_NEIGHBOR, R_NEIGHBOR)