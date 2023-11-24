import sys
import time
import random

#Libraries to access a varaiable(sys) , Use to determine execution time(time), To select a random pivot(random)

def quicksort(arr, low, high):
    stack = [(low, high)]
    while stack:
        low, high = stack.pop()
        if low < high:
            splt = spliting(arr, low, high)
            stack.append((low, splt - 1))
            stack.append((splt + 1, high))
#Taking 3 parameters array , array's lower bund and upper bound
#Make a list to store lower bound and upper bound
#This continues while the stack is not empty
      #Get rid of the low and upper bound from list
      # if lower bund length bigger or equal to high continue sorting
        #We call spliting function to  divide the subarray at get new pivot(Recursion Function)
      #ADD the pivots left and right subarrays adding to stack
      #At the opposite tearm the list will be sorted in case of low>high


def spliting(arr, low, high):
    #pivot_index = random.randint(low, high) #To make random pivot
    #First I tried with random pivot bu it was not an effective way to it so I decided to with this alghortim which I searced from internet
    
    mid = (low + high) // 2 #Go to midddle of the array
    pivot_candidates = [(low, arr[low]["Country"]), (mid, arr[mid]["Country"]), (high, arr[high]["Country"])]#Select a potentiol pivot low, mid or high for the country name
    pivot_candidates.sort(key=lambda x: x[1])
    #SOrt by the country name
    pivot_index = pivot_candidates[1][0]
    # pivot will represent the mid

    arr[low], arr[pivot_index] = arr[pivot_index], arr[low]
    
    pivot = arr[low]["Country"]
    i = low
    j = high

    while i < j:
        while i <= j and arr[i]["Country"] <= pivot:
            i += 1

        while arr[j]["Country"] > pivot:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[low], arr[j] = arr[j], arr[low]
    return j

#Pivot_index choosing by random
#Change array's low  and pivot's place in this case pivot goes to first element of array(SWAP)
#Make pivot equal to the arrays lowest index's  value of Country
#make i lowest bund    j  highest bound
#While highest bound bigger then i
    #Get the left values of PIVOT
    #Get the right values of PIVOT
    #After the operation  j(high) > bigger then i(low) (SWAP) them
#Make sure the pivot is in the right place after SWAP
#After spliting function return j will show the pivots right position(index)




def read_data(file_name, n):
    data = []
    with open(file_name, 'r') as file:
        file.readline()
        for i in range(n):
            line = file.readline().strip().split('\t')
            Txt = {
                "Country": line[0],
                "Item Type": line[1],
                "Order ID": int(line[2]),
                "Units Sold": int(line[3]),
                "Total Profit": float(line[4])
            }
            data.append(Txt)
    return data

#Get filename and n(length of how many data we are going to get from file)
# We are skipping first line by this --file.readline() so we can get the the values directly
#Make List called data we are going to store
#Open the file in read method and after that readlines() from file
#We are going to do in n times so in for loop getting line using readline() method
#I use strip() to avoid whitespace , split() make a list and store the characters in there
#Make a dictinoary to store the datas in there by their characteristic whether they are int, float or string
#after store first line store them in data list
#Return Data list





def write_data(sorted_data):
    with open('sortedN.txt', 'w') as file:
        file.write("Country\tItem Type\tOrder ID\tUnits Sold\tTotal Profit\n")
        for entry in sorted_data:
            file.write(
                f"{entry['Country']}\t{entry['Item Type']}\t{entry['Order ID']}\t"
                f"{entry['Units Sold']}\t{entry['Total Profit']:.2f}\n"
            )

#This function basically write to thr sortedN.txt  which we are sorted

def main():
    N = int(sys.argv[1])
    #Get argument 1 from user
    start_time = time.time()
    #Get time
    sales_data=read_data('sales.txt',N)
    #sales_data = read_data('sortedN.txt', N) to answer question d
    quicksort(sales_data, 0, N - 1)
    #Functions we are using

    Total_time = time.time() - start_time
    #Calculating time

    print(f"Sorting {N} elements took {Total_time:.9f} seconds.")
    #Print time
    write_data(sales_data)
    #Write data to sortedN.txt



if __name__ == "__main__":
    main()

