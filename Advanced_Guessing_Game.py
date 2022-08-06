from ast import For
from Questions import Question
import random

question_list = [
    "\nWhat mammal in the 'Large Cats Family' (Felidae) is typically orange with several vertical like lines spreading from its torso to its tail?\n(a)Zebra\n(b)Leopard\n(c)Tiger\n(d)Okapi\n\n",
    
    "What bi-pedal animal beleonging to the species homosapiens that has been around for ruffly 200,000 years?\n(a)Aliens\n(b)Birds\n(c)Kangaroo\n(d)Humans\n\n",
    
    "What is the first name of the creator of this quiz?\n(a)Leon\n(b)Noel\n(c)Jay\n(d)Bob\n\n" 
]


questions =  [Question(question_list[0],("c")), 
             Question(question_list[1],("d")), 
             Question(question_list[2],("a"))
]
        

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.question) 
        if answer == question.answer:
            score += 1
    print("\nYour Score is "+ str(score) + " out of " + str(len(questions)))

run_test(questions)
