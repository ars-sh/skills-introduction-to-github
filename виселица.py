from random import *

word_list = ["дом", "стол", "кот", "ухо", "нос"]

def get_word():
    result = choice(word_list)
    return result.upper()

def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]

def play():
    win_flag = False
    print('Давайте сыграем в виселицу!')
    word1 = get_word()
    word = list()
    for i in word1:
        word += i
    tries = 6
    word_comp = ['_' * len(word)]
    word_completion = list()
    for j in word_comp:
        word_completion += j
    guessed_letters = [] 
    while win_flag != True:
        print(display_hangman(tries))
        print(word_completion)
        alpha = input('Введите букву!(Язык - русский) ').upper()
        if alpha.isalpha() == False:
            print('Это не буква!')
            continue
        if alpha in guessed_letters:
            print('Вы уже называли эту букву.')
        guessed_letters += alpha
        for n in range(10):
            if alpha in word:
                ind = word.index(alpha)
                word_completion.insert(ind, alpha)
                per = word_completion.pop(ind + 1)
            else: 
                print('Такой буквы нет!')
                tries -= 1
                break
        if '_' not in word_completion:
            print('Поздравляем! Вы отгадали слово', word1)
            break
        if tries == 0:
            print('К сожалению вы не угадали слово', word1)
            break

print(play())