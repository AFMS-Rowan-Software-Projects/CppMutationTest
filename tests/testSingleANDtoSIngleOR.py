from MutatorClass import Mutator
from mutant_dictionary import all_mutants
import unittest

class MutatorTest(unittest.TestCase):

    def setUp(self) -> None:
        self.m = all_mutants["LogicalBitwiseAndToOr"] ##Insert Regex here...

    def test_StringWithoutAnd__ReturnsUnchanged(self):
        str = "if((a && b) | (c || d))"
        self.assertEqual(str, self.m.mutate(str))

    def test_StringWithAnd_ReturnsWithOr(self):
        input_str = "(a & b)"
        final_str = "(a | b)"
        self.assertEqual(final_str, self.m.mutate(input_str))

    def test_GetName(self):
        self.assertEqual("LogicalBitwiseAndToOr", self.m.get_name())

if __name__ == '__main__':
    unittest.main()
