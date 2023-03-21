'''
  Name: Riley Baxter
  James Hargest College
  Programming Internal for 1.7 ~ 4 credits
  Due: 6 April 2023
  
  TIP: Use assessment guide to help guide you through this Internal
'''


# Header 
print("\u001b[31mcreated by Riley Baxter\n"
      "\u001b[31███╗░░░███╗░█████╗░████████╗██╗░░██╗  ░██████╗░██╗░░░██╗██╗███████╗\n"
      "\u001b[38;5;208m████╗░████║██╔══██╗╚══██╔══╝██║░░██║  ██╔═══██╗██║░░░██║██║╚════██║\n"
      "\u001b[93m██╔████╔██║███████║░░░██║░░░███████║  ██║██╗██║██║░░░██║██║░░███╔═╝\n"
      "\u001b[32m██║╚██╔╝██║██╔══██║░░░██║░░░██╔══██║  ╚██████╔╝██║░░░██║██║██╔══╝░░\n"
      "\u001b[34m██║░╚═╝░██║██║░░██║░░░██║░░░██║░░██║  ░╚═██╔═╝░╚██████╔╝██║███████╗\n"
      "\u001b[35m╚═╝░░░░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝  ░░░╚═╝░░░░╚═════╝░╚═╝╚══════╝")
# Imports 


 # Lists
questions = ["What's 100 ÷ 10?>>","What's the square root of 9>>","What is 7 x 9?","How many sides does a triangle have?","If you have 15 apples and you give 5 to your friend, how many apples do you have left?","What is the value of 3 + 6 - 2?","What is 20 divided by 5?","How many degrees are in a right angle?","If a rectangle is 8 units long and 4 units wide, what is its perimeter?","What is the difference between 10 and 4?","If you have 18 marbles and you want to divide them equally between 3 friends, how many marbles will each friend get?","What is the area of a square with sides of length 6 units?"
]
answers = [10,3,63,3,10,7,4,90,24,6,6,36]
# Functions 





# Scripts 
score = 0 
for i in range(len(questions)):
  print("Question", i+1, questions[i])
  answer = int(input("Answer: "))
  if answer == answers[i]:
    print("Correct")
    score = score+1
  else: 
    print("Wrong")
    break 
  
  
  
  


