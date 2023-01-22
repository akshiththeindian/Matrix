#Welcome to the Matrix Game. IF at any time you want to end this program please do so.
print("Welcome to the matrix game!")  
import dataclasses 
from os import system 
import statistics 
from tkinter import Variable 
import numpy as np 
print("Choose the answer to the challenge with out this challenge you will not be able to continue on the path to the Matrix.") 
#Ask the Pre-challenge question "Do you choose the Red Pill or the Blue pill?" 
question = input("Do you choose the Red Pill or the Blue Pill? ")  
print("Options:")  
print("A) Red Pill")  
print("B) Blue Pill")  
answer = input("Enter your answer:") 
if question == "B":   
    print("Goodbye")  
    exit() 
 # If the answer is correct, continue executing code 
print("Correct answer!") 
   #ask question 2 
input("Question: What is the Matrix?") 
print("Options:") 
print("A) something in biology") 
print("B) A AI obsessed with controlling you.") 
print("C) Top G's obsession") 
print("D) or none of the above ") 
answer = input("Enter your answer:") 
print("User answered correctly") 
if answer == ("B","C"):  
        print("Correct!") 
if input("Do you want to exit? (y/n): ") == "y": 
    print("Exiting...") 
    print("Exiting the system..."); 
    print("Good Bye. The System will see you later!!") 
    exit() 
# next part of the challenge 
print("The next part of the challenge is to see if you are old enough to continue. The Matrix is a fickle systme and can corrupt the minds of those who are too young to use it. You have to be 12 or older to enter the Matrix.") 
player_age = int(input("Your age: "))   
if player_age >= 15:   
  print("You are old enough to play!")   
elif player_age >= 13:   
  print("You can be a normal member.")   
elif player_age >=12:   
  print("you can be a junior member.")   
else:   
  print("You are too young to join the club") 

  if input("Do you want to exit? (y/n): ") == "y": 
    print("Exiting...") 
    print("Exiting the system... Please wait while we continue with your exit...") ; 
    print("Good Bye. The System will see you later!!")
    exit() 
     
name = input("Enter your name")        
print("Creating a Avatar for you...... Please enter your name. Remember to be who you say you are.")   
print("welcome" (input)) 
name = input("Enter your name")