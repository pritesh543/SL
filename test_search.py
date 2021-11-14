import unittest
from search import Solution


class SolutionTest(unittest.TestCase):    
    def test_find(self):
        input_strings_list = ["seo","stylight_team","team","helloworld", "foo"]
        solution = Solution(input_strings_list)
        matched_strings_list = solution.find("eos")

        self.assertTrue(["seo"] == matched_strings_list)

    def test_find_with_int(self):
        input_strings_list = ["seo","stylight_team","team","helloworld", "foo", 12]
        solution = Solution(input_strings_list)
        matched_strings_list = solution.find("e")

        self.assertTrue(["seo","stylight_team","team","helloworld"] == matched_strings_list)

    def test_find_empty_match_string(self):
        input_strings_list = ["seo","stylight_team","team","helloworld"]
        solution = Solution(input_strings_list)

        with self.assertRaises(ValueError) as exception_context:
            solution.find("")

        self.assertEqual(str(exception_context.exception), "Empty matching string is not supported!")

    def test_find_match_string_gt_word(self):
        input_strings_list = ["seo","team","hello"]
        solution = Solution(input_strings_list)
        matched_strings_list = solution.find("trysomething")
        self.assertTrue([] == matched_strings_list)



if __name__ == "__main__":
    unittest.main()