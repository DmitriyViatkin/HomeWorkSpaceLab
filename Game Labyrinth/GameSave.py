import json
import os


class GameSave():

    def save_games( file, result_game):
        with open(file, 'w') as f:
            json.dump(result_game, f)

    def load_game(file):
        if os.path.exists(file):
            with open(file, 'r') as f:
                return json.load(f)
        return None
    def save_game( result_game):
        """result_game = {  # Создаем словарь result_game
            'pes_x': pes_x,
            'pes_y': pes_y,
            'karta_1':karta_1,
            'proidennye_kletki':proidennye_kletki,
        }"""
        GameSave.save_games("game.json", result_game)  # Используем созданный словарь
        print('Игра сохранена.')