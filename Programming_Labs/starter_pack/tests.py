import unittest
import modules.iterators as iterators
import modules.generators as gens


class correct_sequences(object):
    """container for correct sequences, such as fib and countdown
    Requires list length at creation"""

    def __init__(self, length):
        self.length = length
        self.sequence = list()

    # fibonacci
    def fibonacci(self):
        self.sequence.clear()

        for i in range(self.length):
            if i == 0 or i == 1:
                self.sequence.append(i)
                continue
            self.sequence.append(self.sequence[i - 1] + self.sequence[i - 2])
        return self.sequence

    # countdown
    def countdown(self):
        self.sequence.clear()
        countdown_start = self.length

        for i in range(countdown_start):
            self.sequence.append(countdown_start)
            countdown_start -= 1
        return self.sequence

    # reversed countdown
    def rev_countdown(self):
        self.sequence.clear()

        for i in range(self.length):
            self.sequence.append(i)
        return self.sequence

    # geometric progression
    def geom_progression(self, ratio):
        self.sequence = [1]

        for i in range(1, self.length):
            self.sequence.append(self.sequence[-1] * ratio)
        return self.sequence


# create instance of class
sequence = correct_sequences(2000)


class iter_test(unittest.TestCase):
    """class with test for iterators module"""

    def test_fib(self):
        i = 0
        correct_sequence = sequence.fibonacci()

        for item in iterators.fib(sequence.length):
            self.assertEqual(item, correct_sequence[i])
            i += 1

    def test_countdown(self):
        i = 0
        correct_sequence = sequence.countdown()

        for item in iterators.countdown(sequence.length):
            self.assertEqual(item, correct_sequence[i])
            i += 1

    def test_geom_progression(self):
        i = 0
        ratio = 5
        correct_sequence = sequence.geom_progression(ratio)

        for item in iterators.GP(sequence.length, ratio):
            self.assertEqual(item, correct_sequence[i])
            i += 1

    def test_rev_countdown(self):
        i = 0
        correct_sequence = sequence.rev_countdown()

        for item in reversed(iterators.countdown(sequence.length)):
            self.assertEqual(item, correct_sequence[i])
            i += 1


class gen_test(unittest.TestCase):
    """class with test for generators module"""

    def test_fib(self):
        item = gens.fib()
        correct_sequence = sequence.fibonacci()

        for i in range(sequence.length):
            self.assertEqual(next(item), correct_sequence[i])

    def test_countdown(self):
        item = gens.countdown(sequence.length)
        correct_sequence = sequence.countdown()

        for i in range(sequence.length):
            self.assertEqual(next(item), correct_sequence[i])

    def test_geom_progression(self):
        item = gens.GeomProg(5)
        correct_sequence = sequence.geom_progression(5)

        for i in range(sequence.length):
            self.assertEqual(next(item), correct_sequence[i])


# main module
if __name__ == '__main__':
    unittest.main()
