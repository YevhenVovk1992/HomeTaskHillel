USER_INPUT = input("Write text here: ")
N = USER_INPUT.count(".")
if USER_INPUT and USER_INPUT[-1] != '.':
    N += 1
print(f'You wrote {N} sentences.')
