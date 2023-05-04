import csv

# matrix to hold distance data
distance_matrix = []
# list to hold address data
address_list = []

#fill list with distance data
def load_distance_data():
    with open('Distances.csv') as distances:
        distance_data = csv.reader(distances, delimiter=',')
        for row in distance_data:
            row.pop()
            distance_matrix.append(row)

#fill matrix with address data
def load_address_data():
    with open('Addresses.csv') as addresses:
        filtered = (line.replace('\n', '') for line in addresses)
        address_data = csv.reader(filtered, delimiter=',')
        for row in address_data:
            for address in row:
                if address != '':
                    address_list.append(address)

#calculate and return the distance between two addresses
def find_distance(address1, address2):
    index1 = address_list.index(address1)
    index2 = address_list.index(address2)
    try:
        distance = distance_matrix[index1][index2]
    except IndexError:
        distance = distance_matrix[index2][index1]
    return distance

#find the minimum distance between the current address and all truck packages
def min_distance_from(from_address, truck_packages):
    shortest_address = truck_packages[0].address
    min_distance = find_distance(from_address, truck_packages[0].address)

    for package in truck_packages:
        distance = find_distance(from_address, package.address)
        if float(distance) < float(min_distance):
            min_distance = distance
            shortest_address = package.address
    return shortest_address