# Author: Nathan Calderon
# File Name: pet_Calderon.py

# This program stores an objects attributes entered by a user.
# The objects attributes are then displayed. 

# Class definition
class Pet:
    
    def __int__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age

# Main function
def main():
    # Get pet data.
    name = input("Enter the pet name: ")
    animal = input("Enter the animal type: ")
    age = input("Enter the animal age: ")

    # Create an instance of the Pet class.
    my_pet = pet.Pet(name, animal_type, age)

    # Display the data that was entered.
    print("Here is the data that you entered:")
    print("Name:", my_pet.get_name())
    print("Type:", my_pet.get_animal_type())
    print("Age:", my_pet.get_age())

# Call main function.
main()
    












    
