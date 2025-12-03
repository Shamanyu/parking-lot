from enum import Enum
from parking_lot.models.vehicle import VehicleSize
from parking_lot.models.vehicle import Vehicle

class SpotSize(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

class ParkingSpot:
    def __init__(self, spot_number: int, spot_size: SpotSize):
        self.spot_number = spot_number
        self.spot_size = spot_size
        self.vehicle = None

    def can_fit_vehicle(self, vehicle_type: VehicleSize):
        if not self.available():
            return False
        if vehicle_type == VehicleSize.SMALL:
            return self.spot_size == SpotSize.SMALL or self.spot_size == SpotSize.MEDIUM or self.spot_size == SpotSize.LARGE
        elif vehicle_type == VehicleSize.MEDIUM:
            return self.spot_size == SpotSize.MEDIUM or self.spot_size == SpotSize.LARGE
        elif vehicle_type == VehicleSize.LARGE:
            return self.spot_size == SpotSize.LARGE
        return False

    def available(self):
        return self.vehicle is None

    def park_vehicle(self, vehicle: Vehicle):
        if self.can_fit_vehicle(vehicle.vehicle_size):
            self.vehicle = vehicle
            return True
        return False

    def leave_spot(self):
        self.vehicle = None