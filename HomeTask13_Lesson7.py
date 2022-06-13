translations = {
   'apple': ['malum', 'pomum', 'popula'],
   'fruit': ['baca', 'bacca', 'popum'],
   'punishment': ['malum', 'multa']
}
inverted_dictionary = dict()
#add to new dict keys and values
for key, value in translations.items():
   for i in value:
      inverted_dictionary[i] = key
print(inverted_dictionary)
