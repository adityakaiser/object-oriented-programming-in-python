class Dog:
    species = "Canine"

    def __init__(self, breed, age):
        self.breed = breed
        self.age = age

dog1 = Dog("German Shepherd", 4)
dog2 = Dog("Golden Retriever", 2)
print("Dog 1 - Breed:", dog1.breed, ", Age:", dog1.age, ", Species:", dog1.species)
print("Dog 2 - Breed:", dog2.breed, ", Age:", dog2.age, ", Species:", dog2.species)