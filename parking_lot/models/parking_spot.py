from __future__ import annotations
import logging
import uuid
from enum import Enum
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from parking_lot.models.vehicle import Vehicle

logger = logging.getLogger(__name__)


class SpotSize(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

class SpotType(Enum):
    REGULAR = 1
    HANDICAPPED = 2

class ParkingSpot:
    def __init__(self, spot_number: uuid.uuid4(), spot_size: SpotSize, spot_type: SpotType = SpotType.REGULAR, 
    has_charger: bool = False):
        logger.info(f"Creating spot {spot_number}")
        self.spot_number = spot_number
        self.spot_size = spot_size
        self.spot_type = spot_type
        self.has_charger = has_charger
        self.vehicle = None
        logger.info(f"Spot {spot_number} created")

    def __str__(self):
        return f"Spot {self.spot_number} with size {self.spot_size} and type {self.spot_type}"

    def is_available(self):
        logger.info(f"Checking availability of spot {self.spot_number}")
        return self.vehicle is None

    def park_vehicle(self, vehicle: Vehicle):
        logger.info(f"Spot {self.spot_number} parking vehicle {vehicle.vehicle_name}")
        self.vehicle = vehicle
        logger.info(f"Vehicle {vehicle.vehicle_name} parked in spot {self.spot_number}")

    def leave_spot(self):
        logger.info(f"Spot {self.spot_number} vacated by vehicle {self.vehicle.vehicle_name}")
        self.vehicle = None
        logger.info(f"Spot {self.spot_number} vacated by vehicle {self.vehicle.vehicle_name}")