# coding: utf8
# import sys
# print sys.getdefaultencoding()
# reload(sys)  # Reload does the trick!
# sys.setdefaultencoding('UTF8')
# print sys.getdefaultencoding()
# from typing import List, Any


class Hotel:
    def __int__(self, number, hotel_name, city, total_rooms, empty_rooms):
        print("hotel")
        self.number = number
        self.hotel_name = hotel_name
        self.city = city
        self.total_rooms = total_rooms
        self.empty_rooms = empty_rooms

        Hotel.hotels.append([self.number,self.hotel_name,self.city,self.total_rooms,self.empty_rooms])
    hotels = []
    def add_hotel(self):
        newHotel = [self.number,self.hotel_name, self.city,self.total_rooms,self.empty_rooms]
        bool_number = True
        bool_name = True
        bool_room = True
        bool_room_empty = True
        print(newHotel)

        if newHotel[3]<=0 or newHotel[4]<0:
            bool_number = False
            print "Please check the number of rooms"

        if newHotel[3] < newHotel[4]:
            bool_room_empty = True
            print "Inaccurate data: The number of empty rooms is greater than the number of rooms available"

        for hotel in Hotel.hotels:
            if hotel[0] == newHotel[0]:
                print("This numbet hotel exist, chose another number: {}".format(newHotel))
                bool_number = False
            if hotel[1] == newHotel[1] and hotel[2] == newHotel[2]:
                bool_name = False
                print("This Hotel is Existing {} ".format(newHotel))

        if bool_number == bool_name == bool_room ==bool_room_empty == True:
            Hotel.hotels.append(newHotel)
            print("Seccesfuly add hotel {}".format(newHotel))
            print("-------------------------")


    def view_all_hotels(self):
        print
        print "List Of Hotels:"
        print "-"*100
        for hotel in Hotel.hotels:
            print "Hotel N°: {}, Hotel Name: {}, City: {}, Total rooms: {}, Empty rooms: {}".format(hotel[0],hotel[1],hotel[2],hotel[3],hotel[4])
        print "-"*100

    # for i in range(10):
    #     add_hotel(i,"hotel{}".format(i),"City{}".format(i),7,7)

    def list_hotels_in_city(self,city_name):
        list_of_hotel_in_city =[]
        i = 0
        while i < len(Hotel.hotels):
            if Hotel.hotels[i][2] == city_name:
                list_of_hotel_in_city.append(Hotel.hotels[i][1])
            i += 1
        print "List of hotel in {} is: {}".format(city_name,list_of_hotel_in_city)

    # add_hotel(10,"hotel1","City",10,0)
    # add_hotel(3,"hotel1","City",7,8)
    # add_hotel(3,"hotel2","City",7,7)
    # add_hotel(1,"hotel3","City",7,7)
    # add_hotel(2,"hotel4","City",7,7)
    # add_hotel(1,"hotel5","City",-7,7)
    # add_hotel(4,"hotel6","City",7,7)
    # add_hotel(3,"hotel7","City",7,7)
    # add_hotel(3,"hotel8","City",7,7)
    # add_hotel(3,"hotel9","City",7,7)



    #print list of hotels
    # view_all_hotels()
    # list_hotels_in_city("City1")
