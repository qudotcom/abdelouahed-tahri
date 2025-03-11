
# Exercise 3: Temperature Converter
from typing import Union

# Defining a Temperature type for cleaner type hints
Temperature = Union[int, float]


def celsius_to_fahrenheit(celsius: Temperature) -> float:
    F = celsius * 9/5 + 32
    return F
    # TODO: Implement this function
    pass


def fahrenheit_to_celsius(fahrenheit: Temperature) -> float:
    C = (fahrenheit - 32) * 5/9
    return C
    # TODO: Implement this function
    pass


def celsius_to_kelvin(celsius: Temperature) -> float:
    K = celsius + 273.15
    return  K

    # TODO: Implement this function
    pass


def kelvin_to_celsius(kelvin: Temperature) -> float:
    C = kelvin - 273.15
    if C >= -273.15 : 
        return C
    raise ValueError("Temperature cannot be below absolute zero")
    


    # TODO: Implement this function
    pass

