import logging

from parking_lot.models.parking_spot import ParkingSpot
from parking_lot.models.vehicle import Vehicle
from parking_lot.models.parking_matcher import ParkingMatcher

logger = logging.getLogger(__name__)


class Floor:
    def __init__(self, floor_number: int, parking_matcher: ParkingMatcher):
        logger.info(f"Creating floor {floor_number}")
        self.floor_number = floor_number
        self.parking_matcher = parking_matcher
        self.spots = []
        logger.info(f"Floor {floor_number} created")

    def __str__(self):
        return f"Floor {self.floor_number} with spots {self.spots}"

    def add_spot(self, spot: ParkingSpot):
        logger.info(f"Adding spot {spot.spot_number} to floor {self.floor_number}")
        self.spots.append(spot)
        logger.info(f"Spot {spot.spot_number} added to floor {self.floor_number}")

    def remove_spot(self, spot: ParkingSpot):
        logger.info(f"Removing spot {spot.spot_number} from floor {self.floor_number}")
        self.spots.remove(spot)
        logger.info(f"Spot {spot.spot_number} removed from floor {self.floor_number}")
    
    def find_available_spot(self, vehicle: Vehicle):
        logger.info(f"Finding available spot for vehicle {vehicle.vehicle_name}")
        for spot in self.spots:
            if not spot.is_available():
                continue
            if self.parking_matcher.can_park(vehicle, spot):
                logger.info(f"Found available spot {spot.spot_number} for vehicle {vehicle.vehicle_name}")
                return spot
        logger.info(f"No available spot found for vehicle {vehicle.vehicle_name}")
        return None
