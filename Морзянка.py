import random

english_words = ['code', 'bit', 'list', 'soul', 'next']

def morse_encode(word):
    """
    Переводит слово с английского в морзе-код
    """
    morse_code = {
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-"
}

# кодируем буквы в слове

    morse_translation = ""
    for letter in word:
        morse_translation += morse_code[letter] + " "

    return morse_translation

def get_word():
    """
    Получает случайное слово из списка слов
    """
    return random.choice(english_words)

def print_statistics(answers):
    """
    Выводит статистику
    """
    total_questions = len(answers)
    right_questions = answers.count(True)
    incorrect_questions = total_questions - right_questions

    return f"Всего задачек: {total_questions} \n"\
           f"Отвечено верно: {right_questions}\n"\
           f"Отвечено неверно: {incorrect_questions}"

# Список ответов

answers = []

input(f"Сегодня мы потренируемся расшифровывать морзянку.\n Нажмите Enter и начнем")

#Цикл вопросов
for i in range(5):
    random_word = get_word()
    morse = morse_encode(random_word)

    user_answer = input(f'Слово {i+1}: {morse}')
    if user_answer == random_word:
        answers.append(True)
        print(f'Верно, {random_word}!')
    else:
        answers.append(False)
        print(f'Неверно, {random_word}!')

print(print_statistics(answers))