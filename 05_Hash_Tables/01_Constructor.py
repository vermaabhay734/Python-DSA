class HashTable:
    # HashTable Constructor
    def __init__(self, size = 7):
        self.data_map = [None] * size


    def __hash(self, key):
        my_hash = 0
        for letter in key:
            # ord(letter) -> Ordinal, it gets ascii numerical value
            # we use 23 because it is prime number, you can use any.
            # % len -> if we devide by its len then remainder is going to anywhere from 0 to 6
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    # Used to print HashTable
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, " : ", val )


my_hash_table = HashTable()
my_hash_table.print_table()