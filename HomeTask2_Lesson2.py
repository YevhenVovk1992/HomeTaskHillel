n = int(input('Please, input three-digit number: '))

e = n%10
w = (n%100 - e)//10
q = (n%1000 - w - e)//100

out = e*100 + w*10 + q
print(out)