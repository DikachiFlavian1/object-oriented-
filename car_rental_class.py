class Vehicle:
    def __init__(self,registration_number,make,model,year,mileage,rented):
        self.registration_number = registration_number
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage 
        self.rented = False
    
    def is_available(self):
        return not self.rented
    
    def rent(self):
        if not self.rented :
            self.rented = True
            return True
        else:
            return False

    def return_vehicle(self):
        if self.rented:
            self.rented = False
            return True
        else:
            return False
        
class Car(Vehicle):
    def __init__(self,registration_number,make, model,  year,mileage, num_doors, num_passengers, fuel_type):
          super().__init__(registration_number,make, model, year, mileage)
          self.num_doors = num_doors
          self.num_passengers = num_passengers
          self.fuel_type = fuel_type

    def calculate_rental_fee(self, rental_duration, additional_features=None):
        base_fee = 50  # Base fee for renting a car
        # You can add logic here to calculate fees based on duration and additional features
        # For example, additional_features can be a list of features like GPS, child seat, etc.
        # You can add fees for each selected feature.
        total_fee = base_fee * rental_duration
        return total_fee      

class Truck(Vehicle):
    def __init__(self, registration_number, make, model, year, mileage, cargo_capacity, truck_type):
        super().__init__(registration_number, make, model, year, mileage)
        self.cargo_capacity = cargo_capacity
        self.truck_type = truck_type

    def calculate_rental_fee(self, rental_duration, cargo_type):
        base_fee = 100  # Base fee for renting a truck
        # You can add logic here to calculate fees based on duration and cargo type
        # For example, you can charge differently for different cargo types.
        total_fee = base_fee * rental_duration
        return total_fee

class RentalManager:
    def __init__(self):
        self.vehicles = {}  # Use a dictionary to store vehicles with registration numbers as keys

    def add_vehicle(self, vehicle):
        self.vehicles[vehicle.registration_number] = vehicle

    def remove_vehicle(self, registration_number):
        if registration_number in self.vehicles:
            del self.vehicles[registration_number]

    def rent_vehicle(self, registration_number, rental_duration, additional_features=None):
        if registration_number in self.vehicles:
            vehicle = self.vehicles[registration_number]
            if vehicle.is_available():
                vehicle.rent()
                return vehicle.calculate_rental_fee(rental_duration, additional_features)
            else:
                return "Vehicle is already rented."
        else:
            return "Vehicle not found."

    def return_vehicle(self, registration_number):
        if registration_number in self.vehicles:
            vehicle = self.vehicles[registration_number]
            if not vehicle.is_available():
                vehicle.return_vehicle()
                return "Vehicle returned. Rental fee: ${:.2f}".format(vehicle.calculate_rental_fee(rental_duration, additional_features))
            else:
                return "Vehicle is not rented."
        else:
            return "Vehicle not found."

    def list_available_vehicles(self):
        available_vehicles = [vehicle for vehicle in self.vehicles.values() if vehicle.is_available()]
        return available_vehicles

    def list_rented_vehicles(self):
        rented_vehicles = [vehicle for vehicle in self.vehicles.values() if not vehicle.is_available()]
        return rented_vehicles

    def calculate_total_revenue(self):
        total_revenue = sum(vehicle.calculate_rental_fee() for vehicle in self.vehicles.values() if not vehicle.is_available())
        return total_revenue

# Usage example:
if __name__ == "__main__":
    manager = RentalManager()

    car1 = Car("CAR001", "Toyota", "Camry", 2022, 15000, 4, 5, "Gasoline")
    car2 = Car("CAR002", "Honda", "Civic", 2021, 12000, 4, 5, "Gasoline")
    truck1 = Truck("TRUCK001", "Ford", "F-150", 2020, 25000, "1500 lbs", "Pickup")

    manager.add_vehicle(car1)
    manager.add_vehicle(car2)
    manager.add_vehicle(truck1)

    print(manager.list_available_vehicles())
    print(manager.rent_vehicle("CAR001", 7))
    print(manager.rent_vehicle("CAR001", 3, additional_features=["GPS"]))
    print(manager.list_rented_vehicles())
    print(manager.return_vehicle("CAR001"))
    print(manager.calculate_total_revenue())    