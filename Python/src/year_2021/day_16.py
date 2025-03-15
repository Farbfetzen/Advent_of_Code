# https://adventofcode.com/2021/day/16

from math import prod
from typing import NamedTuple

from src.util.inputs import Inputs
from src.util.solution import Solution


class Packet(NamedTuple):
    version: int
    type_id: int
    value: int
    sub_packets: list


class Solution2021Day16(Solution):

    def solve(self, inputs: Inputs) -> None:
        for i, sample in enumerate(inputs.samples):
            prepared_input = self.prepare(inputs.samples[i])
            if i < 4:
                self.sample_results_1.append(self.solve_1(prepared_input))
            else:
                self.sample_results_2.append(self.solve_2(prepared_input))

        prepared_input = self.prepare(inputs.input)
        self.result_1 = self.solve_1(prepared_input)
        self.result_2 = self.solve_2(prepared_input)

    @staticmethod
    def prepare(data: str) -> str:
        return bin(int(data, 16))[2:].zfill(len(data) * 4)

    def decode(self, transmission: str, i: int) -> tuple[Packet, int]:
        version = int(transmission[i:(i + 3)], 2)
        type_id = int(transmission[(i + 3):(i + 6)], 2)
        i += 6
        if type_id == 4:
            value, i = self.get_literal_value(transmission, i)
            return Packet(version, type_id, value, []), i
        length_type_id = transmission[i]
        i += 1
        if length_type_id == "0":
            sub_packets, i = self.get_sub_packets_by_length(transmission, i)
        else:
            sub_packets, i = self.get_sub_packets_by_number(transmission, i)
        value = self.calculate_value(type_id, sub_packets)
        return Packet(version, type_id, value, sub_packets), i

    @staticmethod
    def get_literal_value(transmission: str, i: int) -> tuple[int, int]:
        value = ""
        while True:
            last_group = transmission[i] == "0"
            value += transmission[(i + 1):(i + 5)]
            i += 5
            if last_group:
                break
        return int(value, 2), i

    def get_sub_packets_by_length(self, transmission: str, i: int) -> tuple[list[Packet], int]:
        sub_packets = []
        length_of_sub_packets = int(transmission[i:(i + 15)], 2)
        i += 15
        length_used = 0
        while length_used < length_of_sub_packets:
            sub_packet, new_i = self.decode(transmission, i)
            sub_packets.append(sub_packet)
            length_used += new_i - i
            i = new_i
        return sub_packets, i

    def get_sub_packets_by_number(self, transmission: str, i: int) -> tuple[list[Packet], int]:
        sub_packets = []
        number_of_sub_packets = int(transmission[i:(i + 11)], 2)
        i += 11
        for _ in range(number_of_sub_packets):
            sub_packet, i = self.decode(transmission, i)
            sub_packets.append(sub_packet)
        return sub_packets, i

    @staticmethod
    def calculate_value(type_id: int, sub_packets):
        value = 0
        if type_id <= 3:
            values = (sub_packet.value for sub_packet in sub_packets)
            if type_id == 0:
                value = sum(values)
            elif type_id == 1:
                value = prod(values)
            elif type_id == 2:
                value = min(values)
            elif type_id == 3:
                value = max(values)
        else:
            sub_a, sub_b = sub_packets
            if type_id == 5:
                value = sub_a.value > sub_b.value
            elif type_id == 6:
                value = sub_a.value < sub_b.value
            elif type_id == 7:
                value = sub_a.value == sub_b.value
            value = int(value)
        return value

    def sum_versions(self, packet: Packet) -> int:
        total = packet.version
        for sub_packet in packet.sub_packets:
            total += self.sum_versions(sub_packet)
        return total

    def solve_1(self, transmission: str) -> int:
        outer_packet = self.decode(transmission, 0)[0]
        return self.sum_versions(outer_packet)

    def solve_2(self, transmission: str) -> int:
        outer_packet = self.decode(transmission, 0)[0]
        return outer_packet.value
