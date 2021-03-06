from game.server.logger import Logger
from game.server.config import Config, ViewResolver


class Controller:
    def __init__(self):
        self.config = Config()
        self.__actions = self.config.actions
        self.__games = {}
        self.__game_guid = 0
        self.__games_cnt_limit = 10

    def get(self, action, game_id, *params):
        if action in self.__actions and game_id in self.__games:
            # handle end_game request
            if action.startswith('end_game'):
                del self.__games[game_id]
                return

            # send request to model
            result = self._get_model_for_id(action, game_id, params)

            # render view
            if result and self.__actions[action]['view']:
                return self._execute_view_function(action, game_id, result)
            elif not result and self.__actions[action]['error_view']:
                return self._execute_error_function(action, game_id, result)

        elif action.startswith('get_new_game_instance'):
            # handle get_new_game_instance request
            self.__game_guid = self.__game_guid + 1
            if self.__game_guid in self.__games or self.games_active() >= self.__games_cnt_limit:
                raise OverflowError('Too many games')
            self.__games[str(self.__game_guid)] = self.__actions[action]['model'](game_id, *params)
            return self.__game_guid
        else:
            Logger.log('Bad request type')

    def _get_model_for_id(self, action, game_id, params):
        return self.__actions[action]['model'](self.__games[game_id], *params)

    def _execute_view_function(self, action, game_id, result):
        return self.__actions[action]['view'](self._resolve_view(action), self.__games[game_id], result)

    def _execute_error_function(self, action, game_id, result):
        return self.__actions[action]['error_view'](self._resolve_view(action), self.__games[game_id], result)

    def games_active(self):
        return len(self.__games)

    def _resolve_view(self, action):
        return ViewResolver.resolve(action, self.config)
