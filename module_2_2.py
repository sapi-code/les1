first = int(input('введите число:'))
second = int(input('и еще одно:'))
third = int(input('и последний раз:'))
if first == second == third:
        print(3)
elif first == second or first == third or second == third:
    print(2)
elif not(first == second or first == third or second == third):
    print(0)