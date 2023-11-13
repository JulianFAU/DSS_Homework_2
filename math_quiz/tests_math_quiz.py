import unittest
from math_quiz import create_random_int, create_random_math_operation, calculation


class TestMathGame(unittest.TestCase):

    def test_create_random_int(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = create_random_int(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_create_random_math_operation(self):
        self.assertIsInstance(create_random_math_operation(),str)
        

    def test_calculation(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (5, 2, '-', '5 - 2', 3),
                (5, 2, '*', '5 * 2', 10)
                
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                
                issue, answer = calculation(num1,num2,operator)
                self.assertEqual(issue, expected_problem)
                self.assertEqual(answer, expected_answer)
                

if __name__ == "__main__":
    unittest.main()
