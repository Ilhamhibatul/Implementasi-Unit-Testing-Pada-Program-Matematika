import unittest
from unittest.mock import patch


def calculator(operasi, bilangan_1, bilangan_2):
    if operasi == '1':
        hasil = bilangan_1 + bilangan_2
        return hasil
    elif operasi == '2':
        hasil = bilangan_1 - bilangan_2
        return hasil
    elif operasi == '3':
        hasil = bilangan_1 * bilangan_2
        return hasil
    elif operasi == '4':
        hasil = bilangan_1 / bilangan_2
        return hasil
    else:
        return 'Tidak valid'


class TestCalculator(unittest.TestCase):

    @patch('builtins.input', side_effect=['1', '2', '3', '4'])
    def test_valid_operasi_input(self, mock_input):
        self.assertEqual(calculator('1', 5, 3), 8)
        self.assertEqual(calculator('2', 5, 3), 2)
        self.assertEqual(calculator('3', 5, 3), 15)
        self.assertEqual(calculator('4', 6, 2), 3)

    @patch('builtins.input', return_value='5')
    def test_invalid_operasi_input(self, mock_input):
        self.assertEqual(calculator('5', 5, 3), 'Tidak valid')

    @patch('builtins.input', side_effect=['1', '7'])
    def test_invalid_bilangan_input(self, mock_input):
        with self.assertRaises(TypeError):
            calculator('1', 'abc', 3)
        self.assertEqual(calculator('7', 5, 3), 'Tidak valid')


if __name__ == '__main__':
    unittest.main()

#Pengubahan Ekspektasi
import unittest
from unittest.mock import patch

def calculator(operasi, bilangan_1, bilangan_2):
    if operasi == '1':
        hasil = bilangan_1 + bilangan_2
        return hasil
    elif operasi == '2':
        hasil = bilangan_1 - bilangan_2
        return hasil
    elif operasi == '3':
        hasil = bilangan_1 * bilangan_2
        return hasil
    elif operasi == '4':
        hasil = bilangan_1 / bilangan_2
        return hasil
    else:
        return 'Tidak valid'

class TestCalculator(unittest.TestCase):

    @patch('builtins.input', side_effect=['1', '2', '3', '4'])
    def test_valid_operasi_input(self, mock_input):
        self.assertEqual(calculator('1', 5, 3), 9)
        self.assertEqual(calculator('2', 5, 3), 3)
        self.assertEqual(calculator('3', 5, 3), 18)
        self.assertEqual(calculator('4', 6, 2), 4)


    @patch('builtins.input', return_value='5')
    def test_invalid_operasi_input(self, mock_input):
        self.assertEqual(calculator('5', 5, 3), 'Tidak valid')

    @patch('builtins.input', side_effect=['1', '7'])
    def test_invalid_bilangan_input(self, mock_input):
        with self.assertRaises(TypeError):
            calculator('1', 'abc', 3)
        self.assertEqual(calculator('7', 5, 3), 'Tidak valid')

if __name__ == '__main__':
    unittest.main()

