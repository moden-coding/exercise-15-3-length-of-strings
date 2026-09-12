#!/usr/bin/env python3

import inspect
import re
import unittest

from src.lengths_of_strings import lengths


def source_rows(func):
    """Count non-empty, non-comment statement rows in func's source."""
    src = inspect.getsource(func)
    lines = [line.strip() for line in re.split(r'\n|;', src)
             if len(line.strip()) > 0 and not line.strip().startswith("#")]
    return len(lines)


class TestLengths(unittest.TestCase):

    def test_function_exists(self):
        try:
            lengths(["a"])
        except Exception as e:
            self.fail(
                'lengths should be callable as lengths(["a"]). '
                "Got exception: %r" % (e,))

    def test_return_type_is_dict(self):
        result = lengths(["a"])
        self.assertTrue(
            type(result) == dict,
            msg="lengths is expected to return a value which is of type "
            "dict, now it returns a value %s which is of type %s, when it "
            'is called as lengths(["a"]).'
            % (result, type(result).__name__))

    def test_function_body_is_short(self):
        max_lines = 2
        lines = source_rows(lengths)
        self.assertTrue(
            lines <= max_lines,
            msg="Function lengths must have at most %d rows in this "
            "exercise.\nThe function now has a total of %d rows "
            "(excluding empty rows and comments)." % (max_lines, lines))

    def test_worked_example_1(self):
        test_case = ["first", "second", "third"]
        expected = {"first": 5, "second": 6, "third": 5}
        result = lengths(test_case)
        self.assertEqual(
            result, expected,
            msg="Function is expected to return a dictionary\n%s\nwhen it "
            "is called with the parameters\n%s\nnow function returns\n%s"
            % (expected, test_case, result))

    def test_worked_example_2(self):
        test_case = ["dog", "cat", "guinea pig", "hamster", "gerbil", "goldfish"]
        expected = {"dog": 3, "cat": 3, "guinea pig": 10, "hamster": 7,
                    "gerbil": 6, "goldfish": 8}
        result = lengths(test_case)
        self.assertEqual(
            result, expected,
            msg="Function is expected to return a dictionary\n%s\nwhen it "
            "is called with the parameters\n%s\nnow function returns\n%s"
            % (expected, test_case, result))

    def test_worked_example_3(self):
        test_case = ["commodore", "atari", "amstrad", "msx", "spectrum"]
        expected = {"commodore": 9, "atari": 5, "amstrad": 7, "msx": 3,
                    "spectrum": 8}
        result = lengths(test_case)
        self.assertEqual(
            result, expected,
            msg="Function is expected to return a dictionary\n%s\nwhen it "
            "is called with the parameters\n%s\nnow function returns\n%s"
            % (expected, test_case, result))

    def test_empty_list_of_strings(self):
        result = lengths([])
        self.assertEqual(
            result, {},
            msg="lengths([]) should return an empty dictionary, since "
            "there are no strings to measure.")


if __name__ == '__main__':
    unittest.main()
