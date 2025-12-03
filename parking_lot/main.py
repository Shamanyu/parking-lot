from parking_lot.models.vehicle import Vehicle
from parking_lot.models.parking_spot import ParkingSpot
from parking_lot.models.floor import Floor
from parking_lot.services.parking_lot import ParkingLot
from parking_lot.models.parking_spot import SpotSize
from parking_lot.models.vehicle import VehicleSize

def main():
    floor1_spots = [ParkingSpot(1, SpotSize.SMALL), ParkingSpot(2, SpotSize.MEDIUM), ParkingSpot(3, SpotSize.LARGE)]
    floor2_spots = [ParkingSpot(1, SpotSize.SMALL), ParkingSpot(2, SpotSize.MEDIUM)]
    floor3_spots = [ParkingSpot(1, SpotSize.SMALL)]
    floors = [Floor(1, floor1_spots), Floor(2, floor2_spots), Floor(3, floor3_spots)]
    mumbai_parking_lot = ParkingLot("Mumbai Parking Lot", floors)

    print ("HEY")

    # Successful parking
    polo = Vehicle("Polo", VehicleSize.SMALL)
    print (mumbai_parking_lot.park_vehicle(polo))

    harriet = Vehicle("Harriet", VehicleSize.MEDIUM)
    print (mumbai_parking_lot.park_vehicle(harriet))        

    lorry1 = Vehicle("Lorry", VehicleSize.LARGE)
    print (mumbai_parking_lot.park_vehicle(lorry1))        

    # Unsuccessful parking
    lorry2 = Vehicle("Lorry", VehicleSize.LARGE)
    print (mumbai_parking_lot.park_vehicle(lorry2))        

    # Successful departure
    print (mumbai_parking_lot.leave_parking_spot(polo))

    # Unsuccesful departure
    print (mumbai_parking_lot.leave_parking_spot(lorry2))

    # Unsuccessful parking
    lorry3 = Vehicle("Lorry", VehicleSize.LARGE)
    print (mumbai_parking_lot.park_vehicle(lorry3))

    # Successful departure
    print (mumbai_parking_lot.leave_parking_spot(lorry1))

    # Successful parking
    print (mumbai_parking_lot.park_vehicle(lorry3))

    ## Expected output
    # True
    # True
    # True
    # False
    # True
    # False
    # False
    # True
    # True

if __name__ == "__main__":
    main()