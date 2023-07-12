# Задаем списки вопросов и ответов
questions = ["My name ___  Vova ", "I ___ a coder ", "I live ___ Moscow "]
answers = ["is", "am", "in"]
# Задаем переменные
right_answers = 0
score = 0
# Предлагаем пользователю начать
ready = input('''Привет! 
Предлагаю проверить свои знания английского! 
Наберите "ready", чтобы начать!''')
# С помощью условий и циклов задаем программу
if ready == "ready":
    for i in range(len(questions)):
        life = 3
        while life > 0:
            answer = input(questions[i])
            if answer == answers[i]:
                print('Ответ верный!')
                right_answers += 1
                score += life
                break
            life -= 1
            print(f'Осталось попыток: {life}, попробуйте еще раз!')
            if life == 0:
                print(f'Увы, но нет. Верный ответ: {answers[i]}')
    print(f'Вот и всё! Вы ответили на {right_answers} вопросов из {len(questions)} верно, вы набрали {score} баллов.')
else:
    print('Кажется, вы не хотите играть. Очень жаль.')

