class Pet:
    def __init__(self,name,age,species):
        self.name = name
        self.age = age
        self.species = species

    def human_years(self):
        if self.species == "dog":
            # Common "dog years" rule: first 2 years = 10.5 each, then 4 per year
            if self.age <= 2:
                return self.age * 10.5
            else:
                return 21 + (self.age - 2) * 4

        elif self.species == "cat":
            # Cats often use: first 2 years = 12.5 each, then 4 per year
            if self.age <= 2:
                return self.age * 12.5
            else:
                return 25 + (self.age - 2) * 4
        elif self.species == "rabbit":
            #Rabbits often use: first year = 20 years, then 6 per year
            if self.age == 1:
                return self.age * 20
            else:
                return 20 + (self.age - 1) * 6
    def average_lifespan(self):
        if self.species == "dog":
            return 13
        elif self.species == "cat":
            return 14
        elif self.species == "rabbit":
            return 9


jock = Pet("Jock", 15, "dog")
pumpkin_head = Pet("Pumpkin Head", 4, "cat")
lola = Pet("Lola", 5, "rabbit")

print ("Jock's age in human years:",jock.human_years())
print("Pumpkin Head's age in human years:",pumpkin_head.human_years())
print("Lola's age in human years:", lola.human_years())
print("Average lifspan for dog:", jock.average_lifespan(), "for cat:", pumpkin_head.average_lifespan(),"for rabbit:", lola.average_lifespan())