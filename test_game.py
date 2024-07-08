# test_game.py
import unittest
from unittest.mock import patch
from game import get_computer_choice, determine_winner

class TestGame(unittest.TestCase):

    def test_get_computer_choice(self):
        # Test that get_computer_choice returns a valid choice
        self.assertIn(get_computer_choice(), ["rock", "paper", "scissors"])

    @patch('builtins.input', side_effect=["user_input"])  # Mock input() to return "user_input"
    def test_determine_winner(self, mock_input):
        test_cases = [
            ("rock", "rock", "tie"),
            ("rock", "paper", "lose"),
            ("rock", "scissors", "win"),
            # Adding the missing scenarios for comprehensive coverage
            ("paper", "rock", "win"),
            ("paper", "paper", "tie"),
            ("paper", "scissors", "lose"),
            ("scissors", "rock", "lose"),
            ("scissors", "paper", "win"),
            ("scissors", "scissors", "tie"),
        ]
        for user_choice, computer_choice, expected in test_cases:
            with self.subTest(user_choice=user_choice, computer_choice=computer_choice, expected=expected):
                # Test that determine_winner returns the correct result
                self.assertEqual(determine_winner(user_choice, computer_choice), expected)

    # Example test case for invalid input handling, if applicable
    def test_determine_winner_with_invalid_input(self):
        invalid_inputs = ["", "lizard", "spock", 123]
        for invalid_input in invalid_inputs:
            with self.subTest(invalid_input=invalid_input):
                # Assuming your game logic raises a ValueError for invalid inputs
                with self.assertRaises(ValueError):
                    determine_winner(invalid_input, get_computer_choice())

if __name__ == '__main__':
    unittest.main()