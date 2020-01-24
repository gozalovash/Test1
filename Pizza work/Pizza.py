class Pizza:
    category = "snack"

    def __init__(self, name, size):
        self.name=name
        self.size=size

margarita = Pizza("Margarita","small")
caesar = Pizza("Caesar", "medium")

print("Margarita is a {}".format(margarita.__class__.category))
print("")
