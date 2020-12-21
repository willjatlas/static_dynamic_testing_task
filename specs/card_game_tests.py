import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.card_game = CardGame()
        self.card = Card("Hearts", 1)
        self.card2 = Card("Spades", 7)

    def test_ace_check_returns_true(self):
        self.assertTrue(self.card_game.check_for_ace(self.card))
    
    def test_ace_check_returns_false(self):
        self.assertFalse(self.card_game.check_for_ace(self.card2))
    
    def test_check_highest_card(self):
        self.assertEqual(self.card2.value, self.card_game.highest_card
                        (self.card, self.card2).value)
    
    def test_card_total(self):
        cards = [self.card, self.card2]
        self.assertEqual("You have a total of 8", self.card_game.cards_total(cards))
