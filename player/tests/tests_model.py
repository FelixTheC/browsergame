from django.test import TestCase
from ..models import Player


class TestPlayerModel(TestCase):

    def test_create_new_player(self):
        player = Player.objects.create(username='player1',
                                       password='abc45678',
                                       email='test@test.com',
                                       )
        self.assertEqual(0, player.level)
        self.assertEqual(0.0, player.xp)
        self.assertEqual(100, player.live_points)
        self.assertEqual(100, player.max_live_points)
        self.assertEqual(50, player.mana_points)
        self.assertEqual(50, player.max_mana_points)
        self.assertEqual(5.0, player.armor_points)
        self.assertIsNone(player.spells)

    def test_fail_create_new_player(self):
        player = Player.objects.create(username='player2')
        self.assertIsNone(player)