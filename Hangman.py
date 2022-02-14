import random as r 
from word_list import words 

man_condition = [
'''
    +---+
        |
        |
        |
       ===

''',
'''
    +---+
    O   |
        |
        |
       ===
''',
'''
    +---+
    O   |
    |   |
        |
       ===
''',
'''
    +---+
    O   |
   /|   |
        |
       ===

''',
'''
    +---+
    O   |
   /|\  |
        |
       ===
''',
'''
    +---+
    O   |
   /|\  |
   /    |
''',
'''
    +---+
    O   |
   /|\  |
   / \  |
''',
'''
    +---+
   o̴|   |
   /|\  |
   / \  |
''',
'''
   !!!
   \O/  
    |   
   / \  
'''

]   

replace = []
guessed_words = []
def printing(a):
    output = ""
    for i in range (len(a)):
        output += a[i]
        output += " "
    return output

print('''Welcome to Hangman!!!
You are here to save this man 
  
   \O/ 
    |   
   / \ 
   
by guessing the word I give you
Enjoy!!!''')    

word = list(r.choice(words))
len_of_word = len(word)
for i in range (len_of_word):
    replace.append("*")
   
print(printing(replace))

def substitute():
    global string, word, replace
    for i in range (len(word)):
        if word[i] == string:
            replace[i] = string 

def not_guessed ():
    global lives,replace,  man_condition
    lives -= 1
    print(man_condition[7-lives]) 
    print("try again.. you must save him")
    print("remaining tries ", lives)
    print(printing(replace))

def guessed ():
    global lives,replace, man_condition 
    substitute()
    print(man_condition[7-lives])
    print("good one.. but not there yet") 
    print(printing(replace))  

def win ():
    global lives
    print("You saved him")
    print(man_condition[-1])
    if lives == 7:
        print("OH thats a flawless run")
    print("you won with ",lives," lives to spare")

def lost():
    global word
    print("you lost it")
    if guessed_words == []:
        print('''without guessing even a single letter''')
    print("The word was actually ", word)

lives = 7 

while lives>0: 
    string = str(input())
    if len(string) >= 2:
        print("Please enter only one letter at a time")
    
    else:
        if string == ""or string == " ":
            print("Thats a blank attempt.. try again")
        elif string not in guessed_words:
            if string in word:
                guessed()
                if replace != word:
                    pass
                else:
                    win()
                    break
            else:
                not_guessed()
        else:
            print("You already guessed it.. try again")
        
    


    guessed_words.append(string)    
    

if lives == 0:
    lost()   
