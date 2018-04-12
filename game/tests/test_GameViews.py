from unittest import TestCase
from unittest.mock import patch

from game.server.views import OXView


class TestGameViews(TestCase):
    test_view = None

    def setUp(self):
        super().setUp()
        self.test_view = OXView()

    def test_error(self):
        result = self.test_view.error(None, None)

        self.assertFalse(result)

    def test_add_player(self):
        expected_result = 'test'

        result = self.test_view.add_player(model=None, result=expected_result)

        self.assertEqual(expected_result, result)

    def test_get_current_player(self):
        expected_result = 'test'
        result = self.test_view.get_current_player(model=None, result=expected_result)

        self.assertEqual(expected_result, result)

    @patch('game.server.config.OXModel')
    def test_get_board(self, model_mock):
        expected_result = '''\n | | \n-----\n | | \n-----\n | | \n\ntest - X'''
        game_values = [-1, -1, -1, -1, -1, -1, -1, -1, -1]

        model_mock.return_value = model_mock
        model_mock.get_current_player.return_value = "test"
        result = self.test_view.get_board(model=model_mock, result=game_values)

        self.assertEqual(expected_result, result)

    def test_make_move(self):
        expected_result = 'test'

        result = self.test_view.make_move(model=None, result=expected_result)

        self.assertEqual(expected_result, result)

    def test_check_game_result(self):
        expected_result = 'test'

        result = self.test_view.check_game_result(model=None, result=expected_result)

        self.assertEqual(expected_result, result)
