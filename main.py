# Evan Cunningham - Student ID: 002293033

from Package import print_all_package_data
from AddressDistance import *
from Truck import *
from TimeData import *

#load all address data
load_address_data()
#load all distance data
load_distance_data()

#Create truck objects, load the trucks with packages and give
#appropriate response to input selections
while True:
    truck1 = Truck()
    truck2 = Truck()
    truck3 = Truck()
    load_packages(truck1, truck2, truck3)

    response = int(input(
        '''
1 - Check package info after time
2 - total mileage traveled for all trucks
3 - exit\n'''))
    if response == 1:
        time = input('Enter time(in military time, ie 08:00): ')
        hours, minutes = time.split(':')
        military_time = timedelta(hours=float(hours), minutes=float(minutes))

        truck_deliver_packages(truck1, military_time)
        truck_deliver_packages(truck2, military_time)
        truck_deliver_packages(truck3, military_time)

        print_all_package_data()
        reset_time()
    if response == 2:
        total_mileage = 0.0
        truck_deliver_packages(truck1)
        truck_deliver_packages(truck2)
        truck_deliver_packages(truck3)
        total_mileage += truck1.distance_traveled + truck2.distance_traveled + truck3.distance_traveled
        print(f'Total Mileage by all trucks: {round(total_mileage)} miles\n')
        reset_time()
    if response == 3:
        break