import game.client.console as g


def prompt_user_for_game_type():
    game_types = ['ox', 'interval']
    out_game = None
    multi_player = False
    while out_game not in game_types:
        print('\nSelect game number\n 0 - Tic Tac Toe\n 1 - Intervals')
        choice = input()
        if '0' != choice and choice != '1':
            continue
        out_game = game_types[int(choice)]
    if out_game == 'ox':
        choice = input('If you want to play in multiplayer mode please press enter, else type N\n')
        multi_player = len(choice) == 0

    return out_game, multi_player


if __name__ == '__main__':
    game_type, game_mode_multiplayer = prompt_user_for_game_type()
    g.OXGame(game_type, game_mode_multiplayer).play()
