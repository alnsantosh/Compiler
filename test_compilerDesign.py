from unittest import TestCase
from CompilerDesign import CompilerDesign

class TestCompilerDesign(TestCase):

    def test_start_positive(self):
        s=CompilerDesign()
        self.assertEquals(s.start(),[5,1,29])
        self.assertNotEqual(s.start(),[5,1])

    def test_start_negative(self):
        s=CompilerDesign()
        self.assertRaises(Exception,s.start())
