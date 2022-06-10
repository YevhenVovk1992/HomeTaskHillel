LIST_NAME = [i for i in input('Write names: ').split(', ')]
LIST_NAME_SET = set(LIST_NAME)
NAMESAKE = set()
for name in LIST_NAME:
    if LIST_NAME.count(name) > 1:
        NAMESAKE.add(name)
print('Names set without namesake:', LIST_NAME_SET - NAMESAKE)