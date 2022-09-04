from math import trunc, hypot, cos, sin, tan, radians
from random import choice, shuffle
from playsound import playsound


class Main:
    def Run1(self):
        number = float(input('Insert a float number: '))

        print(trunc(number))

    def Run2(self):
        oppositePeccary = float(input('Insert the opposite peccary in cm: '))
        adjacentPeccary = float(input('Insert the adjacent peccary in cm: '))

        print('The hypotenuse is {:.2f} cm.'
              .format(hypot(oppositePeccary, adjacentPeccary)))

    def Run3(self):
        angle = float(input('Insert an angle: '))

        print('Tangent: {:.2f}'.format(tan(radians(angle))))
        print('Sine: {:.2f}'.format(sin(radians(angle))))
        print('Cosine: {:.2f}'.format(cos(radians(angle))))

    def Run4(self):
        students = []
        students.append(input('Insert the first student: '))
        students.append(input('Insert the second student: '))
        students.append(input('Insert the third student: '))
        students.append(input('Insert the fourth student: '))

        selectedStudent = choice(students)

        print('Please {}, erase the blackboard.'.format(
            selectedStudent))

    def Run5(self):
        students = []
        students.append(input('Insert the first student: '))
        students.append(input('Insert the second student: '))
        students.append(input('Insert the third student: '))
        students.append(input('Insert the fourth student: '))

        shuffle(students)

        print('The presentation order is:')
        print('1. {}'.format(students[0]))
        print('2. {}'.format(students[1]))
        print('3. {}'.format(students[2]))
        print('4. {}'.format(students[3]))

    def Run6(self):
        playsound('./Assets/sample.mp3')


main = Main()
main.Run6()
