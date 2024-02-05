import random


class Car:
    """Car with attributes: brand, color - strings;
    tank volume, fuel consumption,
    and current fuel indicator (randomly generated from zero to full tank);
    mileage field (equal to zero, not specified when creating a class instance)"""

    def __init__(self, *, brand: str, color: str, gasoline_tank_volume: int, fuel_consumption: float):

        self.brand = brand
        self.color = color
        self.trip_distance = 0
        self.fuel_consumption = fuel_consumption
        self.gasoline_tank_volume = gasoline_tank_volume
        self.remaining_fuel = random.randrange(0, gasoline_tank_volume)

    def __str__(self):

        return f'{self.color} {self.brand}'

    def move(self, *, distance: float) -> bool:
        """Changes the value of the field - trip distance by the value of the argument - distance;
        reduces the amount of fuel depending on the distance covered;
        returns True if movement has occurred,
        returns False otherwise (with text notification about lack of fuel).
        When trying to move a greater distance than the remaining fuel allows,
        moves as far as there is enough fuel before the tank is empty"""

        gasoline_need = distance * self.fuel_consumption / 100

        if self.remaining_fuel >= gasoline_need:

            self.remaining_fuel -= distance * self.fuel_consumption / 100

            self.trip_distance += distance

            has_it_moved = True

        elif self.remaining_fuel == 0:

            has_it_moved = False

            print(f"{self} out of fuel!")

        else:

            alt_distance = (self.remaining_fuel / self.fuel_consumption) * 100

            self.remaining_fuel = 0

            self.trip_distance += alt_distance

            has_it_moved = True

        return has_it_moved


my_car = Car(brand="audi",
             color="red",
             gasoline_tank_volume=50,
             fuel_consumption=7)

my_neighbour_car = Car(brand="kia",
                       color="green",
                       gasoline_tank_volume=60,
                       fuel_consumption=9)

my_friend_car = Car(brand="mercedes",
                    color="brown",
                    gasoline_tank_volume=55,
                    fuel_consumption=8)


cars_list = [my_car, my_neighbour_car, my_friend_car]
winner = False
finish = 200

party = cars_list.copy()

while not winner:

    if not party:

        print("No winner")

        break

    for car in party:

        step = random.randrange(0, 50)

        if car.move(distance=step):

            if car.trip_distance >= finish:

                print(f'{car} is winner')

                winner = True

                break

        else:

            party.remove(car)

for car in cars_list:

    print(f"{car} traveled {round(car.trip_distance, 1)} km, "
          f"fuel reserve - {round(car.remaining_fuel, 1)} liters")
