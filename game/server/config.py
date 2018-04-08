from game.server.models import OXModel, IntervalModel
from game.server.views import OXView, IntervalView

class ViewResolver:
    ox_view = OXView
    interval_view = IntervalView
    @staticmethod
    def resolve(action):
        if action.endswith('ox'):
            return ViewResolver.ox_view
        if action.endswith('interval'):
            return ViewResolver.interval_view

class Config:
    actions = {'add_player_ox': {'model': OXModel.add_player,
                                 'view': OXView.add_player,
                                 'error_view': OXView.error
                                 },
               'get_current_player_ox': {'model': OXModel.get_current_player,
                                         'view': OXView.get_current_player,
                                         'error_view': OXView.error
                                         },
               'get_board_ox': {'model': OXModel.get_board,
                                'view': OXView.get_board,
                                'error_view': OXView.error
                                },
               'make_move_ox': {'model': OXModel.make_move,
                                'view': OXView.make_move,
                                'error_view': OXView.error
                                },
               'get_new_game_instance_ox': {'model': OXModel,
                                            'view': None,
                                            'error_view': None
                                            },
               'check_game_result_ox': {'model': OXModel.check_game_result,
                                        'view': OXView.check_game_result,
                                        'error_view': OXView.error
                                        },
               'end_game_ox': {'model': None, 'view': None, 'error_view': None},

               'add_player_interval': {'model': IntervalModel.add_player,
                                       'view': IntervalView.add_player,
                                       'error_view': IntervalView.error
                                       },
               'get_current_player_interval': {'model': IntervalModel.get_current_player,
                                               'view': IntervalView.get_current_player,
                                               'error_view': IntervalView.error
                                               },
               'get_board_interval': {'model': IntervalModel.get_board,
                                      'view': IntervalView.get_board,
                                      'error_view': IntervalView.get_board
                                      },
               'make_move_interval': {'model': IntervalModel.make_move,
                                      'view': IntervalView.make_move,
                                      'error_view': IntervalView.error
                                      },
               'get_new_game_instance_interval': {'model': IntervalModel,
                                                  'view': None,
                                                  'error_view': None
                                                  },
               'check_game_result_interval': {'model': IntervalModel.check_game_result,
                                              'view': IntervalView.check_game_result,
                                              'error_view': IntervalView.error
                                              },
               'end_game_interval': {'model': None, 'view': None, 'error_view': None}
               }
