from unittest import TestCase
from unittest.mock import patch

from game.client.console import OXGame


class TestOXGame(TestCase):

    @patch('game.client.OXControllerNetworkClient.OXControllerNetworkClient.get')
    def test_add_player(self, controller_mock):
        game = OXGame()
        game.id = 1

        game.add_player("test", 0)

        controller_mock.assert_called_with(id=1, method='add_player', player_name='test', player_number=0)

    @patch('game.client.OXControllerNetworkClient.OXControllerNetworkClient.get')
    def test_get_current_player(self, controller_mock):
        game = OXGame()
        game.id = 1

        game.get_current_player()

        controller_mock.assert_called_with(id=1, method='get_current_player')

    @patch('game.client.OXControllerNetworkClient.OXControllerNetworkClient.get')
    def test_get_board(self, controller_mock):
        game = OXGame()
        game.id = 1

        game.get_board()

        controller_mock.assert_called_with(id=1, method='get_board')

    @patch('game.client.OXControllerNetworkClient.OXControllerNetworkClient.get')
    def test_make_move(self, controller_mock):
        game = OXGame()
        game.id = 1

        game.make_move(3)

        controller_mock.assert_called_with(id=1, method='make_move', chosen_field=3)

    @patch('game.client.OXControllerNetworkClient.OXControllerNetworkClient.get')
    def test__get_new_game_instance(self, controller_mock):
        game = OXGame()

        game._get_new_game_instance()

        controller_mock.assert_called_with(id=0, method='get_new_game_instance')

    @patch('game.client.OXControllerNetworkClient.OXControllerNetworkClient.get')
    def test_check_game_result_true(self, controller_mock):
        controller_mock.return_value = True
        game = OXGame()
        game.id = 1

        result = game.check_game_result()

        self.assertEqual(True, result)
        controller_mock.assert_called_with(id=1, method='check_game_result')

    @patch('game.client.OXControllerNetworkClient.OXControllerNetworkClient.get')
    def test_check_game_result_none(self, controller_mock):
        controller_mock.return_value = 'False'
        game = OXGame()
        game.id = 1

        result = game.check_game_result()

        self.assertEqual(None, result)
        controller_mock.assert_called_with(id=1, method='check_game_result')

    @patch('game.client.OXControllerNetworkClient.OXControllerNetworkClient.get')
    def test_end_game(self, controller_mock):
        game = OXGame()
        game.id = 1

        game.end_game()

        controller_mock.assert_called_with(id=1, method='end_game')

    @patch('game.client.OXControllerNetworkClient.OXControllerNetworkClient.get')
    def test_play(self, controller_mock):
        controller_mock.return_value = 'True'
        game = OXGame()
        game.id = 1

        with patch('builtins.input', return_value=1):
            game.play()

        controller_mock.assert_called_with(id=1, method='end_game')

    @patch('game.client.OXControllerNetworkClient.OXControllerNetworkClient.get')
    def test__init_players(self, controller_mock):
        game = OXGame()
        game.id = 1

        with patch('builtins.input', return_value='test'):
            game._init_players()

        controller_mock.assert_called_with(id=1, method='add_player', player_name='test', player_number=1)

    @patch('game.client.OXControllerNetworkClient.OXControllerNetworkClient.get')
    def test__perform_next_move(self, controller_mock):
        controller_mock.return_value = 'True'
        game = OXGame()
        game.id = 1

        with patch('builtins.input', return_value=1):
            game._perform_next_move()

        controller_mock.assert_called_with(id=1, method='check_game_result')

    @patch('game.client.OXControllerNetworkClient.OXControllerNetworkClient.get')
    def test__finish_game(self, controller_mock):
        game = OXGame()
        game.id = 1

        game._finish_game("test")

        controller_mock.assert_called_with(id=1, method='end_game')
