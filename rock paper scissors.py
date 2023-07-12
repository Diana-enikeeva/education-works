# Импортируем модуль
import random
#
while True:
    user_action = input("Ваш ход? — Камень, ножницы или бумага: ") # Просим пользователя сделать выбор
    possible_actions = ["камень", "бумага", "ножницы"]
    computer_action = random.choice(possible_actions)
    print(f"\nВы выбрали {user_action}, компьютер выбрал {computer_action}.\n")
    if user_action == computer_action:     # С помощью условного оператора определяем победителя
        print(f"Оба игрока сходили {user_action}. Ничья!!!")
    elif user_action == "камень":
        if computer_action == "ножницы":
            print("Камень ломает ножницы! Победа за вами!")
        else:
            print("Бумага бьет камень! Вы проиграли.")
    elif user_action == "бумага":
        if computer_action == "камень":
            print("Бумага бьет камень! Победа за вами!")
        else:
            print("Ножницы режут бумагу! Вы проиграли.")
    elif user_action == "ножницы":
        if computer_action == "бумага":
            print("Ножницы режут бумагу!Победа за вами!")
        else:
            print("Камень бьет ножницы! Вы проиграли.")
# Спрашиваем, хочет ли пользователь сыграть еще
    play_again = ""
    play_again = input("Сыграем еще? (да/нет): ")
    if play_again.lower() != "да":
        break