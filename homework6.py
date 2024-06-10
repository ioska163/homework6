my_dict = {'Max': 1988, 'Arhtur': 1990, 'Ilya': 1997}
print(my_dict)
print(my_dict['Max'])
print(my_dict.get('Kostya'))
my_dict.update({'Svetlana': 1969, 'Mariya': 1993})
del my_dict['Arhtur']
print(my_dict)

my_set = {1, 2, 3, 4, 5, 1, 2, 3, 4, 'string', True}
print(my_set)
my_set.add(6)
my_set.add((1, 2, 3))
my_set.discard(2)
print(my_set)








