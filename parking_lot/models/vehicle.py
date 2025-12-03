from enum import Enum

class VehicleSize(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

class Vehicle:
    def __init__(self, vehicle_name: str, vehicle_size: VehicleSize):
        self.vehicle_name = vehicle_name
        self.vehicle_size = vehicle_size
        self.vehicle_spot = None