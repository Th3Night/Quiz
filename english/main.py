import random

file = open("words.txt", "r")
rus_file = open("rus_words.txt", "r", encoding="utf-8")
data = file.read()
rus_data = rus_file.read()
file.close()
rus_file.close()

data = data.split("\n")
for i in range(len(data)):
    data[i] = data[i].split(", ")

rus_data = rus_data.split("\n")
for i in range(len(rus_data)):
    rus_data[i] = rus_data[i].split(", ")


def start():
    mode = input("Введите режим, в котором хотите работать...\nНапишите 'all' для работы со всеми словами\n"
                 "Напишите 'select' для выбора группы слов, с которыми хотите работать\n"
                 "Для выхода из режима напишите 'stop...'\n")
    working(mode)


def working(command):
    if command == "all":
        print("Эта команда еще не сделана")
        start()

    elif command == "select":
        print("Вы выбрали режим самостоятельной работы\n")
        mode = input("Выберите режим перевода\n"
                     "Для режима RUS-EN напишите '1'\n"
                     "Для режима EN-RUS напишите '2'...\n")
        if mode != '1' and mode != '2':
            working("select")

        else:
            language_mode(mode)


def language_mode(mode):
    if mode == "1":
        print("Вы выбрали режим RUS-EN...\n"
              "Теперь нужно выбрать номер нужной группы, Возможные группы:\n")
        for i in range(len(rus_data)):
            print(f"{i}) {rus_data[i]}")

        number = input("Введите номер:\n")
        select_mode_1(number)
        print(f"Вы выбрали группу {number}")

    else:
        pass


def select_mode_1(number):
    number = int(number)
    word_number = random.randint(0, len(rus_data[number]) - 1)
    answer = input(f"Переведите {rus_data[number][word_number]} с русского на английский...\n")
    if answer == data[number][word_number]:
        print("Верно!\n")

    elif answer == "stop":
        start()
    else:
        print(f"Неверно!\nПравильно: {data[number][word_number]}\n")

    select_mode_1(number)


start()
