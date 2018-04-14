from game.common.enums.Events import Events
from game.common.enums.GameStatus import GameStatus


class Transition:
    def __init__(self, given_state, event, next_state, action):
        self.given_state = given_state
        self.event = event
        self.next_state = next_state
        self.action = action


class GameTransitionFSM:
    def __init__(self, game):
        self.state = GameStatus.INIT
        self.game = game
        self.transitions = \
            [Transition(GameStatus.INIT, Events.INIT_GAME, GameStatus.IN_GAME, self.game.init_players),
             Transition(GameStatus.IN_GAME, Events.CONTINUE_GAME, GameStatus.IN_GAME, self.game.perform_next_move),
             Transition(GameStatus.IN_GAME, Events.FINISH_GAME, GameStatus.END_GAME, self.game.finish_game)]

    def handle_event(self, event):
        for transition in self.transitions:
            if transition.event == event and self.state == transition.given_state:
                self.state = transition.next_state
                transition.action()
