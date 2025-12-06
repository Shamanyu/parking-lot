from __future__ import annotations
import logging
import uuid
from enum import Enum
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from parking_lot.models.parking_spot import ParkingSpot

logger = logging.getLogger(__name__)


class VehicleSize(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

class Vehicle:
    def __init__(self, vehicle_id: uuid.uuid4(), vehicle_name: str, vehicle_size : VehicleSize, 
    is_ev: bool = False, is_handicap: bool = False):
        logger.info(f"Creating vehicle {vehicle_name} with id {vehicle_id}")
        self.vehicle_id = vehicle_id
        self.vehicle_name = vehicle_name
        self.vehicle_size = vehicle_size
        self.is_ev = is_ev
        self.is_handicap = is_handicap
        self.vehicle_spot = None
        logger.info(f"Vehicle {self.vehicle_name} created with id {self.vehicle_id}")

    def __str__(self):
        return f"Vehicle {self.vehicle_name} with id {self.vehicle_id}"

    def park_vehicle(self, parking_spot: ParkingSpot):
        logger.info(f"Parking vehicle {self.vehicle_name} in spot {parking_spot.spot_number}")
        self.vehicle_spot = parking_spot
        logger.info(f"Vehicle {self.vehicle_name} parked in spot {parking_spot.spot_number}")

    def depart(self):
        logger.info(f"Vehicle {self.vehicle_name} departing from spot {self.vehicle_spot.spot_number}")
        self.vehicle_spot = None
        logger.info(f"Vehicle {self.vehicle_name} departed from spot {self.vehicle_spot.spot_number}")
