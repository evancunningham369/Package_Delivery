import csv
from datetime import timedelta
import HashMap
from Truck import Truck

# hash table reference
hashTable = HashMap.ChainingHashTable()


# class for a package object
class Package:
    def __init__(self, id, address, city, state, zip, deadline, mass, special_notes, delivery_status):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.mass = mass
        self.specialNotes = special_notes
        self.delivery_status = delivery_status

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s" % (
            self.id, self.address, self.city, self.state, self.zip, self.deadline, self.mass, self.specialNotes,
            self.delivery_status)

    def atHub(self):
        self.delivery_status = "At the hub"

    def delivered(self, delivery_time):
        self.delivery_status = f"Delivered at {delivery_time}"

    def en_route(self):
        self.delivery_status = "En route"


# load all package data and insert package into hash table
def loadPackageData(filename):
    with open(filename) as packages:
        packageData = csv.reader(packages, delimiter=',')
        next(packageData)
        for package in packageData:
            id = int(package[0])
            address = package[1]
            city = package[2]
            state = package[3]
            zip = package[4]
            deadline = package[5]
            mass = package[6]
            special_notes = package[7]

            package = Package(id, address, city, state, zip, deadline, mass, special_notes,
                              delivery_status='At the hub')

            hashTable.insert(id, package)


# print all package data in hash table
def print_all_package_data():
    for i in range(0, len(hashTable.table)):
        print(hashTable.search(i + 1))