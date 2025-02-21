import copy
import json
import os
from karta import karta


class Sharik():

    def __init__(self, x, y):
        # start position
        self.x = x
        self.y = y
        #Пройденый путь
        self.proidennye_kletki = list()

    # Передвижение шарика
    def move(self, course):
        course = course.lower()
        new_y, new_x = self.y, self.x  # Устанавливаем

        if course == 'd':
            new_x = self.x + 1
            new_y = self.y
            #print('Raith', new_y, new_x)
        elif course == 'a':
            if self.x > 0:
                new_x = self.x - 1
                #print('Left', new_y, new_x)
        elif course == 's':
            new_y = self.y + 1
            #print('Douwn', new_y, new_x)
        elif course == 'w':
            if self.y > 0:
                new_y = self.y - 1
                #print('Up', new_y, new_x)
        else:
            print("Некоректное направление")
            return None
        return new_y, new_x

    # Устанавливаем последнюю позицию
    def add_to_proidennye(self, y, x):
        self.proidennye_kletki.append((y, x))


class Labirynth():
    def __init__(self, karta_1):
        self.karta_1 = copy.deepcopy(karta)
        self.pes = Sharik(y=1, x=0)
        self.bones = (18, 19)
        self.optimal_path = ((1, 1), (1, 2), (2, 2), (3, 2), (3, 1), (4, 1), (5, 1), (5, 2), (5, 3), (5, 4),
                             (5, 5), (5, 6), (5, 7), (6, 7), (7, 7), (8, 7), (8, 8), (8, 9), (8, 10), (8, 11),
                             (8, 12), (8, 13), (8, 14), (8, 15), (8, 16), (8, 17), (9, 17), (10, 17), (11, 17),
                             (12, 17), (13, 17), (14, 17), (15, 17), (16, 17), (17, 17), (17, 18), (18, 18), (18, 19))

    #Рисуем карту
    def draw_map(self):
        for row in self.karta_1:
            print(''.join(row))
    #Проверяем положение шарика
    def move_dog(self, course):

        y, x = self.pes.y, self.pes.x

        new_pos = self.pes.move(course)

        if new_pos is None:
            print('Нет такого пути')
            return
        self.last_pos()
        new_y, new_x = new_pos
        # Удар о стену

        if self.karta_1[new_y][new_x] == ' # ':
            print('Шарик ударился о стену! Игра окончена')
            # Сохраняем игру
            if input('Сохранить игру? (d/n: ').lower() == 'd':
                self.save_game()
                # Перезапуск
                self.restart()
        # Вернулся на предыдущую клетку
        if (new_y, new_x) in self.pes.proidennye_kletki:
            print('Шарик струсил и убежал! Игра окончена.')
            if input('Сохранить игру? (d/n: ').lower() == 'd':
                self.save_game()
            self.restart()
        # Запись новых координат
        self.pes.y, self.pes.x = new_y, new_x

        # Запись в пройденые клетки
        self.pes.add_to_proidennye(y, x)
        # Идём оптимальным путём
        if (new_y, new_x) in self.optimal_path:
            print("Шарик нашел правильный путь. Следующий ход.")
        else:#Шарик выбрал не оптимальный проход
            print('Шарик заблудился! Игра окончена.')
            if input('Сохранить игру? (d/n: ').lower() == 'd':
                self.save_game()
            self.restart()
        # Нашли кость(Прошли весь оптимальный путь)
        if (new_y, new_x) == self.bones:
            print("Поздравляем! Шарик нашел косточку! Игра окончена.")
            return
        # Отображаем проёденый путь
        self.karta_1[new_y][new_x] = " 0 "
        # Перерисовываем карту
        self.draw_map()

    # Перезапуск игры
    def restart(self):
        self.pes = Sharik(y=1, x=0)  # Создаем нового шарика
        self.karta_1 = copy.deepcopy(karta)  # Копируем карту заново
        self.play()  # Запускаем игру снова

    # Запоминаем последнее положение
    def last_pos(self):
        result_game = {  # Создаем словарь result_game
            'pes_x': self.pes.y,
            'pes_y': self.pes.y,
            'karta_1': self.karta_1,
            'proidennye_kletki': self.pes.proidennye_kletki,
        }

    # Сохраняем игру в файл
    def save_game(self):
        result_game = {  # Создаем словарь result_game
            'pes_x': self.pes.y,
            'pes_y': self.pes.y,
            'karta_1': self.karta_1,
            'proidennye_kletki': self.pes.proidennye_kletki,
        }
        Game.save_games("game.json", result_game)  # Используем созданный словарь
        print('Игра сохранена.')

    # Сама игра
    def play(self):
        # Файл с сохранением
        saved_game =Game.load_game("game.json")
        # Загрузка игры
        if saved_game:
            if input('Загрузить сохраненную игру? (д/н): ').lower() == 'd':
                self.pes.x = saved_game['pes_x']
                self.pes.y = saved_game['pes_y']
                self.karta_1 = saved_game['karta_1']
                self.pes.proidennye_kletki = saved_game['proidennye_kletki']  # Преобразуем список обратно в множество
                self.draw_map()
            # Удаляем игру
            else:
                os.remove('game.json')  # Удаляем сохранение
                print('Новая игра.')
                self.pes = Sharik(y=1, x=0)
                self.karta_1 = copy.deepcopy(karta)
                self.draw_map()
        else: # Запускаем игру
            print('Новая игра.')
            self.pes = Sharik(y=1, x=0)
            self.karta_1 = copy.deepcopy(karta)
            self.draw_map()

        #Цикл игры
        while self.pes.y != self.bones[0] or self.pes.x != self.bones[1]:
            course = input("Введите направление (вверх = W, вниз = S, влево = A, вправо = D): ")
            self.move_dog(course)

#Клас сохранения и загрузки иры в файл
class Game():

    def save_games( file, result_game):
        with open(file, 'w') as f:
            json.dump(result_game, f)

    def load_game(file):
        if os.path.exists(file):
            with open(file, 'r') as f:
                return json.load(f)
        return None

labirint = Labirynth(karta)
labirint.play()
