import time

print('Добро пожаловать в игру Крестики Нолики!')

field = [[" - "]*3 for i in range(3)]

def print_field():
    for row in field:
        print("".join(row))

def prepare():
    ask1 = input('Вы готовы к игре?(y = да, n = нет)')
    if ask1 == 'y':
        time.sleep(1.2)
        print('Начинаем!')

        time.sleep(0.6)
        def game():
            """В этой функции весь геймплей игры"""
            print_field()
            time.sleep(0.4)
            print('Ход первого игрока!')
            time.sleep(0.4)


            def move_player():
                move_1 = input("Укажите координаты в формате x, y(x это строка а y это столбец")
                row_1, col_1 = move_1.split(',')
                if field[row_1][col_1] == ' - ':
                    field[row_1][col_1] = ' X '
                    time.sleep(0.4)
                    print_field()
                    time.sleep(0.4)
                    print('Сейчас ход второго игрока!')
                    move_2 = input("Укажите координаты в формате x, y(x это строка а y это столбец")
                    row_2, col_2 = move_2.split(',')
                    if field[row_2][col_2] == ' - ':
                        field[row_2][col_2] = ' 0 '
                        time.sleep(0.4)
                        print_field()
                        time.sleep(0.4)
                        print('Сейчас ход первого игрока!')
                else:
                    print('Эта клетка уже занята! Попробуйте заного')
        game()




prepare()
