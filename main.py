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
      "\u001b[35m╚═╝░░░░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝  ░░░╚═╝░░░░╚═════╝░╚═╝╚══════╝\n"
     "\033[37mYou have 1 minute to answer each question\n"
     "__________________________________________________________________________")
# Imports 
import time
from termcolor import colored
import os

 # Lists
questions = [  "What is 3 multiplied by 4?",
    "What is the product of 7 and 2?",
    "If you have 8 groups of 5 apples, how many apples do you have in total?",
    "What is the result of 9 multiplied by 0?",
    "If there are 4 people in a room and each person has 2 bags, how many bags are in the room altogether?",
    "What is the value of 6 multiplied by 9 minus 3?",
    "If you have 12 cupcakes and you want to give 3 cupcakes to each of your 4 friends, how many cupcakes will you have left?",
    "What is 8x3?",
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
    24,
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
def display_question(question_number, question):
    print("Question", question_number, question)


def get_answer():
    try:
        answer = int(input("Answer: "))
        return answer
    except ValueError:
        print(colored("Wrong","red"))
        return None


def check_answer(answer, correct_answer):
    if answer == correct_answer:
        print(colored("Correct!~", "green", attrs=["bold"]))
        return True
    else:
        print(colored("Wrong","red"))
        return False


def play_game():
    score = 0
    time_per_question = 60
    start_time = time.time()

    for i in range(len(questions)):
        display_question(i+1, questions[i])
        answer = get_answer()

        if answer is None:
            break

        end_time = time.time()
        time_taken = end_time - start_time
        if time_taken > time_per_question:
            print(colored("Time up!","red"))
            break

        print("Time taken: {:.2f} seconds".format(time_taken))
        if check_answer(answer, answers[i]):
            score += 1
        else:
            break

    total_time_taken = end_time - start_time
    print("Total time taken: {:.2f} seconds".format(total_time_taken))

    return score


def read_high_score():
    if not os.path.exists("high_score.txt"):
        with open("high_score.txt", "w") as f:
            f.write("0")
    with open("high_score.txt", "r") as f:
        high_score = int(f.read())
    return high_score


def write_high_score(new_high_score):
    with open("high_score.txt", "w") as f:
        f.write(str(new_high_score))


# Scripts 
final_score = play_game()
print("Your score is {}/{}".format(final_score, len(questions)))

current_high_score = read_high_score()
print("Your high score is {}/{}".format(current_high_score, len(questions)))
if final_score > current_high_score:
    print("New high score!")
    write_high_score(final_score)
 
    
  
  
  
  


