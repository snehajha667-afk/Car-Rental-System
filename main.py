class Car:
    def __init__(self, name, rent):
        self.name = name
        self.rent = rent

    def show(self):
        print("Car Name:", self.name)
        print("Rent Per Day:", self.rent)


car1 = Car("Swift", 1500)
car2 = Car("Creta", 3000)

print("Available Cars:")
car1.show()
print()
car2.show()

car = input("\nEnter car name: ")
days = int(input("Enter number of days: "))

if car.lower() == "swift":
    bill = days * car1.rent
    print("Total Bill =", bill)

elif car.lower() == "creta":
    bill = days * car2.rent
    print("Total Bill =", bill)

else:
    print("Car not available")
