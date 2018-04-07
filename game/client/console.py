from game.client.OXControllerNetworkClient import OXControllerNetworkClient


class OXGame:

    def __init__(self):
        self.controller = OXControllerNetworkClient()
        self.id = None
        while not self.id:
            self.id = self._get_new_game_instance()

    def add_player(self, name, player_no):
        self.controller.get(method='add_player', id=self.id, player_name=name, player_number=player_no)

    def get_current_player(self):
        return self.controller.get(method='get_current_player', id=self.id)

    def get_board(self):
        return self.controller.get(method='get_board', id=self.id)

    def make_move(self, field):
        return self.controller.get(method='make_move', id=self.id, chosen_field=field)

    def _get_new_game_instance(self):
        return self.controller.get(method='get_new_game_instance', id=0)

    def check_game_result(self):
        result = self.controller.get(method='check_game_result', id=self.id)
        return result if result != 'False' else None

    def end_game(self):
        self.controller.get(method='end_game', id=self.id)

    def play(self):
        try:
            self._init_players()
            result = None
            while not result:
                result = self._perform_next_move()
            self._finish_game(result)
        except EOFError:
            print('Quitting the game...')

    def _init_players(self):
        player1 = input('Please enter yor name (Player 1)\n')
        self.add_player(player1, 0)

        player2 = input('Please enter yor name (Player 2)\n')
        self.add_player(player2, 1)

    def _perform_next_move(self):
        print(self.get_board())
        move_ok = None
        while not move_ok:
            move = input('Player ' + self.get_current_player() + ' enter next move\n')
            move_ok = self.make_move(move)
        return self.check_game_result()

    def _finish_game(self, result):
        print('Game Over!')
        print(self.get_board())
        print(result)
        self.end_game()
        print('Thank you.')


if __name__ == '__main__':
    game = OXGame()
    game.play()
