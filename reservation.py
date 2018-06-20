from hotel import Hotel
from customer import Customer
from notification import Notification
class Reservation:
    reservation_list = []
    def __init__(self,hotel_name,customer_name):
        self.hotel_name = hotel_name
        self.customer_name = customer_name
        self.reservation_list.append([self.hotel_name,self.customer_name])


    def reserve_room(self,hotel_name):
        print("---reservation room---")
        print(hotel_name)
        i = 0
        while i < len(Hotel.hotels):
            if Hotel.hotels[i][1] == hotel_name:
                if Hotel.hotels[i][4] == 0:
                    print "False"
                    return False
                else:
                    Hotel.hotels[i][4] -=1
                print "True"
            return True
        i+=1
        print("---end reservation room---")



    def add_new_reservation(self,hotel_name,customer_name):
        print("---add new reservation---")
        if self.reserve_room(hotel_name):
            self.reservation_list.append([hotel_name,customer_name])
            for customer in Customer.customers_list:
                if customer_name == customer[0]:
                    print(customer_name)
                    Notification("message",customer[1]).send_text_message()
            print "confirmation"
        else:
            print "sorry no rooms available"
        print("---end add new reservation---")





    def list_resevrations_for_hotel(self,hotel_name):
        print("---list of reservation hotel with name---")
        i = 0
        reservation_name = []
        while i < len(self.reservation_list):
            if self.reservation_list[i][0] == hotel_name:
                reservation_name.append(self.reservation_list[i][1])
            i+=1
        print "This names is reservation in Hotel {}: {}".format(hotel_name,reservation_name)
        print("---end list of reservation hotel with name---")


    # add_new_reservation("hotel1","Sami")
    # add_new_reservation("hotel1","Sami")
    # add_new_reservation("hotel1","Sami")
    # add_new_reservation("hotel1","Sami")
    # add_new_reservation("hotel1","Sami")
    # add_new_reservation("hotel1","Sami")
    # add_new_reservation("hotel1","Sami")
    # add_new_reservation("hotel1","Sami")
    # add_new_reservation("hotel1","Sami")
    # add_new_reservation("hotel1","Sami")
    # add_new_reservation("hotel1","Sami")
    # add_new_reservation("hotel2","Ahmed")
    # add_new_reservation("hotel2","Ahmed")
    # add_new_reservation("hotel2","Ahmed")
    # add_new_reservation("hotel2","Ahmed")
    # add_new_reservation("hotel2","Ahmed")
    # add_new_reservation("hotel2","Ahmed")
    # add_new_reservation("hotel2","Ahmed")
    # add_new_reservation("hotel2","Ahmed")
    #
    #
    # list_resevrations_for_hotel("hotel1")
    # list_resevrations_for_hotel("hotel2")
