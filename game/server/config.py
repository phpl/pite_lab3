from game.server.models import OXModel
from game.server.views import GameViews


class Config:
    actions = {'add_player_ox': {'model': OXModel.add_player,
                                 'view': GameViews.add_player_ox,
                                 'error_view': GameViews.error_ox
                                 },
               'get_current_player_ox': {'model': OXModel.get_current_player,
                                         'view': GameViews.get_current_player_ox,
                                         'error_view': GameViews.error_ox
                                         },
               'get_board_ox': {'model': OXModel.get_board,
                                'view': GameViews.get_board_ox,
                                'error_view': GameViews.error_ox
                                },
               'make_move_ox': {'model': OXModel.make_move,
                                'view': GameViews.make_move_ox,
                                'error_view': GameViews.error_ox
                                },
               'get_new_game_instance_ox': {'model': OXModel,
                                            'view': None,
                                            'error_view': None
                                            },
               'check_game_result_ox': {'model': OXModel.check_game_result,
                                        'view': GameViews.check_game_result_ox,
                                        'error_view': GameViews.error_ox
                                        },
               'end_game_ox': {'model': None, 'view': None, 'error_view': None}

               }
