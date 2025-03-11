# Exercise 2: String Utilities


def reverse_string(s: str) -> str:
    return s[::-1]
    # TODO: Implement this function
    pass

print(reverse_string('imad'))

def count_vowels(s: str) -> int:
    L= ['a','e','i','o','u','A','E','I','O','U']
    k=0
    for i in s :
        if i in L :
            k+=1
    return k
   
    # TODO: Implement this function
    pass


def is_palindrome(s: str) -> bool:
    s = s.lower().replace(" ", "")
    return s == s[::-1]

    # TODO: Implement this function
    pass


def capitalize_words(s: str) -> str:
    if "  " in s :
        result = ""
        capitalize_next = True  
    
        for char in s:
            if char == " ":
                result += char 
                capitalize_next = True 
                continue
            if capitalize_next:
                result += char.upper()  
                capitalize_next = False
            else:
                result += char
        return result

    else : 
        mots = s.split()
        mots = [i[0].upper() + i[1:] if i else "" for i in mots]  # Correction de la capitalisation
        return ' '.join(mots)


    

    
    # TODO: Implement this function
    pass
