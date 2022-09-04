from math import sqrt, floor

number = float(input('Insert a number: '))
squareRoot = sqrt(number)

print('The square root of {} is {:.2f}.'
      .format(number, floor(squareRoot)))
