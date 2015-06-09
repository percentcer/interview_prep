import unittest

from logic.bits import *

class TestBits(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_bits(self):
        pass

    def test_insert_number(self):
        self.assertTrue(insert_number(0b10101, 0b10000000000, 6, 2), 0b10001010100)
        self.assertTrue(insert_number(0b110011, 0b111111111111, 10, 2), 0b111001100000)
        self.assertRaises(ValueError, insert_number, 0b11, 0b111, 0, 0)
        self.assertRaises(ValueError, insert_number, 0b111, 0b11, 0, 0)

    def test_right_count(self):
        self.assertEqual(count_right_repeats(0b101100111, 1), 3)
        self.assertEqual(count_right_repeats(0b101100111, 0), 0)
        self.assertEqual(count_right_repeats(0b101100000, 0), 5)

    def test_next_largest_smallest(self):
        self.assertEqual(next_largest_with_same_one_count(0b011001), 0b011010)
        self.assertEqual(next_largest_with_same_one_count(0b000111), 0b001011)
        self.assertEqual(next_smallest_with_same_one_count(0b010101), 0b010011)
        self.assertEqual(next_smallest_with_same_one_count(0b100000), 0b010000)
