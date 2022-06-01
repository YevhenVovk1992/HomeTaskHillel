USER_INPUT = input('Please, write your sentences: ')
CUT_STR = USER_INPUT[USER_INPUT.find(' '):USER_INPUT.rfind(' '):1]
print("Change the letter n to N: ", CUT_STR.replace('n', 'N'))