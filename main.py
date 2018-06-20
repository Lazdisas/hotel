# coding: utf8
# import sys
# print sys.getdefaultencoding()
# reload(sys)  # Reload does the trick!
# sys.setdefaultencoding('UTF8')
# print sys.getdefaultencoding()
from hotel import Hotel
from customer import Customer
from reservation import Reservation
from notification import Notification

def start_app():

    rotana_hotel =  Hotel(20,"Rotana","Abu Dhabi",200,40)
    sheraton_hotel = Hotel(21,"Sheraton","Abu Dhabi",300,100)

    print Hotel.hotels

    customer = Customer("name","0000000000")
    customer.add_customer("name2","phone2")
    print "Customer List : {}".format(customer.customers_list)

    reservation = Reservation(Hotel.hotels[0][1],Customer.customers_list[0][0])
    reservation.add_new_reservation(Hotel.hotels[0][1],Customer.customers_list[0][0])
    print "Reservation List: {}".format(reservation.reservation_list)

    reservation.list_resevrations_for_hotel(Hotel.hotels[0][1])

start_app()