# Problem Set 1: Indexing and Slicing Strings
# Basic Indexing:
# Given the string magic = 'abracadabra',
# a. Retrieve the 5th character.
magic = "abracadabra"
result = magic
print(result[4:5])
# b. Retrieve the second to last character.
print(result[-2])
# c. Find the first occurrence of the letter 'c'.
print(result.find("c"))
# Advanced Slicing:
# Given the string alphabet = 'abcdefghijklmnopqrstuvwxyz',
magic_2 = "abcdefghijklmnopqrstuvwxyz"
result_2 = magic_2
# a. Extract the letters 'hij'.
substring = (result_2.find("hij"))
print(substring)
# b. Extract every second letter starting from 'a' to 'm'.
print(result_2[0:14:2])
# c. Reverse the entire string using slicing.
print(result_2[::-1])
# Problem Set 2: Extracting Information
# From Descriptions:
# Extract the name of the famous personality from the quote "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
quote = "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
print(quote[83:])
# Manipulating Words:
# Given the string info = "Python is fun. Fun is good. Good is subjective.",
info_1= "Python is fun. Fun is good. Good is subjective."
info1 = info_1
# a. Extract the word 'subjective' without knowing its exact position.
info1 = (info_1.find('subjective'))
(info1)
print(info_1[36:46])
# b. Extract every third word.
list = "fun good subjective"
print(list)
# c.Reverse the positions of the words, but keep the characters in each word in the same order.
print("subjective is Good .good is Fun .fun is Python")

# Problem Set 3: String Methods
# Upper & Lower:
# Convert the following text to lowercase: "MAY THE FORCE BE WITH YOU."
sentence = "MAY THE FORCE BE WITH YOU."
lowercase = str.lower("MAY THE FORCE BE WITH YOU.")
print(lowercase)
# String Joining and Splitting:
# Given the list motto = ["Make", "haste", "slowly."],
# a. Convert the list into a single string.
motto = "Make", "haste", "slowly."
print(motto.join)
# b. Now, split the string at every occurrence of the letter 'a'.

# Replacing Words:
# Modify the sentence: "Life is what happens when you are busy making other plans."
sentence2="Life is what happens when you are busy making other plans."
# a. Replace "busy" with "distracted".
print(sentence2.replace ("busy","distracted"))
# b. Replace "plans" with "mistakes".
print(sentence2.replace("plans","mistakes"))
# Problem Set 4: String Properties and Advanced Operations
# Repetition:
# Concatenate the word "Iteration" 7 times.
print("Iteration" * 7)
# Word Search:
# Check if the word "moonlight" appears in the quote: "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
quote1 = "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
moonlight = quote1.find('moonlight')
print(moonlight)
# Length and Count:
# a. Calculate the number of characters (including spaces and punctuation) in the word/phrase: "Supercalifragilisticexpialidocious".


# b. Count the number of times the letter 'i' appears in the same word/phrase.