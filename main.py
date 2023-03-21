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
questions = [  "What is 3 multiplied by 4?",
    "What is the product of 7 and 2?",
    "If you have 8 groups of 5 apples, how many apples do you have in total?",
    "What is the result of 9 multiplied by 0?",
    "If there are 4 people in a room and each person has 2 bags, how many bags are in the room altogether?",
    "What is the value of 6 multiplied by 9 minus 3?",
    "If you have 12 cupcakes and you want to give 3 cupcakes to each of your 4 friends, how many cupcakes will you have left?",
    "What is the product of 8 and 3.5?",
    "If you have 10 boxes, and each box contains 20 pens, how many pens do you have in total?",
    "What is the result of 7 multiplied by 1,000?",
    "If you have 15 packs of gum and each pack contains 10 pieces of gum, how many pieces of gum do you have in total?",
    "What is the value of 5 multiplied by 3 raised to the power of 2?",
    "If there are 24 students in a class, and each student has 5 pencils, how many pencils are in the class altogether?",
    "What is the product of 6.5 and 2.5?",
    "If you have 3 bags of marbles and each bag contains 12 marbles, how many marbles do you have in total?",
    "What is the result of 9 multiplied by 99?",
    "If you have 18 crayons and you want to give 2 crayons to each of your 7 friends, how many crayons will you have left?",
    "What is the product of 0.5 and 0.2?",
    "If there are 5 boxes, and each box contains 6 books, how many books do you have in total?",
    "What is the value of 7 multiplied by 6 raised to the power of 2?"
]
answers = [ 12,
    14,
    40,
    0,
    8,
    51,
    0,
    28,
    200,
    7000,
    150,
    45,
    120,
    16.25,
    36,
    891,
    4,
    0.1,
    30,
    252]
   
# Functions 





# Scripts 
score = 0 
for i in range(len(questions)):
  print("Question", i+1, questions[i])
  try:
    answer = int(input("Answer: "))
  except ValueError:
    print("Wrong")
    break
  if answer == answers[i]:
    print("Correct")
    score = score+1
  else: 
    print("Wrong")
    print("Your score is {}{}".format(score, "/20"))
    break
    
  
  
  
  


