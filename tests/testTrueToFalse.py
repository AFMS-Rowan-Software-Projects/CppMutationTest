from MutatorClass import Mutator
from mutant_dictionary import all_mutants
import unittest

class MutatorTest(unittest.TestCase):

    def setUp(self) -> None:
        self.m = all_mutants["BooleanTrueToFalse"]  ##Insert Regex here...

    def test_StringWithTruePlus__ReturnsUnchanged(self):
        str = "100 true+ 90 true- 80 !true 70"
        self.assertEqual(str, self.m.mutate(str))

    def test_StringWithTrue_ReturnsWithFalse(self):
        input_str = "6 true; 7 true 9 =true 10"
        final_str = "6 false; 7 false 9 =false 10"
        self.assertEqual(final_str, self.m.mutate(input_str))

    def test_GetName(self):
        self.assertEqual("BooleanTrueToFalse", self.m.get_name())

if __name__ == '__main__':
    unittest.main()
