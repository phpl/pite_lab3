from game.common.enums.Events import Events
from game.common.enums.GameStatus import GameStatus


class Transition:
    def __init__(self, given_state, next_state, action):
        self.given_state = given_state
        self.next_state = next_state
        self.action = action


class GameFSM:
    def __init__(self, game):
        self.state = GameStatus.INIT
        self.game = game
        self.transitions = {
            Events.INIT_GAME: Transition(GameStatus.INIT, GameStatus.IN_GAME, self.game.init_players),
            Events.CONTINUE_GAME: Transition(GameStatus.IN_GAME, GameStatus.IN_GAME, self.game.perform_next_move),
            Events.FINISH_GAME: Transition(GameStatus.IN_GAME, GameStatus.END_GAME, self.game.finish_game)
        }

    def handle_event(self, event):
        self.state = self.transitions[event].next_state
        self.transitions[event].action()
