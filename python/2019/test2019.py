import unittest

import day01
import day02
import day03
import day04


class Test2021(unittest.TestCase):

    def test_01(self):
        self.assertEqual(day01.part_1(day01.sample_data), 34241)
        self.assertEqual(day01.part_2(day01.sample_data), 51316)

        self.assertEqual(day01.part_1(day01.challenge_data), 3223398)
        self.assertEqual(day01.part_2(day01.challenge_data), 4832253)

    def test_02(self):
        self.assertEqual(day02.part_1(day02.challenge_data), 3101844)
        self.assertEqual(day02.part_2(day02.challenge_data), 8478)
        
    def test_03(self):
        self.assertEqual(day03.part_1(day03.sample_data_a), 159)
        self.assertEqual(day03.part_1(day03.sample_data_b), 135)
        self.assertEqual(day03.part_2(day03.sample_data_a), 610)
        self.assertEqual(day03.part_2(day03.sample_data_b), 410)

        self.assertEqual(day03.part_1(day03.challenge_data), 489)
        self.assertEqual(day03.part_2(day03.challenge_data), 93654)
        
    def test_04(self):
        self.assertTrue(day04.check_increasing_digits("111111")
                        and day04.check_adjacent_pairs("111111"))
        self.assertFalse(day04.check_increasing_digits("223450")
                         and day04.check_adjacent_pairs("223450"))
        self.assertFalse(day04.check_increasing_digits("123789")
                         and day04.check_adjacent_pairs("123789"))

        self.assertTrue(day04.check_increasing_digits("112233")
                        and day04.check_adjacent_pairs_group("112233"))
        self.assertFalse(day04.check_increasing_digits("123444")
                         and day04.check_adjacent_pairs_group("123444"))
        self.assertTrue(day04.check_increasing_digits("111122")
                        and day04.check_adjacent_pairs_group("111122"))

        challenge_part_1, challenge_part_2 = day04.count_passwords(day04.challenge_data)
        self.assertEqual(challenge_part_1, 1650)
        self.assertEqual(challenge_part_2, 1129)


if __name__ == "__main__":
    unittest.main()
