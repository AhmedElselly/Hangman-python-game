import random
from words import words
import string

def get_word(words):
	word = random.choice(words)
	while '-' in word or ' ' in word:
		word = random.choice(words)
		# print(word)

	return word.upper()


def hangman():
	word = get_word(words)
	word_letters = set(word)
	alphabet = set(string.ascii_uppercase)
	used_letters = set()

	# getting user's input
	while len(word_letters) > 0:
		print('you have used these letters: ', ' '.join(used_letters))
		word_list = [letter if letter in used_letters else '-' for letter in word]
		print('current word: ', ' '.join(word_list))
		user_letter = input('Guess a letter: ').upper()
		if user_letter in alphabet - used_letters:
			used_letters.add(user_letter)
			if user_letter in word_letters:
				word_letters.remove(user_letter)

		elif user_letter in used_letters:
			print('you already guessed that letter. try again!')

	

hangman()