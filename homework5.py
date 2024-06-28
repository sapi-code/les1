immutable_var = 1, True, 'nota', 2.3
print(immutable_var)
immutable_var_1 = 2, False, 'enot'
print(immutable_var + immutable_var_1)
print(immutable_var * 3)
#immutable_var[2] = 5
#print(immutable_var)
#Заменить кортеж нельзя т.к. кортеж не поддерживает обращение по элементам
mutable_list = ['pharmacy', 'street', 'streetlight']
print(mutable_list)
mutable_list[2] = ('lamp')
print(mutable_list)
print(mutable_list[:1])
mutable_list.remove('street')
print(mutable_list)
print('lamp' in mutable_list)
