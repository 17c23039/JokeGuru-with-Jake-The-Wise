from time import sleep
import random



def selection () :
  print("Hi! I am JokeGuru! Please select 1 if you would like puns, and 2 if you would like a dark humour joke.")
  jokesel = int(input())
  if jokesel == 1 :
    puns () 
  elif jokesel == 2 :
    dh ()
  else :
    print("Invalid option!")
    sleep(1)
    selection ()



def puns () :
  print("Welcome to PunGuru, You Can Press 1 To Get A Really High Quality Pun!")
  punselect = input("Press 1 For A Pun:")
  punchoice = random.randint(1, 3)
  if punselect == "1" :
    print("Genarating A Pun...")
    if punchoice == 1 :
      print("What do You Call The Security At A Samsung Factory...")
      sleep(1)
      print("Guardians Of The Galaxy!")
      sleep (2)
      again = int(input("Go again? 1 for yes, any other key for no."))
      if again == 1 :
        puns ()
      else :
        selection ()
    elif punchoice == 2 :
      print("Want To Hear A Joke About Eggs...?")
      sleep(1)
      print("It's Absolutely CRACKING!") #lmao
      sleep (2)
      again = int(input("Go again? 1 for yes, any other key for no."))
      if again == 1 :
        puns ()
      else :
        selection ()
    elif punchoice == 3 :
      print("I don't trust stairs...")
      sleep(1)
      print("They're always up to something...")
      sleep (2)
      again = int(input("Go again? 1 for yes, any other key for no."))
      if again == 1 :
        puns ()
      else :
        selection ()
  else :
    print("Invalid Selection!")
    sleep(2)
    puns()
    
def dh () :
  print("Welcome to DarkGuru! Please select 1 for a great dark humour joke, and any other key to end it. WARNING: If you are a snowflake, do not press 1.")
  dhsel = int(input())
  if dhsel == 1 :
    print("Okay, selecting a dark humour joke...")
    dhselection = random.randint(1, 3)
    sleep(1)
    if dhselection == 1 :
      print("Why are 9/11 victims the fastest readers?")
      sleep(1)
      print("Because they went through multiple stories in seconds.")
      sleep (2)
      again = int(input("Go again? 1 for yes, any other key for no."))
      if again == 1 :
        dh ()
      else :
        selection ()
    elif dhselection == 2 :
      print("A priest, murderer and mafia boss walk into a bar.")
      sleep(1)
      print("He orders a drink.") 
      sleep (2)
      again = int(input("Go again? 1 for yes, any other key for no."))
      if again == 1 :
        dh ()
      else :
        selection ()
    elif dhselection == 3 :
      print("If you drink too much Coke, you get a free job!")
      sleep(1)
      print("A one time, long term coffin tester!")
      print("Courtesy of Jacob Edwards.")
      sleep (2)
      again = int(input("Go again? 1 for yes, any other key for no."))
      if again == 1 :
        dh ()
      else :
        selection ()
  else :
    print("Okay, ending and returning to selection.")
    selection ()
    

selection ()