import unittest

def next_braille_representation(current_rep):
    # Convert the current representation to an integer (treated as binary)
    current_int = int(current_rep, 2)

    # Calculate the next integer representation by adding 1 (0b1)
    next_int = current_int + 1

    # Convert the next integer back to a 6-bit binary string
    next_rep = format(next_int, '06b')

    return next_rep

class TestNextBrailleRepresentation(unittest.TestCase):

    def test_next_braille_representation(self):
        test_cases = {
            '100000': '100001',
            '100001': '100010',
            '011110': '011111',
            '011111': '100000',
        }

        for current_rep, expected_next_rep in test_cases.items():
            with self.subTest(current_rep=current_rep):
                actual_next_rep = next_braille_representation(current_rep)
                self.assertEqual(actual_next_rep, expected_next_rep)

if __name__ == '__main__':
    unittest.main()
