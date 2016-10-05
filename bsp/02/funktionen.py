pets = ["Hamster", "Cat", "Dog", "Canary"]

def not_a_dog_person(animal):
  return animal.replace("Dog", "Fish")

for pet in pets:
  print("Tom: {:10} Tim: {}".format(pet, not_a_dog_person(pet)))

