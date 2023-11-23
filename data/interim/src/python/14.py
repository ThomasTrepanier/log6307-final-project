import unittest

def next_braille_representation(current_rep):
    braille_sequence = "100000101000110000110100100100111000111100101100011000011100100010101010110010110110100110"
    index = braille_sequence.find(current_rep)

    if index != -1 and index < len(braille_sequence) - 6:
        next_rep = braille_sequence[index + 6: index + 12]
    else:
        next_rep = None

    return next_rep

class TestNextBrailleRepresentation(unittest.TestCase):

    def test_next_braille_representation(self):
        test_cases = [
            ('100000', '101000'),
            ('101000', '110000'),
            ('110000', '110100'),
            ('110100', '100100'),
            ('100100', '111000'),
            ('111000', '111100'),
            ('111100', '101100'),
            ('101100', '011000'),
            ('011000', '011100'),
            ('011100', '100010'),
            ('100010', '101010'),
            ('101010', '110010'),
            ('110010', '110110'),
            ('110110', '100110'),
            ('100110', '111010'),
            ('111010', '111110'),
            ('111110', '101110'),
            ('101110', '011010'),
            ('011010', '011110'),
            ('011110', '100011'),
            ('100011', '101011'),
            ('101011', '011101'),
            ('011101', '110011'),
            ('110011', '110111'),
            ('110111', '100111'),
            ('100111', '111011'),
        ]

        for current_rep, expected_next_rep in test_cases:
            with self.subTest(current_rep=current_rep):
                actual_next_rep = next_braille_representation(current_rep)
                self.assertEqual(actual_next_rep, expected_next_rep)

if __name__ == '__main__':
    unittest.main()
