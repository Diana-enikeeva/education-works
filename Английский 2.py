# Пропишем словари по уровням сложности и зададим переменные

words_easy = {
    "family":"семья",
    "hand": "рука",
    "people":"люди",
    "evening": "вечер",
    "minute":"минута",
}

words_medium = {
    "believe":"верить",
    "feel": "чувствовать",
    "make":"делать",
    "open": "открывать",
    "think":"думать",
}

words_hard  = {
    "rural":"деревенский",
    "fortune": "удача",
    "exercise":"упражнение",
    "suggest": "предлагать",
    "except":"кроме",
}

levels = {
   0: "Нулевой",
   1: "Так себе",
   2: "Можно лучше",
   3: "Нормально",
   4: "Хорошо",
   5: "Отлично, ты молодец!",
}

answers = {}
right_answers = 0

# Начинаем с приветствия и предлагаем пользователю выбрать уровень сложности

print("Привет! Давай поугадываем слова?")
print()

selected_level = input("""Выбирай уровень сложности:
лёгкий, средний или сложный? """)
print()
# С помощью цикла и условия сравниваем полученный ответ с возможными уровнями сложности
while selected_level != "лёгкий" and selected_level != "средний" and selected_level != "сложный":
    if selected_level != "лёгкий" and selected_level != "средний" and selected_level != "сложный":
        print("Увы, такого уровня сложности нет.")
        selected_level = input("Выбирай внимательнее: ")
        break
print()
# Программа подбирает словать исходя из выбранного уровня сложности
print(f"""Выбран {selected_level} уровень сложности.
Мы предложим 5 слов, надо подобрать для них перевод!""")
print()
start = input("Нажми Enter, чтобы начать!")
print()
all_dictionaries = {
    "лёгкий": words_easy,
    "средний": words_medium,
    "сложный": words_hard,
}

dictionary = all_dictionaries[selected_level]
#  С помощью цикла сравниваем полученные ответы с верными
for eng, rus in dictionary.items():
    print(f"{eng}, {len(rus)}, начинается на {rus[0]}...")
    user_answer = input("Ваш ответ: ")
    if user_answer == rus:
        print(f"Отлично! {eng} — это {rus}!")
        answers[eng] = True
    else:
        print(f"А вот и нет, {eng} — это {rus}.")
        answers[eng] = False
# Выводим, как итог, правильные и неправильные ответы
print()
print(f"Правильно отвечены слова: ")
for word, correct in answers.items():
  if correct is True:
       print(word)
       right_answers +=1

print()
print("Неправильно отвечены слова: ")
for word, correct in answers.items():
    if correct is False:
        print(word)

# Завершаем программу, выводим ранг
print(f"Вау! Ваш ранг: {levels[right_answers]}")
