from django.test import TestCase
from ..models import Enemy
from element.models import Element


class EnemyModelTest(TestCase):

    def setUp(self):
        Element.objects.create(name='fire')
        Element.objects.create(name='water')

    def test_create_new_enemy(self):
        new_enemy = Enemy.objects.create(name='#1',
                                         level=1,
                                         live_points=100.00,
                                         resist_against_element=Element.objects.get(name='fire'),
                                         weak_against_element=Element.objects.get(pk=2),
                                         max_hit_points=20.00,
                                         min_hit_points=5.00,
                                         armor_points=30.00)
        self.assertIsNotNone(new_enemy)
        self.assertIsInstance(new_enemy, Enemy)

    def test_fail_creating_new_enemy(self):
        new_enemy = Enemy.objects.create(name='#2')
        self.assertIsNone(new_enemy)
