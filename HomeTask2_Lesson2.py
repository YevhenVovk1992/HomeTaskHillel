kolobki = int(input('How many children are in the group Kolobki: '))
zaichiki  = int(input('How many children are in the group Zaichiki: '))

beds = (kolobki//2 + kolobki%2) + (zaichiki//2 + zaichiki%2)

print(f'We need: {beds} beds.')