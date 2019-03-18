from classPet import Pet, Dog

mister_pet = Pet("mister", "Dog")
mister_dog = Dog("mister", True)

print("isinstance(mister_pet, Pet) = ", isinstance(mister_pet, Pet))
print("isinstance(mister_pet, Dog) = ", isinstance(mister_pet, Dog))
print("isinstance(mister_dog, Pet) = ", isinstance(mister_dog, Pet))
print("isinstance(mister_dog, Dog) = ", isinstance(mister_dog, Dog))

print(mister_pet)
print(mister_dog)
