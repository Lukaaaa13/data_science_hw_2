import unittest
from math_quiz import make_random_number, choose_math_symbol, generate_problem_and_solution


class TestMathGame(unittest.TestCase):
    
    def test_function_of_make_random_number(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = make_random_number(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)
    
    def test_function_of_choose_math_symbol(self):
        for _ in range(1000):
            random_symbol = choose_math_symbol()
            self.assertTrue(random_symbol == '+' or random_symbol == '-' or random_symbol == '*')
    
    def test_function_of_generate_problem_and_solution(self):
        test_cases = [(5, 2, '+', '5 + 2', 7), (4,5,'*','4 * 5', 20)]
        
        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            
            # testing the string representation
            string_representation = str(num1) + ' ' + operator + ' ' + str(num2)
            self.assertTrue(string_representation == expected_problem)

            # testing whether the solutions are correctly calculated
            if operator == '+':
                self.assertTrue((num1 + num2) == expected_answer)
            elif operator == '-':
                self.assertTrue((num1 - num2) == expected_answer)
            elif operator == '*':
                self.assertTrue((num1 * num2) == expected_answer)
                    


if __name__ == "__main__":
    unittest.main()
