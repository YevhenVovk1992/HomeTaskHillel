in_number = int(input("Enter the number: "))
#Prime number check
if in_number > 1:
    for i in range(2, in_number):
        if in_number % i == 0:
            print("Number is not simple")
            break
    else:
        print("Number is simple")
else:
    print("Number is not simple")
#prime numbers up to in_number
numbers = 2
while numbers <= in_number:
    for o in range(2, numbers):
        if numbers % o == 0:
            break
    else:
        print(numbers, end=' ')
    numbers += 1