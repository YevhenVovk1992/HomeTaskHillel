#First answer
input_str = input('Please, input three-digit number: ')
print('Inversion: ', input_str[::-1])

#second answer
backwards = input_str[-1]+input_str[-2]+input_str[-3]
print('Inversion: ', backwards)
