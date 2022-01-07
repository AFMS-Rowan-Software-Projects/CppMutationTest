from MutatorClass import Mutator
from mutant_dictionary import all_mutants
import unittest

class MutatorTest(unittest.TestCase):

    def setUp(self) -> None:
        self.m = all_mutants["IfToFalse"]  ##Insert Regex here...

    def test_StringWithoutConditional__ReturnsUnchanged(self):
        str = "printf(\"Test line.\");"
        self.assertEqual(str, self.m.mutate(str))

    def test_StringWithConditional_ReturnsFalseStatement(self):
        input_str = "if((a == b) && (a != b)){ printf(\"Test line.\"); }"
        final_str = "if(false){ printf(\"Test line.\"); }"
        self.assertEqual(final_str, self.m.mutate(input_str))

    def test_StringWithForLoop_ReturnsUnchanged(self):
        str = "for(int i = 0; i < 5; i++){ printf(\"Test line.\"); }"
        self.assertEqual(str, self.m.mutate(str))

    def test_StringWithTrueStatement_ReturnsFalseStatement(self):
        input_str = "if(true){ printf(\"Test line.\"); }"
        final_str = "if(false){ printf(\"Test line.\"); }"
        self.assertEqual(final_str, self.m.mutate(input_str))

    def test_GetName(self):
        self.assertEqual("IfToFalse", self.m.get_name())



if __name__ == '__main__':
    unittest.main()
