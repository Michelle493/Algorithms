import time
import json


# Step 1: Load sample drivers
# (drivers.json was provided by ai for this activity)


def generate_drivers():
    with open("drivers.json", "r") as f:
        drivers = json.load(f)
    return drivers



# Step 2: O(N) - Linear search


def linear_search(drivers, target_id):
    for driver in drivers:
        if driver["id"] == target_id:
            return driver
    return None



# Step 3: O(log N) - Binary search
# (list must be sorted first)


# a function used to tell sort what to sort by
def get_id(driver):
    return driver["id"]

def sort_drivers(drivers):
    return sorted(drivers, key=get_id)

def binary_search(sorted_drivers, target_id):
    low = 0
    high = len(sorted_drivers) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_id = sorted_drivers[mid]["id"]

        if mid_id == target_id:
            return sorted_drivers[mid]
        elif mid_id < target_id:
            low = mid + 1
        else:
            high = mid - 1

    return None



# Step 4: O(1) - Hash map lookup


def build_hash_map(drivers):
    driver_map = {}
    for driver in drivers:
        driver_map[driver["id"]] = driver
    return driver_map


def hash_map_search(driver_map, target_id):
    if target_id in driver_map:
        return driver_map[target_id]
    else:
        return None



# Step 5: Test all three and compare time


drivers = generate_drivers()

# only search among drivers who are available
available_drivers = [d for d in drivers if d["available"]]

# sort a copy for binary search
sorted_drivers = sort_drivers(available_drivers)

# build the hash map
driver_map = build_hash_map(available_drivers)

# pick a driver to search for
target = "KGL-02227"

# a single search is too fast to measure, so repeat it many times
repeats = 1000

# time linear search
start = time.time()
for i in range(repeats):
    result1 = linear_search(available_drivers, target)
end = time.time()
print("Linear search time:", end - start)

# time binary search
start = time.time()
for i in range(repeats):
    result2 = binary_search(sorted_drivers, target)
end = time.time()
print("Binary search time:", end - start)

# time hash map search
start = time.time()
for i in range(repeats):
    result3 = hash_map_search(driver_map, target)
end = time.time()
print("Hash map search time:", end - start)



# Step 6: Search by name, then confirm by id
# (names are not unique, so we need the id to pick
# the exact driver once we find matching names)


# Approach 1: check every driver one by one - O(N)
def find_by_name_linear(drivers, name, target_id):
    for driver in drivers:
        if driver["name"] == name and driver["id"] == target_id:
            return driver
    return None


# Approach 2: sort by name first, then binary search for the
# name, then check nearby drivers with the same name for the
# matching id - O(log N) to find the name, plus a small check
# for duplicates

def get_name(driver):
    return driver["name"]

def sort_by_name(drivers):
    return sorted(drivers, key=get_name)

def find_by_name_binary(sorted_drivers, name, target_id):
    low = 0
    high = len(sorted_drivers) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_name = sorted_drivers[mid]["name"]

        if mid_name == name:
            
            i = mid
            while i >= 0 and sorted_drivers[i]["name"] == name:
                if sorted_drivers[i]["id"] == target_id:
                    return sorted_drivers[i]
                i = i - 1

            i = mid + 1
            while i < len(sorted_drivers) and sorted_drivers[i]["name"] == name:
                if sorted_drivers[i]["id"] == target_id:
                    return sorted_drivers[i]
                i = i + 1

            return None
        elif mid_name < name:
            low = mid + 1
        else:
            high = mid - 1
            
    return None


# Approach 3: hash map keyed by name, where each value is a
# list of drivers who share that name - O(1) to find the list then a short check through that small list for the id

def build_name_map(drivers):
    name_map = {}
    for driver in drivers:
        name = driver["name"]
        if name in name_map:
            name_map[name].append(driver)
        else:
            name_map[name] = [driver]
    return name_map

def find_by_name_hash(name_map, name, target_id):
    if name in name_map:
        matches = name_map[name]
        for driver in matches:
            if driver["id"] == target_id:
                return driver
    return None


# test all three with a name that has duplicates
name_target = "Aline Niyonzima"
id_target = "KGL-09442"

sorted_by_name = sort_by_name(available_drivers)
name_map = build_name_map(available_drivers)

start = time.time()
for i in range(repeats):
    result4 = find_by_name_linear(available_drivers, name_target, id_target)
end = time.time()
print("Name+id linear search time:", end - start)

start = time.time()
for i in range(repeats):
    result5 = find_by_name_binary(sorted_by_name, name_target, id_target)
end = time.time()
print("Name+id binary search time:", end - start)

start = time.time()
for i in range(repeats):
    result6 = find_by_name_hash(name_map, name_target, id_target)
end = time.time()
print("Name+id hash map search time:", end - start)


