
#---------IF-ELIF-ELSE CONDITION---------------------------------------------

name = 'Roger Federer'
length = len(name)

if length < 3:
    print('Name must be atleast 3 characters')
elif length > 50:
    print('Name can be maximum 50 characters')
else:
    print("Name looks good")

#----------EXERCISE: CONVERSION OF WEIGHTS------------------------------------


weight =  int(input('Enter Weight: '))
weight_type = input('(L)bs OR (K)g: ')

#---If The weight is entered in Pounds convert to KG---------------------------

if weight_type.upper() == 'L':
    kilo = weight * 0.45
    print(f'Your weight in Kg is: {kilo}')
else:
    pound = weight / 0.45
    print(f'Your weight in Pound is: {pound}')

#-----------EXERCISE: SECRET GAME-----------------------------------------------

secret_no = 9
guess_limit = 3
count = 1

while count <= guess_limit:
    guess_no = int(input('Guess: '))
    count += 1
    if guess_no == secret_no:
        print('You Win!')
        break
else:
    print('Sorry! You failed')


#-----------EXERCISE: CAR GAME -----------------------------------------------------

command = ""
started = False

while True:
    command = input('< ').lower()

    if command=='start':
        if started:
            print('Car has already started')
        else:
            started = True
            print('Car started')
    elif command=='stop':
        if not started:
            print('Car has already stopped')
        else:
            started = False
            print('Car Stopped')
    elif command=='help':
        print('''
Start - to start the car
Stop - to stop the car
Quit - to exit
''')
    elif command=='quit':
        break
    else:
        print("Sorry i don't understand that")