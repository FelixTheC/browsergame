from django.test import TestCase
from ..models import Spell
from element.models import Element


class TestSpellModel(TestCase):

    def test_create_new_spell(self):
        Element.objects.create(name='earth')
        spell = Spell.objects.create(name='spell#1',
                                     mana_cost=10.0,
                                     element_type=Element.objects.get(name='earth'),
                                     max_hit_points=5.0,
                                     min_hit_points=2.0)
        self.assertIsNotNone(spell)
        self.assertIsInstance(spell, Spell)

    def test_fail_create_new_spell(self):
        spell = Spell.objects.create(name='spell#2')
        self.assertIsNone(spell)