###=========================================================###
###================= PYTHON HACKER-RANK ====================###


###==================  1. IF - ELIF  =======================###
#Given an integer, , perform the following conditional actions:
#If is odd, print Weird
#If is even and in the inclusive range of to,print Not Weird
#If is even and in the inclusive range of to  print Weird
#If is even and greater than, print Not Weird

 if(N % 2 == 0):
    if(N <= 5):
        print("Not Weird")
    elif(N >= 6 and N <=20):
        print("Weird")
    else:
        print("Not Weird")
else:
    print("Weird")
	
	

###=====================  2. LOOPS  ============================###
## Read an integer . For all non-negative integers , print . See the sample for details.

if __name__ == '__main__':
    n = int(input())

i = 0
while i < n:
    print(i*i)
    i = i + 1

	
###===================== 3. WRITE A FUNCTION=======================###
##In the Gregorian calendar three criteria must be taken into account to identify leap years:

##The year can be evenly divided by 4, is a leap year, unless:
##The year can be evenly divided by 100, it is NOT a leap year, unless:
##The year is also evenly divisible by 400. Then it is a leap year.

def is_leap(year):
    leap = False
    
    # Write your logic here
    if(year % 4 == 0):
        leap = True
        if(year % 100 == 0):
            leap = False
            if(year % 400 == 0):
                leap = True

    return leap

year = int(input())
print(is_leap(year))

###=================== 4. print =====================================####

##Read an integer .
##Without using any string methods, try to print the following: 123....N
##Note that "...." represents the values in between.

if __name__ == '__main__':
    n = int(input())

i = 1
while i <= n:
    print(i, end = '')
    i = i + 1
	
###====================5. LIST COMPREHENSION============================###
###Let's learn about list comprehensions! You are given three integers X,Y,Z representing the dimensions of a cuboid along with an integer N
## You have to print a list of all possible coordinates given by (I,J,K) on a 3D grid where the sum of I + J + K is not equal to N.
## Here, 0<=i<=X ; 0<=J<=Y; 0<=K<Z


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

ar = [] 
p = 0 

for i in range ( x + 1 ):
    for j in range( y + 1):
        for k in range(z + 1):
            if (i+j+k) != n:
                ar.append([])
                ar[p] = [ i , j , k]
                p+=1 
print (ar)


###=====================6. FIND THE RUNNER UP SCORE=========================###

##Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given scores. 
##Store them in a list and find the score of the runner-up.

##Input Format:
##The first line contains n. The second line contains an array A[] of n integers each separated by a space.

##Constraints:
## 2<=n<=10, -100<= A[i]<=100

##Output Format:
##Print the runner-up score.

## SAMPLE INPUT:
## n=5, A[] = [2,3,6,6,5]

## SAMPLE OUTPUT:
## The runner up score is 5



