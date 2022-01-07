from MutatorClass import Mutator
from mutant_dictionary import all_mutants
import unittest

class MutatorTest(unittest.TestCase):

    def setUp(self) -> None:
        self.m = all_mutants["LogicalOrToAnd"]  ##Insert Regex here...

    def test_StringWithoutOr__ReturnsUnchanged(self):
        str = "if((a == b) & (c != d))"
        self.assertEqual(str, self.m.mutate(str))

    def test_StringWithOr_ReturnsWithAnd(self):
        input_str = "if((a == b)||(a != b))"
        final_str = "if((a == b)&&(a != b))"
        self.assertEqual(final_str, self.m.mutate(input_str))

    def test_GetName(self):
        self.assertEqual("LogicalOrToAnd", self.m.get_name())

if __name__ == '__main__':
    unittest.main()

