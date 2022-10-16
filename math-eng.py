#Data Structures with Python#
from typing import List

cities: List[str] = ["İstanbul", "İzmir", "Ankara"]
print(cities)

#Append= Add an item to the end of the list. Equivalent to a[len(a):] = [x].#
cities.append("Isparta")
print(cities)

#Exend= Extend the list by appending all the items from the iterable.
# Equivalent to a[len(a):] = iterable.#
cities.extend("Antalya")
print(cities)

#Insert=Insert an item at a given position.
# The first argument is the index of the element before which to insert,
# so a.insert(0, x) inserts at the front of the list, and
# a.insert(len(a), x) is equivalent to a.append(x).#
cities.insert(0,"Balıkesir")
print(cities)

#Insert#
cities.insert(1,"Bursa")
print(cities)

#Remove= Remove the first item from the list whose value is equal to x.
# It raises a ValueError if there is no such item.#
cities.remove("Bursa")
print(cities)

#Pop= Remove the item at the given position in the list, and return it.#
cities.pop(0)
print(cities)

#Clear= Remove all items from the list. Equivalent to del a[:].
cities.clear()
print(cities)

cities.append("İzmir")
cities.sort()
print(cities)
