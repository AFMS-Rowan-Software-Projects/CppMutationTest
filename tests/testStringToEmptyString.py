from MutatorClass import Mutator
from mutant_dictionary import all_mutants
import unittest

class MutatorTest(unittest.TestCase):

    def setUp(self) -> None:
        self.m = all_mutants["StringToEmpty"]  ##Insert Regex here...

    def test_StringWithTrueSemi__ReturnsUnchanged(self):
        str = ''
        self.assertEqual(str, self.m.mutate(str))

    def test_StringWithTrue_ReturnsWithFalse(self):
        input_str = '"abc This is a Test Str1ng w/ speci@l chars!"'
        final_str = ""
        self.assertEqual(final_str, self.m.mutate(input_str))

    def test_GetName(self):
        self.assertEqual("StringToEmpty", self.m.get_name())

if __name__ == '__main__':
    unittest.main()
