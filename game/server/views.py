class GameView:
    def error(self, model, result):
        return False

    def add_player(self, model, result):
        return result

    def get_current_player(self, model, result):
        return result

    def make_move(self, model, result):
        return result

    def check_game_result(self, model, result):
        return result


class OXView(GameView):

    def get_board(self, model, result):
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
        board.append('\n\n')
        display_board = ''.join(board)
        display_board = display_board + model.get_current_player() + ' - ' + display_chars[
            model.get_current_player_number()]
        return display_board


class IntervalView(GameView):

    def get_board(self, model, result):
        if model.get_last_guess() == model.get_random_secret():
            prompt = '\n'
        else:
            prompt = '\nGuess a number between [ {:d} - {:d} ]\n'.format(model.get_lower_limit(),
                                                                         model.get_upper_limit())
            if result:
                prompt += '\nPrevious guesses:\n' + str(result)
                number_order = 'greater' if model.get_last_guess() > model.get_random_secret() else 'lower'
                prompt += '\n\nNumber {:d} is {:s} than the secret number\n'.format(model.get_last_guess(),
                                                                                    number_order)
        return prompt
