from time import sleep
import os
floor_max = 7
floor_min = 1

lift_floor = 4
human_floor = 6
human_in_lift = False


def printFloor():
    print(10 * "-")

    for floor in range(floor_max, floor_min-1, -1):
        if human_in_lift and floor == lift_floor:
            print(f'{floor} |[ H ]|')
        elif floor == human_floor and floor == lift_floor and not human_in_lift:
            print(f'{floor} |[   ]|   H')
        elif floor == human_floor and not human_in_lift :
            print(f'{floor} |     |   H')
        elif floor == lift_floor:
            print(f'{floor} |[   ]|')
        else:
            print(f'{floor} |     |')
    print(10 * "-")


def printMenu():
    print('1. Coll')
    print('2. destination')
    print('3. enter')
    print('4. exit')
    option = int(input('>>> '))
    return option


def call():
    global lift_floor
    while lift_floor != human_floor:
        sleep(0.5)
        lift_floor -= 1
        if lift_floor < 1:
            lift_floor = 7
        os.system('cls')
        printFloor()


def destination():
    global lift_floor
    where_to = int(input('where floor>>> '))
    while lift_floor != where_to:
        if lift_floor < where_to:
            sleep(0.5)
            lift_floor += 1
        if lift_floor > where_to:
            sleep(0.5)
            lift_floor -= 1
        os.system('cls')
        printFloor()


def enter():
    global human_in_lift
    if lift_floor != human_floor:
        print('WARNING you can fall!!')
    else:
        human_in_lift = True


def exit():
    global human_in_lift, human_floor
    if human_in_lift:
        human_in_lift = False
        human_floor = lift_floor


while True:
    os.system('cls')
    printFloor()
    option = printMenu()
    if option == 1:
        call()
    elif option == 2:
        destination()
    elif option == 3:
        enter()
    elif option == 4:
        exit()
