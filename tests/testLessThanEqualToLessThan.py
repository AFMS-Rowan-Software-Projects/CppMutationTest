from MutatorClass import Mutator
from mutant_dictionary import all_mutants
import unittest

class MutatorTest(unittest.TestCase):

    def setUp(self) -> None:
        self.m = all_mutants["ConditionalLessEqualsToLess"]  ##Insert Regex here...

    def test_StringWithDoubleLessThan__ReturnsUnchanged(self):
        str = "100 << 90 << 80 << 70"
        self.assertEqual(str, self.m.mutate(str))

    def test_StringWithLessThanEqual_ReturnsWithLessThan(self):
        input_str = "6 < 7 <= 9 <+ 10"
        final_str = "6 < 7 < 9 <+ 10"
        self.assertEqual(final_str, self.m.mutate(input_str))

    def test_GetName(self):
        self.assertEqual("ConditionalLessEqualsToLess", self.m.get_name())

if __name__ == '__main__':
    unittest.main()
