# https://adventofcode.com/2020/day/9

from src.util.exceptions import ResultExpectedError
from src.util.inputs import Inputs
from src.util.solution import Solution


class Solution2020Day09(Solution):

    def solve(self, inputs: Inputs) -> None:
        prepared_input = self.prepare(inputs.samples[0])
        invalid_number = self.solve_1(prepared_input, 5)
        self.sample_results_1.append(invalid_number)
        self.sample_results_2.append(self.solve_2(prepared_input, invalid_number))

        prepared_input = self.prepare(inputs.input)
        invalid_number = self.solve_1(prepared_input, 25)
        self.result_1 = invalid_number
        self.result_2 = self.solve_2(prepared_input, invalid_number)

    @staticmethod
    def prepare(data: str) -> list[int]:
        return [int(i) for i in data.splitlines()]

    def solve_1(self, numbers: list[int], pre_len: int) -> int:
        for i, n in enumerate(numbers[pre_len:]):
            if not self.valid(numbers[i : (pre_len + i)], n):
                return n
        raise ResultExpectedError

    @staticmethod
    def solve_2(numbers: list[int], target: int) -> int:
        for i in range(len(numbers)):
            for j in range(i + 2, len(numbers)):
                numbers_slice = numbers[i:j]
                sum_ = sum(numbers_slice)
                if sum_ == target:
                    return min(numbers_slice) + max(numbers_slice)
                if sum_ > target:
                    break
        raise ResultExpectedError

    @staticmethod
    def valid(preamble, n) -> bool:
        for i, a in enumerate(preamble[:-1]):
            for b in preamble[(i + 1) :]:
                if a + b == n:
                    return True
        return False
