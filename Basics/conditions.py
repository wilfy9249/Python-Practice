
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
        print('Start - to start the car Stop - to stop the car Quit - to exit')

    elif command=='quit':
        break
    else:
        print("Sorry i don't understand that")

#------------FOR LOOP--------------------------------------------------------------

prices = [10,20,30]

total = 0
for items in prices:
    total +=items
print(f' The total of the items is: {total}')

#-----------EXERCISE: FOR LOOPS-----------------------------------------------

numbers = [5,2,5,2,2]
for x in numbers:
    print(x * 'X')

#----------EXERCISE:NESTED LOOPS (Print F)----------------------------------------------

numbers = [5,2,5,2,2]
numbers_l = [1,1,1,1,5] #------Print l

for x_count in numbers_l:
    output = ''
    for y in range(x_count):
        output += 'X'
    print(output)

#----------EXERCISE: FIND THE LARGEST NO IN A LIST---------------------------------------

numbers = [2,8,19,32,3,5]
max =0
for item in numbers:
    if item > max:
        max = item
print(f'The largest number in the list is {max}')



















