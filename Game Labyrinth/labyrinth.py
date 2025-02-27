import copy
from karta import karta


class Labirynth():

    def __init__(self, karta_1):
        self.karta_1 = copy.deepcopy(karta)
        self.bones = (18, 19)
        self.optimal_path = ((1, 1), (1, 2), (2, 2), (3, 2), (3, 1), (4, 1), (5, 1), (5, 2), (5, 3), (5, 4),
                             (5, 5), (5, 6), (5, 7), (6, 7), (7, 7), (8, 7), (8, 8), (8, 9), (8, 10), (8, 11),
                             (8, 12), (8, 13), (8, 14), (8, 15), (8, 16), (8, 17), (9, 17), (10, 17), (11, 17),
                             (12, 17), (13, 17), (14, 17), (15, 17), (16, 17), (17, 17), (17, 18), (18, 18), (18, 19))

    def draw_map(self):  # Рисуем карту
        for row in self.karta_1:
            print(''.join(row))
