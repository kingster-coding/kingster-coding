class Friends:
    numbers_of_friends = 2

    def __init__(self, name, food, place):
        self.name = name
        self.food = food
        self.place = place

    def print_information(self):
        return f"Here is the information: {self.name}.{self.food}.{self.place}"

a = Friends("mayank", "samosa", "ghar")
b = Friends("ansh", "aloo banda", "bahar")

print(a.numbers_of_friends)  # Corrected the method call
