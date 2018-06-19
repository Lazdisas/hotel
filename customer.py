from random import randint
class Customer:
    customers_list = []
    def __init__(self,name,phone):
        self.name = name
        self.phone = phone
        self.customers_list.append(self,[name,phone])


def add_customer(self,customer_name, phone):
    new_customer = [customer_name,phone]
    bool_customer = True
    for customer in self.customers_list:
        if new_customer == customer:
            bool_customer = False
    if bool_customer:
        self.customers_list.append(new_customer)

def view_all_customer(self):
    i = 0
    print
    print "All Customer Name:"
    print "-"*100
    while i < len(self.customers_list):
        print "Customer N:{}, Name is : {} Phone Number : {}".format(i,self.customers_list[i][0],self.customers_list[i][1])
        i += 1
    print "-"*100

for i in range(10):
    add_customer("name{}".format(i),"+000{}".format(randint(000000000,999999999)))

add_customer("Sami","+213557098309")
add_customer("Hocin","+213672899204")

view_all_customer()
