"""Docstring: I developed this game based on the first book/movie
of Harry Potter. As the fans of Harry Potter would know, he passed
through plenty of adventures; however, I wanted to reflect on the
last part of the movie. In this part, Harry potter has overcome
several challenges for retrieving the Sorcerer Stone. The user will
always choose among four possible answers, and each question has
1 correct and 3 wrong answers. The purpose of this game is to practice all
the concepts that we learned in class."""
# import random library
import random as rd
# import copy library/ no need of installing any package
import copy as cp


# import datetime library

# The first question is about the name of the user to personalize the experience

def introduction():
    # secure that the user enter his name an make a while true the user enter at least more than one character
    while True:
        # declare the variable name
        name = input(prompt="What is your name? \n>")
        # make the first if statement in which I asked if the name is empty
        if name == "":
            # print the message in case the variable name is empty
            print("please type your name again")
        else:
            # in case is not empty, the code continues
            break
    # Introduction of the game
    print(f"""{'*' * 100}
Welcome {name.strip().capitalize()}, this is a game based on Harry Potter, the child who survived against the 
evilest and most powerful wizard, Voldermort. After his parents having been murdered by Voldermort, Harry didn\'t
know that he was a wizard until he turned 11 years old. Hagrid, the guard of the forbidden Forest, 
rescued him from his uncle and told him the entire truth. Harry met his two best friends in Hogwarts:
Hermione and Ron. Harry, with the help of his friends, has to beat Voldermort to avoid that he obtains the
Sorcerer’s Stone, which can give him back his power and eternal life.
So now {name.strip().capitalize()}, it is your turn to help Harry Potter to beat the wizard, whom you must not repeat his name, 
and retrieve the Sorcerer’s Stone.

You have only 2 opportunities for each stage

Are you ready? 
Press ENTER to continue.""")
    # the input to continue playing
    key1 = input(prompt=">")
    # the first Question
    room1()


# declaring a variable of wrong answers for the first question
lst_a1 = ["Invoke fire towards the monster.",
          "Summon a sword to start cutting it.",
          "Convoke flying broom to escape.",
          "Despair and do nothing.",
          "Spell a secret charm to destroy it.",
          "Cast Abracadabra to float the plant and run away."]
# declaring a variable of possible responses for each answer of the first question
lst_c1 = ["Wrong Answer: I am really sorry, you burnt all your friends.",
          "Wrong Answer: I am really sorry, noone knows how to summon a sword.",
          "Wrong Answer: I am really sorry, even if someone knew how to do it, they wouldn\'t be able to escape.",
          "Wrong Answer: I am really sorry, if you despair the plant will notice and twist you harder.",
          "Wrong Answer: The students are in their first year so they don\'t know secret casts.",
          "Wrong Answer: I am really sorry, the plant is too big for making it float.",
          "Good Work!"]

# declaring the correct answer of the first question in a variable
correctanswer1 = """Calm down and wait that the plant releases you"""

# declaring a variable of wrong answers for the second question
lst_a2 = ["Levitate and try to use different keys to crack the opening.",
          "Stop time with a spell and fly in the magic mop to grab something to help you open the door.",
          "Use the Alohomora charm.",
          "Teleport to the other side of the wall.",
          "Set the whole room on fire to burn the wood.",
          "Convoke a troll to break the entrance for you."]

# declaring a variable of possible responses for each answer of the second question
lst_c2 = ["Wrong Answer: I am really sorry, Harry and his friends don\'t know how to levitate yet.",
          "Wrong Answer:I am really sorry, Harry and his friends don\'t know how to stop time.",
          "Wrong Answer:I am really sorry, Hermione tried and it didn\'t work.",
          "Wrong Answer:I am really sorry, Harry and his friends don\'t know how to teleport to other places.",
          "Wrong Answer:I am really sorry, you have done severe harm to your friends.",
          "Wrong Answer:I am really sorry, the troll ended up killing Harry and his friends.",
          "Good Work!"]

# declaring the second correct answer in a variable
correctanswer2 = """Flying in circles in the broom until you see an opener for the gate"""

# declaring a variable of wrong answers for the third question
lst_a3 = ["Send Hermione, the rook, to kill the pawn behind her.",
          "Send Harry Potter, the bishop, to attack the horse that is diagonally in front of him.",
          "Perform an explosion charm against the opposing King.",
          "Order Harry Potter to set fire to the chessboard.",
          "Use the cloak of invisibility to pass unnoticed to the next stage.",
          "Say a levitation spell towards all the pieces and you run down below the pieces."]

# declaring a variable of possible responses for each answer of the third question
lst_c3 = ["Wrong Answer: I am really sorry, that is a bad move.",
          "Wrong Answer: I am really sorry, that is a bad move.",
          "Wrong Answer: I am really sorry, the pieces are not affected by magic. Good try, though!",
          "Wrong Answer: I am really sorry, the pieces are not affected by fire. Good try, though!",
          "Wrong Answer: I am really sorry, the pieces still can feel your presence.",
          "Wrong Answer: I am really sorry, the pieces are not affected by magic. Good try, though!",
          "Good Work!"]

# declaring the correct answer in a variable
correctanswer3 = """Send Ron, who is playing knight, to sacrifice himself by checking so that Harry can then kill the King."""


# declaring a fail function in case the user loses
def fail():
    # make a stop to allow the user exit the game
    print(""" 

  ________                        ________                     
 /  _____/_____    _____   ____   \_____  \___  __ ___________ 
/   \  ___\__  \  /     \_/ __ \   /   |   \  \/ // __ \_  __ \

\    \_\  \/ __ \|  Y Y  \  ___/  /    |    \   /\  ___/|  | \/
 \______  (____  /__|_|  /\___  > \_______  /\_/  \___  >__|   
        \/     \/      \/     \/          \/          \/       


    """)
    restart = input(prompt="""Do you want to play again?
Please type your answer:
>""")
    while True:
        # remove all the especial character
        for char in restart:
            # looking for the especial character
            if char in "?.!/;:)(*%$#@^&-_+= ":
                # replacing the especial character
                restart = restart.replace(char, '')
                # asking if the answer was positive
        if restart.casefold().strip() in ('y', 'yes', 'affirmative', '1'):
            # in case is positive we are going to send the user to the starting point of the game
            introduction()
            break
        # ask if the answer was negative
        elif restart.casefold().strip() in ('n', 'no', 'negative', '2'):
            input(prompt="""< Press any key to exit >
>""")
            # in case is negative we finish the game
            break
        # in case we don't understand the answer we ask to the user that enter again his response
        elif restart.casefold().strip() not in ("n", "no", "y", "yes"):
            # making a statement that the system didn't get the responso
            print("I didn't understand, please try again")
            input(prompt="< Press any key to exit >")
            break
        else:
            continue


# declaring a win function in case the user win
def win():
    # make a stop to allow the user to exit when he wins
    input(prompt="""< Press any key to exit >
>""")
    # print congratulation
    print("""
_________                                     __        .__          __  .__                     ._.
\_   ___ \  ____   ____    ________________ _/  |_ __ __|  | _____ _/  |_|__| ____   ____   _____| |
/    \  \/ /  _ \ /    \  / ___\_  __ \__  \\   __\  |  \  | \__  \\   __\  |/  _ \ /    \ /  ___/ |
\     \___(  <_> )   |  \/ /_/  >  | \// __ \|  | |  |  /  |__/ __ \|  | |  (  <_> )   |  \\___ \ \|
 \______  /\____/|___|  /\___  /|__|  (____  /__| |____/|____(____  /__| |__|\____/|___|  /____  >__
        \/            \//_____/            \/                     \/                    \/     \/ \/

       """
          )


# make a function to have 3 random fake answers
# lst = the list of fake answers, n = quantity of fake answers that every question is going to have
# c_ans = is the correct answer that is going to be included in the list of random fake answers
def random(lst, n, c_ans):
    """This function helps the game to make a random selection among answers and place the correct answer
to a random position.
The argumentes are:
lst = the list of wrong answers,
n = quantity of fake answers that every question is going to have
c_ans = is the correct answer that is going to be included in the list of wrong answers"""
    # declare the variable that is going to content my final result
    result = []
    x = 0
    # Use sample function of the random library to choose only 3 fake answers of the 6 fake answers
    result = rd.sample(lst, n)
    # use random interger function of the random library to have a random number
    x = rd.randint(0, n)
    # the random number is used to insert the correct answer in a random position in the list of fake answers.
    result.insert(x, c_ans)
    # return the final result
    return result


# declare a function that is going to help me to transform a list into a organize text of possible answers.
def makelist(lst):
    """This function assembles the individual parts of the sentence into one text.
The arguments are:
lst = the list of items that you want to transform into a big text"""
    # declare a variable that is going to be the starting point
    a = 0
    # declare a variable that is going to store my final result
    result = ""
    # make a loop to translate the previous list into a text with numbers.
    for i in lst:
        # make a counter that is going to be use to number every possible answer
        a += 1
        # start to concatening my text of possible answers.
        result = result + f"""
        {a}) {i}"""
        # return the final result
    return result


# make a function that is going to help me evaluate the answers of the user
# lst = the random list of fake answers, choice = user choice,
# lst2 = the list of possible responses to the answer of the user,
# c_ans = correct answer, list3 = the list with the random position of the fake and correct answer
def coorectans(lst, choice, lst2, c_ans, lst3):
    """This function evaluates the answers of the user
The argumentes are:
lst = the random list of wrong answers
choice = user choice
lst2 = the list of possible responses to the answer of the user
c_ans = correct answer
list3 = the list with the random position of the wrong and correct answer
"""
    # declare the variables that are going to help me to store all the information that I want
    analyze = ""
    result = ""
    t = ""
    ind = 0
    a = 0
    # make a loop to evaluate every item in the list
    for i in lst:
        # make a counter to evaluate if the user type a number as a possible answer
        a += 1
        # handling error if the input of the user is a number or a string

        try:
            # try to transform the choice of the user into a interger
            choice = int(choice)
        except:
            choice = choice.casefold().strip()
            # convert the answer of the user and my possible answers in a lowercase string without spaces at the end or beginning
            for char in "?.!/;:)(*%$#@^&-_+=":
                if char in choice:
                    choice = choice.replace(char, '')
        try:
            # try to transform the choice of the user into a interger
            choice = int(choice)
        except:
            choice = choice.casefold().strip()
            # convert the answer of the user and my possible answers in a lowercase string without spaces at the end or beginning
            for char in "?.!/;:)(*%$#@^&-_+=":
                if char in choice:
                    choice = choice.replace(char, '')

        # transform the correct answer in lower case without special characters and the retire the blank spaces at the end and the beggining
        c_ans = c_ans.casefold().strip()
        # make a copy of the element of the list and store in variable t
        t = cp.copy(i)
        # make a casefold and strip of this variable
        t = t.casefold().strip()
        # if the type of the choice is a integer then we are going to explore this path
        listsplit = t.split(' ')
        resultlist = []
        # spliting our possible answers to analyze if we have some of them in the user's response
        for item in listsplit:
            if len(item) > 3:
                # append only the words that have more than 3 characters to avoid pronouns
                resultlist.append(item)

        if type(choice) == int:
            # if the choice match
            if a == int(choice):
                # if the choice is the correct answer
                if t == c_ans:
                    # we going to display to the user "Good Work!"
                    result = lst2[-1]
                else:
                    # if it is not the correct answer, we are going to analyze in which position the answer is of the original list of fake answer
                    # because every answer has a specific response and is set in the same order of the fake answers.
                    analyze = i
                    # we look for the position of the fake answer
                    ind = lst3.index(analyze)
                    # we set response for that specific fake answer into the result variable
                    result = lst2[ind]
                # break statement to stop the loop
                break
                # if the choice is not a integer we are going to look with the in function where it can be the possible answer
        elif choice in t:
            # if the string that the user typed is the correct answer
            if t == c_ans:
                # let's store the specific response for the correct answer
                result = lst2[-1]
            else:
                # let's analyze the incorrect answer and search it the list of fake answers
                analyze = i
                # we search the incorrect answer with index function
                ind = lst3.index(analyze)
                # we store the incorrect result
                result = lst2[ind]
            break
        else:
            for z in resultlist:
                if z in choice.casefold().strip():
                    # if the string that the user typed is the correct answer
                    if t == c_ans:
                        # let's store the specific response for the correct answer
                        result = lst2[-1]
                        break
                    else:
                        # let's analyze the incorrect answer and search it the list of fake answers
                        analyze = i
                        # we search the incorrect answer with index function
                        ind = lst3.index(analyze)
                        # we store the incorrect result
                        result = lst2[ind]
                        break

        # if we didn't have a positive result for the search, we understand that we didn't find in any answer the response of the user
    if result == "" or choice == "":
        # we set a specific response for this situation
        result = """Sorry I didn't understand. I am smart, but not AS smart, so please try again."""
    # the final return of my function
    return result


# definition of the function that is going to store the room1

# define how is going to be question and answers in the first room
def room1():
    # declare my global variable because the player is going to have only 4 lives
    life = 2
    # declare my local variable for the defined function
    yesorno = ""
    # Make a while to repeat several time the stage until the user lost his lives
    while True:
        # print the first question
        print(f"""
{'*' * 100}
You are with Harry Potter, Ron and Hermione. You must go to retrieve 
the Sorcerer's Stone. Harry knows that Dumbledore saved the stone on the third 
floor and has placed several traps. Moreover, the floor is forbidden to students 
including Harry. When he arrived at the first test, luckily for him, the giant 
dog of three heads was sleeping. Nevertheless, Harry fell down into a big 
plant, Devil's Snare, that started to twist snake-like tendrils around his 
ankles. Now you have to help Hermione remember what Professor Sprout said
in class.
Select what you think the professor taught about fighting the Devil's Snare:""")
        # convoke the function that I created for look into the list of fake answers and possible comments to any answer and store into a variable
        # store the possible answers of the question 1 in list format. One of them contains the correct answer
        pos_ans_1 = random(lst_a1, 3, correctanswer1)
        # store all the possible answers in one big text
        pos_ans_1_txt = makelist(pos_ans_1)
        # print the variable that contents the random possible answer with the correct answer included
        print(pos_ans_1_txt)
        # store the first response of the user
        choice_1 = input(prompt="""Please type your answer here:
>""")

        rs1 = coorectans(pos_ans_1, choice_1, lst_c1, correctanswer1, lst_a1)

        # let's make a counter variable that helps me count the chances of the user
        life -= 1
        # let's analyze if the user's response is empty
        try:
            long = len(choice_1.strip().casefold())
        except:
            long = 40
        # let's do a if statement to see what happen according the comment answer
        # if is empty we must ask the user that repeat again his responser
        if long == 0:
            print("Please type something")
            input(prompt="""<Press ENTER to continue>
>""")
            # add a chance to the user because technically he didn't make a mistake.
            life += 1
        elif rs1 == 'Good Work!':
            # if the comment answer was a good work, he pass to the level 2
            print(f"""
{'*' * 100}
{rs1}
{'*' * 100}
            """)
            input(prompt="""<Press ENTER to continue>
>""")
            room2()
            break
        elif rs1 == """Sorry I didn't understand. I am smart, but not AS smart, so please try again.""":
            # if the comment answer tells you to try again, it's gonna repeat again the room 1
            print(rs1)
            input(prompt="""<Press ENTER to continue>
>""")
            # add a chance to the user because technically he didn't make a mistake.
            life += 1
        elif life == 0:
            # print game over to the user
            print(f"""
{'*' * 100}
{rs1}
{'*' * 100}
            """)
            print("Game over! Thank you for trying!")
            # make a stop to the user can read what is happening
            input(prompt="""<Press ENTER to continue>
>""")
            fail()
            break
        else:
            # printing the response for a wrong answer
            print(f"""
{'*' * 100}
{rs1}
{'*' * 100}
            """)
            print("Do you want to try again?")
            while True:
                yesorno = input(prompt="""please type your response here:
>""")
                # let's retire all the especial character in case the user's response is a string
                for char in yesorno:
                    if char in "?.!/;:)(*%$#@^&-_+=1234":
                        # replacing the especial characters
                        yesorno = yesorno.replace(char, '')
                # searching the answer of the user in yes or y
                if yesorno.casefold().strip() in ("y", "yes", "affirmative", 'yeah', 'sure', 'ok', 'okay'):
                    # print game over to the user
                    print(f"""{'*' * 100}
You lost a chance. And now you have {life} more.
{'*' * 100}""")
                    # make a stop to the user can read what is happening
                    input(prompt="""<Press ENTER to continue>
>""")
                    # break to assure not to loop
                    break
                elif yesorno.casefold().strip() in ("n", "no"):
                    # make a pause to the user
                    input(prompt="""<Press ENTER to continue>
>""")
                    # convoke a fail function
                    fail()
                    # break to assure not to loop
                    break
                elif yesorno.casefold().strip() not in (
                "n", "no", "y", "yes", "affirmative", 'yeah', 'sure', 'ok', 'okay'):
                    # make a pause to the user and tell the user that I didn't understand and repeat again
                    print('Please try again. I didn\'t understand')
                    input(prompt="""<Press ENTER to continue>
>""")
                else:
                    continue


def room2():
    life = 2
    yesorno = ""
    while True:
        # print the second question for the user
        print(f"""
{'*' * 100}
Now that you passed the first challenge, there is another one for you to pass. You entered 
another room, in which there are a lot of flying keys. Only one of them can open the door, 
but you don't know which. 
What do you do?""")
        # store the possible answers of the question 2 in list format. One of them contains the correct answer
        pos_ans_2 = random(lst_a2, 3, correctanswer2)
        # store all the possible answers in one big text
        pos_ans_2_txt = makelist(pos_ans_2)
        # print the possible answers
        print(pos_ans_2_txt)
        # store the second response of the user
        choice_2 = input(prompt="""Please type your answer here:
>""")

        # let's convoke and store the function to evaluate the answer and response according to your answer
        rs2 = coorectans(pos_ans_2, choice_2, lst_c2, correctanswer2, lst_a2)

        # let's make a counter variable that helps me count the chances of the user
        life -= 1
        try:
            long = len(choice_2.strip().casefold())
        except:
            long = 40
        # let's do a if statement to see what happen according the comment answer
        # if is empty we must ask the user that repeat again his responser
        if long == 0:
            print("Please type something")
            input(prompt="""<Press ENTER to continue>
>""")
            # add a chance to the user because technically he didn't make a mistake.
            life += 1
        elif rs2 == 'Good Work!':
            # print the response according the user's answer
            print(f"""
{'*' * 100}
{rs2}
{'*' * 100}
            """)
            # if the comment answer was a good work, he pass to the level 3
            input(prompt="""<Press ENTER to continue>
>""")
            room3()
            break
        elif rs2 == """Sorry I didn't understand. I am smart, but not AS smart, so please try again.""":
            print(rs2)
            # if the comment answer tells you to try again, it's gonna epeat again the room 2
            input(prompt="""<Press ENTER to continue>
>""")
            # add a chance to the user because technically he didn't make a mistake.
            life += 1
        elif life == 0:
            print(f"""
{'*' * 100}
{rs2}
{'*' * 100}
            """)
            # print game over to the user
            print("Game over! Thanks for trying!")
            # make a stop to the user can read what is happening
            input(prompt="""<Press ENTER to continue>
>""")
            fail()
            break
        else:
            # printing the response for the wrong answer
            print(f"""
{'*' * 100}
{rs2}
{'*' * 100}
            """)
            # if you loose it's going to lead the user for this path and question if he wants to try again
            print('Do you want to try again?')
            # making a loop that will stop when the user choose a correct answer or he quit the game
            while True:
                # declaring a yes or no question
                yesorno = input(prompt="""please type your answer here:
>""")
                # let's retire all the especial character in case the user's response is a string
                for char in yesorno:
                    if char in "?.!/;:)(*%$#@^&-_+=":
                        yesorno = yesorno.replace(char, '')
                if yesorno.casefold().strip() in ("y", "yes", 'yeah', 'sure', "affirmative", 'ok', 'okay'):
                    # print game over to the user
                    print(f"""{'*' * 100}
You lost a chance. And now you have {life} more.
{'*' * 100}""")
                    # make a stop to the user can read what is happening
                    input(prompt="""<Press ENTER to continue>
>""")
                    # break to assure not to loop
                    break
                elif yesorno.casefold().strip() in ("n", "no"):
                    # make a pause to the user
                    input(prompt="""<Press ENTER to continue>
>""")
                    # convoke a fail function
                    fail()
                    # break to assure not to loop
                    break
                elif yesorno.casefold().strip() not in (
                "n", "no", "y", "yes", "affirmative", 'yeah', 'sure', 'ok', 'okay'):
                    # make a pause to the user and tell the user that I didn't understand and repeat again
                    print('Please try again. I didn\'t understand.')
                    input(prompt="""<Press ENTER to continue>
>""")
                    # break to assure not to loop


def room3():
    life = 2
    yesorno = ""
    rand = []
    rand = ['Harry won Voldermort', 'Harry lost against Voldermort', 'Harry is afraid and he run away from Voldermort']
    choice = rd.randint(0, 2)
    final_choice_a = rand[choice]

    while True:
        # print the second question for the user
        print(f"""
{'*' * 100}
Now that you passed the second trial, there is one last challenge you must help Harry to pass. 
You enter another room, in which a magic chess game takes place. In order for our heroes to pass, they have to
play deadly moves as Harry, Ron and Hermione are part of the black pieces as a Bishop, Knight, and Castle 
(Rook). Ron helped you to make some moves. However, you must decide on the last move. 
What are you going to do?.""")
        # store the possible answers of the question 1 in list format. One of them contains the correct answer
        pos_ans_3 = random(lst_a3, 3, correctanswer3)
        # store all the possible answers in one big text
        pos_ans_3_txt = makelist(pos_ans_3)
        # print the possible answers
        print(pos_ans_3_txt)
        # store the third response of the user
        choice_3 = input(prompt="""Please type your answer here:
>""")
        # convoke the function that helps me to analyze if the input choice of the user is the correct one
        rs3 = coorectans(pos_ans_3, choice_3, lst_c3, correctanswer3, lst_a3)
        # let's make a counter variable that helps me count the chances of the user
        life -= 1
        try:
            long = len(choice_3.strip().casefold())
        except:
            long = 1
        # let's do a if statement to see what happen according the comment answer
        # if is empty we must ask the user that repeat again his responser
        if long == 0:
            print("Please type something")
            input(prompt="<Press ENTER to continue.>")
            # add a chance to the user because technically he didn't make a mistake.
            life += 1
        elif long == 4 and choice_3.strip().casefold() == 'send':
            # print the response according the user's answer
            print('Please specify who you want to send')
            input(prompt="""<Press ENTER to continue>
>""")
            # add a chance to the user because technically he didn't make a mistake.
            life += 1
        elif choice_3.strip().casefold() == 'harry' or choice_3.strip().casefold() == 'harry potter':
            # print the response according the user's answer
            print('Please be more specific')
            input(prompt="""<Press ENTER to continue>
>""")
            # add a chance to the user because technically he didn't make a mistake.
            life += 1
        elif rs3 == 'Good Work!':
            # print the response according the user's answer
            print(f"""
{'*' * 100}
{rs3}
{'*' * 100}
            """)
            # if the comment answer was a good work, he finished the fame
            print(f"""Congratulations! You helped Harry Potter to reach the last stage. From now on, he has
to defeat Voldemort by himself.
Now let's see what happened with Harry.
{'*' * 100}
{final_choice_a}
{'*' * 100}
""")
            input(prompt="""<Press ENTER to continue>
>""")
            win()
            break
        elif rs3 == """Sorry I didn't understand. I am smart, but not AS smart, so please try again.""":
            # print the response according the user's answer
            print(f"""
{'*' * 100}
{rs3}
{'*' * 100}
            """)
            # if the comment answer tells you to try again, it's gonna repeat again the room 3
            input(prompt="""<Press ENTER to continue>
>""")
            # add a chance to the user because technically he didn't make a mistake.
            life += 1

        elif life == 0:
            # print the response according the user's answer
            print(f"""
{'*' * 100}
{rs3}
{'*' * 100}
            """)
            # print game over to the user
            print("Game over! Thanks for trying!")
            # make a stop to the user can read what is happening
            input(prompt="""<Press enter to continue>
>""")
            fail()
            break
        else:
            # printing the response of the wrong answer
            print(f"""
{'*' * 100}
{rs3}
{'*' * 100}
            """)
            # if you loose it's going to lead the user for this path and question if he wants to try again
            print('Do you want to try again?')
            # doing a inner loop to assure that the user only use yes or no
            while True:
                yesorno = input(prompt="""please type your answer:
>""")
                # let's retire all the especial character in case the user's response is a string
                for char in yesorno:
                    if char in "?.!/;:)(*%$#@^&-_+=":
                        yesorno = yesorno.replace(char, '')
                if yesorno.casefold().strip() in ("y", "yes", 'sure', 'yeah', 'affirmative', 'ok', 'okay'):
                    # print game over to the user
                    print(f"""{'*' * 100}
You lost a chance. And now you have {life} more.
{'*' * 100}""")
                    # break to assure not to loop
                    break
                elif yesorno.casefold().strip() in ("n", "no"):
                    # make a pause to the user
                    input(prompt="""<Press ENTER to continue>
>""")
                    # convoke a fail function
                    fail()
                    # break to assure not to loop
                    break
                elif yesorno.casefold().strip() not in (
                "n", "no", "y", "yes", 'sure', 'yeah', 'affirmative', 'ok', 'okay'):
                    # make a pause to the user and tell the user that I didn't understand and repeat again
                    print('Please try again. I didn\'t understand')
                    input(prompt="""<Press ENTER to continue>
>""")
                else:
                    continue
                    # break to assure not to loop


# start the game
introduction()
