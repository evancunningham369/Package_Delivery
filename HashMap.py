# class representing a chaining hash table
# Citing source: WGU code repository W-2_ChainingHashTable_zyBooks_Key-Value_CSV_Greedy.py
# from Ref C950 WGUPS Project - Implementation Steps
class ChainingHashTable:
    # Constructor with optional initial capacity parameter.
    # Assigns all buckets with an empty list.
    def __init__(self, initial_capacity=40):
        # initialize the hash table with empty bucket list entries.
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # inserts or updates the package into the list
    def insert(self, id, item):
        bucket = hash(id) % len(self.table)
        bucket_list = self.table[bucket]

        # update key if it is already in the bucket
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == id:
                kv[1] = item
                return True

        # if not updating, insert the item to the end of the bucket list.
        key_value = [id, item]
        bucket_list.append(key_value)
        return True

    # finds the package based on the key
    def search(self, id):
        bucket = hash(id) % len(self.table)
        bucket_list = self.table[bucket]
        # print(bucket_list)

        # search for the key in the bucket list
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == id:
                return kv[1]  # value
        return None