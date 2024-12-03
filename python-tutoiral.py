import math

print("Welcome to COS101")

first_name = input("Please enter your name: ")

def calculate_kinetic_energy():
    mass = float(input('Please enter the Mass:  '))
    velocity = float(input('Please enter the Velocity: '))
    result = 0.5 * mass * velocity **2
    print(f'Kinetic Energy = {result}')

def calculate_quadratic():
    equ_type = input('Is the equation in form a*x^2 + b*x + c = 0? (Y/N) ')
    if equ_type.upper()  == 'Y':
        a = float(input('Please enter the value of a: '))
        b = float(input('Please enter the value of b: '))
        c = float(input('Please enter the value of c: '))

        print(f'a = {a} | b = {b} | c = {c}')

        discriminant = (b ** 2) - (4 * a * c)

        if discriminant >= 0:
            x1 = (-b + math.sqrt(discriminant)) / (2 * a)
            x2 = (-b - math.sqrt(discriminant)) / (2 * a)
            print(f'x1 = {x1} | x2 = {x2}')
        else:
            print("The equation has no real roots.")
    else:
        print("Invalid input or unsupported equation format.")

def gravitational_force():
    mass1 = float(input('Please enter the first term: '))
    mass2 = float(input('Please enter the second mass: '))
    radius = float(input('Please enter radius: '))


    G = 6.674 * (10 ** -11)
    force = G * (mass1 * mass2) / (radius ** 2)
    print(f'Gravitational force = {force}')

def calculate_AP():
    a = float(input('Please enter the first term: '))
    n = float(input('Please enter the number of terms: '))
    d = float(input('Please enter the common difference: '))
    result = a + (n - 1) * d
    print(f'The nth term of the arithmetic progression is {result}')


def calculate_power():
    workdone = float(input('Please enter the work done: '))
    time = float(input('Please enter the time: '))

    power = workdone / time
    print(f'Power = {power}')


def main_menu():
        print("\nChoose an option :")
        print("1) Solve a Quadratic Equation")
        print("2) Calculate Kinetic Energy")
        print("3) Calculate Gravitational Force")
        print("4) Find the nth term of an Arithmetic Progression (AP)")
        print("5) Calculate Power")

        choice = input("Enter your choice : ").lower()

        if choice == '1':
            calculate_quadratic()
        elif choice == '2':
            calculate_kinetic_energy()
        elif choice == '3':
            gravitational_force()
        elif choice == '4':
            calculate_AP()
        elif choice == '5':
            calculate_power()
        else:
            print("option not found")


main_menu()

print(f'Thank you {first_name} ')