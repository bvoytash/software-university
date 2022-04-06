class Vehicle:
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def __init__(self, fuel, horse_power):
        self.fuel = fuel
        self.horse_power = horse_power
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION

    def drive(self, kilometers):
        fuel_to_drive = self.fuel_consumption * kilometers
        if fuel_to_drive <= self.fuel:
            self.fuel -= fuel_to_drive
