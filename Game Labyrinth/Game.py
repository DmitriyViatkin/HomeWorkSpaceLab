import copy
from GameSave import GameSave
from karta import karta
from Sharik import Sharik
import os
from labyrinth import Labirynth


class Game():

    def __init__(self):
        self.pes = Sharik(y=1, x=0)
        self.labirint = Labirynth(karta)

    # Проверяем положение шарика
    def move_dog(self, course):

        y, x = self.pes.y, self.pes.x

        new_pos = self.pes.move(course)

        if new_pos is None:
            print('Нет такого пути')
            return
        self.last_pos()

        new_y, new_x = new_pos
        #Удар о стену

        if self.labirint.karta_1[new_y][new_x] == ' # ':
            print('Шарик ударился о стену! Игра окончена')
            # Сохраняем игру
            if input('Сохранить игру? (d/n: ').lower() == 'd':
                GameSave.save_game(self.last_pos())
                # Перезапуск
                self.restart()

        # Вернулся на предыдущую клетку
        if (new_y, new_x) in self.pes.proidennye_kletki:
            print('Шарик струсил и убежал! Игра окончена.')
            if input('Сохранить игру? (d/n: ').lower() == 'd':
                GameSave.save_game(self.last_pos())
            self.restart()
        # Запись новых координат
        self.pes.y, self.pes.x = new_y, new_x

        # Запись в пройденые клетки
        self.pes.add_to_proidennye(y, x)
        # Идём оптимальным путём
        if (new_y, new_x) in self.labirint.optimal_path:
            print("Шарик нашел правильный путь. Следующий ход.")
        else:  # Шарик выбрал не оптимальный проход
            print('Шарик заблудился! Игра окончена.')
            if input('Сохранить игру? (d/n: ').lower() == 'd':
                GameSave.save_game(self.last_pos())
            self.restart()
        # Нашли кость(Прошли весь оптимальный путь)
        if (new_y, new_x) == self.labirint.bones:
            print("Поздравляем! Шарик нашел косточку! Игра окончена.")
            return
        # Отображаем проёденый путьn

        self.labirint.karta_1[new_y][new_x] = " 0 "
        # Перерисовываем карту
        self.labirint.draw_map()

        # Перезапуск игры

    def last_pos(self):
        result_game = {  # Создаем словарь result_game
            'pes_x': self.pes.x,
            'pes_y': self.pes.y,
            'karta_1': self.labirint.karta_1,
            'proidennye_kletki': self.pes.proidennye_kletki,
        }
        return result_game

    def restart(self):
        self.pes = Sharik(y=1, x=0)  # Создаем нового шарика
        self.labirint.karta_1 = copy.deepcopy(karta)  # Копируем карту заново
        self.play()  # Запускаем игру снова

    def play(self):
        # Файл с сохранением
        saved_game = GameSave.load_game("game.json")
        # Загрузка игры
        if saved_game:
            if input('Загрузить сохраненную игру? (д/н): ').lower() == 'd':
                self.pes.x = saved_game['pes_x']
                self.pes.y = saved_game['pes_y']
                self.labirint.karta_1 = saved_game['karta_1']
                self.pes.proidennye_kletki = saved_game['proidennye_kletki']
                self.labirint.draw_map()
            # Удаляем игру
            else:
                os.remove('game.json')  # Удаляем сохранение
                print('Новая игра.')
                self.restart()
        else:  # Запускаем игру
            print('Новая игра.')
            self.pes = Sharik(y=1, x=0)  # Создаем нового шарика
            self.labirint.karta_1 = copy.deepcopy(karta)  # Копируем карту заново
            self.labirint.draw_map()

        #Цикл игры
        while self.pes.y != self.labirint.bones[0] or self.pes.x != self.labirint.bones[1]:
            course = input("Введите направление (вверх = W, вниз = S, влево = A, вправо = D): ")
            self.move_dog(course)

if __name__== "__main__":
    game = Game()
    game.play()
