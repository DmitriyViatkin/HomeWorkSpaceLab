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