TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

registered_users = {
   "bob":"123",
   "ann":"pass123",
   "mike":"password123",
   "liz":"pass123"}

username= input("Enter your username:")
password = input("Enter your password:")

separator= ("-" * 40)
print(separator)

def word_list(enter_number):
    chosen_text= TEXTS[enter_number-1]
    without_invisible_characters= chosen_text.replace("\n"," ")
    without_space= without_invisible_characters.split()
    return without_space

def upper_capital(enter_number):
    LIST = word_list(enter_number)
    count=[]
    for word in LIST:
        if word.istitle():
            count.append(word)
        else:
            continue
    return count

def all_words_capital(enter_number):
    LIST = word_list(enter_number)
    capital=[]
    for s in LIST:
        if s.isupper() and s.isalpha():
            capital.append(s)
        else:
            continue
    return capital

def all_words_lower(enter_number):
    LIST = word_list(enter_number)
    lower=[]
    for word in LIST:
        if word.islower():
            lower.append(word)
        else:
            continue
    return lower
    
def numeric_words(enter_number):
    LIST = word_list(enter_number)
    numeric=[]
    for h in LIST:
        if h.isnumeric():
            numeric.append(h)
        else:
            continue
    return numeric

if username not in registered_users.keys():
    print("unregistered user, terminating the program..")
elif registered_users[username] == password:
    print("Welcome to the app,",username,"\nWe have 3 texts to be analyzed.")
    print(separator)
    enter_number= input("Enter a number btw. 1 and 3 to select:")
    enter_number = int(enter_number)
    if enter_number in range(1,4):
        print(separator)
        clear_text=word_list(enter_number)
        print("There are",len(clear_text),"words in the selected text.")
        print("There are",len(upper_capital(enter_number)),"titlecase words.")
        print("There are",len(all_words_capital(enter_number)),"uppercase words.")
        print("There are",len(all_words_lower(enter_number)),"lowercase words.")
        print("There are",len(numeric_words(enter_number)) ,"numeric strings.")
        sum_words= sum(int(num) for num in numeric_words(enter_number))
        print("The sum of all the numbers",sum_words)

        print(separator)
        print(f"LEN|  OCCURENCES  |NR.")
        print(separator)
        """
        a simple bar graph that will represent the frequency of different word lengths in the text.
        """
        words = word_list(1)
        word_lengths = [len(word.strip(',.')) for word in words]
        word_length_counts = {}

        for lenght in word_lengths:
            word_length_counts[lenght] = word_length_counts.get(lenght, 0) + 1
            
        max_count = max(word_length_counts.values())

        for lenght in sorted(word_length_counts.keys()):
            count = word_length_counts[lenght]
            print(f"{lenght:3}|{'*' * count:14}|{count}")
    else:
        print("You have chosen incorrect number.") 
else:
    print("unregistered user, terminating the program..")
