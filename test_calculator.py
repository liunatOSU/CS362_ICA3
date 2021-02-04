import unittest
from calculator import addition, subtraction, multiplication, division

class TestCalc(unittest.TestCase):
  def test_addition(self):
    self.assertEqual(addition(5, 10), 15)
    
  def test_additionNeg(self):
    self.assertEqual(addition(6, -14), -8)
  
  def test_additionFloat(self):
    self.assertAlmostEqual(addition(3.4, 5), 8.4)
  
  def test_additionInvalid(self):
    self.assertEqual(addition("test", 5), None)
    
  def test_subtraction(self):
    self.assertEqual(subtraction(6, 8), -2)
    
  def test_subtractionNeg(self):
    self.assertEqual(subtraction(6, -8), 14)
  
  def test_subtractionFloat(self):
    self.assertAlmostEqual(subtraction(4.2, 2), 2.2)
  
  def test_subtractionInvalid(self):
    self.assertEqual(subtraction("test", 4), None)
    
  def test_multiplcation(self):
    self.assertEqual(multiplication(4, 8), 32)
    
  def test_multiplcationNeg(self):
    self.assertEqual(multiplication(6, -5), -30)
  
  def test_multiplcationFloat(self):
    self.assertAlmostEqual(multiplication(4, 6.8), 27.2)
  
  def test_multiplcationInvalid(self):
    self.assertEqual(multiplication("test", 7), None)
    
  def test_division(self):
    self.assertEqual(division(25, 5), 5)
    
  def test_divisionNeg(self):
    self.assertEqual(division(16, -2), -8)
  
  def test_divisionFloat(self):
    self.assertAlmostEqual(division(10, 4), 2.5)
    
  def test_divisionZero(self):
    self.assertEqual(division(5, 0), None)
  
  def test_divisionInvalid(self):
    self.assertEqual(division("test", 1), None)


if __name__ == '__main__':
    unittest.main()
