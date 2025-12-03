from parking_lot.models.parking_spot import ParkingSpot
from parking_lot.models.vehicle import VehicleSize

class Floor:
    def __init__(self, floor_number: int, spots: list[ParkingSpot]):
        self.floor_number = floor_number
        self.spots = spots

    def find_available_spot(self, vehicle_size: VehicleSize):
        for spot in self.spots:
            if spot.can_fit_vehicle(vehicle_size):
                return spot
        return None
