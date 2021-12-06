import unittest

import day01


class Test2021(unittest.TestCase):

    def test_01(self):
        self.assertEqual(day01.part_1(day01.sample_data), 34241)
        self.assertEqual(day01.part_2(day01.sample_data), 51316)

        self.assertEqual(day01.part_1(day01.challenge_data), 3223398)
        self.assertEqual(day01.part_2(day01.challenge_data), 4832253)


if __name__ == "__main__":
    unittest.main()
