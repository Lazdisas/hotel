hotels_list = []
customers_list = []
reservation_list = []
# hotels_list.append([1,"hotel1","City1",7,7])
# hotels_list.append([2,"hotel2","City2",5,5])


def view_all_hotels():
    print
    print "List Of Hotels:"
    print "-"*100
    for hotel in hotels_list:
        print "Hotel N°: {}, Hotel Name: {}, City: {}, Total rooms: {}, Empty rooms: {}".format(hotel[0],hotel[1],hotel[2],hotel[3],hotel[4])
    print "-"*100


def add_hotel(number,hotel_name, city,total_rooms,empty_rooms):
    newHotel = [number,hotel_name, city,total_rooms,empty_rooms]
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

    for hotel in hotels_list:
        if hotel[0] == newHotel[0]:
            print("This numbet hotel exist, chose another number: {}".format(newHotel))
            bool_number = False
        if hotel[1] == newHotel[1] and hotel[2] == newHotel[2]:
            bool_name = False
            print("This Hotel is Existing {} ".format(newHotel))

    if bool_number == bool_name == bool_room ==bool_room_empty == True:
            hotels_list.append(newHotel)
            print("Seccesfuly add hotel {}".format(newHotel))
            print("-------------------------")


def add_customer(customer_name):
    bool_customer = True
    for customer in customers_list:
        if customer_name == customer:
            bool_customer = False
    if bool_customer:
        customers_list.append(customer_name)

def view_all_customer():
    i = 0
    print
    print "All Customer Name:"
    print "-"*100
    while i < len(customers_list):
        print "Customer N:{}, Name is : {}".format(i,customers_list[i])
        i += 1
    print "-"*100






#Pratic
for i in range(10):
    add_hotel(i,"hotel{}".format(i),"City{}".format(i),7,7)
    add_customer("name{}".format(i))



add_hotel(10,"hotel1","City",10,0)
add_hotel(3,"hotel1","City",7,8)
add_hotel(3,"hotel2","City",7,7)
add_hotel(1,"hotel3","City",7,7)
add_hotel(2,"hotel4","City",7,7)
add_hotel(1,"hotel5","City",-7,7)
add_hotel(4,"hotel6","City",7,7)
add_hotel(3,"hotel7","City",7,7)
add_hotel(3,"hotel8","City",7,7)
add_hotel(3,"hotel9","City",7,7)


add_customer("Sami")
add_customer("Hocin")

#print list of hotels
view_all_hotels()
view_all_customer()

#print customer names

def reserve_room (hotel_name):
    i = 0
    while i < len(hotels_list):
        if hotels_list[i][1] == hotel_name:
            if hotels_list[i][4] == 0:
                print "False"
                return False
            else:
                hotels_list[i][4] -=1
                print "True"
                return True
        i+=1



def add_new_reservation(hotel_name, customer_name):
    if reserve_room(hotel_name):
        reservation_list.append([hotel_name,customer_name])
        print "confirmation"
    else:
        print "sorry no rooms available"



def list_hotels_in_city(city_name):
    list_of_hotel_in_city =[]
    i = 0
    while i < len(hotels_list):
        if hotels_list[i][2] == city_name:
            list_of_hotel_in_city.append(hotels_list[i][1])
        i += 1
    print "List of hotel in {} is: {}".format(city_name,list_of_hotel_in_city)


def list_resevrations_for_hotel(hotel_name):
    i = 0
    reservation_name = []
    while i < len(reservation_list):
        if reservation_list[i][0] == hotel_name:
            reservation_name.append(reservation_list[i][1])
        i+=1
    print "This names is reservation in Hotel {}: {}".format(hotel_name,reservation_name)
    # search for hotel_name in reservation list and print customer name




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


# search for city in hotels and print hotel name, total number of rooms if found
list_hotels_in_city("City1")


# print reservation_list
# print hotels_list
list_resevrations_for_hotel("hotel1")
list_resevrations_for_hotel("hotel2")