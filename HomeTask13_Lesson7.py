translations = {
   'apple': ['malum', 'pomum', 'popula'],
   'fruit': ['baca', 'bacca', 'popum'],
   'punishment': ['malum', 'multa']
}
inverted_dictionary = dict()
# Add to new dict keys and values
for key, value in translations.items():
   for i in value:
      if i in inverted_dictionary:
         inverted_dictionary[i] += [key]
      else:
         inverted_dictionary[i] = [key]
print(inverted_dictionary)
