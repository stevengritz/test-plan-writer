from typing import List, Union

def factorial(n: int) -> int:
    """Calculates the factorial of a number.
    
    Args:
        n: A non-negative integer
        
    Returns:
        The factorial of n
        
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0:
        return 1
    return n * factorial(n - 1)

def fibonacci(n: int) -> int:
    """Returns the nth number in the Fibonacci sequence.
    
    Args:
        n: The position in the sequence (0-based)
        
    Returns:
        The nth Fibonacci number
        
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("Fibonacci sequence not defined for negative indices")
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def calculate_mean(numbers: List[Union[int, float]]) -> float:
    """Calculates the arithmetic mean of a list of numbers.
    
    Args:
        numbers: List of numbers
        
    Returns:
        The arithmetic mean
        
    Raises:
        ValueError: If the list is empty
    """
    if not numbers:
        raise ValueError("Cannot calculate mean of empty list")
    return sum(numbers) / len(numbers)

def is_prime(n: int) -> bool:
    """Determines if a number is prime.
    
    Args:
        n: The number to check
        
    Returns:
        True if the number is prime, False otherwise
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
