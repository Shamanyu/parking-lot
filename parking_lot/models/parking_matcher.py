import logging
from abc import ABC, abstractmethod

from parking_lot.models.vehicle import Vehicle
from parking_lot.models.parking_spot import ParkingSpot, SpotSize, SpotType

logger = logging.getLogger(__name__)


class ParkingRule(ABC):
    @abstractmethod
    def allows(self, vehicle: Vehicle, spot: ParkingSpot):
        pass

class SizeRule(ParkingRule):
    def allows(self, vehicle: Vehicle, spot: ParkingSpot):
        return spot.spot_size.value >= vehicle.vehicle_size.value

class EVRule(ParkingRule):
    def allows(self, vehicle: Vehicle, spot: ParkingSpot):
        return not vehicle.is_ev or spot.has_charger

class HandicapRule(ParkingRule):
    def allows(self, vehicle: Vehicle, spot: ParkingSpot):
        return not vehicle.is_handicap or spot.spot_type == SpotType.HANDICAPPED

class ParkingMatcher:
    def __init__(self, rules: list[ParkingRule]):
        self.rules = rules

    def __str__(self):
        return f"Parking matcher with rules {self.rules}"

    def can_park(self, vehicle: Vehicle, spot: ParkingSpot):    
        logger.info(f"Checking if vehicle {vehicle.vehicle_name} can park in spot {spot.spot_number}")
        for rule in self.rules:
            if not rule.allows(vehicle, spot):
                logger.info(f"Vehicle {vehicle.vehicle_name} cannot park in spot {spot.spot_number}")
                return False
        logger.info(f"Vehicle {vehicle.vehicle_name} can park in spot {spot.spot_number}")
        return True
        