import hotel
from customer import Customer
from notification import Notification
class Reservation():

    reservation_list = []

    def reserve_room (hotel_name):
        i = 0
        while i < len(hotel.hotels_list):
            if hotel.hotels_list[i][1] == hotel_name:
                if hotel.hotels_list[i][4] == 0:
                    print "False"
                    return False
                else:
                    hotels_list[i][4] -=1
                print "True"
            return True
            i+=1



    def add_new_reservation(hotel_name, customer_name):
        if Reservation.reserve_room(hotel_name):
            Reservation.reservation_list.append([hotel_name,customer_name])
            for customer in Customer.customers_list:
                if customer_name == customer[0]:
                    print(customer_name)
                    Notification("message",customer[1]).send_text_message()
            print "confirmation"
        else:
            print "sorry no rooms available"





    def list_resevrations_for_hotel(hotel_name):
        i = 0
        reservation_name = []
        while i < len(Reservation.reservation_list):
            if Reservation.reservation_list[i][0] == hotel_name:
                reservation_name.append(Reservation.reservation_list[i][1])
            i+=1
        print "This names is reservation in Hotel {}: {}".format(hotel_name,reservation_name)


    add_new_reservation("hotel1","Sami")
    add_new_reservation("hotel1","Sami")
    add_new_reservation("hotel1","Sami")
    add_new_reservation("hotel1","Sami")
    add_new_reservation("hotel1","Sami")
    add_new_reservation("hotel1","Sami")
    add_new_reservation("hotel1","Sami")
    add_new_reservation("hotel1","Sami")
    add_new_reservation("hotel1","Sami")
    add_new_reservation("hotel1","Sami")
    add_new_reservation("hotel1","Sami")
    add_new_reservation("hotel2","Ahmed")
    add_new_reservation("hotel2","Ahmed")
    add_new_reservation("hotel2","Ahmed")
    add_new_reservation("hotel2","Ahmed")
    add_new_reservation("hotel2","Ahmed")
    add_new_reservation("hotel2","Ahmed")
    add_new_reservation("hotel2","Ahmed")
    add_new_reservation("hotel2","Ahmed")


    list_resevrations_for_hotel("hotel1")
    list_resevrations_for_hotel("hotel2")
