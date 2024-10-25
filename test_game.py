import unittest
from main import check_error_line, switch_player

# Тесты для функции check_error_line
class TestCheckErrorLine(unittest.TestCase):
    def test_correct_input(self):
        # Тестирование правильного ввода
        self.assertTrue(check_error_line(5, 5))

    def test_incorrect_input(self):
        # Тестирование неправильного ввода
        self.assertFalse(check_error_line(3, 5))

# Тесты для функции switch_player
class TestSwitchPlayer(unittest.TestCase):
    def test_switch_to_player_2(self):
        # Тестирование смены с игрока 1 на игрока 2
        self.assertEqual(switch_player(1), 2)

    def test_switch_to_player_1(self):
        # Тестирование смены с игрока 2 на игрока 1
        self.assertEqual(switch_player(2), 1)

if __name__ == "__main__":
    unittest.main()
