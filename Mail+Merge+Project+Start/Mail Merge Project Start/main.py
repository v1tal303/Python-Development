#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Letters/starting_letter.txt") as file:
    text = file.readlines()
    first_line = text[0]
    rest = text[1:]

with open("./Input/Names/invited_names.txt") as file:
    txt = file.readlines()
    names = []
    for i in txt:
        names.append("Dear " + i.strip("\n") + "\n")

for i in names:
    file_name = i.strip("\n")
    text[0] = i
    with open(f"./Output/ReadyToSend/{file_name}.txt", "w") as file:
        for i in text:
            file.write(i)

    print(text)



