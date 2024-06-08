#!/usr/bin/python3
"""Module containing pickle module and CustomObject"""


class CustomObject:
    """The CustomObject class"""

    def __init__(self, name: str, age: int, is_student: bool):
        """Initialization of instance"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Function to print attributes"""
        print(f"Name: {self.name}\nAge: {self.age}\nIs Student: {self.is_student}")

    def serialize(self, filename):
        """Method to serialize the Object and write it to the file"""
        import pickle

        try:
            # Writing serialized data to the file
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception as e:
            print("Error occurred:", e)

    @classmethod
    def deserialize(cls, filename):
        """Method to deserialize the Object from file"""
        import pickle

        try:
            # Reading file content for deserialization
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except Exception as e:
            print("Error occurred:", e)
            return None
