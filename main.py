import hotel
import customer
import reservation
import tester
import notification

def start_app():
    rotana_hotel = hotel([20,"Rotana","Abu Dhabi",200,40])
    sheraton_hotel = hotel(21,"Sheraton","Abu Dhabi",300,100)

    print hotel.hotels

start_app()