# hello
import math

inter_num = 2
float_num = 2.1

text = "deez nuts"

#ordered, mutable
my_list = [1,2,3,4] 

#ordered but does NOT support item assignment 
my_tuple = (1,2,3,4)

my_set = {1,2,3,4}

#multiple keys per value allowed, but multiples values per key not allowed
my_dict = {"apple": 1, "banana": 2, "cherry": 3 } 


print(my_list[0]) #prints 1
print(my_tuple[2]) #prints 3

print(my_dict["apple"]) #prints 1

a = 17
b = 3
print(a / b) # python defaults to floating point division; expected: 5.67
print (a // b) # floor divison, expected: 5

# if statements work the same as in c++
if a >= b:
    print("a is greater than or equal to b")
else:
    print("b is greater than a")

for i in range(5): #for i in range [0,4]
    print("cucumber", i)

for item in my_list: #for-each loop
    print("list", item)

print(my_dict)
for key in my_dict:
    print(key) # goes over keys, not values
for values in my_dict.values():
    print(values) # now goes over values
for key,value in my_dict.items():
    print(key, value) # both key and value

count = 1
while count <= 5: # while loops work the same way 
    print(count)
    count += 1

for i in range(10):
    if i == 3:
        break # we will break loop prematurely when i == 3
    print(i, end = ' ') # expected: 0 1 2
print()

def great(name): # function definition
    print("great job" , name)

great("Vincent")

def add (a, b):
    c = a + b
    return c

print(add(3, 5)) # expected: 8

# useful functions
print(len(my_list)) #expected: 4, O(1)
print(sum(my_list)) #expected: 10, O(n) 
print(min(my_list)) #expected: 1

print(math.sqrt(16)) #expected: 4.0 
print(math.ceil(4.4)) #expected: 5

# python classes
class Vertex:

    def __init__(self, value): # constructor; self argument passes in instance of object (in this case itself)
        self.value = value
        self.edges = {}

    def add_edge(self, vertex, weight=0): 
        self.edges[vertex] = weight
    
vertex_a = Vertex("A")
vertex_b = Vertex("B")
vertex_a.add_edge(vertex_b, 5)
