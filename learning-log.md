//Day 1
What I Learned today:
I learnt how to introduce myself, study plans, and study time.

What I found confusing:
combining yesterdays and todays study time calculations.

What I changed or figured out by myself:
taught about it after starring at the code for a while.


Day 2
#String enables the storing of text in a variable.
#strip removes spaces at the begining and end, while .title capitalizes first letters of a Text.
#added title because i wanted to see how it worked

loops exercise
#range function used to specify looping duration
#break, ends the loop.


Day 3 & 4
Started a Python Development: Getting Started with Programming in Python course.
1. Got introduced to Jupyter, ran the installations, and played around with it.
2. Built in functions are part of the core programming lang, no import statements, functions in global namespace, no name variables with the same name as built in function
3. Data types, some str assigning a str to it.
4. lists are sequential containers that can change in size.
5. Sets are unindexed, unordered collections.
6. Dictionaries are an associative data type, map from keys to values
7. f strs are great way of avoiding errors, where we fail to match up input arguments with a format string.
8. List: ["", ""]

More for Day 4
1. Exceptions: problems in your code.

Day 5
1. Writing code that can handle errors. ValueError: when the user attempt to input a value not accepted.
2. use break when you want to end a loop. eg, while True:
    try:
        x = int(input("What is the value of x? "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
    else:
        break

print(f"The value of x is: {x}")
3. return: values from functions(can break too).
4. pass: on handling an error without prompting the user on a possible solution.
5. prompt
6. raise 

Libraries
are files of code you can use. modules(features built in it for reuse of code). 
1. random library(inbuilt modules). 
2. import allows u to import random modules. 
3. random.choice(seq). 
4. from(importing modules, allows you to be more specific)
5. random.randint(a, b): do things less predictable around a range.
6. random.shuffle(x): shuffles the argument in place
7. statistics: for calculating mean, average, modes, etc.
8. command-line arguments: inputs to the program just when you're executing it.
9. sys.argv[]
10. packages: 3rd party library for more functions.(pypi.org) cowsay (For now, use %pip install inside your notebooks when installing packages for notebook exercises.)

