import unittest
from search import Solution


class SolutionTest(unittest.TestCase):    
    def test_find(self):
        words = ["seo","stylight_team","team","helloworld", "foo"]
        solution = Solution(words)
        matched_words = solution.find("eos")

        self.assertTrue(["seo"] == matched_words)

    def test_find_with_int(self):
        words = ["seo","stylight_team","team","helloworld", "foo", 12]
        solution = Solution(words)
        matched_words = solution.find("e")

        self.assertTrue(["seo","stylight_team","team","helloworld"] == matched_words)

    def test_find_empty_match_string(self):
        words = ["seo","stylight_team","team","helloworld"]
        solution = Solution(words)

        with self.assertRaises(ValueError) as exception_context:
            solution.find("")

        self.assertEqual(str(exception_context.exception), "Empty matching string is not supported!")

    def test_find_match_string_gt_word(self):
        words = ["seo","team","hello"]
        solution = Solution(words)
        matched_words = solution.find("trysomething")
        self.assertTrue([] == matched_words)



if __name__ == "__main__":
    unittest.main()