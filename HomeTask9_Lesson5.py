import random

#generate an array of length user_number from elements from 0 to user_number
user_number = int(input("Please, input a number: "))
array = [random.randrange(0, user_number+1) for i in range(user_number)]
#input second number
user_number_2 = int(input("Please, input second number: "))
is_found = True
for i, el in enumerate(array):
    # user_number is in array?
    if el != user_number_2:
        continue
    # if user_number is the first
    elif i == 0 :
        l_neighbor = None
        r_neighbor = array[i + 1]
        print(l_neighbor, r_neighbor)
    # if user_number_2 is last
    elif i == len(array) - 1:
        l_neighbor = array[i - 1]
        r_neighbor = None
        print(l_neighbor, r_neighbor)
    # if user_number_2 is inside an array
    else:
        l_neighbor = array[i - 1]
        r_neighbor = array[i + 1]
        print(l_neighbor, r_neighbor)
    is_found = False
if is_found:
    print("Not found")
