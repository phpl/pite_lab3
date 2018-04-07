class GameViews:
    def error_ox(self, model, result):
        return False

    def add_player_ox(self, model, result):
        return result

    def get_current_player_ox(self, model, result):
        return result

    def get_board_ox(self, model, result):
        '''render a nice board here'''
        if not result:
            return result
        display_chars = ['O', 'X', ' ']
        board = list(map(lambda f: display_chars[f], result))
        for i in reversed(range(1, len(board))):
            ch = '|'
            if i % 3 == 0:
                ch = '\n-----\n'
            board.insert(i, ch)
        board.insert(0, '\n')
        board.append('\n')
        return ''.join(board)

    def make_move_ox(self, model, result):
        return result

    def check_game_result_ox(self, model, result):
        return result
