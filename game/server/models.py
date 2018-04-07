import math


class OXModel:
    def __init__(self, game_id):
        self.__id = game_id
        self.__players = ['Player 1', 'Player2']
        self.__current_player = 0
        self.__board_len = 9
        self.__board = [-1 for it in range(0, self.__board_len)]

    def add_player(self, name, player_id):
        player_id = self.__str_to_int(player_id)
        if self._can_add_player(name, player_id):
            self.__players[player_id] = str(name)
            return True

    def _can_add_player(self, name, player_id):
        return player_id is not None and len(self.__players) > player_id >= 0 and name

    def get_players_count(self):
        return len(self.__players)

    def get_current_player(self):
        return self.__players[self.__current_player]

    def get_board(self):
        return self.__board[:]

    def __is_move_valid(self, field):
        if self._is_field_on_board(field) and self._is_field_untouched(field):
            return True

    def _is_field_on_board(self, field):
        return 0 <= field < len(self.__board)

    def _is_field_untouched(self, field):
        return self.__board[field] == -1

    def __str_to_int(self, val):
        try:
            val = int(val)
            return val
        except ValueError:
            return

    def make_move(self, field):
        field = self.__str_to_int(field)
        if self._can_make_a_move(field):
            self.__board[field] = self.__current_player
            self._switch_player()
            return True
        return False

    def _can_make_a_move(self, field):
        return field is not None and self.__is_move_valid(field)

    def _switch_player(self):
        self.__current_player = (self.__current_player + 1) % len(self.__players)

    def check_game_result(self):
        dim = int(math.sqrt(self.__board_len))
        result = None

        class FoundException(Exception):
            pass

        def row():
            return self.__board[i * dim: i * dim + dim]

        def col():
            return [self.__board[j * dim + i] for j in range(0, dim)]

        def diag():
            return [self.__board[j * dim + j] for j in range(0, dim)]

        def diag2():
            return [self.__board[j * dim + dim - j - 1] for j in range(0, dim)]

        def check_slice(sli):
            if _is_slice_filled_for_one_player(sli):
                raise FoundException(self.__players[min(sli)])  # winner = min, because he is starting

        def _is_slice_filled_for_one_player(sli):
            return max(sli) == min(sli) != -1

        def _is_game_out_of_moves():
            return all(map(lambda x: x != -1, self.__board))

        try:
            for i in range(0, dim):
                check_slice(row())
                check_slice(col())
            check_slice(diag())
            check_slice(diag2())
            if _is_game_out_of_moves():
                result = 'A draw'
        except FoundException as e:
            result = str(e) + ' won the game!'
        return result if result is not None else 'False'



