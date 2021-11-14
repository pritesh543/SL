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
    input_strings_list : List[str]
        a list of strings
    match_string : str
        the string to match in list of strings

    Methods
    -------
    find(match_string)
        Prints the list of strings which have match_string in any order
    """


    def __init__(self, input_strings_list: List[str]):
        """
        Parameters
        ----------
        input_strings_list : List[str]
            The list of strings
        """

        self.input_strings_list = input_strings_list
    

    def find(self, match_string: str) -> List[str]:
        """Find the list of strings from given list with match_string.

        If the arguments are not valid then raising exceptions.


        Parameters
        ----------
        match_string : str
            The string to find in given list of strings

        Returns
        -------
        matched_strings_list: List[str]
            The list of strings found with given matching string sequence

        Raises
        ------
        ValueError
            If string to match is empty or type other than str
        """

        if type(match_string) != str:
            raise ValueError("matching string of type other than type str is not supported!")

        if match_string == "":
            raise ValueError("Empty matching string is not supported!")


        matched_strings_list = []

        # for each input_string in input_strings_list
        for input_string in self.input_strings_list:
            
            # if input string is not str then skip
            if type(input_string) != str:
                continue

            # if len(match_string) is gt then len(input_string) then skip
            # bcoz the match_string will not found in input input_string

            if len(match_string) > len(input_string):
                continue

            # counter to maintain the 
            # len of consecutive search chars

            match_counter = 0
            
            # for each char in input_strings
            
            for char in input_string:
                
                # if char is present in given string to match 
                # i.e. in match_string (consecutive)

                if char in match_string:
                    match_counter += 1
                else:
                    match_counter = 0

                # if match_string is already found in string 
                # then stop iterating over the string

                if len(match_string) == match_counter: 
                    matched_strings_list.append(input_string)
                    break


        return matched_strings_list



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='String finder')
    parser.add_argument('-l', '--input_strings_list', help='List of strings to search in', required=True)
    parser.add_argument('-m', '--match_string', help='string to search in list of strings', required=True)

    args = parser.parse_args()

    solution = Solution(args.input_strings_list.split(","))
    matched_strings_list = solution.find(args.match_string)
    print(matched_strings_list)