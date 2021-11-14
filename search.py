"""
The string search module: Search a string sequence in given list of string in any order

Quickly search your matching string in a given list of strings
"""

from typing import List
import argparse


class Solution:
    """
    A class used to represent a String Search

    ...

    Attributes
    ----------
    words : List[str]
        a list of strings/words
    match_string : str
        the string to match in list of strings/words

    Methods
    -------
    find(match_string)
        Prints the list of strings/words which have match_string in any order
    """


    def __init__(self, words: List[str]):
        """
        Parameters
        ----------
        words : List[str]
            The list of strings/words
        """

        self.words = words
    

    def find(self, match_string: str) -> List[str]:
        """Find the list of words from given list with match_string.

        If the arguments are not valid then raising exceptions.


        Parameters
        ----------
        match_string : str
            The string to find in given list of strings/words

        Returns
        -------
        matched_words: List[str]
            The list of strings/words found with given matching string sequence

        Raises
        ------
        ValueError
            If string to match is empty or type other than str
        """

        if type(match_string) != str:
            raise ValueError("matching string of type other than str is not supported!")

        if match_string == "":
            raise ValueError("Empty matching string is not supported!")


        matched_words = []

        # for each word/string in words
        for word in self.words:
            
            # if input string is not str then skip
            if type(word) != str:
                continue

            # if match_string is gt then the input word then skip
            # bcoz the match_string will not found in input word

            if len(match_string) > len(word):
                continue

            # counter to maintain the 
            # len of consecutive search chars

            match_counter = 0
            
            # for each char in word
            
            for char in word:
                
                # if char is present in given string to match 
                # i.e. in match_string (consecutive)

                if char in match_string:
                    match_counter += 1
                else:
                    match_counter = 0

                # if match_string is already found in string 
                # then stop iterating over the string

                if len(match_string) == match_counter: 
                    matched_words.append(word)
                    break


        return matched_words



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='String finder')
    parser.add_argument('-l', '--words', help='List of strings to search in', required=True)
    parser.add_argument('-m', '--match_string', help='string to search in list of strings/words', required=True)

    args = parser.parse_args()

    solution = Solution(args.words.split(","))
    matched_words = solution.find(args.match_string)
    print(matched_words)