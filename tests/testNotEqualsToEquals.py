from MutatorClass import Mutator
from mutant_dictionary import all_mutants
import unittest

class MutatorTest(unittest.TestCase):

    def setUp(self) -> None:
        self.m = all_mutants["EqualityNotEqualsToEquals"] ##Insert Regex here...

    def test_StringWithoutNotEquals__ReturnsUnchanged(self):
        str = "if((a || b) & (c || d))"
        self.assertEqual(str, self.m.mutate(str))

    def test_StringWithNotEquals_ReturnsWithEquals(self):
        input_str = "if((a == b) & (a != b))"
        final_str = "if((a == b) & (a == b))"
        self.assertEqual(final_str, self.m.mutate(input_str))

    def test_GetName(self):
        self.assertEqual("EqualityNotEqualsToEquals", self.m.get_name())

if __name__ == '__main__':
    unittest.main()