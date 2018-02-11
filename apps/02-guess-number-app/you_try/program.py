#Guess the Number Game
import random

def check_guess(guess, the_number):
    if guess > the_number:  
        print("Your guess of {0} is too high.".format(guess))
        return False;
    elif guess < the_number:
       print("Your guess of {0} is too low.".format(guess))
       return False
    else :
      return True

def check_guess_in_bounds(guess, min,max):
    return guess>max or guess<min         
        
print("---------------------------------")
print("-------Guess the Number ---------")
print("---------------------------------")
print()

#Maximum tries to give user to guess the number
guess_max_tries = 3
the_number_min = 1
the_number_max = 20

#set the winning number
the_number = random.randint(the_number_min,the_number_max) 

#initialize to anything except the correct number and guess coount
guess = the_number+1 
guess_count = 1 

#show a hint for debugging purposes
print("Hint: " + str(the_number))

while guess!=the_number and guess_count<=guess_max_tries: 
    print("\nAttempt #{0}".format(guess_count)) if guess_count<guess_max_tries else print("\nLast Chance!")
    guess_text = input("Guess my number from {0} to {1}: ".format(the_number_min,the_number_max))
    guess = int(guess_text)

    if check_guess_in_bounds(guess,the_number_min,the_number_max)==False: 
       if check_guess(guess,the_number)==True:
          break
       guess_count = guess_count +1
    else:
       print("Read the instructions, idiot.")
    

print()
print("Results....")
if guess_count>guess_max_tries:
    print("You are a failure! The number was " + str(the_number))
else: 
    print("You got it! You clever monkey!")


