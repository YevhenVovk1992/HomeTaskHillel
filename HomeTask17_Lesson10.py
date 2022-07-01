cities = input('Here, you will write all cities: ').split()
L = len(cities)
all_chains = []


def chain_city(lst: list, id: int, now_chain=None, used_cities=None) -> list:
    """
     we call a recursive function with initial cities.
     At startup, we mark the city as used and add it to the chain,
     run a loop in which we check if the city is not yet used and
     its first letter is the same as the last letter of the current city,
     then we launch the recursive procedure for the new city.
     :param lst: list with all cities
     :param id: id of city in list with cities
     :param now_chain: list of the cities in correct order
     :param used_cities: buffer of used cities
     :return: list of the cities in correct order
    """
    if now_chain is None and used_cities is None:
        used_cities = set()
        now_chain = []
    start = lst[id]
    used_cities.add(start)
    now_chain.append(start)
    for i in range(len(lst)):
        if i == id:
            continue
        if lst[i] not in used_cities and lst[i][0] == start[-1].upper():
            chain_city(lst, i, now_chain, used_cities)
    return now_chain


# Create chains to all cities and put them in one list
for n in range(L):
    all_chains.append(chain_city(cities, n))
# Print the longest chain in the list
print('The longest chain is ')
print(max(all_chains, key=lambda x: len(x)))
