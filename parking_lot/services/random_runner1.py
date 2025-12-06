import uuid
import random
import logging

from parking_lot.models.parking_spot import ParkingSpot, SpotType, SpotSize
from parking_lot.models.floor import Floor
from parking_lot.models.parking_lot import ParkingLot, VehicleNotParkedException   
from parking_lot.models.vehicle import Vehicle, VehicleSize
from parking_lot.models.parking_matcher import ParkingMatcher, SizeRule, EVRule, HandicapRule

logger = logging.getLogger(__name__)


def random_runner1():
    # Problem size
    num_floors = 2
    num_spots_per_floor = 10
    num_vehicles = 10

    # Create parking lot
    logger.info("Creating parking lot")
    parking_lot_name = "Mumbai Parking Lot"
    parking_matcher = ParkingMatcher([SizeRule(), EVRule(), HandicapRule()])
    floors = list()
    for i in range(1, num_floors+1):
        floor = Floor(i, parking_matcher)
        floors.append(floor)
    parking_lot = ParkingLot(parking_lot_name, parking_matcher, floors)
    for i in range(1, num_floors+1):
        for j in range(1, num_spots_per_floor+1):
            id = uuid.uuid4()
            random_size = random.choice([SpotSize.SMALL, SpotSize.MEDIUM, SpotSize.LARGE])
            random_type = random.choice([SpotType.REGULAR, SpotType.HANDICAPPED])
            random_charger = random.choice([True, False])
            spot = ParkingSpot(id, random_size, random_type, random_charger)
            floors[i-1].add_spot(spot)
        logger.debug(f"Floor {i} created with spots {floors[i-1]}")
    logger.debug(f"Parking lot created {parking_lot}")

    # Create vehicles
    logger.debug("Creating vehicles")
    vehicles = list()
    for i in range(1, num_vehicles+1):
        id = uuid.uuid4()
        random_name = str(uuid.uuid4())
        random_size = random.choice([VehicleSize.SMALL, VehicleSize.MEDIUM, VehicleSize.LARGE])
        random_ev = random.choice([True, False])
        random_handicap = random.choice([True, False])
        vehicle = Vehicle(id, random_name, random_size, random_ev, random_handicap)
        vehicles.append(vehicle)
    logger.debug(f"Vehicles created {vehicles}")

    # Park vehicles
    logger.debug("Parking vehicles")
    for vehicle in vehicles:
        parking_lot.park_vehicle(vehicle)
    logger.debug("Vehicles parked")

    # Leave vehicles
    logger.debug("Departing vehicles")
    for vehicle in vehicles:
        try:
            parking_lot.leave_parking_spot(vehicle)
        except VehicleNotParkedException:
            logger.debug(f"Vehicle {vehicle.vehicle_name} is not parked in any spot")
            continue
    logger.debug("Vehicles departed")