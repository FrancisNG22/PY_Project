import unittest
import myProgramlab5 as prog

class TestMyProgram(unittest.TestCase):

    def test_EngineType(self):
        print("Testing")

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_EngineType(self):
        vios = prog.Vehicle('4', 'petrol', 5, 180)
        self.assertEqual(vios.type_of_tanks, 'petrol')


if __name__ == '__main__':
    unittest.main()
