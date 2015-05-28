import unittest

from logic.arrays import *

class TestArrayProblems(unittest.TestCase):
    def setUp(self):
        self.cross = [
            [1,1,0,1],
            [0,0,0,0],
            [1,1,0,1],
            [1,1,0,1],
        ]
        self.no_columns = [[]]
        self.string = "The quick brown fox jumps over the lazy dog."

    def test_unique(self):
        self.assertFalse(unique(self.string))
        self.assertTrue(unique("uniqe str"))
        self.assertTrue(unique('\0\n\t'))
        self.assertTrue(unique(''))

    def test_reverse(self):
        self.assertEqual(self.string[::-1] + '\0', reverse_cstr(self.string + '\0'))
        self.assertEqual('alihP\0', reverse_cstr('Phila\0delphia\0'))
        self.assertRaises(ValueError, reverse_cstr, '')
        self.assertRaises(ValueError, reverse_cstr, 'non c string')

    def test_anagrams(self):
        self.assertTrue(anagrams('pots', 'stop'))
        self.assertTrue(anagrams('', ''))

    def test_space_replace(self):
        self.assertEqual(self.string.replace(' ', '%20'), space_replace0(self.string))
        self.assertEqual(self.string.replace(' ', '%20'), space_replace1(self.string))
        self.assertEqual(self.string.replace(' ', '%20'), space_replace2(self.string))

    def test_rotate(self):
        test1 = [
            [1,0,1,1],
            [0,0,0,0],
            [1,0,1,1],
            [1,0,1,1],
        ]
        self.assertEqual(self.cross, rotate(test1))
        self.assertRaises(ValueError, rotate, self.no_columns)
        self.assertEqual([], rotate([]))

    def test_rotate_ip(self):
        test1 = [
            [1,0,1,1],
            [0,0,0,0],
            [1,0,1,1],
            [1,0,1,1],
        ]
        rotate_ip(test1)
        self.assertEqual(self.cross, test1)

        test2 = []
        rotate_ip(test2)
        self.assertEqual([], test2)

        test3 = [[]]
        self.assertRaises(ValueError, rotate_ip, test3)

    def test_is_rotated(self):
        self.assertTrue(is_rotated("waterbottle", "erbottlewat"))
        self.assertFalse(is_rotated("waterbotle", "erbottlewat"))
        self.assertFalse(is_rotated("watterbotle", "erbottlewat"))

    def test_row_blanker(self):
        inval = [
            [1,1,1,1],
            [1,1,0,1],
            [1,1,1,1],
            [1,1,1,1],
        ]

        self.assertEqual(self.cross, row_blanker(inval))
