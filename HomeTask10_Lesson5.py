import random

#generate an array of length N from elements from 0 to N
N = int(input("Please, input a number: "))
ARRAY = []
for i in range(N):
    ARRAY.append(random.randrange(0, N+1))

N2 = int(input("Please, input second number: "))
for i in range(len(ARRAY)):
    for j in range(i+1, len(ARRAY)):
        if ARRAY[i]+ARRAY[j] == N2:
            print(f'The sum of this elements {[i, j]} is a second number')
            exit()
print('There are no such couples!')