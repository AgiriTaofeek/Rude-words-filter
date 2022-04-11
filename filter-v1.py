import string # import all the punctuation symbols to use the strip method to get rid of them

# There are two ways to open a file and close them
# solution 1
# my_file = open("read_me.txt")
# print(my_file.read())
# my_file.close()

# solution 2
# with open("read_me.txt") as my_file:
#     print(my_file.read())


# How to create a new file in writing mode and add content to it  
# with open("new_file.txt", "w") as file:
#     file.write("This my new writing")

# Open the file in reading mode    
# with open("new_file.txt", "r") as open:
#     content = open.read()
    
# print(content) 


# How to add the content of a old file to a new file
# Solution 1
# with open("old_file.txt") as old: #TODO i need add a file called old_file.txt to the folder
#     content = old.read()

# with open("new_file.txt", "w") as new:
#     new.write(content)
    
# with open("new_file.txt") as new:
#     content = new.read()
    
# print(content)

# Solution 2
# with open("old_file.txt") as old_file: #TODO add a file to the folder
#     with open("new_file.txt", "w") as new_file:
#         new_file.write(old_file.read())

# with open("new_file.txt") as new_file:
#     print(new_file.read())

# How to write to file in loop
# Solution 1
# with open("new.txt", "w") as new:
#     for i in range(0, 32, 2):
#         new.write(str(i))
#         new.write("\n")
# with open("new.txt") as new:
#     content = new.read()
    
# print(content)      
    
# Code to look for bad words and repace with asterisks
# import string # Import the string module so we can use string.punctuation
# test_words = ["crap", "darn!", "Heck!!!", "jerk...", "idiot?", "butt", "devil"]

# def bleeper(word):
#     pos = 0 # Track the position (index) of the character so we can replace it
#     for character in word:
#         if character not in string.punctuation:
#             character = "*" # If it wasn't punctuation, replace it
#         word = word.replace(word[pos], character) # Replace the character at the current position
#         pos += 1 # Move to the next character position
#     return word

# for word in test_words:
#     print(bleeper(word))    

rude_words = ["crap", "darn", "heck", "jerk", "idiot", "butt", "devil"]

# function to split the a line of sentence into strings of words and check if some of the stringed words is in the rude_word list
def check_line(line):
    rude_count = 0 # counter start
    words = line.split(" ")
    for word in words:
        word = word.strip(string.punctuation).lower() # Removes punctuations and convert to lowercase since all the words in rudeword list are in lower case
        if word in rude_words:
            rude_count += 1
            print(f"Found rude word: {word}")
    return rude_count # returns the count to the index of where a rude word was found

# function that checks for a filename and keep file open when in use and closes it when not in use
def check_file(filename):
    with open(filename) as myfile:
        rude_count = 0
        for line in myfile: # For line loop is a special python loop to check for words in one line at a time instead of checking through the whole lines  of code
            rude_count += check_line(line)

    if rude_count == 0:
        print("Congratulations, your file has no rude words.")
        print("At least, no rude words I know.")

# Script footer 
if __name__ == '__main__':
    check_file("my_story.txt") #TODO I have to add a file to the folder in this case my_story.txt