def adder(self, key):
    h = self.hasher(key)  # Calculate the hash
    # print("lisättävä hash", h)
    contains = False  # Set the variable contains to false, this will be used to see if the key already exists in the hash table
    # Loop through the linked list at the given index (from the hash value)
    for index in range(len(self.arr[h])):
        if self.arr[h][index] == key:  # If the key is already found in the linked list
            contains = True  # Set contains to true
            break  # Break out of the loop, do not add anything to the list/hash table
    # If the key is not found in the list/table (contains stays as False)
    if not contains:
        # Append the key to the appropriate linked list
        self.arr[h].append(key)


for index in range(len(self.arr[h])):
            # If the key to be searched matches the current loop element
            if self.arr[h][index] == key:
                # return key  # return key
                spot = ("Key found at list " + str(h+1))
                return spot
        else:
            return "key not found"