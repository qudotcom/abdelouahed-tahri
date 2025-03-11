# Exercise 2: String Utilities


def reverse_string(s: str) -> str:
    """
    Return the input string in reverse order.

    Args:
        s: Input string

    Returns:
        The reversed string
    """
    return s[::-1]

def count_vowels(s: str) -> int:
    """
    Return the number of vowels (a, e, i, o, u) in the input string.
    Case-insensitive: both uppercase and lowercase vowels should be counted.

    Args:
        s: Input string

    Returns:
        The number of vowels in the string
    """
    Vowels = (a, e, i, o, u, A, E, I, O, U)
    c=0
    for l in s:
        if l in Vowels : c+=1 
    return c

def is_palindrome(s: str) -> bool:
    """
    Check if the input string is a palindrome.
    A palindrome reads the same backward as forward.
    Spaces and case should be ignored.

    Args:
        s: Input string

    Returns:
        True if the string is a palindrome, False otherwise
    """
    L1=s.split()
    if len(L1[0]) == 1 : 
         L2=L[::-1]
         return L1 == L2
    else :
         L11=[]
         for i in range(len(L1)) : L11 += L1[i]
         L22=L11[::-1]
         return L11 = L22

def capitalize_words(s: str) -> str:
    """
    Capitalize the first letter of each word in the input string.

    Args:
        s: Input string

    Returns:
        The input string with the first letter of each word capitalized
    """
    L = s.split()
    for x in in range(len(L)) : L[x] = capitalize(L[x])
    result = ""
    for x in range(L) : result += L[x]
    return result
