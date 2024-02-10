print("Welcome to my computer quiz")

playing  = input("Do you want to play? ").strip()

if playing.lower() != "yes" :
   quit()

print("Okay ! Let's play :) ")

answer = input("What does CPU stands for? ").strip()
if answer.lower() == "central processing unit":
    print("Correct!")
elif answer.upper() == "CENTRAL PROCESSING UNIT":
   print("correct!")
else:
   print("Incorrect!")

answer = input("What does VPN stands for? ").strip()
if answer.lower() == "virtual private network":
   print("Correct!")
elif answer.upper() == "VIRTUAL PRIVATE NETWORK ":
   print("Correct!")
else:
   print("Incorrect!")

answer = input("What does HTML stands for? ").strip()
if answer == "Hyper Text Markup Language":
    
   print("Correct!")
else:
   print("Incorrect!")

answer = input("What does GPU stands for? ").strip()
if answer.lower() == "graphics processing unit":
    
   print("Correct!")
else:
   print("Incorrect!")

answer = input("What does OS stands for? ").strip()
if answer.lower() == "operating system":
    print("Correct!")
elif answer.upper() == "OPERATING SYSTEM ":    
    print("Correct!")
else:
    print("Incorrect!")