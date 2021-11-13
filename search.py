"""
The string search module: Search a string sequence in given list of string in any order

Quickly search your matching string in a given list of strings
"""

from typing import List


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
        """Prints what the animals name is and what sound it makes.

        If the argument `sound` isn't passed in, the default Animal
        sound is used.

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
        NotImplementedError
            If string to match is empty
        """

        if self.match_string == "":
            raise NotImplementedError("Empty matching string is not supported!")


        matched_words = []

        # for each word/string in words
        for word in self.words:
            
            if type(word) != str:
                raise ValueError("Only considering string as of now!")
                

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

