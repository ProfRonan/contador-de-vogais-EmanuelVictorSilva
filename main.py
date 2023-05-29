"""This program counts the number of vowels in a string."""
def as_vogais(c):
    vogais = "aeiouAEIOU"
    if (c in vogais):
      return  True
    else:
        return False
def count_vowels(string:str) -> int:
    soma = 0
    for c in string:
        if(as_vogais(c) == True):
            soma += 1
    return soma

    """
    Takes in a string and returns the number of vowels in the string.

    Args:
        string (str): The string to count vowels in.

    Returns:
        int: The number of vowels in the string.
    """
