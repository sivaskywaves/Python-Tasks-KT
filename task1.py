
#Problem 1
"""
Create a dictionary where the keys are tuples representing coordinates (x, y) and the values are city names. 
Write a Python program to print the city name for a given coordinate. 
Example Dictionary: #{(40.7128, -74.0060): "New York", (34.0522, -118.2437): "Los Angeles"} # 
Input: (40.7128, -74.0060)
Expected Output: "New York"

"""
input={(40.7128,-74.0060):"New York",(34.0522,-118.2437):"Los Angels"}
print(input[40.7128,-74.0060])

#Problem 2
""" 
Write a Python program to sort a tuple of tuples based on the second element of each tuple 
Example Tuple: ((1, 2), (3, 1), (5, 0))
Expected Output: ((5, 0), (3, 1), (1, 2))

"""
input = ((1,2),(3,1),(5,0))
print (sorted(input,key=lambda x :x[1]))

#Problem 3
""" 
Write a Python program to find the minimum and maximum elements in a tuple of integers
Example Tuple: (10, 20, 5, 40, 25) 
Expected Output: Min: 5, Max: 40

"""
i=(10,20,5,40,25)
def min_max():
    print("Min:",min(i))
    print("Max:",max(i))
min_max()

#Problem 4
"""
Given a tuple containing nested tuples, write a Python program to flatten it into a single tuple
Example Tuple: (1, (2, 3), (4, 5, 6))
Expected Output: (1, 2, 3, 4, 5, 6)

"""
input= (1,(2,3,),(4,5,6))
output=[]
for integer in input:
    if isinstance(integer,list):
        output.extend(integer)
    elif isinstance(integer,tuple):
        output.extend(integer)
    else:
        output.append(integer) 
print(output)   