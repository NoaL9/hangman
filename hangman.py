def title(MAX_TRIES):
	"""A function that display the title of the game and 
	the number of worng guesses that user can guess.
	:param MAX_TRIES: the number of worng guesses that user can guess
	:type MAX_TRIES: int
	:return: nothing
	:rtype: not relevant
	"""

	HANGMAN_ASCII_ART = """       _    _
	  | |  | |
	  | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __ 
	  |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \\
	  | |  | | (_| | | | | (_| | | | | | | (_| | | | |
	  |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
						   __/ |                     
						  |___/"""
						  
	print (HANGMAN_ASCII_ART, "\n",MAX_TRIES)

HANGMAN_PHOTOS = {"1" : "    x-------x",

"2" : """    x-------x 
    | 
    | 
    |
    |
    |""",

"3" : """    x-------x
    |       |
    |       0
    |
    |
    |""",

"4" : """    x-------x
    |       |
    |       0
    |       |
    |
    |""",

"5" : """    x-------x
    |       |
    |       0
    |      /|\\
    |
    |""",

"6" : """    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |""",

"7" : """    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |"""}
		
def print_hangman(num_of_tries):
	"""A function that display visually the stage in hangman,
	which is based on the number of worng gusses of the player.
	:param num_of_tries: The number of worng gusses of the player
	:type num_of_tries: int
	:return: The stage in hangman (visually), which is based on the number
	of worng gusses of the player
	:rtype: string	
	"""	
	
	global HANGMAN_PHOTOS
	return(HANGMAN_PHOTOS[num_of_tries])

def choose_word(file_path, index):
	"""A function that choose word to guss from a file.
	:param file_path: string that represents a path to a text file that contains spaced words
	:param index: an integer that represents the location of a particular word in the file
	:type file_path: string
	:type index: int
	:return: list of two members in the following order: 
	(1) the number of different words in the file 
	(2) a word in the position obtained as an argument to the function (index).
	:rtype: list
	"""
	
	file_of_words = open (file_path, "r")
	line = file_of_words.read()
	file_of_words.close()	
	lst = line.split()
	l = len(lst)		
	uniq_lst = set(lst)

	"""if the index that user enter is greater than the last index, 
	the count continues so that the next index is the first index, 
	followed by the second index and so on.
	"""
	index = int(index)
	while (index > l):
		index = index - l
		
	j = 0	
	for i in lst:
		j += 1
		if j == index:
			break
	word = i
	
	return (word)

def show_hidden_word(secret_word, old_letters_guessed):
	"""A function that display the progress in word guessing.
	:param secret_word: The word the user has to guess
	:param old_letters_guessed: letters the user guessed
	:type secret_word: string
	:type old_letters_guessed:string
	:return: string which consists of letters and lower hopes. 
	The string displays the letters from the old_letters_guessed 
	list that are in the secret_word string in their appropriate 
	position, and the rest of the letters in the string (which the 
	player has not yet guessed) as underlines.
	:rtype: string
	"""
	secret_word = list(secret_word)
	word = "_" * len(secret_word)
	word = list(word)
		
	for letter in old_letters_guessed:
		if letter in secret_word:
			for i in range(len(secret_word)):
				if letter == secret_word[i]:
					word[i] = letter
	word = " ".join(word)
	print(word)		

def check_valid_input(letter_guessed, old_letters_guessed):
	"""A Boolean function that check if the current 
	character that user guessed is valid.
	:param letter_guessed: The letter the user guess
	:param old_letters_guessed: letters the user guessed
	:type letter_guessed: string
	:type old_letters_guessed:string
	:return: True if the input is a one letter and 
	the player has not guessed this signal before. 
	Otherwise, the function returns a False.
	:rtype: Boolean
	"""
	return((len(letter_guessed) > 1) or not (letter_guessed.isalpha()) or (letter_guessed in old_letters_guessed))


	
def try_update_letter_guessed(letter_guessed, old_letters_guessed):
	"""A Boolean function that use the check_valid_input function
	to know if the character is valid and has not been guessed in the past.
	:param letter_guessed: The letter the user guess
	:param old_letters_guessed: letters the user guessed
	:type letter_guessed: string
	:type old_letters_guessed:string
	:return: If the character is correct and has not been guessed before - 
	the function adds the character to the guess list and returns true.
	Otherwise,the function prints the character X (as a capital letter), 
	below it the list of letters that have already been guessed and returns a False.
	:rtype: Boolean
	"""      
	if check_valid_input(letter_guessed, old_letters_guessed):
		old_letters_guessed.sort()
		char = " -> "
		print("X\n", char.join(old_letters_guessed))
	else:
	    return("True")
		
    

def check_win(secret_word, old_letters_guessed):
	"""A Boolean function that check  if all the letters 
	that make up the secret word are included in the list of 
	letters the user guessed.
	:param secret_word: The word the user has to guess
	:param old_letters_guessed: letters the user guessed
	:type secret_word: string
	:type old_letters_guessed:string
	:return: true if all the letters 
	that make up the secret word are included in the list of 
	letters the user guessed. Otherwise, the function returns a false.
	:rtype: Boolean
	"""
	for i in secret_word:
		if i not in old_letters_guessed:
			return(False)
		
	return(True)
	
def main():
	global HANGMAN_PHOTOS
	MAX_TRIES = 6
	
	title(MAX_TRIES)

	path = input("Enter file path:")

	"""validating the path input - check that that the user 
	has indeed typed a correct path for a real existing file
	"""
	import os
	while not os.path.isfile(path):
		path = input("Whoops! No such file! Please enter the name of the file you'd like to use.\nEnter file path:")
	
	index = input("Enter index:")
	print ("\n")
	print ("Let’s start!")
	print ("\n")
	secret_word = choose_word(path, index)
	print(HANGMAN_PHOTOS["1"], "\n")
	print ("\n")
	
	num_of_tries = 1
	old_letters_guessed = []
	show_hidden_word(secret_word, old_letters_guessed)
	result = "LOSE"

	while (num_of_tries <= MAX_TRIES):
		letter_guessed = input("Guess a letter:")
		letter_guessed = letter_guessed.lower()
		while not(try_update_letter_guessed(letter_guessed, old_letters_guessed)):
			letter_guessed = input("Guess a letter:")
			letter_guessed = letter_guessed.lower()
		old_letters_guessed.append(letter_guessed)
		if letter_guessed not in secret_word:			
			print(":(")
			num_of_tries += 1
			num_of_tries_str = str(num_of_tries)
			print(HANGMAN_PHOTOS[num_of_tries_str], "\n")			
		show_hidden_word(secret_word, old_letters_guessed)
		if check_win(secret_word, old_letters_guessed):
			result = "WIN"
			break
				
	print(result)


if __name__ == "__main__":
    main()
