from MutatorClass import Mutator
from mutant_dictionary import all_mutants
import unittest

class MutatorTest(unittest.TestCase):

    def setUp(self) -> None:
        self.m = all_mutants["BooleanFalseToTrue"]  ##Insert Regex here...

    def test_StringWithTrueSemi__ReturnsUnchanged(self):
        str = "100 false+ 90 false- 80 !false 70"
        self.assertEqual(str, self.m.mutate(str))

    def test_StringWithTrue_ReturnsWithFalse(self):
        input_str = "6 false; 7 false 9 =false 10"
        final_str = "6 true; 7 true 9 =true 10"
        self.assertEqual(final_str, self.m.mutate(input_str))

    def test_GetName(self):
        self.assertEqual("BooleanFalseToTrue", self.m.get_name())

if __name__ == '__main__':
    unittest.main()
