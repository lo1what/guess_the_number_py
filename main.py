import random
number = int(input("Введите число от 1 до 100: "))

x = 1
y = 100
guess = random.randint (x, y)
tries = 1

if number == guess:
    print('С первой попытки!')
else:
    while guess != number:
        if number > guess:
            print("Загаданное число больше: ", guess)
            x = guess
            guess = random.randint(x, y)
            tries += 1
        elif number < guess:
            print("Загаданное число меньше: ", guess)
            y = guess
            guess = random.randint(x, y)
            tries += 1
    print (number)
    print ('Вы победили, с', tries, 'попытки')