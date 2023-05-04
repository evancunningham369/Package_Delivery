from datetime import timedelta

import Package
from AddressDistance import min_distance_from, find_distance
from TimeData import get_time, add_time


# class to represent truck object
class Truck:

    def __init__(self):
        self.current_address = None
        self.speed = 18.0
        self.packages = []
        self.truck_capacity = 16
        self.distance_traveled = 0.0


# loads three trucks with packages
def load_packages(truck1, truck2, truck3):
    Package.loadPackageData('PackageFile.csv')
    package_table = Package.hashTable

    truck1_package_ids = [8, 40, 10, 11, 12, 17, 20, 21, 22, 23, 24, 31, 26, 27, 33, 29]
    for package_id in truck1_package_ids:
        package = package_table.search(package_id)
        truck1.packages.append(package)
    truck2_package_ids = [1, 2, 3, 18, 36, 38, 14, 15, 19, 16, 13, 20, 4, 5, 30, 7]
    for package_id in truck2_package_ids:
        package = package_table.search(package_id)
        truck2.packages.append(package)
    truck3_package_ids = [6, 25, 28, 32, 34, 35, 36, 37, 38, 39, 9]
    for package_id in truck3_package_ids:
        package = package_table.search(package_id)
        truck3.packages.append(package)


# delivers each package based on the time given and based on the closest address
def truck_deliver_packages(truck, time_to_stop=timedelta(hours=23)):
    truck.current_address = '4001 South 700 East'
    while len(truck.packages) != 0 and get_time() < time_to_stop:
        minimum_distance_address = min_distance_from(truck.current_address, truck.packages)
        for package in truck.packages:
            package.en_route()
            if package.address == minimum_distance_address:
                distance = find_distance(truck.current_address, minimum_distance_address)
                truck.current_address = minimum_distance_address
                time_to_deliver = float(distance) / float(truck.speed)
                truck.distance_traveled += float(distance)
                add_time(timedelta(hours=time_to_deliver))

                package.delivered(get_time())
                truck.packages.remove(package)