N = int(input('Enter number: '))

#consider Fibonacci number by recursion function
def fibonacci(x: int):
    if x == 0:
        cash = 0
    elif x == 1 or x == 2:
        cash = 1
    else:
        cash = fibonacci(x-1) + fibonacci(x-2)
    return cash

#consider Fibonacci number by loop
fibo_1 = 1
fibo_2 = 1
i = 2
while i < N:
    fibo_rezult = fibo_2 + fibo_1
    fibo_1 = fibo_2
    fibo_2 = fibo_rezult
    i += 1
print('Fibonacci number - ', fibo_rezult)
print('Fibonacci number - ', fibonacci(N))