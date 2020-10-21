"""Python functions for JavaScript Trials 1."""

import doctest

def output_all_items(items):
    """ Print each item in the given array
        >>> items = [1, 'hello', 'true']
        >>> output_all_items(items)
    """
    for item in items:
        print(item)


def get_all_evens(nums):
    """given list of nums, return list of even nums
    >>> nums = [7, 8, 10, 1, 2, 2]
    >>> get_all_evens(nums)
        [8, 10, 2, 2]
    """
    even_nums = []
    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)
    return even_nums


def get_odd_indices(items):
    """given list of items, return all elements at odd numbered indices.
    >>> get_odd_indices([1, 'hello', 'true', 500])
        ['hello', 500]
    """

    result = []
    for idx in range(len(items)):
        if idx % 2 != 0:
            result.append(items[idx])
    return result


def print_as_numbered_list(items):
    """Given an array, output a numbered list.
    >>> items = [1, 'hello', 'true']
    >>> print_as_numbered_list(items)
    1. 1
    2. hello
    3. true
    """
    
    for i, item in enumerate(items):
        print(f"{i+1}. {item}")


def get_range(start, stop):
    """ Return an array of numbers in a certain range. 
    >>> get_range(0,5)
    [0, 1, 2, 3, 4]
    >>> get_range(1,3)
    [1, 2]
    """
    nums = []
    for num in range(start,stop):
        nums.append(num)
    
    return nums

def censor_vowels(word):
    """ Given a string, return a string where vowels are replaced with '*'.
    >>> word = 'hello world'
    >>> censor_vowels(word)
    'h*ll* w*rld'
   """
    vowels = ["a", "e", "i", "o", "u"]
    censor = []
    for char in word:
        if char in vowels:
            censor.append("*")
        else:
            censor.append(char)
    return "".join(censor)
            

def snake_to_camel(string):
    """Given a string in snake case, return a string in upper camel case.
    >>> string = 'hello_world'
    >>> print(snake_to_camel(string))
    HelloWorld
    """
    camel_case = []
    split_string = string.split('_')
    
    for word in split_string:
        camel_case.append(word.title())
    return "".join(camel_case)


def longest_word_length(words):
    """Return the length of the longest word in the given array of words.
    >>> words = ['hello', 'world']
    >>> longest_word_length(words)
    5
    >>> words = ['jellyfish', 'zebra']
    >>> longest_word_length(words)
    9
    """

    length_of_words = []
    for word in words:
        length_of_words.append(len(word))
    length_of_words.sort()
    return length_of_words[-1]


def truncate(string):
    """Truncate repeating characters into one character.
    >>> string = 'aaaabbbbcccca'
    >>> truncate(string)
    'abca'
    >>> string = 'hi***!!!! wooow'
    >>> truncate(string)
    'hi*! wow'
    """
    result = []

    for char in string:
        if (len(result) == 0) or (char != result[len(result)-1]):
            result.append(char)

    return "".join(result)

def has_balanced_parens(string):
    """Return true if all parentheses in a given string are balanced.

    """
    par = 0
    for char in string:
        if char == "(":
            par += 1
        elif char == ")":
            par -= 1
    return par == 0
    # if par != 0:
    #     return False



def compress(string):
    """ Return a compressed version of the given string.
    >>> string = 'aabbaabb'
    >>> compress(string)
    'Hel2o, world! Cows go mo4.3'
    """

    compressed = []
    curr_char = ""
    char_count = 0
    
    if char_count>1:
        compressed.append(str(char_count))

    return "".join(compressed) 
    return "".join(compressed)


if __name__ == '__main__':
    import doctest
    result = doctest.testmod()
    if result.failed == 0:
        print('ALL TESTS PASSED') 
