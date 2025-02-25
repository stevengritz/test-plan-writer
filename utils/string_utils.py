def reverse_string(text: str) -> str:
    """Reverses the input string.
    
    Args:
        text: The string to reverse
        
    Returns:
        The reversed string
    """
    return text[::-1]

def count_vowels(text: str) -> int:
    """Counts the number of vowels in a string.
    
    Args:
        text: The string to analyze
        
    Returns:
        The number of vowels found
    """
    vowels = set('aeiouAEIOU')
    return sum(1 for char in text if char in vowels)

def is_palindrome(text: str) -> bool:
    """Checks if a string is a palindrome.
    
    Args:
        text: The string to check
        
    Returns:
        True if the string is a palindrome, False otherwise
    """
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned_text == cleaned_text[::-1]

def word_frequency(text: str) -> dict:
    """Counts the frequency of each word in a string.
    
    Args:
        text: The string to analyze
        
    Returns:
        A dictionary with words as keys and their frequencies as values
    """
    words = text.lower().split()
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency
