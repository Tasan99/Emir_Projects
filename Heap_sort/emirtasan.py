import sys
import time


class Vehicle:
    def __init__(self, vehicle_id, location, distance, speed):
        # Initialize vehicle attributes
        self.vehicle_id = vehicle_id
        self.location = location
        self.distance = float(distance)
        self.speed = int(speed)
        self.estimated_time = self.calculate_estimated_time()

    def calculate_estimated_time(self):
        # Calculate estimated time for the vehicle
        return self.distance / self.speed

def read_file_vehicles():
    # Read vehicle data from 'vehicles.txt' file and return a dictionary
    file = 'vehicles.txt'
    vehicles = {}
    with open(file, 'r') as file:
        file.readline()  # Skip header
        for line in file:
            # Parse and create Vehicle objects
            vehicle_id, location, distance, speed = line.strip().split()
            vehicle = Vehicle(vehicle_id, location, distance, speed)
            vehicles[vehicle_id] = vehicle
    return vehicles

def heapify(arr, n, i):
    # Heapify the subtree rooted at index i
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Find the smallest element among the root, left child, and right child
    if left < n and arr[left].estimated_time < arr[smallest].estimated_time:
        smallest = left

    if right < n and arr[right].estimated_time < arr[smallest].estimated_time:
        smallest = right

    # Swap if needed and recursively heapify the affected sub-tree
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify(arr, n, smallest)

def build_heap(arr):
    # Build a min-heap from the given array
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

def print_sorted_array(arr):
    # Print the array sorted based on estimated time
    print("Sorted Order")
    for index, vehicle_data in enumerate(arr, start=0):
        print(f"{index}. Vehicle ID: {vehicle_data.vehicle_id}, Estimated Time: {vehicle_data.estimated_time:.2f} hours")

def simulate_operations(vehicles_list, total_operations):
    # Simulate extract operations on the min-heap
    operations_count = 0
    call_history = []

    while operations_count < total_operations and vehicles_list:
        # Simulate extract operation
        root = vehicles_list[0]
        call_history.append(root.vehicle_id)
        operations_count += 1

        # Replace the root with the last element and heapify the reduced heap
        vehicles_list[0], vehicles_list[-1] = vehicles_list[-1], vehicles_list[0]
        vehicles_list.pop()
        heapify(vehicles_list, len(vehicles_list), 0)

    return call_history

def main():
    vehicles_dict = read_file_vehicles()

    # Convert values of the dictionary to a list
    vehicles_list = list(vehicles_dict.values())

    # Build a min-heap based on estimated time
    build_heap(vehicles_list)

    # Print the sorted array
    print_sorted_array(vehicles_list)

    total_operations = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    start_time = time.time()

    call_history = simulate_operations(vehicles_list, total_operations)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed Time: {elapsed_time:.2f} seconds for {total_operations} operations.")

    # Write call history to file
    with open('call_history.txt', 'w') as history_file:
        for vehicle_id in call_history:
            history_file.write(f"{vehicle_id}\n")

if __name__ == "__main__":
    main()


"""
#The other way I tried to do it but coulnd't
#class Vehicle:
    #Making a class of vehicles to give their attributes
    #def __init__(self, vehicle_id, location, distance, speed):
        #self.vehicle_id = vehicle_id
        #self.location = location
        #self.distance = float(distance)
        #self.speed = int(speed)
        #Calculating their estimated time calling calculate_estimates time function
        #self.estimated_time = self.calculate_estimated_time()
    #Calculate the estimated time for each vehicle
    #def calculate_estimated_time(self):
        #return self.distance / self.speed

#class Heap:
    #Making an heap class to store the datas
    #def __init__(self):
        #self.heap = []
    #Adding a vehicle to heap by using this func
    #def push(self, vehicle):
        #self.heap.append(vehicle)
        #Calling heap_upwards to modify the heap
        #self._heap_upwards()

    #def pop(self):
        #Removing item from heap and return the min estimeted time vehicle id
        #empty check
        #if not self.heap:
            #return None
        #not empty
        #if len(self.heap) == 1:
            #Remove from heap
            #return self.heap.pop()
        #Get the root of the heap, Replace the root with the last element in the heap and remove the last element.
        #root = self.heap[0]
        #self.heap[0] = self.heap.pop()
        #Make sure it is maintained
        #self._heap_down()
        #return root

    #def decrease_key(self, index):
        #Decreasing the key value in paramters(index)
        # used to decrease the key value of a vehicle at a specified index in the heap.(I looked up this function from internet)
        #I didnt know how to decrease a specific value from heap
        #self.heap[index].estimated_time = -float('inf')
        #self._heap_upwards(index)

    def _heap_upwards(self, index=0):
       #upwards in the heap.
        while index > 0:
            #Algoritm to take the parent from middel index
            parent_index = (index - 1) // 2
            #Compare estimated time and reorder if condotion True swap
            if self.heap[index].estimated_time < self.heap[parent_index].estimated_time:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    def _heap_down(self, index=0):
        #downwars in the heap
        while True:
            #determine the right , left child and if there is condition swap them using samallest value (index)
            smallest = index
            right_child_index = 2 * index + 2
            left_child_index = 2 * index + 1

            #If the left child's estimated time is smaller, smallest is updated to the left child's index. If the right child's estimated time is smaller, smallest is updated to the right child's index.
            if left_child_index < len(self.heap) and self.heap[left_child_index].estimated_time < self.heap[smallest].estimated_time:
                smallest = left_child_index

            if right_child_index < len(self.heap) and self.heap[right_child_index].estimated_time < self.heap[smallest].estimated_time:
                smallest = right_child_index

            if smallest != index:
                self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
                index = smallest
            else:
                break

#def read_file_vehicles():
    #Read the vehicles.txt file
    file_path = 'vehicles.txt'
    #make a list to append the attributes
    vehicles = []
    with open(file_path, 'r') as file:
        file.readline()  # Skip header
        for line in file:
            #make data clean
            vehicle_id, location, distance, speed = line.strip().split()
            #Append them to the list
            vehicle = Vehicle(vehicle_id, location, distance, speed)
            vehicles.append(vehicle)
    #return vehicles

#def read_requests():
    #Read the requests.txt file
    file_path='requests.txt'
    #make a list to append the data
    requests = []
    with open(file_path, 'r') as file:
        file.readline()  # Skip header
        for line in file: #make the data clean
            parts = line.strip().split()
            location, distance, lucky_number = parts[0], float(parts[1]), int(parts[2])
            requests.append((location, distance, lucky_number))
    #return requests

#def process_requests(min_heap, vehicles, requests,total_operations):
    # Move the start_time inside the function, to calculate Elapsed time
    start_time = time.time()  
    #To count thr operation numbers
    operations_count = 0
    #Cintinue doing if there is a operation to do
    #File path we are going to write
    call_history_file_path = "call_history.txt"
    #while total_operations > 0 and requests:
        #request = requests.pop(0)
        #lucky_number = request[2]
        #if the lucky number zero write to the file least estimated time vehicle id
        #after that pop out
        #increment the operation count
        #if lucky_number == 0 and min_heap.heap:
            #called_vehicle = min_heap.pop()
            #with open(call_history_file_path, 'a') as file:
                #file.write(f"{called_vehicle.vehicle_id}\n")
            #operations_count += 1

            #called_vehicle.location = request[0]
            #called_vehicle.distance = request[1]
            #called_vehicle.estimated_time = called_vehicle.calculate_estimated_time()

            #min_heap.push(called_vehicle)
        #If a request has a lucky number (non-zero), the code decreases the key of the corresponding vehicle in the min-heap using min_heap.decrease_key(lucky_number - 1)
        #decrease the specific index value from heap
        # Add the index which is lucky number to the file
        # increase operation count       
        #elif lucky_number != 0 and 0 <= lucky_number - 1 < len(min_heap.heap):
            #min_heap.decrease_key(lucky_number - 1)
            #called_vehicle = min_heap.pop()
            #with open(call_history_file_path, 'a') as file:
              #  file.write(f"{called_vehicle.vehicle_id}\n")
            #operations_count += 1

            #called_vehicle.location = request[0]
            #called_vehicle.distance = request[1]
            #called_vehicle.estimated_time = called_vehicle.calculate_estimated_time()

            #min_heap.push(called_vehicle)

       # total_operations -= 1

    #Calculate the time
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed Time: {elapsed_time:.2f} seconds for {operations_count} operations.")


