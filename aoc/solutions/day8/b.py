from aoc.lib.util import Input, get_problem_input

problem_input: Input = get_problem_input()
test_input: Input = get_problem_input(test=True)


def solve(problem_input: Input) -> int:
    total = 0

    for line in problem_input.lines():
        digits: dict[int, set(str)] = {i: set() for i in range(10)}
        signal_line, output = line.split("|")
        signals = [set(s) for s in signal_line.split()]

        for signal in signals:
            match len(signal):
                case 2:
                    # 1
                    digits[1] = signal
                case 3:
                    # 7
                    digits[7] = signal
                case 4:
                    # 4
                    digits[4] = signal
                case 7:
                    digits[8] = signal

        signals.remove(digits[1])
        signals.remove(digits[7])
        signals.remove(digits[4])
        signals.remove(digits[8])

        segment_a = digits[1].pop()
        segment_b = digits[1].pop()
        digits[1] = set([segment_a, segment_b])

        fragment_8_diff_1 = digits[8].difference(digits[1])

        if fragment_8_diff_1.union(segment_a) in signals:
            # Hit, we found 6
            digits[6] = fragment_8_diff_1.union(segment_a)
        else:
            # Only one other choice
            digits[6] = fragment_8_diff_1.union(segment_b)

        signals.remove(digits[6])

        # Remaining digits of length 6: 9 and 0
        # 4 and 9 fully intersect
        # i.e. 4 diff 9 == 0 and 4 intersect 9 == 4
        len_6 = []
        for s in signals:
            if len(s) == 6:
                len_6.append(s)

        if len(digits[4].difference(len_6[0])) == 0:
            # 9 found
            digits[9] = len_6[0]
            digits[0] = len_6[1]
        else:
            # 0 found
            digits[9] = len_6[1]
            digits[0] = len_6[0]

        signals.remove(digits[9])
        signals.remove(digits[0])

        # Remaining digits: 2, 3, 5
        # 1 and 3 fully intersect
        for s in signals:
            if len(digits[1].difference(s)) == 0:
                # 3 found
                digits[3] = s
                break

        signals.remove(digits[3])

        # 5 and 9 fully intersect
        if len(signals[0].difference(digits[9])) == 0:
            # 5 found
            digits[5] = signals[0]
            digits[2] = signals[1]
        else:
            # 2 found
            digits[2] = signals[0]
            digits[5] = signals[1]

        s = ""
        for d in output.split():
            digit = set(d)
            for k, v in digits.items():
                if v == digit:
                    s += str(k)

        total += int(s)

    return total


def test() -> str:
    return str(solve(test_input))


def run() -> str:
    return str(solve(problem_input))
