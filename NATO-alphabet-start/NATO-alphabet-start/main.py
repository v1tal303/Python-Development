student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:

#Read pandas csv
nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")

#Create a python dictionary from csv
nato_dict = {row.letter:row.code for (index, row) in nato_data.iterrows()}
print(nato_dict)


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

error = True

while error == True:
    #User input capitalized and spaces replaced
    user_input = input("What is your name?").upper().replace(" ", "")

    #Split the input into list of letters
    user_letter = [letter for letter in user_input]

    #Match the list of letters to the dictionary
    try:
        user_nato_name = [nato_dict[letter] for letter in user_letter]
    except KeyError:
        print("Please only use letters")
    else:
        print(user_nato_name)
        error = False