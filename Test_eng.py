# словари со словами, которые нужно будет угадывать

words_easy = {
    "family": "семья",
    "hand": "рука",
    "people": "люди",
    "evening": "вечер",
    "minute": "минута",
}

words_medium = {
    "believe": "верить",
    "feel": "чувствовать",
    "make": "делать",
    "open": "открывать",
    "think": "думать",
}

words_hard = {
    "rural": "деревенский",
    "fortune": "удача",
    "exercise": "упражнение",
    "suggest": "предлагать",
    "except": "кроме",
}

# уровни, которые будет получать пользователь после решения задач

levels = {
    0: "Нулевой",
    1: "Так себе",
    2: "Можно лучше",
    3: "Норм",
    4: "Хорошо",
    5: "Отлично",
}

# правильные и неправильные слова

answers = {}
right_answers = 0

# Получим у пользователя уровень сложности

elected_level = input("Выберите уровень сложности (easy, medium, hard):  ")

all_dictionaries = {
    "easy": words_easy,
    "medium": words_medium,
    "hard": words_hard,
}

work_dict = all_dictionaries[elected_level]
print()

for rus, eng in work_dict.items():
    answer = input(f"{rus}, {len(eng)}, начинается на {eng[0]}... Ответ: ")
    if answer == eng:
        print(f"Верно, {rus} — это {eng}.")
    else:
        print(f"Неверно. {rus} — это {eng}.")
    answers[rus] = answer == eng

print()
print("Правильно отвечены слова: ")
for word, correct in answers.items():
    if correct is True:
        print(word)
        right_answers += 1

print()
print("Неправильно отвечены слова: ")
for word, correct in answers.items():
    if correct is False:
        print(word)

print(f"Ваш ранг: \n{levels[right_answers]}")