from enum import Enum

class SpotSize(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

class ParkingSpot:
    def __init__(self, spot_number: int, spot_size: SpotSize):
        self.spot_number = spot_number
        self.spot_size = spot_size
        self.vehicle = None

    def can_fit_vehicle(self, vehicle_type: VehicleType):
        if vehicle_type == VehicleType.SMALL:
            return self.spot_size == SpotSize.SMALL or self.spot_size == SpotSize.MEDIUM or self.spot_size == SpotSize.LARGE
        elif vehicle_type == VehicleType.MEDIUM:
            return self.spot_size == SpotSize.MEDIUM or self.spot_size == SpotSize.LARGE
        elif vehicle_type == VehicleType.LARGE:
            return self.spot_size == SpotSize.LARGE
        return False

    def park_vehicle(self, vehicle: Vehicle):
        if self.can_fit_vehicle(vehicle.vehicle_type):
            self.vehicle = vehicle
            return True
        return False

    def leave_spot(self):
        self.vehicle = None