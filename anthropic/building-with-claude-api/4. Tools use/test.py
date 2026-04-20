import unittest
import math
from main import greeting, calculate_pi


class TestMain(unittest.TestCase):
    """Test cases for main.py functions"""
    
    def test_greeting(self):
        """Test that greeting function runs without error"""
        # This function prints but doesn't return anything
        # We just verify it doesn't raise an exception
        try:
            greeting()
            self.assertTrue(True)
        except Exception as e:
            self.fail(f"greeting() raised {type(e).__name__}: {e}")
    
    def test_calculate_pi_5_digits(self):
        """Test pi calculation to 5 decimal places"""
        result = calculate_pi(5)
        expected = 3.14159
        self.assertEqual(result, expected, 
                        f"Expected pi to 5 digits to be {expected}, got {result}")
    
    def test_calculate_pi_accuracy(self):
        """Test that calculated pi is close to math.pi"""
        result = calculate_pi(5)
        # Check that it's within a reasonable tolerance
        self.assertAlmostEqual(result, math.pi, places=5,
                              msg="Calculated pi should match math.pi to 5 decimal places")
    
    def test_calculate_pi_default(self):
        """Test pi calculation with default argument"""
        result = calculate_pi()
        self.assertEqual(result, 3.14159,
                        "Default calculation should return pi to 5 decimal places")
    
    def test_calculate_pi_different_precisions(self):
        """Test pi calculation with different precision values"""
        # Test 2 decimal places
        result_2 = calculate_pi(2)
        self.assertEqual(result_2, 3.14)
        
        # Test 3 decimal places
        result_3 = calculate_pi(3)
        self.assertEqual(result_3, 3.142)
        
        # Test 4 decimal places
        result_4 = calculate_pi(4)
        self.assertEqual(result_4, 3.1416)
    
    def test_calculate_pi_return_type(self):
        """Test that calculate_pi returns a float"""
        result = calculate_pi(5)
        self.assertIsInstance(result, float,
                            "calculate_pi should return a float")


if __name__ == '__main__':
    # Run the tests with verbose output
    print("Running tests for main.py...")
    print("=" * 70)
    unittest.main(verbosity=2)
