from __future__ import annotations

from collections import deque
from uuid import uuid4

from aoc.lib.util import Input, get_problem_input

problem_input: Input = get_problem_input()
test_input: Input = get_problem_input(test=True)


class Packet:
    sub_packets: list[Packet] = []
    key: str
    value: int = 0
    version: int
    type_id: int
    length: int
    level = 0

    def __init__(self, bit_string: str, level=0):
        self.key = uuid4()
        self.level = level

        self.dprint(f"parsing: {bit_string}")
        self.version = int(bit_string[0:3], 2)
        self.type_id = int(bit_string[3:6], 2)

        self.dprint(f"version string: {bit_string[0:3]}")
        self.dprint(f"type id string: {bit_string[3:6]}")

        self.length = 6
        self.parse(bit_string[6:])

    def dprint(self, s: str) -> None:
        print(f"{'  ' * self.level}{s}")

    def parse(self, chunk: str) -> None:
        match (self.type_id):
            case 4:
                # Literal
                bits = ""
                self.dprint("literal packet found")

                for i in range(0, len(chunk), 5):
                    bits += chunk[i+1:i+5]
                    self.length += 5
                    if chunk[i] == "0":
                        break

                self.value = int(bits, 2)
                self.dprint(f"value is {self.value}")
            case _:
                # Operator
                self.dprint("operator packet found")
                length_type_id = int(chunk[0], 2)
                self.length += 1
                if length_type_id == 0:
                    length = int(chunk[1:16], 2)
                    self.length += 15
                    offset = 0
                    self.dprint(f"...by length {length}")

                    while True:
                        self.dprint(f"parsing sub-packet with offset {offset}")
                        new_packet = Packet(chunk[16 + offset:], self.level + 1)
                        self.sub_packets.append(new_packet)
                        offset += new_packet.length
                        self.length += new_packet.length
                        if offset >= length:
                            break
                else:
                    number_of_packets = int(chunk[1:12], 2)
                    self.dprint(f"...by number of packets: {number_of_packets}")
                    self.length += 11
                    offset = 0

                    for i in range(number_of_packets):
                        self.dprint(f"parsing sub-packet {i + 1} / {number_of_packets}")
                        new_packet = Packet(chunk[12 + offset:], self.level + 1)
                        offset += new_packet.length
                        self.length += new_packet.length
                        self.sub_packets.append(new_packet)
        self.dprint(f"packet length: {self.length}")

    def version_sum(self):
        total = 0
        queue: deque[Packet] = deque()
        visited: set[str] = set()

        queue.append(self)

        while len(queue) > 0:
            p = queue.popleft()
            if p.key in visited:
                continue

            visited.add(p.key)

            for packet in p.sub_packets:
                queue.append(packet)
            total += p.version

        return total


def hex_to_bin(hex_string: str) -> str:
    binary_string = ""
    for c in hex_string:
        b = int(c, base=16)
        binary_string += bin(b)[2:].zfill(4)

    return binary_string


def solve(problem_input: Input) -> int:
    binary_string = hex_to_bin(problem_input.raw(strip=True))
    packet = Packet(binary_string)

    return packet.version_sum()


def test() -> str:
    return str(solve(test_input))


def run() -> str:
    return str(solve(problem_input))
