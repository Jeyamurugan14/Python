# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 10:02:30 2019

@author: jkrishnakumar
"""

###########################################################################################################################################


#   Password generator


ans = input("Do you want to create a password?: ")
ans1 = "Do you want it to be strong one or a weak one?: "

ans_y = ["yes","Yes","ok"]

ans_n = ["no","No","Nope"]

if ans in ans_n:
    print("No worries. Thank you!")
elif ans in ans_y:
    input(ans1)

if ans1 == "strong":
    strong_pass()
elif ans1 == "weak":
    weak_pass()
    
alpha_s = [chr(x) for x in range(ord('a'),ord('z')+1)]

#test_list = list(map(chr, range(97, 123))) 

alpha_u = [x.upper() for x in alpha_s]

numbs = list(range(1,50))

#symbols = {'~','!','@','$','%','^','&','*','(',')','-','+','=','{','[','}','}','|','\',':',';'}

import random
from numpy import random 

def strong_pass():
    pass_1 = random.choice(alpha_s,4)
    pass_2 = random.choices(alpha_u,3)
    numbs1 = random.choice(numbs,3)
    new_pass = pass_1 + pass_2 + numbs1
    new_pass_1 = new_pass.join()
    print("Your password is: ", new_pass_1)
    next1 = input("You want to generate another password? ")
    if next1 in ans_y:
        strong_pass()
    elif next1 in ans_n:
        print("Thank you! Now fuck off !!!! ")
    
strong_pass()    

###########################################################################################################################################



#    Cows and bulls game 


import random
numb_c = random.randint(1000,9999)
#numb_c = str(8686)
numb_c = list(str(numb_c))
tries = 0

def bullsandcows():
    global tries
    numb = input("Guess the 4 digit number: ")
#numb = str(8989)
    numb = list(numb)
    cows = 0
    bulls = 0 
    tries += 1

    if numb == numb_c:
        print("Thats fucking awesome!!!")
        

    for i,j in zip (numb, numb_c):
        if i == j:
            cows += 1
        else :
            bulls += 1

    print("You have: {} cows and {} bulls in {} tries".format(cows, bulls,tries))
    
    res = input("Do you want to continue?? ")

    if res == 'yes':
        bullsandcows()
    else :
        print("Thank you !!! ")


bullsandcows()



###########################################################################################################################################



#     Palindrome checker


word = input("Enter a word to see if its a palindrome : ")

word = list(word)

for i in range(1,len(word)):
    if word[i-1] == word[-i]:
        i += 1
        print(word , " is a palindrome")
        break
    else:
        print("Not a palindrome")


print(word[-1])
print(word[0])

word[0:i] == word[i:0]


rvs=word[::-1]
print(rvs)


###########################################################################################################################################


#   Rock paper scissor game


player1 = input("You are player1. Rock, paper or scissor? : ")

player2 = input("You are player2. Rock, paper or scissor? : ")


while player1 == "rock":
    if player2 == "rock":
        print("Its a tie !!! ")
        break
    elif player2 == "scissor":
        print("Player 1 wins !!! ")
        break
    elif player2 == "paper":
        print("Bravo..Player 2 wins !!! ")
        break 

###########################################################################################################################################


#     Random number guesser
 
try1 = 0

def game1():
    user_value = int(input("I have random number. Can you guess the number between 1 and 9 : "))
    import random
    rand_value = random.randint(1,9)
    print("The random number that was generated was :", rand_value)
    print("Your guess was : ", user_value)
    try1 += 1

    if abs(user_value - rand_value) > 4:
        print("It was nowhwere near the randomly generated number")
    elif abs(user_value - rand_value) < 4:
        print("So close. You almost had it! ")
    elif abs(user_value == rand_value):
        print("Whoa! You guessed it right!! Arent you a sorcerer?")
    
    res = input("Do you want to go again? : ")
    ans = ['yes','Yes','YES','1','ok']
    exit1 = ['exit','no','NO']
    if res in ans:
        game1()
    elif res in exit1:
        print("It took you", try1, "tries")
        print("Ok. Thank you!!")


game1()



###########################################################################################################################################


#     Finding a number if its prime or not

          
numb = int(input("Enter a number: "))

for i in range(2,numb-1):
    rem = numb % i
    if rem == 0: 
        print(numb, " is not a prime number")
        break
    elif rem != 0:
        print( numb, " is a Prime number indeed !!!")
        break
    
###########################################################################################################################################


#   Fibonacci series  generator


def fibo():
    numb1 = int(input("How many numbers do you want to consider for Fibonacci series?: "))
    numb2 = 0
    numb3 = 1
    print("The Fibonacci series for,",numb1, "are : ")
    print(numb2)
    print(numb3)
    for i in range(1,numb1):
        num1 = numb2 + numb3
        print(num1)
        numb2 = numb3
        numb3 = num1
        
    
fibo()

###########################################################################################################################################


# Sentence reverser


sent = input("Enter a setence to see it reversed: ")

for i in sent:
    sentr = sent [::-1]
print(sentr)


###########################################################################################################################################



















