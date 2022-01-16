import unittest

import day01
import day02
import day03
import day04
import day06


class Test2021(unittest.TestCase):

    def test_01(self):
        sample_data = day01.get_data(day01.SAMPLE_PATH)
        self.assertEqual(day01.part_1(sample_data), 34241)
        self.assertEqual(day01.part_2(sample_data), 51316)

        challenge_data = day01.get_data(day01.INPUT_PATH)
        self.assertEqual(day01.part_1(challenge_data), 3223398)
        self.assertEqual(day01.part_2(challenge_data), 4832253)

    def test_02(self):
        challenge_data = day02.get_data(day02.INPUT_PATH)
        self.assertEqual(day02.part_1(challenge_data), 3101844)
        self.assertEqual(day02.part_2(challenge_data), 8478)
        
    def test_03(self):
        sample_data = day03.get_data(day03.SAMPLE_PATH)
        self.assertEqual(day03.part_1(sample_data[0]), 159)
        self.assertEqual(day03.part_1(sample_data[1]), 135)
        self.assertEqual(day03.part_2(sample_data[0]), 610)
        self.assertEqual(day03.part_2(sample_data[1]), 410)

        challenge_data = day03.get_data(day03.INPUT_PATH)[0]
        self.assertEqual(day03.part_1(challenge_data), 489)
        self.assertEqual(day03.part_2(challenge_data), 93654)
        
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

        challenge_data = day04.get_data(day04.INPUT_PATH)
        challenge_part_1, challenge_part_2 = day04.count_passwords(challenge_data)
        self.assertEqual(challenge_part_1, 1650)
        self.assertEqual(challenge_part_2, 1129)

    def test_06(self):
        sample_data = day06.get_data(day06.SAMPLE_PATH)
        self.assertEqual(day06.part_1(day06.decode_orbits(sample_data[0])), 42)
        self.assertEqual(day06.part_2(day06.decode_orbits(sample_data[1])), 4)

        challenge_data = day06.decode_orbits(day06.get_data(day06.INPUT_PATH)[0])
        self.assertEqual(day06.part_1(challenge_data), 253104)
        self.assertEqual(day06.part_2(challenge_data), 499)


if __name__ == "__main__":
    unittest.main()
