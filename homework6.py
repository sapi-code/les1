my_dict = {'dim': 90484, 'mat': 141112, 'cat': 190984}
print(my_dict)
print(my_dict['cat'])
my_dict['margo'] = 160610
print(my_dict)
del my_dict['cat']
print(my_dict)
my_dict.update({'kat': 190984,
                'mam': 10657,
                'pap': 280955})
print(my_dict)

print(my_dict.get('kat'))
print(my_dict.get('ben', 'он не с нами'))
my_dict.pop('dim')
print(my_dict)
g = my_dict.pop('kat')
print(g)
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
my_set = {1, 2, 3, 3, 2, 1, 1, 2, 'Di', 'fr', 'fr', 'demo', True, 2.0, 2.0, 3.5}
print(my_set)
print(my_set.add(8))
print(my_set)
print(my_set.remove(3))
print(my_set)

list_ = (1, 2, 3, 3, 2, 1, 1, 2, 8, 9)
list_ = set(list_)
print(list_)
print(list_.discard(1))
print(list_.add(13))
print(list_)


