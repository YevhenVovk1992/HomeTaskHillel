cities = [i for i in input('Here, you will write all cities: ').split()]
L = len(cities)
all_chains = []
now_chain = []
used_cities = {}

def chain_city(lst: list, id: int):
    """
    we call a recursive function with initial cities.
    At startup, we mark the city as used and add it to the chain,
    run a loop in which we check if the city is not yet used and
    its first letter is the same as the last letter of the current city,
    then we launch the recursive procedure for the new city.
    :param lst: list with all cities
    :param id: id of city in list with cities
    :return: now_chain
    """
    start = lst[id]
    used_cities[start] = True
    now_chain.append(start)
    for i in range(len(lst)):
        if i == id:
            continue
        if lst[i] not in used_cities and lst[i][0] == start[-1].upper():
            return chain_city(lst, i)

# Create chains to all cities and put them in one list
for n in range(L):
    chain_city(cities, n)
    all_chains.append(now_chain)
    now_chain = []
    used_cities = {}

# Cort list with chains and print the longest chain
all_chains.sort(key=lambda x: len(x))
print('The longest chain is ')
print(all_chains[-1])

