# python_code/person.py

"""Provide a class to represent a person.

This module allows the user to create a person.

Examples:
    Creating a person object and printing their information.
    >>> from python_code import person
    >>> person = Person("John", "Doe", 30)
    >>> person.info()
    My name is John Doe. I am 30 years old.

    Providing additional information to the info() method.

    >>> person = Person("John", "Doe", 30)
    >>> person.info(" I like to play guitar.")
    My name is John Doe. I am 30 years old. I like to play guitar.
"""

class Person:
    """
    A class to represent a person.

    Attributes:
        name (str): First name of the person.
        surname (str): Family name of the person.
        age (int): Age of the person.

    Methods:
        __init__(name, surname, age):
            Constructs all the necessary attributes for the person object.

        info(additional=""):
            Prints the person's name and age.
    """

    def __init__(self, name, surname, age):
        """
        Constructs all the necessary attributes for the person object.

        Args:
            name (str): First name of the person.
            surname (str): Family name of the person.
            age (int): Age of the person.
        """

        self.name = name
        self.surname = surname
        self.age = age

    def info(self, additional=""):
        """
        Prints the person's name and age.

        If the argument 'additional' is passed, then it is appended after the main info.

        Args:
            additional (str, optional): More info to be displayed (default is None).

        """

        
        print(f'My name is {self.name} {self.surname}. I am {self.age} years old.' + additional)
        