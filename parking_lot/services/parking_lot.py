from parking_lot.models.floor import Floor
from parking_lot.models.vehicle import Vehicle

class ParkingLot:
    def __init__(self, name: str, floors: list[Floor]):
        self.name = name
        self.floors = floors

    def park_vehicle(self, vehicle: Vehicle):
        for floor in self.floors:
            spot = floor.find_available_spot(vehicle.vehicle_size)
            if spot:
                spot.park_vehicle(vehicle)
                return True
        return False        

    def leave_parking_spot(self, vehicle: Vehicle):
        for floor in self.floors:
            for spot in floor.spots:
                if spot.vehicle == vehicle:
                    spot.leave_spot()
                    return True
        return False