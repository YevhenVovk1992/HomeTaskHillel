text = input('Please, write your text: ')
dictionary = dict()

for word in text.split():
    if word in dictionary:
        dictionary[word] += 1
    else:
        dictionary[word] = 1

print('TOP 5: ', end='')
for key, value in sorted(dictionary.items(), key=lambda para: -para[1])[:5]:
    print(key, '-', value, end=' ')
print()
for key, value in dictionary.items():
    print(key, '-', value)