score = 0

def questionA(x):  #this is a function where a. is the only correct answer
    global score
    answer = input(x)    #the question can be addded as a parameter here
    while True:
        if answer.lower() == "a":
            print("""
Correct!""")
            score = score + 1
            print("""
Your current score is""",score)
            break

        elif answer.lower() == "b":
            print("""
Incorrect!""")
            print("""
Your current score is""",score)
            break

        elif answer.lower() == "c":
            print("""
Incorrect!""")
            print("""
Your current score is""",score)
            break

        elif answer.lower() == "d":
            print("""
Incorrect!""")
            print("""
Your current score is""",score)
            break

        else:
            print("""
Please type in a valid answer.""")
            return questionA(x)   #repeats the function

def questionB(y):  #this is a function where b. is the only correct answer
    global score
    answer = input(y)    #the question can be addded as a parameter here
    while True:
        if answer.lower() == "b":
            print("""
Correct!""")
            score = score + 1
            print("""
Your current score is""",score)
            break

        elif answer.lower() == "a":
            print("""
Incorrect!""")
            print("""
Your current score is""",score)
            break

        elif answer.lower() == "c":
            print("""
Incorrect!""")
            print("""
Your current score is""",score)
            break

        elif answer.lower() == "d":
            print("""
Incorrect!""")
            print("""
Your current score is""",score)
            break

        else:
            print("""
Please type in a valid answer.""")
            return questionB(y)      #repeats the function

def questionC(z):  #this is a function where c. is the only correct answer
    global score
    answer = input(z)    #the question can be addded as a parameter here
    while True:
        if answer.lower() == "c":
            print("""
Correct!""")
            score = score + 1
            print("""
Your current score is""",score)
            break

        elif answer.lower() == "b":
            print("""
Incorrect!""")
            print("""
Your current score is""",score)
            break

        elif answer.lower() == "a":
            print("""
Incorrect!""")
            print("""
Your current score is""",score)
            break

        elif answer.lower() == "d":
            print("""
Incorrect!""")
            print("""
Your current score is""",score)
            break

        else:
            print("""
Please type in a valid answer.""")
            return questionC(z)    #repeats the function

def questionD(a):  #this is a function where d. is the only correct answer
    global score
    answer = input(a)    #the question can be addded as a parameter here
    while True:
        if answer.lower() == "d":
            print("""
Correct!""")
            score = score + 1
            print("""
Your current score is""",score)
            break

        elif answer.lower() == "a":
            print("""
Incorrect!""")
            print("""
Your current score is""",score)
            break

        elif answer.lower() == "b":
            print("""
Incorrect!""")
            print("""
Your current score is""",score)
            break

        elif answer.lower() == "c":
            print("""
Incorrect!""")
            print("""
Your current score is""",score)
            break

        else:
            print("""
Please type in a valid answer.""")
            return questionD(a)   #repeats the function

question1 = """
1. How many planets are there in our solar system?
A. 6
B. 7
C. 8
D. 9"""

question2 = """
2. What country is in Central Asia?
A. Afghanistan
B. Mongolia
C. Armenia
D. Saint Kitts & Nevis"""

question3 = """
3. What is the increment of time in between each World cup?
A. 1 year
B. 2 years
C. 3 years
D. 4 years"""

question4 = """
4. When did WW1 start?
A. 1914
B. 1916
C. 1918
D. 1922"""

question5 = """
5. During which era were humans hunter gatherers?
A. Paleolithic Era
B. Neolithic Era
C. Ancient Era
D. Classical Era"""

question6 = """
6. Which of these is not an insect?
A. Spider
B. Cockroach
C. Butterfly
D. Ant"""

question7 = """
7. Which sea was Carthage located next to?
A. Red Sea
B. Indian Ocean
C. Mediterranean Sea
D. Caspian Sea"""

question8 = """
8. Who founded the company Apple?
A. Bill Gates
B. Bill Nye the Science Guy
C. Junehyuk Yoo
D. Steve Jobs"""

question9 = """
9. What does MOBA stand for?
A. Multiplayer Online Battle Action
B. Multplayer Online Baking Active
C. Mountain On Backstreet Action
D. Multiplayer Online Battle Arena"""

question10 = """
10. What element is Ba?
A. Balium
B. Barium
C. Badult
D. Bastrome"""

question11 = """
11. What is the world's largest desert?
A. Thar
B. Kalahari
C. Sahara
D. Sonoran"""

question12 = """
12. Where is Mount Everest located?
A. Nepal
B. Tibet
C. China
D. India"""

question13 = """
13. Which country is/was called the "Land of Rising Sun"?
A. Russia
B. Japan
C. Korea
D. Thailand"""

question14 = """
14. What is the hottest planet in the solar system?
A. Mercury
B. Venus
C. Jupiter
D. Uranus
"""

question15 = """
15. What is the largest ocean in the world?
A. The Indian Ocean
B. The Antarctic
C. The Atlantic Ocean
D. The Pacific Ocean"""

name = input("Hello there! What is your name?")

while True:
    intro = input("Hey " + name + ", would you like to take a quiz?")
    if intro.lower() == "yes":
        print("""
That's great! Lets go onto the first question""")
        break
    elif intro.lower() == "no":
        print("""
Are you sure?""")
        intro = input("So " + name + ", would you like to take the quiz?")
        if intro.lower() == "yes":
            print("""
That's great! Lets go onto the first question""")
            break
        elif intro.lower() == "no":
            print("""
Well you're gonna be missing out on some fun. Are you
really really sure?""")
            intro = input("Cmon " + name + ", wont you like to take the quiz?")
            if intro.lower() == "yes":
                print("""
That's great! Lets go onto the first question""")
                break
            elif intro.lower() == "no":
                print("""
I mean you get to learn new stuff. Who doesn't like
learning new stuff???""")
                intro = input(name + ", just take the quiz.")
                if intro.lower() == "yes":
                    print("""
That's great! Lets go onto the first question""")
                    break
                elif intro.lower() == "no":
                    print("""
I'm going to make you play.""")

                else:
                    print("""
I don't really understand that.""")
            else:
                print("""
I don't really understand that.""")

        else:
            print("""
I don't really understand that.""")

    else:
        print("""
I don't really understand that.""")

questionC(question1)
questionC(question2)
questionD(question3)
questionA(question4)
questionB(question5)
questionA(question6)
questionC(question7)
questionD(question8)
questionD(question9)
questionB(question10)
questionC(question11)
questionA(question12)
questionB(question13)
questionB(question14)
questionD(question15)

if score > 14:     #this is to show the grade you get at the end
    print("Your score was",score,", you get an A. Congrats!")
elif score >= 12:
    print("Your score was",score,", you get an A-. Pretty good!")
elif score >= 10:
    print("Your score was",score,", you get an B+.")
elif score >= 8:
    print("Your score was",score,", you get an B.")
elif score >= 5:
    print("Your score was",score,", you get an C. You can do better.")
elif score >= 3:
    print("Your score was",score,", you get an D. What are you doing?")
elif score >= 0:
    print("Your score was",score,", you get an F. You're pretty dumb.")
