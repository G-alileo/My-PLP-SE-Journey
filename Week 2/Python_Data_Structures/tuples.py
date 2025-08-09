# Tuples are ordered, immutable collections.
# Declaration 
my_tuple = ("Audi", "BMW", "Honda", "Toyota")

print("Original Tuple : ", my_tuple)

# Tuple operations 
# Accessing elements (indexing, slicing)

print("Index accessing : ", my_tuple[2])
print("Slicing middle cars : ", my_tuple[1:3])

# Concatenation (+) and Repetition (*)
ext_tuple = ("Lexus", "Nissan", "Accura")

print("Concartenation : ", my_tuple + ext_tuple)  # concartenation
print("Repetition : ", my_tuple * 2)

# Searching (index, count)
print("Search : index", my_tuple.index("Honda"), sep="_" )
print("Count : ", my_tuple.count("Audi"))

# Unpacking into variables
car_1, car_2, *rest = my_tuple

print(car_1)
print(car_2)
print(rest)

# Length (len)
print("Length : ", len(my_tuple))

# Membership (in, not in)
print("Honda" in my_tuple) # True

print("Dodge" not in my_tuple) # True

# Conversion between lists and tuples
my_list = list(my_tuple)
print("List : ", my_list)

my_tuple = tuple(my_list)
print("Tuple  : ", my_tuple)