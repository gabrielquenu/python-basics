number = int(input('Type an integer: '))

print('The number {} is between {} and {}'
      .format(number, number - 1, number + 1))

print('The double of {} is {}'.format(number, number * 2))
print('The triple of {} is {}'.format(number, number * 3))
print('The square root of {} is {:.2f}'.format(number, number ** (1 / 2)))

print('{} * 1 = {}'.format(number, number * 1))
print('{} * 2 = {}'.format(number, number * 2))
print('{} * 3 = {}'.format(number, number * 3))
print('{} * 4 = {}'.format(number, number * 4))
print('{} * 5 = {}'.format(number, number * 5))
print('{} * 6 = {}'.format(number, number * 6))
print('{} * 7 = {}'.format(number, number * 7))
print('{} * 8 = {}'.format(number, number * 8))
print('{} * 9 = {}'.format(number, number * 9))
print('{} * 10 = {}'.format(number, number * 10))

score1 = float(input('Insert the first score: '))
score2 = float(input('Insert the second score: '))

print('The average score is {:.2f}.'.format((score1 + score2) / 2))

meters = float(input('Insert a meters quantity: '))

print('{} meter(s) are {} centimeter(s) or {} milimeter(s).'
      .format(meters, meters * 100, meters * 1000))

money = float(input('How much money do you have? '))

print('You can buy {:.2f} US dollars.'.format(money / 3.27))

height = float(input('Insert the wall height: '))
width = float(input('Insert the wall width: '))
wallArea = height * width

print("It'll be necessary {} liter(s) of paint.".format(wallArea / 2))

productPrice = float(input('Insert the product price: '))

print('The product with 5 off is {:.2f}.'.format(productPrice * 0.95))

salary = float(input('Insert the salary: '))

print('The salary with a 15% raise is {:.2f}.'.format(salary * 1.15))
