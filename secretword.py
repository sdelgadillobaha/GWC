# # import random

# # # A list of words that 
# # potential_words = ["Python", "JavaScript", "Java", "HTML", "CSS"]

# # word = random.choice(potential_words)

# secret_word = "python"

# # Use to test your code:
# # print(word)

# # Converts the word to lowercase
# secret_word = secret_word.lower()

# # Make it a list of letters for someone to guess
# current_word = ["_", "_"] # TIP: the number of letters should match the word

# # Some useful variables
# guesses = []
# maxfails = 7
# fails = 0

# while fails < maxfails:
# 	guess = input("Guess a letter: ")
#     guesses.append(guess)
   
# 	# check if the guess is valid: Is it one letter? Have they already guessed it?

# 	# check if the guess is correct: Is it in the word? If so, reveal the letters!

# 	print(current_word)

# 	fails = fails+1
# 	print("You have " + str(maxfails - fails) + " tries left!")







#     # assign secret word the user must guess. 
#     # make a list of the letters in the secret word. 
#         # example: ['_', '_', '_', '_']
    
#     # have some var which tells us if the game keeps going and to continue the while loop. 


#     #  if user's guess is in the word, fill in the list according to where the letter is in the word..
#     #  if user's guess is NOT in the word, ask again. Do not update the list. 

secret_word = "python"

sw_list = ["p", "y", "t", "h", "o", "n"] 


guesses = ['_', '_', '_', '_', '_', '_']
maxfails = 7
fails = 0

while fails < maxfails:
	guess = input("Guess a letter: ")

for i in sw_list(0,5):
    if i[0] == 'p':
        sw_list.append(i)
sw_list

 





