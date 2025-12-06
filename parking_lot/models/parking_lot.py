import logging

from parking_lot.models.floor import Floor
from parking_lot.models.vehicle import Vehicle
from parking_lot.models.parking_matcher import ParkingMatcher

logger = logging.getLogger(__name__)

class VehicleNotParkedException(Exception):
    """Exception raised when a vehicle is not parked in any spot"""
    pass


class ParkingLot:
    def __init__(self, name: str, parking_matcher: ParkingMatcher, floors: list[Floor]):
        logger.info(f"Creating parking lot {name}")
        self.name = name
        self.parking_matcher = parking_matcher
        self.floors = floors
        logger.info(f"Parking lot {name} created")

    def __str__(self):
        return f"Parking lot {self.name} with floors {self.floors}"

    def park_vehicle(self, vehicle: Vehicle):
        logger.info(f"Parking vehicle {vehicle.vehicle_name}")
        for floor in self.floors:
            spot = floor.find_available_spot(vehicle)
            if spot:
                spot.park_vehicle(vehicle)
                logger.info(f"Vehicle {vehicle.vehicle_name} parked in spot {spot.spot_number}")
                return True
        logger.info(f"Vehicle {vehicle.vehicle_name} could not be parked")
        return False        

    def leave_parking_spot(self, vehicle: Vehicle):
        logger.info(f"Leaving parking spot for vehicle {vehicle.vehicle_name}")
        try:
            vehicle.vehicle_spot.leave_spot()
        except AttributeError:
            raise VehicleNotParkedException(f"Vehicle {vehicle.vehicle_name} is not parked in any spot")
        vehicle.depart()
        logger.info(f"Vehicle {vehicle.vehicle_name} left parking spot")