n1 = int(input('A value: '))
n2 = int(input('Another value: '))

print('{} + {} = {}'.format(n1, n2, n1 + n2))
print('{} - {} = {}'.format(n1, n2, n1 - n2))
print('{} / {} = {}'.format(n1, n2, n1 / n2))
print('{} // {} = {}'.format(n1, n2, n1 // n2))
print('{} ** {} = {}'.format(n1, n2, n1 ** n2))

decimal = 3.1415
print('{} formatted is {:.2f}'.format(decimal, decimal))

print('This line will continue in another print:', end=' ')
print('There it is!')

print('This print will break in the middle.\nGot it?')
