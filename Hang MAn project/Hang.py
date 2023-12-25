import random
import pyfiglet

heading = pyfiglet.figlet_format('H A N G M A N')
print(heading)

print("THEME: INDIAN CITIES")
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ['Mumbai', 'delhi', 'bangalore', 'hyderabad', 'ahmedabad', 'chennai', 'kolkata', 'surat', 'pune', 'jaipur',
             'lucknow', 'kanpur', 'nagpur', 'indore', 'thane', 'bhopal', 'visakhapatnam', 'patna',
             'vadodara', 'ghaziabad', 'ludhiana', 'agra', 'nashik', 'faridabad', 'meerut', 'rajkot', 'varanasi',
             'srinagar', 'aurangabad', 'dhanbad', 'amritsar', 'navimumbai', 'allahabad', 'howrah', 'ranchi', 'gwalior',
             'jabalpur', 'coimbatore', 'vijayawada', 'jodhpur', 'madurai', 'raipur', 'kota', 'chandigarh', 'guwahati',
             'solapur', 'mysore', 'tiruchirappali', 'bareilly', 'aligarh', 'tiruppur', 'gurugram', 'moradabad',
             'jalandhar', 'bhubaneswar', 'salem', 'warangal', 'jalgaon', 'guntur', 'thiruvananthapuram', 'bhiwandi',
             'saharanpur', 'gorakhpur', 'bikaner', 'amravati', 'noida', 'jamshedpur', 'bhilai', 'cuttack', 'firozabad',
             'kochi', 'nellore', 'bhavnagar', 'dehradun', 'shimla']

word = random.choice(word_list)
choosen_word = word.upper()
word_length = len(choosen_word)

letter_list = []
i = 0
while i < word_length:
    letter_list += '_'
    i = i + 1
print(letter_list)

lives = 6
guessed_letters = []
end_of_game = False
while not end_of_game:
    guess = input('Guess a letter: ').upper()
    for dash in range(word_length):
        letter = choosen_word[dash]
        if letter == guess:
            letter_list[dash] = letter

    if guess not in choosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    guessed_letters += guess
    print(guessed_letters)


    print(f"{' '.join(letter_list)}")
    if "_" not in letter_list:
        end_of_game = True
        print("You win.")

    print(stages[lives])

print(choosen_word)